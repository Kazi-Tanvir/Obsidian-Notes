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
FOLDER_MOVIES = os.path.join(WORKSPACE_DIR, "movies")
OMDB_KEY = "aaeada7a"

# List of movies to import
MOVIES_LIST = [
    {"query": "A Quiet Place", "year": "2018"},
    {"query": "Interstellar", "year": "2014"},
    {"query": "Oppenheimer", "year": "2023"},
    {"query": "Borat Subsequent Moviefilm", "year": "2020"}, # 2nd Borat movie
    {"query": "The Dictator", "year": "2012"},
    {"query": "The Dreamers", "year": "2003"},
    {"query": "12th Fail", "year": "2023"},
    {"query": "Train to Busan", "year": "2016"},
    {"query": "Oldboy", "year": "2003"},
    {"query": "The Lunchbox", "year": "2013"},
    {"query": "The Shawshank Redemption", "year": "1994"},
    {"query": "The Wolf of Wall Street", "year": "2013"},
    {"query": "The Truman Show", "year": "1998"},
    {"query": "Parasite", "year": "2019"},
    {"query": "Inception", "year": "2010"},
    {"query": "Fight Club", "year": "1999"},
    {"query": "Zindagi Na Milegi Dobara", "year": "2011"},
    {"query": "12 Angry Men", "year": "1957"},
    {"query": "The Call", "year": "2020"},
    {"query": "The Pursuit of Happyness", "year": "2006"},
    {"query": "Stolen", "year": "2024"},
    {"query": "Homebound", "year": "2021"},
    {"query": "Memento", "year": "2000"},
    
    # Pirates of the Caribbean - First Three Movies
    {"query": "Pirates of the Caribbean: The Curse of the Black Pearl", "year": "2003"},
    {"query": "Pirates of the Caribbean: Dead Man's Chest", "year": "2006"},
    {"query": "Pirates of the Caribbean: At World's End", "year": "2007"}
]

# Ensure movies directory exists
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
        dt = datetime.strptime(date_str, "%d %b %Y")
        return f"{dt.month:02d}/{dt.day:02d}/{dt.year}"
    except Exception:
        return date_str

def query_omdb(query, year):
    params = {
        "apikey": OMDB_KEY,
        "t": query,
        "type": "movie",
        "y": year
    }
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
                # Try without year if strict match failed
                print(f"  -> Exact match failed for '{query}' ({year}). Retrying general search...")
                params.pop("y", None)
                url_retry = f"https://www.omdbapi.com/?{urllib.parse.urlencode(params)}"
                req_retry = urllib.request.Request(url_retry, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req_retry) as response_retry:
                    res_data_retry = json.loads(response_retry.read().decode('utf-8'))
                    if res_data_retry.get("Response") == "True":
                        return res_data_retry
                print(f"OMDb Error for query '{query}': {res_data.get('Error')}")
                return None
    except Exception as e:
        print(f"Network/API Error for query '{query}': {e}")
        return None

def main():
    print("=" * 80)
    print("                      Importing Movies from OMDb                       ")
    print("=" * 80 + "\n")
    
    success_count = 0
    fail_count = 0
    
    for idx, item in enumerate(MOVIES_LIST, 1):
        query = item["query"]
        year = item["year"]
        
        print(f"[{idx}/{len(MOVIES_LIST)}] Querying OMDb for movie: '{query}' ({year})...")
        
        data = query_omdb(query, year)
        if not data:
            print(f"  -> Failed to import '{query}'.")
            fail_count += 1
            continue
            
        title = data.get("Title")
        clean_year = data.get("Year", year)
        
        # Determine target file
        safe_title = sanitize_filename(title)
        filename = f"{safe_title} ({clean_year}).md"
        filepath = os.path.join(FOLDER_MOVIES, filename)
            
        print(f"  -> Found: '{title}' ({clean_year})")
        
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
        
        # Build tags list
        movie_tags = []
        for g in genres:
            movie_tags.append(f"genre/{sanitize_tag(g)}")

        # Build Markdown content
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
genres:{format_list(genres)}
director:{format_wikilink_list(directors)}
writer:{format_wikilink_list(writers)}
studio: {format_wikilink_list([])}
duration: {duration}
episodes: 1
onlineRating: {online_rating}
actors:{format_wikilink_list(actors)}
image: {image_url}
released: true
streamingServices: []
premiere: {aired_from}
dateStarted: ""
dateCompleted: ""
watched: true
lastWatched: ""
personalRating: 0
status: "Completed"
franchise: ""
prequel: ""
sequel: ""
favorite: false
rewatchCount: 0
tags:{format_list(movie_tags)}
---
"""
        
        try:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(frontmatter)
            print(f"  -> Successfully imported to 'movies/{filename}'!")
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
