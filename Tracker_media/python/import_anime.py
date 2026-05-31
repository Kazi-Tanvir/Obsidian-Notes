import os
import re
import json
import urllib.request
import urllib.parse
import urllib.error
import time
from datetime import datetime

# Paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WORKSPACE_DIR = os.path.dirname(SCRIPT_DIR)
FOLDER_ANIME = os.path.join(WORKSPACE_DIR, "anime")
FOLDER_ANIME_MOVIES = os.path.join(WORKSPACE_DIR, "anime movies")
FOLDER_MANGA = os.path.join(WORKSPACE_DIR, "manga")

# Ensure directories exist
os.makedirs(FOLDER_ANIME, exist_ok=True)
os.makedirs(FOLDER_ANIME_MOVIES, exist_ok=True)
os.makedirs(FOLDER_MANGA, exist_ok=True)

def sanitize_filename(title):
    sanitized = title.replace(":", " -")
    sanitized = re.sub(r'[\\#%&{}/*<>$"@.?]', '', sanitized)
    sanitized = " ".join(sanitized.split())
    return sanitized

def sanitize_tag(genre):
    sanitized = genre.replace(" ", "-").replace("&", "and")
    sanitized = re.sub(r'[^a-zA-Z0-9/\-]', '', sanitized)
    return sanitized

def format_plot(text):
    if not text:
        return '""'
    # Strip HTML tags
    clean_text = re.sub(r'<[^>]*>', '', text).strip()
    lines = clean_text.replace('\r\n', '\n').replace('\r', '\n').split('\n')
    indented_lines = ["  " + line if line.strip() else "" for line in lines]
    return "|-\n" + "\n".join(indented_lines)

def format_list(lst):
    if not lst:
        return " []"
    lines = [f'  - "{str(item).replace('"', '\\"')}"' for item in lst]
    return "\n" + "\n".join(lines)

def format_wikilink_list(lst):
    if not lst:
        return " []"
    lines = [f'  - "[[{str(item).replace('"', '\\"')}]]"' for item in lst]
    return "\n" + "\n".join(lines)

def format_date(date_dict):
    """Convert AniList date dict {year, month, day} to MM/DD/YYYY."""
    if not date_dict or not date_dict.get("year"):
        return ""
    year = date_dict.get("year")
    month = date_dict.get("month") or 1
    day = date_dict.get("day") or 1
    return f"{month:02d}/{day:02d}/{year}"

def query_anilist(query_str, variables):
    """Perform GraphQL POST request to AniList API."""
    url = "https://graphql.anilist.co"
    req_data = json.dumps({"query": query_str, "variables": variables}).encode("utf-8")
    try:
        req = urllib.request.Request(
            url,
            data=req_data,
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json",
                "User-Agent": "AntigravityMediaVaultAgent/1.0"
            },
            method="POST"
        )
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print(f"  -> AniList API HTTP Error: {e.code} - {e.reason}")
        return None
    except Exception as e:
        print(f"  -> AniList Network Error: {e}")
        return None

# GraphQL Search Query
SEARCH_QUERY = """
query ($search: String, $type: MediaType, $format: MediaFormat) {
  Page(page: 1, perPage: 5) {
    media(search: $search, type: $type, format: $format) {
      id
      title {
        romaji
        english
        native
      }
      type
      format
      startDate {
        year
        month
        day
      }
      endDate {
        year
        month
        day
      }
      episodes
      chapters
      volumes
      duration
      averageScore
      description
      coverImage {
        large
      }
      genres
      synonyms
      studios(isMain: true) {
        nodes {
          name
        }
      }
      staff {
        edges {
          role
          node {
            name {
              full
            }
          }
        }
      }
    }
  }
}
"""

def search_anilist(query, media_type, format_filter=None):
    """Search AniList for media matching title query and type."""
    variables = {"search": query, "type": media_type}
    if format_filter:
        variables["format"] = format_filter
    data = query_anilist(SEARCH_QUERY, variables)
    if data and "data" in data and "Page" in data["data"] and "media" in data["data"]["Page"]:
        return data["data"]["Page"]["media"]
    return []

def import_anilist_media(media, media_type, import_format, custom_status="Plan to Watch"):
    """Format and write the Markdown note from AniList data."""
    media_id = media.get("id")
    titles = media.get("title") or {}
    romaji_title = titles.get("romaji") or ""
    english_title = titles.get("english") or romaji_title
    native_title = titles.get("native") or ""
    
    # Year
    start_date = media.get("startDate") or {}
    clean_year = start_date.get("year") or "unknown"
    release_date_formatted = format_date(start_date)
    end_date_formatted = format_date(media.get("endDate"))

    # Descriptions
    description = media.get("description") or ""
    # Strip HTML tags
    description_clean = re.sub(r'<[^>]*>', '', description).strip()
    
    # Genres & Tags
    genres = media.get("genres") or []
    media_tags = [f"genre/{sanitize_tag(g)}" for g in genres]
    
    # Image
    image_url = media.get("coverImage", {}).get("large") or ""
    
    # Score
    avg_score = media.get("averageScore") or 0
    online_rating = round(avg_score / 10, 2) if avg_score else 0.0

    # Studios / Networks
    studios_raw = media.get("studios", {}).get("nodes", []) or []
    studios = [s.get("name") for s in studios_raw if s.get("name")]

    # Synonyms / Alternate Titles
    alternate_titles = []
    if english_title and english_title != romaji_title:
        alternate_titles.append(english_title)
    if native_title:
        alternate_titles.append(native_title)
    synonyms = media.get("synonyms") or []
    for s in synonyms:
        if s not in alternate_titles and s != romaji_title:
            alternate_titles.append(s)

    # Classify file folder & build frontmatter schema
    if media_type == "ANIME":
        # Check if it is a movie
        format_str = media.get("format") or ""
        is_movie = (import_format == "MOVIE" or format_str == "MOVIE")
        
        safe_title = sanitize_filename(romaji_title)
        filename = f"{safe_title} ({clean_year}).md" if clean_year != "unknown" else f"{safe_title}.md"
        
        # Staff: Writers/Directors
        staff_edges = media.get("staff", {}).get("edges", []) or []
        directors = []
        writers = []
        for edge in staff_edges:
            role = edge.get("role", "").lower()
            name = edge.get("node", {}).get("name", {}).get("full")
            if not name:
                continue
            if "director" in role:
                directors.append(name)
            if "script" in role or "series composition" in role or "writer" in role:
                writers.append(name)

        if is_movie:
            filepath = os.path.join(FOLDER_ANIME_MOVIES, filename)
            target_desc = f"anime movies/{filename}"
            
            # Check duplicate
            if os.path.exists(filepath):
                print(f"  -> File '{filename}' already exists in Anime Movies. Skipping.")
                return True
                
            frontmatter = f"""---
type: movie
subType: "anime-movie"
title: "{romaji_title.replace('"', '\\"')}"
englishTitle: "{english_title.replace('"', '\\"')}"
year: "{clean_year}"
dataSource: AniList
url: https://anilist.co/anime/{media_id}
id: {media_id}
plot: {format_plot(description)}
genres:{format_list(genres)}
director:{format_wikilink_list(directors)}
writer:{format_wikilink_list(writers)}
studio:{format_wikilink_list(studios)}
duration: "{media.get('duration') or 90} min"
episodes: 1
onlineRating: {online_rating}
actors: []
image: {image_url}
released: true
streamingServices: []
premiere: {release_date_formatted}
watched: false
lastWatched: ""
personalRating: 0
status: "{custom_status}"
tags:{format_list(media_tags)}
---

{description_clean}
"""
        else:
            filepath = os.path.join(FOLDER_ANIME, filename)
            target_desc = f"anime/{filename}"
            
            # Check duplicate
            if os.path.exists(filepath):
                print(f"  -> File '{filename}' already exists in Anime. Skipping.")
                return True
                
            sub_type = format_str.lower() if format_str else "tv"
            
            frontmatter = f"""---
type: series
subType: "{sub_type}"
title: "{romaji_title.replace('"', '\\"')}"
englishTitle: "{english_title.replace('"', '\\"')}"
year: {clean_year if isinstance(clean_year, int) or str(clean_year).isdigit() else f'"{clean_year}"'}
dataSource: AniList
url: https://anilist.co/anime/{media_id}
id: {media_id}
plot: {format_plot(description)}
alternateTitles:{format_list(alternate_titles)}
genres:{format_list(genres)}
writer:{format_wikilink_list(writers)}
studio:{format_wikilink_list(studios)}
episodes: {media.get('episodes') or 0}
duration: "{media.get('duration') or 24} min per ep"
onlineRating: {online_rating}
streamingServices: []
image: {image_url}
released: {str(media.get('episodes') is not None).lower()}
airedFrom: {release_date_formatted}
airedTo: {end_date_formatted}
airing: false
watched: false
lastWatched: ""
personalRating: 0
status: "{custom_status}"
tags:{format_list(media_tags)}
---

{description_clean}
"""

    else: # MANGA
        safe_title = sanitize_filename(romaji_title)
        filename = f"{safe_title} ({clean_year}).md" if clean_year != "unknown" else f"{safe_title}.md"
        filepath = os.path.join(FOLDER_MANGA, filename)
        target_desc = f"manga/{filename}"
        
        # Check duplicate
        if os.path.exists(filepath):
            print(f"  -> File '{filename}' already exists in Manga. Skipping.")
            return True
            
        # Authors / Creators
        staff_edges = media.get("staff", {}).get("edges", []) or []
        authors = []
        for edge in staff_edges:
            role = edge.get("role", "").lower()
            name = edge.get("node", {}).get("name", {}).get("full")
            if not name:
                continue
            if "story" in role or "art" in role or "author" in role or "writer" in role:
                authors.append(name)
        
        frontmatter = f"""---
type: manga
subType: manga
title: "{romaji_title.replace('"', '\\"')}"
englishTitle: "{english_title.replace('"', '\\"')}"
year: {clean_year if isinstance(clean_year, int) or str(clean_year).isdigit() else f'"{clean_year}"'}
dataSource: AniList
url: https://anilist.co/manga/{media_id}
id: {media_id}
plot: {format_plot(description)}
alternateTitles:{format_list(alternate_titles)}
genres:{format_list(genres)}
authors:{format_wikilink_list(authors)}
chapters: {media.get('chapters') or 0}
volumes: {media.get('volumes') or 0}
onlineRating: {online_rating}
image: {image_url}
released: {str(media.get('volumes') is not None).lower()}
status: "{custom_status}"
publishingStatus: ""
publishedFrom: {release_date_formatted}
publishedTo: {end_date_formatted}
watched: false
lastWatched: ""
personalRating: 0
tags:{format_list(media_tags)}
---

{description_clean}
"""

    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(frontmatter)
        print(f"  -> Successfully imported to {target_desc}!")
        return True
    except Exception as e:
        print(f"  -> Failed to write file: {e}")
        return False

def show_interactive_search():
    """Menu interface to select media category, search, and import."""
    print("\nSelect Media Category to Import:")
    print(" 1. Anime Series (TV/OVA/ONA)")
    print(" 2. Anime Movie")
    print(" 3. Manga / Light Novel")
    print(" 0. Cancel")
    
    category = input("\nEnter category (0-3): ").strip()
    if category == "0" or not category:
        return
        
    media_type = "ANIME"
    format_filter = None
    status_map = {}
    default_status = "Plan to Watch"
    
    if category == "1":
        # Anime Series
        media_type = "ANIME"
        # Standard status options
        status_map = {
            "1": "Plan to Watch",
            "2": "Currently Watching",
            "3": "Completed",
            "4": "On Hold",
            "5": "Dropped"
        }
    elif category == "2":
        # Anime Movie
        media_type = "ANIME"
        format_filter = "MOVIE"
        status_map = {
            "1": "Plan to Watch",
            "2": "Completed",
            "3": "Dropped"
        }
    elif category == "3":
        # Manga
        media_type = "MANGA"
        default_status = "Plan to Read"
        status_map = {
            "1": "Plan to Read",
            "2": "Currently Reading",
            "3": "Completed",
            "4": "On Hold",
            "5": "Dropped"
        }
    else:
        print("Invalid category selection.")
        return

    query = input("\nEnter title to search on AniList: ").strip()
    if not query:
        return

    print(f"Searching AniList API for '{query}'...")
    results = search_anilist(query, media_type, format_filter)
    if not results:
        print("No matching results found on AniList.")
        return

    print("\nSearch Results:")
    for idx, r in enumerate(results, 1):
        titles = r.get("title") or {}
        name = titles.get("romaji") or titles.get("english") or "Unknown"
        released = r.get("startDate", {}) or {}
        year = released.get("year") or "unknown"
        fmt = r.get("format") or "unknown"
        print(f" {idx}. {name} ({year}) [Format: {fmt}] [ID: {r.get('id')}]")
    print(" 0. Cancel search")

    try:
        sel = input(f"\nSelect an item to import (0-{len(results)}): ").strip()
        if not sel.isdigit():
            print("Invalid selection.")
            return
            
        val = int(sel)
        if val == 0:
            print("Search cancelled.")
            return
        elif 1 <= val <= len(results):
            selected = results[val - 1]
            
            # Select status
            print(f"\nSelect a vault status for the import:")
            for k, v in status_map.items():
                print(f" {k}. {v}")
            status_sel = input("Enter choice: ").strip()
            status = status_map.get(status_sel, default_status)
            
            import_anilist_media(selected, media_type, format_filter, status)
        else:
            print("Selection out of range.")
    except Exception as e:
        print(f"Error during selection: {e}")

def main():
    print("=" * 80)
    print("                    Importing Anime & Manga from AniList                       ")
    print("=" * 80)

    while True:
        print("\nMain Menu:")
        print(" 1. Search & Import Anime or Manga (AniList API)")
        print(" 0. Exit")
        
        choice = input("\nEnter choice: ").strip()
        if choice == "1":
            show_interactive_search()
        elif choice == "0" or choice == "":
            print("\nExiting. Happy reading and watching!")
            break
        else:
            print("Invalid choice.")
            
        time.sleep(0.5)

if __name__ == "__main__":
    main()
