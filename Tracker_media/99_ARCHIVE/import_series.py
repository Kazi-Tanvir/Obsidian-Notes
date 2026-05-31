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
OMDB_KEY = "aaeada7a"

# List of media to import
MEDIA_LIST = [
    # Unticked (Currently Watching)
    {"query": "Narcos", "type": "series", "status": "Currently Watching"},
    {"query": "Sherlock", "type": "series", "status": "Currently Watching"},
    {"query": "Hannibal", "type": "series", "status": "Currently Watching"},
    {"query": "Ozark", "type": "series", "status": "Currently Watching"},
    
    # Ticked (Completed)
    {"query": "Breaking Bad", "type": "series", "status": "Completed"},
    {"query": "Better Call Saul", "type": "series", "status": "Completed"},
    {"query": "Game of Thrones", "type": "series", "status": "Completed"},
    {"query": "House of the Dragon", "type": "series", "status": "Completed"},
    {"query": "The Boys", "type": "series", "status": "Completed"},
    {"query": "Gen V", "type": "series", "status": "Completed"},
    {"query": "Peaky Blinders", "type": "series", "status": "Completed"},
    {"query": "The Witcher", "type": "series", "status": "Completed"},
    {"query": "Dark", "type": "series", "status": "Completed"},
    {"query": "Kota Factory", "type": "series", "status": "Completed"},
    {"query": "Stranger Things", "type": "series", "status": "Completed"},
    {"query": "Shogun", "type": "series", "year": "2024", "status": "Completed"},
    {"query": "Borat", "type": "movie", "status": "Completed"},
    {"query": "Hostel Daze", "type": "series", "status": "Completed"},
    {"query": "Adolescence", "type": "series", "year": "2025", "status": "Completed"},
    {"query": "Mirzapur", "type": "series", "status": "Completed"},
    {"query": "Panchayat", "type": "series", "status": "Completed"}
]

# Ensure target directories exist
os.makedirs(FOLDER_SERIES, exist_ok=True)
os.makedirs(FOLDER_MOVIES, exist_ok=True)

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
    indented_lines = ["  " + line for line in lines]
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
    if not date_str or date_str == "N/A":
        return "unknown"
    try:
        # OMDb date format: "13 Mar 2025" or "17 May 2011"
        dt = datetime.strptime(date_str, "%d %b %Y")
        return f"{dt.month:02d}/{dt.day:02d}/{dt.year}"
    except Exception:
        return date_str

def query_omdb(query, media_type, year=None):
    params = {
        "apikey": OMDB_KEY,
        "t": query,
        "type": media_type
    }
    if year:
        params["y"] = year
        
    url = f"https://www.omdbapi.com/?{urllib.parse.urlencode(params)}"
    
    try:
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        )
        with urllib.request.urlopen(req) as response:
            res_data = json.loads(response.read().decode('utf-8'))
            if res_data.get("Response") == "True":
                return res_data
            else:
                print(f"OMDb Error for query '{query}': {res_data.get('Error')}")
                return None
    except Exception as e:
        print(f"Network/API Error for query '{query}': {e}")
        return None

def main():
    print("=" * 80)
    print("                      Importing Web/TV Series from OMDb                       ")
    print("=" * 80 + "\n")
    
    success_count = 0
    fail_count = 0
    
    for idx, item in enumerate(MEDIA_LIST, 1):
        query = item["query"]
        media_type = item["type"]
        status = item["status"]
        year = item.get("year")
        
        print(f"[{idx}/{len(MEDIA_LIST)}] Querying OMDb for {media_type}: '{query}'...")
        
        data = query_omdb(query, media_type, year)
        if not data:
            print(f"  -> Failed to get data. Attempting general search...")
            # Retry without year if it failed
            if year:
                data = query_omdb(query, media_type)
            if not data:
                print(f"  -> Failed to import '{query}'.")
                fail_count += 1
                continue
                
        title = data.get("Title")
        # Format year (series is usually "2008–2013" or "2015–")
        raw_year = data.get("Year", "unknown")
        
        # Determine target folder and file
        safe_title = sanitize_filename(title)
        # For years, we want a clean single year for the filename if it's like 2008-2013
        clean_year_match = re.match(r'^(\d{4})', raw_year)
        clean_year = clean_year_match.group(1) if clean_year_match else "unknown"
        
        filename = f"{safe_title} ({clean_year}).md" if clean_year != "unknown" else f"{safe_title}.md"
        
        if media_type == "movie":
            target_folder = FOLDER_MOVIES
            filepath = os.path.join(target_folder, filename)
        else:
            target_folder = FOLDER_SERIES
            filepath = os.path.join(target_folder, filename)
            
        print(f"  -> Found: '{title}' ({raw_year})")
        
        # Check if already exists
        if os.path.exists(filepath):
            print(f"  -> File '{filename}' already exists. Skipping.")
            success_count += 1
            continue
            
        # Parse fields
        genres = [g.strip() for g in data.get("Genre", "").split(",") if g.strip()]
        writers = [w.strip() for w in data.get("Writer", "").split(",") if w.strip()]
        actors = [a.strip() for a in data.get("Actors", "").split(",") if a.strip()]
        directors = [d.strip() for d in data.get("Director", "").split(",") if d.strip()]
        
        online_rating_raw = data.get("imdbRating", "0.0")
        try:
            online_rating = float(online_rating_raw) if online_rating_raw != "N/A" else 0.0
        except ValueError:
            online_rating = 0.0
            
        duration = data.get("Runtime", "unknown")
        image_url = data.get("Poster", "")
        if image_url == "N/A":
            image_url = ""
            
        imdb_id = data.get("imdbID", "")
        plot = data.get("Plot", "")
        released_str = data.get("Released", "N/A")
        aired_from = format_date(released_str)
        
        watched_val = str(status == "Completed").lower()
        
        # Build tags list
        media_tags = []
        for g in genres:
            media_tags.append(f"genre/{sanitize_tag(g)}")

        # Build Markdown content
        if media_type == "movie":
            frontmatter = f"""---
type: movie
subType: ""
title: "{title.replace('"', '\\"')}"
englishTitle: "{title.replace('"', '\\"')}"
year: "{clean_year}"
dataSource: OMDbAPI
url: https://www.imdb.com/title/{imdb_id}/
id: {imdb_id}
plot: {format_plot(plot)}
genres: {format_list(genres)}
director: {format_wikilink_list(directors)}
writer: {format_wikilink_list(writers)}
studio: {format_wikilink_list([])}
duration: {duration}
episodes: 1
onlineRating: {online_rating}
actors: {format_wikilink_list(actors)}
image: {image_url}
released: true
streamingServices: []
premiere: {aired_from}
dateStarted: ""
dateCompleted: ""
watched: {watched_val}
lastWatched: ""
personalRating: 0
status: "{status}"
franchise: ""
prequel: ""
sequel: ""
favorite: false
rewatchCount: 0
tags:{format_list(media_tags)}
---
"""
        else:
            frontmatter = f"""---
type: series
subType: "series"
title: "{title.replace('"', '\\"')}"
englishTitle: "{title.replace('"', '\\"')}"
year: "{raw_year}"
dataSource: OMDbAPI
url: https://www.imdb.com/title/{imdb_id}/
id: {imdb_id}
plot: {format_plot(plot)}
genres: {format_list(genres)}
writer: {format_wikilink_list(writers)}
studio: {format_wikilink_list([])}
currentEpisode: 0
episodes: 0
duration: {duration}
onlineRating: {online_rating}
streamingServices: []
image: {image_url}
released: true
airedFrom: {aired_from}
airedTo: "unknown"
airing: {str("–" in raw_year and raw_year.endswith("–")).lower()}
dateStarted: ""
dateCompleted: ""
watched: {watched_val}
lastWatched: ""
personalRating: 0
status: "{status}"
franchise: ""
prequel: ""
sequel: ""
favorite: false
rewatchCount: 0
tags:{format_list(media_tags)}
---
"""
        
        try:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(frontmatter)
            print(f"  -> Successfully imported to '{os.path.basename(target_folder)}/{filename}'!")
            success_count += 1
        except Exception as e:
            print(f"  -> Failed to write file: {e}")
            fail_count += 1
            
        # Polite API delay
        time.sleep(0.5)
        
    print("\n" + "=" * 80)
    print(f"Import Finished! Successfully Imported/Verified: {success_count}, Failed: {fail_count}")
    print("=" * 80)

if __name__ == "__main__":
    main()
