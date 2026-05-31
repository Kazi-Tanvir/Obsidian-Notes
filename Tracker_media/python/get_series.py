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
FOLDER_SERIES = os.path.join(WORKSPACE_DIR, "series")
FOLDER_MOVIES = os.path.join(WORKSPACE_DIR, "movies")
CONFIG_PATH = os.path.join(SCRIPT_DIR, "config.json")

# Ensure directories exist
os.makedirs(FOLDER_SERIES, exist_ok=True)
os.makedirs(FOLDER_MOVIES, exist_ok=True)

def load_api_key():
    """Load TMDb API Key from environment or local config.json, or prompt user if missing."""
    # 1. Check environment variable
    api_key = os.environ.get("TMDB_API_KEY")
    if api_key:
        return api_key

    # 2. Check local config.json
    config = {}
    if os.path.exists(CONFIG_PATH):
        try:
            with open(CONFIG_PATH, "r", encoding="utf-8") as f:
                config = json.load(f)
                api_key = config.get("tmdb_api_key")
                if api_key:
                    return api_key
        except Exception as e:
            print(f"Error loading config.json: {e}")

    # 3. Prompt user for API key if running in an interactive terminal
    print("\n" + "!" * 80)
    print(" TMDb API KEY NOT FOUND!")
    print(" You can get a free TMDb API key by signing up at: https://www.themoviedb.org")
    print("!" * 80)
    
    try:
        api_key = input("\nPlease enter your TMDb API Key: ").strip()
        if api_key:
            # Save it to config.json without overwriting other keys (e.g. rawg_api_key)
            config["tmdb_api_key"] = api_key
            with open(CONFIG_PATH, "w", encoding="utf-8") as f:
                json.dump(config, f, indent=4)
            print(f"-> Saved TMDb API key to: config.json")
            return api_key
    except (IOError, KeyboardInterrupt):
        pass

    raise ValueError("TMDb API Key is required to query movie/series metadata. Please set TMDB_API_KEY env var or add it to config.json.")

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
    lines = text.replace('\r\n', '\n').replace('\r', '\n').strip().split('\n')
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

def format_date(date_str):
    """Convert YYYY-MM-DD to MM/DD/YYYY."""
    if not date_str or date_str == "N/A":
        return ""
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
        return f"{dt.month:02d}/{dt.day:02d}/{dt.year}"
    except Exception:
        return date_str

def make_request(url):
    """Perform HTTP GET request and return JSON response."""
    try:
        req = urllib.request.Request(
            url,
            headers={'User-Agent': 'AntigravityMediaVaultAgent/1.0'}
        )
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"  -> TMDb HTTP Error: {e.code} - {e.reason}")
        return None
    except Exception as e:
        print(f"  -> TMDb Network Error: {e}")
        return None

def search_tmdb(api_key, query, media_type):
    """Search TMDb for TV series or movies."""
    encoded_query = urllib.parse.quote(query)
    search_path = "tv" if media_type == "TV" else "movie"
    url = f"https://api.themoviedb.org/3/search/{search_path}?api_key={api_key}&query={encoded_query}&page=1"
    data = make_request(url)
    if data and "results" in data:
        return data["results"]
    return []

def get_details(api_key, media_id, media_type):
    """Retrieve detailed TV show or movie metadata from TMDb."""
    details_path = "tv" if media_type == "TV" else "movie"
    url = f"https://api.themoviedb.org/3/{details_path}/{media_id}?api_key={api_key}&append_to_response=credits"
    return make_request(url)

def import_tmdb_media(api_key, media_id, media_type, custom_status="Plan to Watch"):
    """Fetch details, format, and write the Markdown note from TMDb."""
    print(f"  -> Fetching full details from TMDb...")
    details = get_details(api_key, media_id, media_type)
    if not details:
        print("  -> Error: Failed to fetch metadata from TMDb.")
        return False

    # Extract names and dates
    if media_type == "TV":
        title = details.get("name", "Unknown TV Show")
        original_title = details.get("original_name") or title
        release_date = details.get("first_air_date") or ""
    else:
        title = details.get("title", "Unknown Movie")
        original_title = details.get("original_title") or title
        release_date = details.get("release_date") or ""
        
    release_date_formatted = format_date(release_date)
    
    clean_year = "unknown"
    if release_date:
        match = re.match(r'^(\d{4})', release_date)
        if match:
            clean_year = match.group(1)

    # Alternate titles
    alternate_titles = []
    if title and title != original_title:
        alternate_titles.append(title)

    # Rating (scaled out of 10)
    vote_average = details.get("vote_average", 0.0)
    online_rating = round(vote_average, 2) if vote_average else 0.0

    # Image
    poster_path = details.get("poster_path")
    image_url = f"https://image.tmdb.org/t/p/w500{poster_path}" if poster_path else ""

    # Plot
    plot = details.get("overview") or ""

    # Genres & Tags
    genres_raw = details.get("genres", []) or []
    genres = [g.get("name") for g in genres_raw if g.get("name")]
    media_tags = [f"genre/{sanitize_tag(g)}" for g in genres]

    # Studios / Networks / Production companies
    studios_raw = details.get("production_companies", []) or []
    studios = [s.get("name") for s in studios_raw if s.get("name")]
    
    # TV Specific Network overrides
    if media_type == "TV":
        networks_raw = details.get("networks", []) or []
        networks = [n.get("name") for n in networks_raw if n.get("name")]
        for net in networks:
            if net not in studios:
                studios.append(net)

    # Staff: Writers/Directors/Actors
    credits = details.get("credits", {}) or {}
    cast = credits.get("cast", []) or []
    crew = credits.get("crew", []) or []
    
    actors = [actor.get("name") for actor in cast[:8] if actor.get("name")]
    directors = [person.get("name") for person in crew if person.get("job") == "Director"]
    writers = [person.get("name") for person in crew if person.get("job") in ["Writer", "Screenplay", "Teleplay"]]

    # Filename
    safe_title = sanitize_filename(original_title)
    filename = f"{safe_title} ({clean_year}).md" if clean_year != "unknown" else f"{safe_title}.md"

    if media_type == "TV":
        filepath = os.path.join(FOLDER_SERIES, filename)
        target_desc = f"series/{filename}"
        
        if os.path.exists(filepath):
            print(f"  -> File '{filename}' already exists in TV Series. Skipping.")
            return True

        episodes = details.get("number_of_episodes") or 0
        runtimes = details.get("episode_run_time") or []
        runtime = runtimes[0] if runtimes else 45
        
        frontmatter = f"""---
type: series
subType: "tv"
title: "{original_title.replace('"', '\\"')}"
englishTitle: "{title.replace('"', '\\"')}"
year: {clean_year if clean_year.isdigit() else f'"{clean_year}"'}
dataSource: TMDb
url: https://www.themoviedb.org/tv/{media_id}
id: {media_id}
plot: {format_plot(plot)}
alternateTitles:{format_list(alternate_titles)}
genres:{format_list(genres)}
writer:{format_wikilink_list(writers)}
studio:{format_wikilink_list(studios)}
episodes: {episodes}
duration: "{runtime} min per ep"
onlineRating: {online_rating}
streamingServices: []
image: {image_url}
released: {str(details.get('status') == 'Ended').lower()}
airedFrom: {release_date_formatted}
airedTo: {format_date(details.get('last_air_date'))}
airing: {str(details.get('status') == 'Returning Series').lower()}
watched: false
lastWatched: ""
personalRating: 0
status: "{custom_status}"
tags:{format_list(media_tags)}
---

{plot}
"""
    else: # MOVIE
        filepath = os.path.join(FOLDER_MOVIES, filename)
        target_desc = f"movies/{filename}"
        
        if os.path.exists(filepath):
            print(f"  -> File '{filename}' already exists in Movies. Skipping.")
            return True

        runtime = details.get("runtime") or 100
        
        frontmatter = f"""---
type: movie
subType: "movie"
title: "{original_title.replace('"', '\\"')}"
englishTitle: "{title.replace('"', '\\"')}"
year: "{clean_year}"
dataSource: TMDb
url: https://www.themoviedb.org/movie/{media_id}
id: {media_id}
plot: {format_plot(plot)}
genres:{format_list(genres)}
director:{format_wikilink_list(directors)}
writer:{format_wikilink_list(writers)}
studio:{format_wikilink_list(studios)}
duration: "{runtime} min"
episodes: 1
onlineRating: {online_rating}
actors:{format_wikilink_list(actors)}
image: {image_url}
released: {str(details.get('status') == 'Released').lower()}
streamingServices: []
premiere: {release_date_formatted}
watched: false
lastWatched: ""
personalRating: 0
status: "{custom_status}"
tags:{format_list(media_tags)}
---

{plot}
"""

    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(frontmatter)
        print(f"  -> Successfully imported to {target_desc}!")
        return True
    except Exception as e:
        print(f"  -> Failed to write file: {e}")
        return False

def show_interactive_search(api_key):
    """Prompt user to search and select a TV show or Movie."""
    print("\nSelect Media Category to Import:")
    print(" 1. TV Series")
    print(" 2. Live-Action Movie")
    print(" 0. Cancel")
    
    category = input("\nEnter category (0-2): ").strip()
    if category == "0" or not category:
        return
        
    media_type = "TV" if category == "1" else "MOVIE"
    default_status = "Plan to Watch"
    
    status_map = {
        "1": "Plan to Watch",
        "2": "Currently Watching" if media_type == "TV" else "Completed",
        "3": "Completed" if media_type == "TV" else "Dropped",
        "4": "On Hold" if media_type == "TV" else "Plan to Watch",
        "5": "Dropped" if media_type == "TV" else "Plan to Watch"
    }
    
    if media_type == "MOVIE":
        status_map = {
            "1": "Plan to Watch",
            "2": "Completed",
            "3": "Dropped"
        }

    query = input("\nEnter title to search on TMDb: ").strip()
    if not query:
        return

    print(f"Searching TMDb API for '{query}'...")
    results = search_tmdb(api_key, query, media_type)
    if not results:
        print("No matching results found on TMDb.")
        return

    print("\nSearch Results:")
    for idx, r in enumerate(results, 1):
        if media_type == "TV":
            name = r.get("name")
            release = r.get("first_air_date") or "unknown"
        else:
            name = r.get("title")
            release = r.get("release_date") or "unknown"
        year = release.split("-")[0] if "-" in release else release
        print(f" {idx}. {name} ({year}) [ID: {r.get('id')}]")
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
            media_id = selected["id"]
            
            # Select status
            print(f"\nSelect a vault status for the import:")
            for k, v in status_map.items():
                print(f" {k}. {v}")
            status_sel = input("Enter choice: ").strip()
            status = status_map.get(status_sel, default_status)
            
            import_tmdb_media(api_key, media_id, media_type, status)
        else:
            print("Selection out of range.")
    except Exception as e:
        print(f"Error during selection: {e}")

def main():
    print("=" * 80)
    print("                     Importing Media from TMDb.org                             ")
    print("=" * 80)

    try:
        api_key = load_api_key()
    except Exception as e:
        print(f"\nError: {e}")
        return

    while True:
        print("\nMain Menu:")
        print(" 1. Search & Import Movies or TV Series (TMDb API)")
        print(" 2. Reset / Update TMDb API Key")
        print(" 0. Exit")
        
        choice = input("\nEnter choice: ").strip()
        if choice == "1":
            show_interactive_search(api_key)
        elif choice == "2":
            if os.path.exists(CONFIG_PATH):
                try:
                    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
                        config = json.load(f)
                    if "tmdb_api_key" in config:
                        del config["tmdb_api_key"]
                    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
                        json.dump(config, f, indent=4)
                except Exception:
                    pass
            print("TMDb API Key reset. Please re-run the key setup.")
            try:
                api_key = load_api_key()
            except Exception as e:
                print(f"Error: {e}")
                break
        elif choice == "0" or choice == "":
            print("\nExiting. Happy watching!")
            break
        else:
            print("Invalid choice.")
            
        time.sleep(0.5)

if __name__ == "__main__":
    main()
