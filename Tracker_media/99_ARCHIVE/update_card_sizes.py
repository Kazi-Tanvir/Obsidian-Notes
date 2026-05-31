import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WORKSPACE_DIR = os.path.dirname(SCRIPT_DIR)

TARGET_FILES = [
    "Anime Movie View.base",
    "Anime View.base",
    "Manga View.base",
    "Movie View.base",
    "Series View.base"
]

def main():
    print("Starting card size configuration update...")
    
    for filename in TARGET_FILES:
        filepath = os.path.join(WORKSPACE_DIR, filename)
        if not os.path.exists(filepath):
            print(f"Skipping {filename} (not found).")
            continue

        print(f"Processing view file: '{filename}'...")
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                lines = f.readlines()
        except Exception as e:
            print(f"Error reading {filename}: {e}")
            continue

        # Strip any existing cardSize declarations to avoid duplicates
        clean_lines = []
        for line in lines:
            if "cardSize:" not in line:
                clean_lines.append(line)

        # Inject cardSize: 150 under every cards view tab
        new_lines = []
        for line in clean_lines:
            new_lines.append(line)
            # Match view list header
            if line.strip().startswith("- type: cards"):
                # Align indentation perfectly (usually 4 spaces)
                indent = "    "
                new_lines.append(f"{indent}cardSize: 150\n")

        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.writelines(new_lines)
            print(f"-> Successfully updated card sizes to 150 in {filename}!")
        except Exception as e:
            print(f"Error writing {filename}: {e}")

    print("Card sizes completely updated!")

if __name__ == "__main__":
    main()
