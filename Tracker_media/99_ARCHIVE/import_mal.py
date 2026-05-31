import os
import re
import xml.etree.ElementTree as ET
import json
import time
import urllib.request
import urllib.error
import sys
from datetime import datetime

# Attempt to force UTF-8 terminal encoding if supported
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass


# Paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WORKSPACE_DIR = os.path.dirname(SCRIPT_DIR)
PREVIOUS_DATA_DIR = os.path.join(SCRIPT_DIR, "previous_data")
CACHE_FILE = os.path.join(PREVIOUS_DATA_DIR, "import_cache.json")
LOG_FILE = os.path.join(SCRIPT_DIR, "import_log.txt")

# Target folders
FOLDER_ANIME = os.path.join(WORKSPACE_DIR, "anime")
FOLDER_MOVIES = os.path.join(WORKSPACE_DIR, "movies")
FOLDER_MANGA = os.path.join(WORKSPACE_DIR, "manga")

# Initialize double logger
class DoubleLogger:
    def __init__(self, filepath):
        self.terminal = sys.stdout
        try:
            self.log = open(filepath, "w", encoding="utf-8")
        except Exception as e:
            self.log = None
            print(f"Warning: Could not create log file at {filepath}: {e}")

    def write(self, message):
        try:
            self.terminal.write(message)
        except UnicodeEncodeError:
            encoding = getattr(self.terminal, 'encoding', 'ascii') or 'ascii'
            if not encoding:
                encoding = 'ascii'
            clean_message = message.encode(encoding, errors='replace').decode(encoding)
            self.terminal.write(clean_message)
        if self.log:
            try:
                self.log.write(message)
                self.log.flush()
            except Exception:
                pass

    def flush(self):
        try:
            self.terminal.flush()
        except Exception:
            pass
        if self.log:
            try:
                self.log.flush()
            except Exception:
                pass

    def close(self):
        if self.log:
            try:
                self.log.close()
            except Exception:
                pass

# Redirect stdout to double logger
sys.stdout = DoubleLogger(LOG_FILE)

def log(msg):
    print(msg)

def log_header(title):
    log("\n" + "=" * 80)
    log(f" {title.center(78)} ")
    log("=" * 80 + "\n")

# Make sure target directories exist
for folder in [FOLDER_ANIME, FOLDER_MOVIES, FOLDER_MANGA]:
    os.makedirs(folder, exist_ok=True)

# Helper to sanitize filenames
def sanitize_filename(title):
    # Replace ":" with " -" and remove invalid windows/obsidian filename characters
    sanitized = title.replace(":", " -")
    sanitized = re.sub(r'[\\#%&{}/*<>$"@.?]', '', sanitized)
    sanitized = " ".join(sanitized.split())
    return sanitized

def sanitize_tag(genre):
    sanitized = genre.replace(" ", "-").replace("&", "and")
    sanitized = re.sub(r'[^a-zA-Z0-9/\-]', '', sanitized)
    return sanitized

# Helper to format plot/synopsis using YAML block scalar style |-
def format_plot(text):
    if not text:
        return '""'
    # Escape quotes or clean characters, but block scalar handles almost everything
    # Let's ensure lines are indented by 2 spaces
    lines = text.replace('\r\n', '\n').replace('\r', '\n').strip().split('\n')
    indented_lines = ["  " + line for line in lines]
    return "|-\n" + "\n".join(indented_lines)

# Helper to format lists for YAML
def format_list(lst):
    if not lst:
        return "[]"
    lines = []
    for item in lst:
        cleaned = str(item).replace('"', '\\"')
        lines.append(f'  - "{cleaned}"')
    return "\n" + "\n".join(lines)

# Helper to format lists as wikilinks for YAML
def format_wikilink_list(lst):
    if not lst:
        return "[]"
    lines = []
    for item in lst:
        cleaned = str(item).replace('"', '\\"')
        if cleaned.strip() and not (cleaned.startswith("[[") and cleaned.endswith("]]")):
            cleaned = f"[[{cleaned}]]"
        lines.append(f'  - "{cleaned}"')
    return "\n" + "\n".join(lines)

# Helper to format date strings to M/D/YYYY
def format_date(date_str):
    if not date_str:
        return ""
    try:
        date_str = date_str.split('T')[0]
        dt = datetime.strptime(date_str, "%Y-%m-%d")
        return f"{dt.month}/{dt.day}/{dt.year}"
    except Exception:
        return date_str

# Helper to map MAL status to cards status
def map_status(mal_status, media_type):
    mal_status = str(mal_status).strip().lower()
    if media_type == "manga":
        if mal_status in ["reading", "currently reading"]:
            return "Currently Reading"
        elif mal_status in ["plan to read", "plan_to_read"]:
            return "Plan to Read"
    else:
        if mal_status in ["watching", "currently watching"]:
            return "Currently Watching"
        elif mal_status in ["plan to watch", "plan_to_watch"]:
            return "Plan to Watch"
    
    if mal_status == "completed":
        return "Completed"
    elif mal_status in ["on-hold", "on hold", "onhold"]:
        return "On Hold"
    elif mal_status == "dropped":
        return "Dropped"
    
    # Fallback capitalization
    return mal_status.title()

# Load Cache
cache = {}
if os.path.exists(CACHE_FILE):
    try:
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            cache = json.load(f)
        log(f"Loaded {len(cache)} cached API responses from import_cache.json.")
    except Exception as e:
        log(f"Warning: Failed to load cache file: {e}")

def save_cache():
    try:
        with open(CACHE_FILE, "w", encoding="utf-8") as f:
            json.dump(cache, f, ensure_ascii=False, indent=2)
    except Exception as e:
        log(f"Warning: Failed to save cache file: {e}")

# Fetch detailed data from Jikan API v4 (zero-dependency)
def fetch_jikan_data(media_type, mal_id):
    cache_key = f"{media_type}_{mal_id}"
    if cache_key in cache:
        return cache[cache_key], True

    url = f"https://api.jikan.moe/v4/{media_type}/{mal_id}/full"
    
    # Jikan API rate limit: 3 requests per second, 60 requests per minute
    time.sleep(2.0)
    
    try:
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        )
        with urllib.request.urlopen(req) as response:
            res_data = json.loads(response.read().decode('utf-8'))
            data = res_data.get("data", {})
            cache[cache_key] = data
            save_cache()
            return data, False
    except urllib.error.HTTPError as e:
        if e.code == 429:
            log("Rate limit hit (429)! Waiting 10 seconds before retrying...")
            time.sleep(10.0)
            return fetch_jikan_data(media_type, mal_id)
        else:
            log(f"API Error (HTTP {e.code}) for {media_type} ID {mal_id}: {e.reason}")
            return None, False
    except Exception as e:
        log(f"Network/Parser Error for {media_type} ID {mal_id}: {e}")
        return None, False

# Find lists in previous_data/
def find_xml_files():
    animelist_path = None
    mangalist_path = None
    if os.path.exists(PREVIOUS_DATA_DIR):
        for filename in os.listdir(PREVIOUS_DATA_DIR):
            if filename.startswith("animelist_") and filename.endswith(".xml"):
                animelist_path = os.path.join(PREVIOUS_DATA_DIR, filename)
            elif filename.startswith("mangalist_") and filename.endswith(".xml"):
                mangalist_path = os.path.join(PREVIOUS_DATA_DIR, filename)
    return animelist_path, mangalist_path

def import_manga(xml_path):
    log_header("Manga List Import Progress")
    if not xml_path:
        log("No mangalist XML file found in previous_data/. Skipping manga import.")
        return

    log(f"Reading manga list from {os.path.basename(xml_path)}...")
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()
    except Exception as e:
        log(f"Failed to parse Manga XML: {e}")
        return

    manga_entries = root.findall("manga")
    total = len(manga_entries)
    log(f"Found {total} manga list entries to process.")

    imported_count = 0
    skipped_count = 0
    failed_count = 0

    for idx, item in enumerate(manga_entries, 1):
        manga_id = item.findtext("manga_mangadb_id")
        raw_title = item.findtext("manga_title")
        my_status = item.findtext("my_status")
        my_score = item.findtext("my_score") or "0"

        if not manga_id:
            log(f"[{idx}/{total}] Warning: Skipping manga entry without ID.")
            failed_count += 1
            continue

        log(f"[{idx}/{total}] Processing manga: \"{raw_title}\" (ID: {manga_id})...")
        
        # Query detailed Jikan API
        data, cached = fetch_jikan_data("manga", manga_id)
        if not data:
            log(f"  -> Error: Could not fetch metadata for ID {manga_id}. Skipping.")
            failed_count += 1
            continue

        # Extract values
        title = data.get("title") or raw_title
        english_title = data.get("title_english") or title
        year_val = data.get("published", {}).get("prop", {}).get("from", {}).get("year")
        year_str = str(year_val) if year_val else "unknown"

        # Sanitize filename
        safe_title = sanitize_filename(english_title)
        filename = f"{safe_title} ({year_str}).md" if year_str != "unknown" else f"{safe_title}.md"
        filepath = os.path.join(FOLDER_MANGA, filename)

        # Resume Check
        if os.path.exists(filepath):
            log(f"  -> File \"{filename}\" already exists. Skipping import.")
            skipped_count += 1
            continue

        # Extract extra properties
        alternate_titles = [title]
        if data.get("title_english"): alternate_titles.append(data.get("title_english"))
        if data.get("title_japanese"): alternate_titles.append(data.get("title_japanese"))
        for syn in data.get("title_synonyms", []): alternate_titles.append(syn)
        alternate_titles = list(set(alternate_titles))

        genres = [genre.get("name") for genre in data.get("genres", [])]
        authors = [author.get("name") for author in data.get("authors", [])]
        chapters = data.get("chapters") or ""
        volumes = data.get("volumes") or ""
        online_rating = data.get("score") or "0.0"
        image_url = data.get("images", {}).get("jpg", {}).get("image_url") or ""
        
        publishing_status = data.get("status") or "Unknown"
        pub_from = format_date(data.get("published", {}).get("from"))
        pub_to = format_date(data.get("published", {}).get("to"))

        # Map user tracking fields
        cards_status = map_status(my_status, "manga")
        user_rating = int(my_score) if my_score.isdigit() else 0

        # Build tags list
        manga_tags = []
        for g in genres:
            manga_tags.append(f"genre/{sanitize_tag(g)}")

        # Build frontmatter block
        frontmatter = f"""---
type: manga
subType: manga
title: "{title.replace('"', '\\"')}"
englishTitle: "{english_title.replace('"', '\\"')}"
year: {year_str}
dataSource: MALAPI Manga
url: https://myanimelist.net/manga/{manga_id}/{sanitize_filename(title).replace(" ", "_")}
id: {manga_id}
plot: {format_plot(data.get("synopsis"))}
alternateTitles: {format_list(alternate_titles)}
genres: {format_list(genres)}
authors: {format_wikilink_list(authors)}
currentChapter: 0
currentVolume: 0
chapters: {chapters}
volumes: {volumes}
onlineRating: {online_rating}
image: {image_url}
released: true
status: "{cards_status}"
publishingStatus: "{publishing_status}"
publishedFrom: {pub_from}
publishedTo: {pub_to}
dateStarted: ""
dateCompleted: ""
watched: {str(cards_status == 'Completed').lower()}
lastWatched: ""
personalRating: {user_rating}
franchise: ""
prequel: ""
sequel: ""
favorite: false
rewatchCount: 0
tags:{format_list(manga_tags)}
---
"""
        try:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(frontmatter)
            log(f"  -> Successfully imported as \"{filename}\" ({'Cached' if cached else 'API'}).")
            imported_count += 1
        except Exception as e:
            log(f"  -> Error: Failed to write file: {e}")
            failed_count += 1

    log(f"\nManga Import Complete! Imported: {imported_count}, Skipped (Exists): {skipped_count}, Failed: {failed_count}.")

def import_anime(xml_path):
    log_header("Anime List Import Progress")
    if not xml_path:
        log("No animelist XML file found in previous_data/. Skipping anime import.")
        return

    log(f"Reading anime list from {os.path.basename(xml_path)}...")
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()
    except Exception as e:
        log(f"Failed to parse Anime XML: {e}")
        return

    anime_entries = root.findall("anime")
    total = len(anime_entries)
    log(f"Found {total} anime list entries to process.")

    imported_count = 0
    skipped_count = 0
    failed_count = 0

    for idx, item in enumerate(anime_entries, 1):
        anime_id = item.findtext("series_animedb_id")
        raw_title = item.findtext("series_title")
        series_type = item.findtext("series_type")
        my_status = item.findtext("my_status")
        my_score = item.findtext("my_score") or "0"

        if not anime_id:
            log(f"[{idx}/{total}] Warning: Skipping anime entry without ID.")
            failed_count += 1
            continue

        log(f"[{idx}/{total}] Processing anime: \"{raw_title}\" (ID: {anime_id})...")

        # Query detailed Jikan API
        data, cached = fetch_jikan_data("anime", anime_id)
        if not data:
            log(f"  -> Error: Could not fetch metadata for ID {anime_id}. Skipping.")
            failed_count += 1
            continue

        # Extract values
        title = data.get("title") or raw_title
        english_title = data.get("title_english") or title
        year_val = data.get("year") or data.get("aired", {}).get("prop", {}).get("from", {}).get("year")
        year_str = str(year_val) if year_val else "unknown"

        # Categorize (Series vs Movie)
        is_movie = series_type == "Movie" or data.get("type") == "Movie"
        target_folder = FOLDER_MOVIES if is_movie else FOLDER_ANIME

        # Sanitize filename
        safe_title = sanitize_filename(english_title)
        filename = f"{safe_title} ({year_str}).md" if year_str != "unknown" else f"{safe_title}.md"
        filepath = os.path.join(target_folder, filename)

        # Resume Check
        if os.path.exists(filepath):
            log(f"  -> File \"{filename}\" already exists in folder \"{os.path.basename(target_folder)}\". Skipping.")
            skipped_count += 1
            continue

        # Extract extra properties
        alternate_titles = [title]
        if data.get("title_english"): alternate_titles.append(data.get("title_english"))
        if data.get("title_japanese"): alternate_titles.append(data.get("title_japanese"))
        for syn in data.get("title_synonyms", []): alternate_titles.append(syn)
        alternate_titles = list(set(alternate_titles))

        genres = [genre.get("name") for genre in data.get("genres", [])]
        studios = [studio.get("name") for studio in data.get("studios", [])]
        online_rating = data.get("score") or "0.0"
        image_url = data.get("images", {}).get("jpg", {}).get("image_url") or ""
        duration = data.get("duration") or "unknown"
        
        # Map user tracking fields
        cards_status = map_status(my_status, "anime")
        user_rating = int(my_score) if my_score.isdigit() else 0
        watched_val = str(cards_status == 'Completed').lower()

        # Build tags list
        anime_tags = []
        for g in genres:
            anime_tags.append(f"genre/{sanitize_tag(g)}")

        # Build frontmatter blocks depending on movie vs series type
        if is_movie:
            studio_str = ", ".join(studios) if studios else "N/A"
            premiere = format_date(data.get("aired", {}).get("from"))
            streaming = [stream.get("name") for stream in data.get("streaming", [])]

            frontmatter = f"""---
type: movie
subType: "anime-movie"
title: "{title.replace('"', '\\"')}"
englishTitle: "{english_title.replace('"', '\\"')}"
year: {year_str}
dataSource: MALAPI
url: https://myanimelist.net/anime/{anime_id}/{sanitize_filename(title).replace(" ", "_")}
id: {anime_id}
plot: {format_plot(data.get("synopsis"))}
alternateTitles: {format_list(alternate_titles)}
genres: {format_list(genres)}
director: {format_wikilink_list([])}
writer: {format_wikilink_list([])}
studio: {format_wikilink_list(studios)}
duration: {duration}
episodes: 1
onlineRating: {online_rating}
actors: {format_wikilink_list([])}
image: {image_url}
released: true
streamingServices: {format_list(streaming)}
premiere: {premiere}
dateStarted: ""
dateCompleted: ""
watched: {watched_val}
lastWatched: ""
personalRating: {user_rating}
status: "{cards_status}"
franchise: ""
prequel: ""
sequel: ""
favorite: false
rewatchCount: 0
tags:{format_list(anime_tags)}
---
"""
        else:
            sub_type = str(data.get("type") or "series").lower()
            episodes = data.get("episodes") or 0
            aired_from = format_date(data.get("aired", {}).get("from"))
            aired_to = format_date(data.get("aired", {}).get("to"))
            airing = str(data.get("airing", False)).lower()
            streaming = [stream.get("name") for stream in data.get("streaming", [])]

            frontmatter = f"""---
type: series
subType: "{sub_type}"
title: "{title.replace('"', '\\"')}"
englishTitle: "{english_title.replace('"', '\\"')}"
year: {year_str}
dataSource: MALAPI
url: https://myanimelist.net/anime/{anime_id}/{sanitize_filename(title).replace(" ", "_")}
id: {anime_id}
plot: {format_plot(data.get("synopsis"))}
alternateTitles: {format_list(alternate_titles)}
genres: {format_list(genres)}
writer: {format_wikilink_list([])}
studio: {format_wikilink_list(studios)}
currentEpisode: 0
episodes: {episodes}
duration: {duration}
onlineRating: {online_rating}
streamingServices: {format_list(streaming)}
image: {image_url}
released: true
airedFrom: {aired_from}
airedTo: {aired_to}
airing: {airing}
dateStarted: ""
dateCompleted: ""
watched: {watched_val}
lastWatched: ""
personalRating: {user_rating}
status: "{cards_status}"
franchise: ""
prequel: ""
sequel: ""
favorite: false
rewatchCount: 0
tags:{format_list(anime_tags)}
---
"""
        try:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(frontmatter)
            log(f"  -> Successfully imported as \"{filename}\" in folder \"{os.path.basename(target_folder)}\" ({'Cached' if cached else 'API'}).")
            imported_count += 1
        except Exception as e:
            log(f"  -> Error: Failed to write file: {e}")
            failed_count += 1

    log(f"\nAnime Import Complete! Imported: {imported_count}, Skipped (Exists): {skipped_count}, Failed: {failed_count}.")

def main():
    log_header("MyAnimeList Import Script Initiating")
    
    animelist_path, mangalist_path = find_xml_files()
    
    if not animelist_path and not mangalist_path:
        log("Error: No animelist_...xml or mangalist_...xml files found in your 'previous_data' directory!")
        log(f"Please place your MyAnimeList XML export files inside: {PREVIOUS_DATA_DIR}")
        return

    # Process manga list first
    import_manga(mangalist_path)

    # Process anime list next
    import_anime(animelist_path)

    log_header("MAL List Import Complete!")
    log(f"Detailed logs saved to \"{os.path.basename(LOG_FILE)}\".")

if __name__ == "__main__":
    try:
        main()
    finally:
        # Close the double logger
        if hasattr(sys.stdout, "close"):
            sys.stdout.close()
