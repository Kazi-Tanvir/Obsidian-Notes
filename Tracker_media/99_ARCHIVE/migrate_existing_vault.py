import os
import re
import shutil

# Root path resolution
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WORKSPACE_DIR = os.path.dirname(SCRIPT_DIR)

ANIME_MOVIES_DIR = os.path.join(WORKSPACE_DIR, "anime movies")
MOVIES_DIR = os.path.join(WORKSPACE_DIR, "movies")
MOBILE_GAMES_DIR = os.path.join(WORKSPACE_DIR, "mobile games")
GAMES_DIR = os.path.join(WORKSPACE_DIR, "games")

MEDIA_FOLDERS = ["anime", "manga", "movies", "series", "games"]

def log(msg):
    print(f"[MIGRATION] {msg}")

def move_anime_movies():
    if not os.path.exists(ANIME_MOVIES_DIR):
        log("No 'anime movies' folder found, skipping merge.")
        return

    os.makedirs(MOVIES_DIR, exist_ok=True)
    moved_count = 0

    for filename in os.listdir(ANIME_MOVIES_DIR):
        if filename.endswith(".md"):
            src_path = os.path.join(ANIME_MOVIES_DIR, filename)
            dest_path = os.path.join(MOVIES_DIR, filename)
            
            # Resolve duplicate filename nicely
            if os.path.exists(dest_path):
                name, ext = os.path.splitext(filename)
                dest_path = os.path.join(MOVIES_DIR, f"{name} - Anime{ext}")
                log(f"Conflict resolved: Renaming to {os.path.basename(dest_path)}")
                
            shutil.move(src_path, dest_path)
            moved_count += 1

    log(f"Moved {moved_count} anime movies into '{MOVIES_DIR}'.")

    # Clean up empty directory
    try:
        if len(os.listdir(ANIME_MOVIES_DIR)) == 0:
            os.rmdir(ANIME_MOVIES_DIR)
            log("Removed empty 'anime movies' folder.")
    except Exception as e:
        log(f"Failed to remove 'anime movies' folder: {e}")

def clean_mobile_games():
    if os.path.exists(MOBILE_GAMES_DIR):
        try:
            # Move any games if somehow present in mobile games
            moved_count = 0
            for filename in os.listdir(MOBILE_GAMES_DIR):
                if filename.endswith(".md"):
                    src_path = os.path.join(MOBILE_GAMES_DIR, filename)
                    dest_path = os.path.join(GAMES_DIR, filename)
                    shutil.move(src_path, dest_path)
                    moved_count += 1
            if moved_count > 0:
                log(f"Moved {moved_count} mobile games into '{GAMES_DIR}'.")
            
            if len(os.listdir(MOBILE_GAMES_DIR)) == 0:
                os.rmdir(MOBILE_GAMES_DIR)
                log("Removed empty 'mobile games' folder.")
        except Exception as e:
            log(f"Failed to remove 'mobile games' folder: {e}")

def parse_frontmatter(content):
    parts = content.split('---', 2)
    if len(parts) < 3 or not content.startswith('---'):
        return None, None, None
    
    yaml_text = parts[1]
    body_text = parts[2]
    
    lines = yaml_text.splitlines()
    properties = {}
    prop_order = []
    current_key = None
    
    for line in lines:
        match = re.match(r'^([a-zA-Z0-9_-]+):\s*(.*)$', line)
        if match:
            current_key = match.group(1)
            value = match.group(2)
            properties[current_key] = {
                'header': line,
                'value': value.strip(),
                'lines': []
            }
            prop_order.append(current_key)
        elif current_key is not None:
            properties[current_key]['lines'].append(line)
            
    return properties, prop_order, body_text

def format_frontmatter(properties, prop_order):
    yaml_lines = []
    for key in prop_order:
        prop = properties[key]
        yaml_lines.append(prop['header'])
        for line in prop['lines']:
            yaml_lines.append(line)
    return "---\n" + "\n".join(yaml_lines) + "\n---\n"

def wrap_in_wikilink(val):
    val_clean = val.strip().strip('"\'')
    if not val_clean or val_clean.lower() in ["n/a", "unknown", "[]", "none"]:
        return val
    if val_clean.startswith("[[") and val_clean.endswith("]]"):
        return val
    return f"[[{val_clean}]]"

def process_wikilink_field(prop):
    val = prop['value'].strip()
    lines = prop['lines']
    
    if val and val.startswith('[') and val.endswith(']'):
        # Inline list format e.g. ["FromSoftware", "Bandai"]
        items = [x.strip().strip('"\'') for x in val[1:-1].split(',') if x.strip()]
        new_items = []
        for item in items:
            if item.lower() not in ["n/a", "unknown", "none"] and item:
                if not (item.startswith("[[") and item.endswith("]]")):
                    item = f"[[{item}]]"
                new_items.append(f'"{item}"')
        prop['value'] = f"[{', '.join(new_items)}]"
        prop['header'] = f"{prop['header'].split(':')[0]}: {prop['value']}"
        prop['lines'] = []
    elif lines:
        # Multi-line list format
        new_lines = []
        for line in lines:
            match = re.match(r'^(\s*-\s*["\']?)(.*?)(["\']?\s*)$', line)
            if match:
                prefix, content, suffix = match.groups()
                content_clean = content.strip()
                if content_clean and content_clean.lower() not in ["n/a", "unknown", "none"]:
                    if not (content_clean.startswith("[[") and content_clean.endswith("]]")):
                        content_clean = f"[[{content_clean}]]"
                new_lines.append(f'{prefix}{content_clean}{suffix}')
            else:
                new_lines.append(line)
        prop['lines'] = new_lines
    elif val:
        # Flat string format
        wrapped = wrap_in_wikilink(val)
        prop['value'] = f'"{wrapped}"' if wrapped.startswith("[[") else wrapped
        prop['header'] = f"{prop['header'].split(':')[0]}: {prop['value']}"

def add_or_update_property(properties, prop_order, key, default_value, before_key=None):
    if key in properties:
        return
    
    # If default is string, ensure quoted appropriately if it contains wikilink
    # If before_key is specified, insert it before that key in prop_order
    properties[key] = {
        'header': f"{key}: {default_value}",
        'value': str(default_value),
        'lines': []
    }
    
    if before_key and before_key in prop_order:
        idx = prop_order.index(before_key)
        prop_order.insert(idx, key)
    else:
        prop_order.append(key)

def upgrade_frontmatter(properties, prop_order, filepath, is_anime_movie):
    media_type = properties.get('type', {}).get('value', '').strip().strip('"\'')
    
    # Identify anime movie subType upgrade
    if is_anime_movie and media_type == 'movie':
        properties['subType'] = {
            'header': 'subType: "anime-movie"',
            'value': '"anime-movie"',
            'lines': []
        }
        if 'subType' not in prop_order:
            prop_order.insert(1, 'subType')

    # Convert specific list/string fields to wikilinks
    wikilink_fields = []
    if media_type == 'series' or media_type == 'movie':
        wikilink_fields = ['studio', 'actors', 'director', 'writer']
    elif media_type == 'manga':
        wikilink_fields = ['authors']
    elif media_type == 'game':
        wikilink_fields = ['developers', 'publishers']

    for field in wikilink_fields:
        if field in properties:
            process_wikilink_field(properties[field])

    # Progress and Time Tracking Schema Inject
    if media_type == 'series':
        add_or_update_property(properties, prop_order, 'currentEpisode', 0, before_key='episodes')
    elif media_type == 'manga':
        add_or_update_property(properties, prop_order, 'currentChapter', 0, before_key='chapters')
        add_or_update_property(properties, prop_order, 'currentVolume', 0, before_key='volumes')
    
    # Standard metadata additions
    add_or_update_property(properties, prop_order, 'dateStarted', '""', before_key='watched')
    add_or_update_property(properties, prop_order, 'dateCompleted', '""', before_key='watched')
    
    # Platform and Playtime for Games
    if media_type == 'game':
        # Default empty platform if missing (it gets list format usually)
        add_or_update_property(properties, prop_order, 'platform', '[]', before_key='played')
        add_or_update_property(properties, prop_order, 'playtime', '0', before_key='played')

    # Franchise and relationships interlinking
    add_or_update_property(properties, prop_order, 'franchise', '""', before_key='personalRating')
    add_or_update_property(properties, prop_order, 'prequel', '""', before_key='personalRating')
    add_or_update_property(properties, prop_order, 'sequel', '""', before_key='personalRating')

    # Personal Meta-Tags
    add_or_update_property(properties, prop_order, 'favorite', 'false', before_key='status')
    if media_type == 'game':
        add_or_update_property(properties, prop_order, 'replayCount', 0, before_key='tags')
    else:
        add_or_update_property(properties, prop_order, 'rewatchCount', 0, before_key='tags')

def upgrade_all_vault_files():
    log("Upgrading all existing files in the vault...")
    upgraded_files = 0

    for folder_name in MEDIA_FOLDERS:
        folder_path = os.path.join(WORKSPACE_DIR, folder_name)
        if not os.path.exists(folder_path):
            log(f"Folder '{folder_name}' not found. Skipping.")
            continue

        log(f"Scanning folder: '{folder_name}'...")
        count = 0
        for root, _, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".md"):
                    filepath = os.path.join(root, file)
                    
                    try:
                        with open(filepath, 'r', encoding='utf-8') as f:
                            content = f.read()
                    except Exception as e:
                        log(f"Error reading {filepath}: {e}")
                        continue

                    properties, prop_order, body_text = parse_frontmatter(content)
                    if not properties:
                        continue

                    # Check if it was an anime movie (originally in anime movies folder)
                    is_anime_movie = (folder_name == "movies" and (
                        properties.get('dataSource', {}).get('value', '').strip().strip('"\'') == 'MALAPI' or
                        'genre/Anime' in properties.get('tags', {}).get('value', '') or
                        any('genre/Anime' in line for line in properties.get('tags', {}).get('lines', []))
                    ))

                    upgrade_frontmatter(properties, prop_order, filepath, is_anime_movie)

                    # Reconstruct frontmatter and write back
                    new_frontmatter = format_frontmatter(properties, prop_order)
                    new_content = new_frontmatter + body_text

                    try:
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        count += 1
                        upgraded_files += 1
                    except Exception as e:
                        log(f"Error writing to {filepath}: {e}")

        log(f"Upgraded {count} files in '{folder_name}'.")

    log(f"Successfully upgraded {upgraded_files} total vault files!")

def main():
    log("Starting structural merge and schema migration...")
    move_anime_movies()
    clean_mobile_games()
    upgrade_all_vault_files()
    log("Vault migration completely finished!")

if __name__ == "__main__":
    main()
