import os
import re

def parse_frontmatter(file_path):
    """
    Parses YAML frontmatter and body from a Markdown file.
    Robust implementation that supports:
      - String, integer, float, and boolean values
      - Multi-line block strings (using |, |-, >, etc.)
      - List arrays (including cleaning up quotes and [[wikilinks]])
      - Extracts any remaining Markdown body text below frontmatter
    """
    metadata = {}
    if not os.path.exists(file_path):
        return metadata
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return metadata

    # Split into frontmatter and body
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", content, re.DOTALL)
    if not match:
        match_only_fm = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
        if not match_only_fm:
            return metadata
        frontmatter_text = match_only_fm.group(1)
        body_text = ""
    else:
        frontmatter_text = match.group(1)
        body_text = match.group(2)

    lines = frontmatter_text.splitlines()
    
    current_key = None
    multiline_mode = False
    multiline_indent = None
    multiline_lines = []
    
    for line in lines:
        stripped = line.strip()
        
        # If we are in multiline mode, check indentation
        if multiline_mode:
            # Check if this line is empty
            if line.strip() == "":
                multiline_lines.append("")
                continue
            
            # Find indentation level (number of leading spaces)
            leading_spaces = len(line) - len(line.lstrip())
            if leading_spaces >= multiline_indent:
                # Accumulate the line without the common indentation
                multiline_lines.append(line[multiline_indent:])
                continue
            else:
                # We exited multiline mode
                metadata[current_key] = "\n".join(multiline_lines).strip()
                multiline_mode = False
                current_key = None
                multiline_lines = []
        
        if not stripped:
            continue
            
        # Is it a list item?
        if stripped.startswith("-"):
            if current_key:
                val = re.sub(r'^[\-\s]+', '', stripped)
                if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
                    val = val[1:-1]
                if val.startswith("[[") and val.endswith("]]"):
                    val = val[2:-2]
                
                if not isinstance(metadata.get(current_key), list):
                    metadata[current_key] = []
                metadata[current_key].append(val)
            continue
            
        # Key-Value match
        match_kv = re.match(r"^([\w\-]+)\s*:\s*(.*)$", line)
        if match_kv:
            current_key = match_kv.group(1)
            val_str = match_kv.group(2).strip()
            
            if val_str in ["|", "|-", ">", ">-"]:
                multiline_mode = True
                # Determine the expected indentation of the multiline block from the current line's indentation
                current_line_indent = len(line) - len(line.lstrip())
                multiline_indent = current_line_indent + 2
                multiline_lines = []
                metadata[current_key] = ""
            elif val_str == "[]" or val_str == "":
                metadata[current_key] = []
            else:
                # Strip quotes if string
                if (val_str.startswith('"') and val_str.endswith('"')) or (val_str.startswith("'") and val_str.endswith("'")):
                    val_str = val_str[1:-1]
                
                # Check for standard types
                val_lower = val_str.lower()
                if val_lower == "true":
                    metadata[current_key] = True
                elif val_lower == "false":
                    metadata[current_key] = False
                elif val_str.isdigit():
                    metadata[current_key] = int(val_str)
                else:
                    try:
                        metadata[current_key] = float(val_str)
                    except ValueError:
                        metadata[current_key] = val_str
            continue

    # If file ended while in multiline mode
    if multiline_mode and current_key:
        metadata[current_key] = "\n".join(multiline_lines).strip()
        
    # Add body text if not empty
    body_text_stripped = body_text.strip()
    if body_text_stripped:
        metadata["bodyText"] = body_text_stripped
        
    return metadata

def generate_markdown_table(headers, alignments, rows):
    """
    Generates a beautifully aligned Markdown table.
    headers: list of str
    alignments: list of str ('left', 'center', 'right')
    rows: list of lists of str
    """
    num_cols = len(headers)
    col_widths = [len(h) for h in headers]
    
    for row in rows:
        for i in range(num_cols):
            val = str(row[i]) if row[i] is not None else ""
            if len(val) > col_widths[i]:
                col_widths[i] = len(val)
                
    # Create the header row
    header_line = "| " + " | ".join(headers[idx].ljust(col_widths[idx]) for idx in range(num_cols)) + " |"
    
    # Create the separator row
    separator_parts = []
    for idx, align in enumerate(alignments):
        width = col_widths[idx]
        if align == 'center':
            separator_parts.append(":" + "-" * (width - 2) + ":")
        elif align == 'right':
            separator_parts.append("-" * (width - 1) + ":")
        else: # left
            separator_parts.append(":" + "-" * (width - 1))
    separator_line = "| " + " | ".join(separator_parts) + " |"
    
    # Create data rows
    data_lines = []
    for row in rows:
        row_cells = []
        for idx, cell in enumerate(row):
            val = str(cell) if cell is not None else ""
            align = alignments[idx]
            width = col_widths[idx]
            if align == 'center':
                row_cells.append(val.center(width))
            elif align == 'right':
                row_cells.append(val.rjust(width))
            else: # left
                row_cells.append(val.ljust(width))
        data_lines.append("| " + " | ".join(row_cells) + " |")
        
    return "\n".join([header_line, separator_line] + data_lines) + "\n"

def format_header(key):
    """Converts camelCase, snake_case, or kebab-case into neat Title Case."""
    if key == "bodyText":
        return "Body Text"
    s = re.sub(r'(?<!^)(?=[A-Z])', ' ', key)
    s = s.replace('_', ' ').replace('-', ' ')
    words = [w.capitalize() for w in s.split()]
    return " ".join(words)

def format_value(key, val):
    """Formats values based on their types and keys."""
    if val is None or val == "" or val == [] or val == {}:
        return "-"
    
    if isinstance(val, list):
        cleaned = []
        for x in val:
            if x is not None and str(x).strip() != "":
                cleaned.append(str(x).strip())
        if not cleaned:
            return "-"
        return ", ".join(cleaned)
    
    if isinstance(val, bool):
        return "true" if val else "false"
        
    if "rating" in key.lower():
        try:
            r_num = float(val)
            if r_num.is_integer():
                r_num = int(r_num)
            if "personal" in key.lower() or key == "Rating":
                return f"★ {r_num}/10" if r_num > 0 else "-"
            else:
                return f"★ {r_num}" if r_num > 0 else "-"
        except (ValueError, TypeError):
            pass
            
    # Clean newlines from strings to prevent breaking Markdown tables
    if isinstance(val, str):
        cleaned_str = val.replace("\r\n", " ").replace("\n", " ").replace("\r", " ")
        cleaned_str = " ".join(cleaned_str.split())
        return cleaned_str if cleaned_str else "-"
        
    return str(val)

def get_column_alignment(key):
    """Determines alignment based on field characteristics."""
    center_keys = {
        "year", "status", "personalrating", "onlinerating", "rating", "released", "played", 
        "playtime", "play_time", "episodes", "chapters", "volumes", "releasedate", "duration", 
        "favorite", "id", "type", "subtype", "currentepisode", "currentchapter", "currentvolume",
        "datecompleted", "datestarted", "watched", "rewatchcount", "replaycount", "airedfrom",
        "airedto", "airing", "publishedfrom", "publishedto", "premiere", "lastwatched"
    }
    if key.lower() in center_keys:
        return "center"
    return "left"

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(script_dir)
    
    # Target database directory
    database_dir = os.path.join(root_dir, "database")
    os.makedirs(database_dir, exist_ok=True)
    print(f"Target database folder: {database_dir}")
    
    media_folders = ["anime", "anime movies", "games", "manga", "movies", "series"]
    
    for folder in media_folders:
        folder_path = os.path.join(root_dir, folder)
        if not os.path.exists(folder_path):
            print(f"Directory not found: {folder_path}")
            continue
        
        md_files = []
        # Scan the folder recursively for markdown files
        for root_sub, _, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".md"):
                    full_path = os.path.join(root_sub, file)
                    md_files.append((file, full_path))
                    
        # Sort the files alphabetically by filename
        md_files.sort(key=lambda x: x[0])
        
        # Parse all files and gather all unique keys
        parsed_entries = []
        unique_keys = set()
        
        for file, full_path in md_files:
            filename = os.path.splitext(file)[0]
            meta = parse_frontmatter(full_path)
            
            # Default title to filename if not in frontmatter
            if "title" not in meta:
                meta["title"] = filename
                
            parsed_entries.append(meta)
            for k in meta.keys():
                unique_keys.add(k)
                
        if not parsed_entries:
            txt_filename = f"{folder}.txt"
            txt_path = os.path.join(database_dir, txt_filename)
            with open(txt_path, "w", encoding="utf-8") as f:
                f.write("")
            print(f"Generated {txt_filename} with 0 entries (empty folder).")
            continue
            
        # Logical sorting of keys (most important identifier fields first)
        preferred_order = [
            "title", "englishTitle", "year", "status", "personalRating", 
            "onlineRating", "subType", "type"
        ]
        
        # Build final key ordering
        ordered_keys = []
        for pk in preferred_order:
            if pk in unique_keys:
                ordered_keys.append(pk)
                
        # Add remaining keys in alphabetical order
        remaining_keys = sorted(list(unique_keys - set(preferred_order) - {"bodyText"}))
        ordered_keys.extend(remaining_keys)
        
        # Put bodyText at the very end if it exists
        if "bodyText" in unique_keys:
            ordered_keys.append("bodyText")
            
        # Build headers and alignments
        headers = [format_header(k) for k in ordered_keys]
        alignments = [get_column_alignment(k) for k in ordered_keys]
        
        # Build rows
        rows = []
        for entry in parsed_entries:
            row = []
            for k in ordered_keys:
                val = entry.get(k)
                row.append(format_value(k, val))
            rows.append(row)
            
        # Generate and write markdown table
        txt_filename = f"{folder}.txt"
        txt_path = os.path.join(database_dir, txt_filename)
        
        table_content = generate_markdown_table(headers, alignments, rows)
        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(table_content)
            
        print(f"Generated {txt_filename} with {len(rows)} entries and {len(headers)} columns.")

if __name__ == "__main__":
    main()
