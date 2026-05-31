import os
import re

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WORKSPACE_DIR = os.path.dirname(SCRIPT_DIR)
GAMES_DIR = os.path.join(WORKSPACE_DIR, "games")

def main():
    print(f"Scanning games folder: '{GAMES_DIR}'...")
    if not os.path.exists(GAMES_DIR):
        print("Error: games folder not found!")
        return

    updated_count = 0

    for root, _, files in os.walk(GAMES_DIR):
        for file in files:
            if file.endswith(".md"):
                filepath = os.path.join(root, file)
                
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                except Exception as e:
                    print(f"Error reading {file}: {e}")
                    continue

                if "---" in content:
                    parts = content.split("---", 2)
                    if len(parts) >= 3 and content.startswith("---"):
                        frontmatter = parts[1]
                        body = parts[2]
                        
                        # Replace playtime: with playTime:
                        new_frontmatter, count = re.subn(r'^playtime\s*:', 'playTime:', frontmatter, flags=re.MULTILINE)
                        
                        if count > 0:
                            new_content = f"---{new_frontmatter}---{body}"
                            try:
                                with open(filepath, 'w', encoding='utf-8') as f:
                                    f.write(new_content)
                                updated_count += 1
                            except Exception as e:
                                print(f"Error writing {file}: {e}")

    print(f"Successfully updated 'playTime' casing in {updated_count} game files!")

if __name__ == "__main__":
    main()
