import os
import re

# Root path resolution
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WORKSPACE_DIR = os.path.dirname(SCRIPT_DIR)

MEDIA_FOLDERS = ["anime", "manga", "movies", "series", "games"]

FRANCHISE_RULES = [
    ("Attack on Titan", "[[Attack on Titan Franchise]]"),
    ("Bleach", "[[Bleach Franchise]]"),
    ("Naruto", "[[Naruto Franchise]]"),
    ("Boruto", "[[Naruto Franchise]]"),
    ("KonoSuba", "[[KonoSuba Franchise]]"),
    ("Konosuba", "[[KonoSuba Franchise]]"),
    ("Demon Slayer", "[[Demon Slayer Franchise]]"),
    ("Kimetsu no Yaiba", "[[Demon Slayer Franchise]]"),
    ("The Witcher", "[[The Witcher Franchise]]"),
    ("Witcher", "[[The Witcher Franchise]]"),
    ("Fullmetal Alchemist", "[[Fullmetal Alchemist Franchise]]"),
    ("Gintama", "[[Gintama Franchise]]"),
    ("Haikyu", "[[Haikyu Franchise]]"),
    ("Jujutsu Kaisen", "[[Jujutsu Kaisen Franchise]]"),
    ("Kaguya-sama", "[[Kaguya-sama Franchise]]"),
    ("Classroom of the Elite", "[[Classroom of the Elite Franchise]]"),
    ("Link Click", "[[Link Click Franchise]]"),
    ("Made in Abyss", "[[Made in Abyss Franchise]]"),
    ("Mob Psycho 100", "[[Mob Psycho 100 Franchise]]"),
    ("Mushoku Tensei", "[[Mushoku Tensei Franchise]]"),
    ("My Dress-Up Darling", "[[My Dress-Up Darling Franchise]]"),
    ("My Hero Academia", "[[My Hero Academia Franchise]]"),
    ("One Piece", "[[One Piece Franchise]]"),
    ("One-Punch Man", "[[One-Punch Man Franchise]]"),
    ("Ranma", "[[Ranma ½ Franchise]]"),
    ("Re -ZERO", "[[Re:ZERO Franchise]]"),
    ("Re:ZERO", "[[Re:ZERO Franchise]]"),
    ("Rent-a-Girlfriend", "[[Rent-a-Girlfriend Franchise]]"),
    ("Solo Leveling", "[[Solo Leveling Franchise]]"),
    ("Spy x Family", "[[Spy x Family Franchise]]"),
    ("SPY x FAMILY", "[[Spy x Family Franchise]]"),
    ("Steins;Gate", "[[Steins;Gate Franchise]]"),
    ("Steins Gate", "[[Steins;Gate Franchise]]"),
    ("The Apothecary Diaries", "[[The Apothecary Diaries Franchise]]"),
    ("To Your Eternity", "[[To Your Eternity Franchise]]"),
    ("Tokyo Ghoul", "[[Tokyo Ghoul Franchise]]"),
    ("Tonikawa", "[[Tonikawa Franchise]]"),
    ("Vinland Saga", "[[Vinland Saga Franchise]]"),
    ("Pirates of the Caribbean", "[[Pirates of the Caribbean Franchise]]"),
    ("Breaking Bad", "[[Breaking Bad Franchise]]"),
    ("Better Call Saul", "[[Breaking Bad Franchise]]"),
    ("Assassination Classroom", "[[Assassination Classroom Franchise]]"),
    ("Delicious in Dungeon", "[[Delicious in Dungeon Franchise]]"),
    ("Dan Da Dan", "[[Dan Da Dan Franchise]]"),
    ("Grand Blue", "[[Grand Blue Franchise]]"),
    ("Evangelion", "[[Evangelion Franchise]]"),
    ("High School DxD", "[[High School DxD Franchise]]"),
    ("Komi Can't", "[[Komi Can't Communicate Franchise]]"),
    ("Tawawa on Monday", "[[Tawawa on Monday Franchise]]"),
    ("Violet Evergarden", "[[Violet Evergarden Franchise]]"),
    ("A Quiet Place", "[[A Quiet Place Franchise]]"),
    ("Borat", "[[Borat Franchise]]")
]

def log(msg):
    print(f"[FRANCHISE] {msg}")

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

def match_franchise(title):
    for pattern, franchise in FRANCHISE_RULES:
        if pattern.lower() in title.lower():
            return franchise
    return None

def main():
    log("Starting franchise classification...")
    processed_count = 0
    updated_count = 0

    for folder_name in MEDIA_FOLDERS:
        folder_path = os.path.join(WORKSPACE_DIR, folder_name)
        if not os.path.exists(folder_path):
            continue

        for root, _, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".md"):
                    filepath = os.path.join(root, file)
                    processed_count += 1
                    
                    try:
                        with open(filepath, 'r', encoding='utf-8') as f:
                            content = f.read()
                    except Exception as e:
                        continue

                    properties, prop_order, body_text = parse_frontmatter(content)
                    if not properties:
                        continue

                    # Determine title to match against
                    title = ""
                    if 'englishTitle' in properties:
                        title = properties['englishTitle']['value'].strip().strip('"\'')
                    if not title and 'title' in properties:
                        title = properties['title']['value'].strip().strip('"\'')
                    if not title:
                        title = os.path.splitext(file)[0]

                    matched_f = match_franchise(title)
                    if matched_f:
                        # Update franchise property
                        # Check if already has a value, let's override default empty string or missing
                        current_f = properties.get('franchise', {}).get('value', '').strip().strip('"\'')
                        if not current_f or current_f == '""':
                            properties['franchise'] = {
                                'header': f'franchise: "{matched_f}"',
                                'value': f'"{matched_f}"',
                                'lines': []
                            }
                            if 'franchise' not in prop_order:
                                prop_order.append('franchise')
                            
                            new_frontmatter = format_frontmatter(properties, prop_order)
                            new_content = new_frontmatter + body_text
                            
                            try:
                                with open(filepath, 'w', encoding='utf-8') as f:
                                    f.write(new_content)
                                updated_count += 1
                            except Exception as e:
                                log(f"Failed to write franchise to {file}: {e}")

    log(f"Franchise classification complete! Checked {processed_count} files, successfully populated {updated_count} franchises.")

if __name__ == "__main__":
    main()
