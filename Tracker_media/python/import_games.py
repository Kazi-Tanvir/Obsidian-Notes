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
FOLDER_GAMES = os.path.join(WORKSPACE_DIR, "games")
FOLDER_MOBILE_GAMES = os.path.join(WORKSPACE_DIR, "games")
CONFIG_PATH = os.path.join(SCRIPT_DIR, "config.json")

# Ensure directories exist
os.makedirs(FOLDER_GAMES, exist_ok=True)
os.makedirs(FOLDER_MOBILE_GAMES, exist_ok=True)

# Default games list for quick selection/import
DEFAULT_GAMES_LIST = [
    {"query": "The Witcher 3: Wild Hunt"},
    {"query": "Grand Theft Auto V"},
    {"query": "Cyberpunk 2077"},
    {"query": "Minecraft"},
    {"query": "Portal 2"},
    {"query": "Red Dead Redemption 2"},
    {"query": "Elden Ring"},
    {"query": "Hollow Knight"}
]

def load_api_key():
    """Load RAWG API Key from environment or local config.json, or prompt user if missing."""
    # 1. Check environment variable
    api_key = os.environ.get("RAWG_API_KEY")
    if api_key:
        return api_key

    # 2. Check local config.json
    if os.path.exists(CONFIG_PATH):
        try:
            with open(CONFIG_PATH, "r", encoding="utf-8") as f:
                config = json.load(f)
                api_key = config.get("rawg_api_key")
                if api_key:
                    return api_key
        except Exception as e:
            print(f"Error loading config.json: {e}")

    # 3. Prompt user for API key if running in an interactive terminal
    print("\n" + "!" * 80)
    print(" RAWG API KEY NOT FOUND!")
    print(" You can get a free RAWG API key by signing up at: https://rawg.io/apidocs")
    print("!" * 80)
    
    try:
        api_key = input("\nPlease enter your RAWG API Key: ").strip()
        if api_key:
            # Save it to config.json
            with open(CONFIG_PATH, "w", encoding="utf-8") as f:
                json.dump({"rawg_api_key": api_key}, f, indent=4)
            print(f"-> Saved API key to: config.json")
            return api_key
    except (IOError, KeyboardInterrupt):
        pass

    raise ValueError("RAWG API Key is required to query game metadata. Please set RAWG_API_KEY env var or add it to config.json.")

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
    # Normalize line endings
    lines = text.replace('\r\n', '\n').replace('\r', '\n').strip().split('\n')
    # Filter out empty or duplicate trailing newlines and indent
    indented_lines = ["  " + line if line.strip() else "" for line in lines]
    return "|-\n" + "\n".join(indented_lines)

def format_list(lst):
    if not lst:
        return "[]"
    lines = [f'  - "{str(item).replace('"', '\\"')}"' for item in lst]
    return "\n" + "\n".join(lines)

def format_wikilink_list(lst):
    if not lst:
        return "[]"
    lines = [f'  - "[[{str(item).replace('"', '\\"')}]]"' for item in lst]
    return "\n" + "\n".join(lines)

def format_date(date_str):
    """Convert YYYY-MM-DD to MM/DD/YYYY."""
    if not date_str or date_str == "N/A":
        return "unknown"
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
            headers={'User-Agent': 'AntigravityMediaVaultAgent/1.0 (Mozilla/5.0)'}
        )
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"  -> HTTP Error: {e.code} - {e.reason}")
        return None
    except Exception as e:
        print(f"  -> Network Error: {e}")
        return None

def search_games(api_key, query):
    """Search RAWG API for matching games."""
    encoded_query = urllib.parse.quote(query)
    url = f"https://api.rawg.io/api/games?key={api_key}&search={encoded_query}&page_size=5"
    data = make_request(url)
    if data and "results" in data:
        return data["results"]
    return []

def get_game_details(api_key, game_id):
    """Retrieve detailed game metadata from RAWG API."""
    url = f"https://api.rawg.io/api/games/{game_id}?key={api_key}"
    return make_request(url)

def classify_subtype_and_folder(parent_platforms):
    """
    Classify game into subType and target directory.
    If released only on Mobile (iOS/Android), it goes to 'mobile games'.
    Otherwise, PC/Console and 'games'.
    """
    if not parent_platforms:
        return "PC/Console", FOLDER_GAMES

    platform_slugs = {p.get("platform", {}).get("slug", "") for p in parent_platforms if p.get("platform")}
    
    # Standard non-mobile platforms
    pc_console_slugs = {"pc", "playstation", "xbox", "nintendo", "mac", "linux", "atari", "sega", "3do", "neo-geo"}
    
    has_pc_console = bool(platform_slugs & pc_console_slugs)
    has_mobile = bool(platform_slugs & {"ios", "android"})

    if has_mobile and not has_pc_console:
        return "Mobile", FOLDER_MOBILE_GAMES
    
    return "PC/Console", FOLDER_GAMES

def import_game(api_key, game_id, custom_status="Plan to Play"):
    """Fetch game details, format them, and write the Markdown note."""
    print(f"  -> Fetching full details for game ID {game_id}...")
    details = get_game_details(api_key, game_id)
    if not details:
        print("  -> Error: Failed to fetch game details from RAWG.")
        return False

    title = details.get("name", "Unknown Game")
    slug = details.get("slug", "")
    
    # Release date & year
    released_str = details.get("released") or ""
    release_date_formatted = format_date(released_str)
    
    clean_year = "unknown"
    if released_str:
        match = re.match(r'^(\d{4})', released_str)
        if match:
            clean_year = match.group(1)

    # Classify platforms and save folder
    parent_platforms = details.get("parent_platforms", [])
    sub_type, target_dir = classify_subtype_and_folder(parent_platforms)
    
    # Extract actual platforms list
    platforms_raw = details.get("platforms", [])
    platforms = [p.get("platform", {}).get("name") for p in platforms_raw if p.get("platform")]
    platforms = sorted(list(set([plat for plat in platforms if plat])))
    
    # Extract playtime
    playtime = details.get("playtime") or 0
    
    # Filename
    safe_title = sanitize_filename(title)
    filename = f"{safe_title} ({clean_year}).md" if clean_year != "unknown" else f"{safe_title}.md"
    filepath = os.path.join(target_dir, filename)

    print(f"  -> Title: '{title}' ({clean_year})")
    print(f"  -> Platform subType: {sub_type}")
    print(f"  -> Destination: {os.path.basename(target_dir)}/{filename}")

    # Duplicate check
    if os.path.exists(filepath):
        print(f"  -> File '{filename}' already exists. Skipping import.")
        return True

    # Parse details
    developers = [d.get("name") for d in details.get("developers", []) if d.get("name")]
    publishers = [p.get("name") for p in details.get("publishers", []) if p.get("name")]
    genres = [g.get("name") for g in details.get("genres", []) if g.get("name")]
    
    # Calculate online rating: metacritic if available, otherwise rating * 20 (scaled to 100)
    metacritic = details.get("metacritic")
    rawg_rating = details.get("rating", 0.0)
    
    if metacritic is not None:
        online_rating = int(metacritic)
    elif rawg_rating:
        online_rating = int(rawg_rating * 20)
    else:
        online_rating = 0

    image_url = details.get("background_image") or ""
    
    # Plot/Description
    description = details.get("description_raw") or details.get("description") or ""
    # Strip HTML tags just in case description_raw is empty and description has HTML
    description_clean = re.sub(r'<[^>]*>', '', description).strip()
    
    # Build tag list
    game_tags = []
    for g in genres:
        game_tags.append(f"genre/{sanitize_tag(g)}")

    # Check if released is true (release date exists and is in the past)
    is_released = False
    if released_str:
        try:
            r_date = datetime.strptime(released_str, "%Y-%m-%d").date()
            is_released = r_date <= datetime.today().date()
        except Exception:
            is_released = True

    # Build YAML frontmatter
    frontmatter = f"""---
type: game
subType: {sub_type}
status: "{custom_status}"
title: "{title.replace('"', '\\"')}"
englishTitle: "{title.replace('"', '\\"')}"
year: "{clean_year}"
dataSource: RAWG
url: https://rawg.io/games/{slug}
id: {game_id}
developers:{format_wikilink_list(developers)}
publishers:{format_wikilink_list(publishers)}
genres:{format_list(genres)}
onlineRating: {online_rating}
image: {image_url}
released: {str(is_released).lower()}
releaseDate: {release_date_formatted}
dateStarted: ""
dateCompleted: ""
platform: {format_list(platforms)}
playtime: {playtime}
played: false
personalRating: 0
franchise: ""
prequel: ""
sequel: ""
favorite: false
replayCount: 0
tags:{format_list(game_tags)}
publishingStatus: ""
---

{description_clean}
"""

    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(frontmatter)
        print(f"  -> Successfully imported to {os.path.basename(target_dir)}/{filename}!")
        return True
    except Exception as e:
        print(f"  -> Failed to write file: {e}")
        return False

def show_interactive_search(api_key):
    """Prompt user to search and select a game."""
    query = input("\nEnter game name to search: ").strip()
    if not query:
        return

    print(f"Searching RAWG API for '{query}'...")
    results = search_games(api_key, query)
    if not results:
        print("No matching games found.")
        return

    print("\nSearch Results:")
    for idx, r in enumerate(results, 1):
        name = r.get("name")
        released = r.get("released") or "unknown"
        year = released.split("-")[0] if "-" in released else released
        print(f" {idx}. {name} ({year}) [ID: {r.get('id')}]")

    print(f" 0. Cancel search")
    
    try:
        sel = input(f"\nSelect a game to import (0-{len(results)}): ").strip()
        if not sel.isdigit():
            print("Invalid selection.")
            return
        
        val = int(sel)
        if val == 0:
            print("Search cancelled.")
            return
        elif 1 <= val <= len(results):
            selected = results[val - 1]
            game_id = selected["id"]
            
            # Allow setting status
            print("\nSelect a vault status for the game:")
            print(" 1. Plan to Play (Default)")
            print(" 2. Currently Playing")
            print(" 3. Completed")
            print(" 4. On Hold")
            print(" 5. Dropped")
            status_sel = input("Enter option (1-5): ").strip()
            
            status_map = {
                "1": "Plan to Play",
                "2": "Currently Playing",
                "3": "Completed",
                "4": "On Hold",
                "5": "Dropped"
            }
            status = status_map.get(status_sel, "Plan to Play")
            
            import_game(api_key, game_id, status)
        else:
            print("Selection out of range.")
    except Exception as e:
        print(f"Error during selection: {e}")

def show_preset_import(api_key):
    """Show a menu of predefined popular games to import."""
    print("\nPreset Games List:")
    for idx, g in enumerate(DEFAULT_GAMES_LIST, 1):
        print(f" {idx}. {g['query']}")
    print(" 0. Back")
    
    sel = input(f"\nSelect a game to search & import (0-{len(DEFAULT_GAMES_LIST)}): ").strip()
    if not sel.isdigit():
        return
    
    val = int(sel)
    if val == 0:
        return
    elif 1 <= val <= len(DEFAULT_GAMES_LIST):
        query = DEFAULT_GAMES_LIST[val - 1]["query"]
        print(f"\nSearching for '{query}'...")
        results = search_games(api_key, query)
        if not results:
            print("No matching games found.")
            return
        
        # Match the first result for preset list convenience
        best_match = results[0]
        import_game(api_key, best_match["id"])
    else:
        print("Selection out of range.")

def main():
    print("=" * 80)
    print("                      Importing Games from RAWG.io                             ")
    print("=" * 80)

    try:
        api_key = load_api_key()
    except Exception as e:
        print(f"\nError: {e}")
        return

    while True:
        print("\nMain Menu:")
        print(" 1. Search & Import Game (Interactive)")
        print(" 2. Search & Import Game from Presets")
        print(" 3. Reset / Update RAWG API Key")
        print(" 0. Exit")
        
        choice = input("\nEnter your choice: ").strip()
        if choice == "1":
            show_interactive_search(api_key)
        elif choice == "2":
            show_preset_import(api_key)
        elif choice == "3":
            if os.path.exists(CONFIG_PATH):
                os.remove(CONFIG_PATH)
            print("API Key reset. Please re-run the key setup.")
            try:
                api_key = load_api_key()
            except Exception as e:
                print(f"Error: {e}")
                break
        elif choice == "0" or choice == "":
            print("\nExiting. Happy gaming!")
            break
        else:
            print("Invalid choice.")
        
        time.sleep(0.5)

if __name__ == "__main__":
    main()
