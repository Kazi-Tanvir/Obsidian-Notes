import os
import re
import xml.etree.ElementTree as ET
from datetime import datetime

# Define workspace and paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WORKSPACE_DIR = os.path.dirname(SCRIPT_DIR)
PREVIOUS_DATA_DIR = os.path.join(SCRIPT_DIR, "previous_data")

# Source directories
DIR_MOVIES = os.path.join(WORKSPACE_DIR, "movies")
DIR_SERIES = os.path.join(WORKSPACE_DIR, "series")
DIR_GAMES = os.path.join(WORKSPACE_DIR, "games")

# Ensure output directory exists
os.makedirs(PREVIOUS_DATA_DIR, exist_ok=True)

# User information matching existing MyAnimeList and MyMangaList backups
USER_ID = "13864737"
USER_NAME = "SENPAI778"

def log(message):
    """Utility log function with a nice timestamp prefix."""
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}")

def parse_markdown_file(filepath):
    """
    Parses an Obsidian markdown note.
    Separates YAML frontmatter from body content.
    Returns:
        - metadata (dict of key-values)
        - body_text (str of the note description body)
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        log(f"Error reading file {os.path.basename(filepath)}: {e}")
        return None, ""

    # Split frontmatter boundaries (---)
    parts = content.split("---", 2)
    if len(parts) < 3:
        return None, ""

    frontmatter_text = parts[1]
    body_text = parts[2].strip()

    metadata = {}
    lines = frontmatter_text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue

        # Match key: value or start of block
        match = re.match(r'^([a-zA-Z0-9_-]+)\s*:\s*(.*)$', line)
        if match:
            key = match.group(1)
            val = match.group(2).strip()

            # Handle multiline string indicator "|-"
            if val == "|-":
                block_lines = []
                i += 1
                while i < len(lines) and (lines[i].startswith("  ") or not lines[i].strip()):
                    block_lines.append(lines[i])
                    i += 1
                # Join with original structure preserved
                metadata[key] = "\n".join(block_lines).strip()
                continue
            
            # Handle list elements or empty lists/strings
            elif not val or val == "[]" or val == '""' or val == "''":
                list_items = []
                temp_i = i + 1
                is_list = False
                while temp_i < len(lines) and (lines[temp_i].startswith("  - ") or lines[temp_i].startswith("    - ")):
                    item_match = re.match(r'^\s*-\s*(.*)$', lines[temp_i])
                    if item_match:
                        item_val = item_match.group(1).strip()
                        # Unquote if encapsulated
                        if (item_val.startswith('"') and item_val.endswith('"')) or (item_val.startswith("'") and item_val.endswith("'")):
                            item_val = item_val[1:-1]
                        list_items.append(item_val)
                    is_list = True
                    temp_i += 1
                
                if is_list:
                    metadata[key] = list_items
                    i = temp_i
                    continue
                else:
                    metadata[key] = [] if val == "[]" else ""
            else:
                # Simple value
                # Unquote if encapsulated
                if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
                    val = val[1:-1]
                
                # Type conversions
                if val.lower() == "true":
                    val = True
                elif val.lower() == "false":
                    val = False
                elif val.lower() in ("null", "~"):
                    val = ""
                else:
                    try:
                        if "." in val:
                            val = float(val)
                        else:
                            val = int(val)
                    except ValueError:
                        pass
                metadata[key] = val
        i += 1

    return metadata, body_text

def format_xml_tag(key, val, indent=4):
    """Helper to convert key/values into indented, XML safe string formats."""
    spaces = " " * indent
    if val is None:
        return f"{spaces}<{key}></{key}>"
    
    if isinstance(val, list):
        plural_tag = key
        # Determine clean singular tag name
        singular_tag = key[:-1] if key.endswith("s") else key
        if key == "genres": singular_tag = "genre"
        elif key == "tags": singular_tag = "tag"
        
        lines = [f"{spaces}<{plural_tag}>"]
        for item in val:
            lines.append(f"{spaces}  <{singular_tag}><![CDATA[{item}]]></{singular_tag}>")
        lines.append(f"{spaces}</{plural_tag}>")
        return "\n".join(lines)
    
    elif isinstance(val, bool):
        val_str = str(val).lower()
        return f"{spaces}<{key}>{val_str}</{key}>"
    
    elif isinstance(val, (int, float)):
        return f"{spaces}<{key}>{val}</{key}>"
    
    else:
        # String and multiline structures
        return f"{spaces}<{key}><![CDATA[{str(val)}]]></{key}>"

def build_xml_list(export_type, items_list):
    """
    Builds a beautifully structured XML string for a specific export type.
    Includes user information headers and calculates summary totals.
    """
    # Calculate status counts based on type
    total_count = len(items_list)
    completed_count = 0
    watching_count = 0
    onhold_count = 0
    dropped_count = 0
    plan_count = 0
    
    for item_meta, _ in items_list:
        status = str(item_meta.get("status", "")).strip().lower()
        if status == "completed":
            completed_count += 1
        elif status in ("currently watching", "watching", "currently playing", "playing"):
            watching_count += 1
        elif status in ("on hold", "on-hold"):
            onhold_count += 1
        elif status == "dropped":
            dropped_count += 1
        elif status in ("plan to watch", "plan to play"):
            plan_count += 1

    # Root XML node name matching MAL conventions
    root_tag = "mymedialist"
    if "game" in export_type:
        root_tag = "mygamelist"
        watching_label = "user_total_currently_playing"
        plan_label = "user_total_plan_to_play"
    else:
        watching_label = "user_total_watching"
        plan_label = "user_total_plan_to_watch"

    xml_lines = []
    xml_lines.append('<?xml version="1.0" encoding="UTF-8" ?>')
    xml_lines.append(f"<!-- Created by Antigravity Media Vault Exporter -->")
    xml_lines.append(f"<{root_tag}>")
    
    # Add User Statistics Metadata
    xml_lines.append("  <myinfo>")
    xml_lines.append(f"    <user_id>{USER_ID}</user_id>")
    xml_lines.append(f"    <user_name>{USER_NAME}</user_name>")
    xml_lines.append(f"    <user_export_type>{export_type}</user_export_type>")
    xml_lines.append(f"    <user_total_items>{total_count}</user_total_items>")
    xml_lines.append(f"    <user_total_completed>{completed_count}</user_total_completed>")
    xml_lines.append(f"    <{watching_label}>{watching_count}</{watching_label}>")
    xml_lines.append(f"    <user_total_onhold>{onhold_count}</user_total_onhold>")
    xml_lines.append(f"    <user_total_dropped>{dropped_count}</user_total_dropped>")
    xml_lines.append(f"    <{plan_label}>{plan_count}</{plan_label}>")
    xml_lines.append("  </myinfo>")
    
    # Order for standardized frontmatter output
    ordered_keys = [
        "id", "type", "subType", "title", "englishTitle", "year", "dataSource", "url",
        "plot", "duration", "episodes", "onlineRating", "image", "released", "releaseDate",
        "premiere", "airedFrom", "airedTo", "airing", "played", "watched", "lastWatched",
        "personalRating", "status", "publishingStatus"
    ]
    
    # Process items
    item_element_name = "item"
    if export_type == "movies": item_element_name = "movie"
    elif export_type == "series": item_element_name = "series"
    elif export_type == "games": item_element_name = "game"
    elif export_type == "mobile_games": item_element_name = "mobile_game"
    
    for item_meta, item_body in items_list:
        xml_lines.append(f"  <{item_element_name}>")
        
        # Group and output keys
        all_keys = ordered_keys + [k for k in item_meta.keys() if k not in ordered_keys]
        for key in all_keys:
            if key not in item_meta:
                continue
            xml_lines.append(format_xml_tag(key, item_meta[key], indent=4))
            
        # Add markdown file text body (plot description) to save all notes
        if item_body.strip():
            xml_lines.append(format_xml_tag("description", item_body, indent=4))
            
        xml_lines.append(f"  </{item_element_name}>")
        
    xml_lines.append(f"</{root_tag}>")
    return "\n".join(xml_lines)

def process_directory(directory, target_type_filter=None):
    """Scans and reads all Markdown files in a directory."""
    items = []
    if not os.path.exists(directory):
        log(f"Directory not found, skipping: {directory}")
        return items

    for filename in sorted(os.listdir(directory)):
        if filename.endswith(".md"):
            filepath = os.path.join(directory, filename)
            meta, body = parse_markdown_file(filepath)
            if meta:
                # Filter by type or subType if required
                if target_type_filter:
                    sub_type = str(meta.get("subType", "")).strip().lower()
                    if target_type_filter == "mobile" and sub_type != "mobile":
                        continue
                    elif target_type_filter == "pc_console" and sub_type == "mobile":
                        continue
                items.append((meta, body))
    return items

def save_xml_file(content, filename):
    """Writes the generated XML string to previous_data folder."""
    output_path = os.path.join(PREVIOUS_DATA_DIR, filename)
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)
        log(f"Successfully generated backup file: {filename}")
        return True
    except Exception as e:
        log(f"Error saving XML file {filename}: {e}")
        return False

def main():
    log("Starting Obsidian Vault Media Database XML Export...")
    print("=" * 80)
    
    # 1. Process movies
    log("Processing movies directory...")
    movies = process_directory(DIR_MOVIES)
    log(f"Found {len(movies)} movie records.")
    
    # 2. Process series
    log("Processing series directory...")
    series = process_directory(DIR_SERIES)
    log(f"Found {len(series)} series records.")
    
    # 3. Process games (PC/Console platform games)
    log("Processing games (PC/Console) records...")
    pc_games = process_directory(DIR_GAMES, target_type_filter="pc_console")
    log(f"Found {len(pc_games)} PC/Console game records.")
    
    # 4. Process mobile games
    log("Processing games (Mobile) records...")
    mobile_games = process_directory(DIR_GAMES, target_type_filter="mobile")
    log(f"Found {len(mobile_games)} Mobile game records.")
    
    # Compile XML backups
    log("Compiling XML database backups...")
    
    movielist_xml = build_xml_list("movies", movies)
    serieslist_xml = build_xml_list("series", series)
    gamelist_xml = build_xml_list("games", pc_games)
    mobilegamelist_xml = build_xml_list("mobile_games", mobile_games)
    
    # Master XML backup (combines all lists)
    all_items = []
    for item in movies: all_items.append((item[0], item[1]))
    for item in series: all_items.append((item[0], item[1]))
    for item in pc_games: all_items.append((item[0], item[1]))
    for item in mobile_games: all_items.append((item[0], item[1]))
    master_xml = build_xml_list("all_vault_media", all_items)
    
    # Save files
    save_xml_file(movielist_xml, "movielist_export.xml")
    save_xml_file(serieslist_xml, "serieslist_export.xml")
    save_xml_file(gamelist_xml, "gamelist_export.xml")
    save_xml_file(mobilegamelist_xml, "mobilegamelist_export.xml")
    save_xml_file(master_xml, "all_media_vault.xml")
    
    print("\n" + "=" * 80)
    print("                      XML DATABASE BACKUP SUMMARY                      ")
    print("=" * 80)
    print(f" Movies:        {len(movies):<4} | Generated: movielist_export.xml")
    print(f" TV Series:     {len(series):<4} | Generated: serieslist_export.xml")
    print(f" PC/Console:    {len(pc_games):<4} | Generated: gamelist_export.xml")
    print(f" Mobile Games:  {len(mobile_games):<4} | Generated: mobilegamelist_export.xml")
    print(f" Master Backup: {len(all_items):<4} | Generated: all_media_vault.xml")
    print("=" * 80)
    log("Backup complete! All files saved safely in 99_ARCHIVE/previous_data/.")

if __name__ == "__main__":
    main()
