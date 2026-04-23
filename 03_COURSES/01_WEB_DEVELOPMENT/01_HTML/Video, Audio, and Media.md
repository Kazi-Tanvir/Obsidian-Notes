---
tags:
- html
- media
- multimedia
---
# Video, Audio, and Media

## What's the Actual Use?
HTML5 introduced native support for video and audio files without needing external plugins like Flash. This allows for seamless media integration directly in the browser.

## Other Common Use Cases
- Embedding background videos for landing pages.
- Providing audio players for podcasts or music clips.

## Documentation & Code
The `<video>` and `<audio>` tags use `<source>` child elements to provide different file formats for better browser compatibility.

````html
<!-- Video Player -->
<video controls width="400">
    <source src="movie.mp4" type="video/mp4">
    Your browser does not support the video tag.
</video>

<!-- Audio Player -->
<audio controls>
    <source src="music.mp3" type="audio/mpeg">
</audio>
````
