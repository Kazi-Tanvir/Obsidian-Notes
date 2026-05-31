import os
import re
import ast
import shutil

# Configuration
MEDIA_FOLDERS = ["anime", "games", "manga", "movies", "series"]
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WORKSPACE_DIR = os.path.dirname(SCRIPT_DIR)
BACKUP_DIR = os.path.join(SCRIPT_DIR, "previous_data", "backup_before_tag_migration")

# Create backup directory
os.makedirs(BACKUP_DIR, exist_ok=True)

def sanitize_tag(genre):
    # Replace spaces with hyphens, & with and, and strip other non-alphanumeric characters (except hyphen or slash)
    sanitized = genre.replace(" ", "-").replace("&", "and")
    sanitized = re.sub(r'[^a-zA-Z0-9/\-]', '', sanitized)
    return sanitized

def parse_frontmatter(content):
    # Split by frontmatter delimiters
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
        # Match a top-level key (starts at line beginning, no spaces, word, colon)
        match = re.match(r'^([a-zA-Z0-9_-]+):\s*(.*)$', line)
        if match:
            current_key = match.group(1)
            value = match.group(2)
            properties[current_key] = {
                'header': line,
                'value': value,
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

def process_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return False

    properties, prop_order, body_text = parse_frontmatter(content)
    if not properties or 'genres' not in properties:
        # No frontmatter or no genres field
        return False

    # Extract genres list
    genres_list = []
    genres_prop = properties['genres']
    val = genres_prop['value'].strip()
    if val.startswith('[') and val.endswith(']'):
        try:
            genres_list = ast.literal_eval(val)
        except Exception:
            genres_list = [x.strip(' "\'') for x in val[1:-1].split(',') if x.strip()]
    else:
        for line in genres_prop['lines']:
            m = re.match(r'^\s*-\s*["\']?(.*?)["\']?\s*$', line)
            if m:
                genres_list.append(m.group(1))

    if not genres_list:
        return False

    # Extract existing tags
    tags_list = []
    has_tags = 'tags' in properties
    if has_tags:
        tags_prop = properties['tags']
        val = tags_prop['value'].strip()
        if val.startswith('[') and val.endswith(']'):
            try:
                tags_list = ast.literal_eval(val)
            except Exception:
                tags_list = [x.strip(' "\'') for x in val[1:-1].split(',') if x.strip()]
        elif val:
            tags_list = [val.strip(' "\'')]
        else:
            for line in tags_prop['lines']:
                m = re.match(r'^\s*-\s*["\']?(.*?)["\']?\s*$', line)
                if m:
                    tags_list.append(m.group(1))

    # Generate new tags list (excluding mediaDB tags)
    new_tags = []
    for tag in tags_list:
        if not tag.startswith("mediaDB") and tag not in new_tags:
            new_tags.append(tag)
            
    # Add genres as hierarchical tags (genre/Name)
    for genre in genres_list:
        sanitized = sanitize_tag(genre)
        hierarchical_tag = f"genre/{sanitized}"
        if hierarchical_tag not in new_tags:
            new_tags.append(hierarchical_tag)

    # Check if the tags list actually changed (either removed mediaDB or added new genres)
    if set(new_tags) == set(tags_list) and has_tags:
        return False

    # Backup the original file
    relative_path = os.path.relpath(filepath, WORKSPACE_DIR)
    backup_path = os.path.join(BACKUP_DIR, relative_path)
    os.makedirs(os.path.dirname(backup_path), exist_ok=True)
    shutil.copy2(filepath, backup_path)

    # Reconstruct the tags property
    properties['tags'] = {
        'header': 'tags:',
        'value': '',
        'lines': [f'  - "{t}"' for t in new_tags]
    }
    
    if 'tags' not in prop_order:
        # If tags property didn't exist, place it right before the closing ---
        prop_order.append('tags')

    # Build and write new content
    new_frontmatter = format_frontmatter(properties, prop_order)
    new_content = new_frontmatter + body_text

    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    except Exception as e:
        print(f"Error writing {filepath}: {e}")
        return False

def main():
    print("=" * 80)
    print("               Converting Frontmatter Genres to Obsidian Tags                 ")
    print("=" * 80 + "\n")
    
    total_processed = 0
    total_modified = 0
    
    for folder_name in MEDIA_FOLDERS:
        folder_path = os.path.join(WORKSPACE_DIR, folder_name)
        if not os.path.exists(folder_path):
            print(f"Directory '{folder_name}' not found. Skipping.")
            continue
            
        print(f"Scanning directory: {folder_name}...")
        file_count = 0
        mod_count = 0
        
        for root, _, files in os.walk(folder_path):
            for file in files:
                if file.endswith('.md'):
                    filepath = os.path.join(root, file)
                    file_count += 1
                    if process_file(filepath):
                        mod_count += 1
                        
        print(f"  -> Found {file_count} markdown files, modified {mod_count} files.\n")
        total_processed += file_count
        total_modified += mod_count
        
    print("=" * 80)
    print(f"Migration Finished! Checked: {total_processed} files, Successfully Modified: {total_modified} files.")
    print(f"Backups of all modified files have been saved to: previous_data/backup_before_tag_migration/")
    print("=" * 80)

if __name__ == "__main__":
    main()
