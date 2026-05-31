---
cssclasses:
  - media-dashboard
  - wide
  - max
---

```dataviewjs
const allPages = dv.pages().array();

// Anime Pages
const animePages = allPages.filter(p => 
  p.file.folder === "anime" || 
  p.subType === "anime-movie" ||
  p.file.folder === "anime movies"
);

// Manga Pages
const mangaPages = allPages.filter(p => p.file.folder === "manga");

// Game Pages
const gamePages = allPages.filter(p => p.file.folder === "games" || p.file.folder === "mobile games");

// Series Pages (Live-action TV Shows)
const seriesPages = allPages.filter(p => p.file.folder === "series" && p.subType !== "anime-movie");

// Movie Pages (Live-action Movies)
const moviePages = allPages.filter(p => p.file.folder === "movies" && p.subType !== "anime-movie");

// Helpers
function getDuration(p) {
  if (!p.duration) return 24;
  if (typeof p.duration === "number") return p.duration;
  const match = String(p.duration).match(/(\d+)/);
  return match ? parseInt(match[1]) : 24;
}

function getRating(p) {
  return p.personalRating || 0;
}

// Anime aggregates
const aniWatching = animePages.filter(p => p.status === "Currently Watching").length;
const aniCompleted = animePages.filter(p => p.status === "Completed").length;
const aniOnHold = animePages.filter(p => p.status === "On Hold").length;
const aniDropped = animePages.filter(p => p.status === "Dropped").length;
const aniPlan = animePages.filter(p => p.status === "Plan to Watch").length;
const aniTotal = aniWatching + aniCompleted + aniOnHold + aniDropped + aniPlan;

let animeMin = 0;
animePages.forEach(p => {
  const eps = p.status === "Completed" ? (p.episodes || 1) : (p.currentEpisode || 0);
  animeMin += eps * getDuration(p);
});
const aniDays = (animeMin / 1440).toFixed(1);

const aniRated = animePages.filter(p => getRating(p) > 0);
const aniMean = aniRated.length ? (aniRated.reduce((sum, p) => sum + getRating(p), 0) / aniRated.length).toFixed(2) : "0.00";
const aniEps = animePages.reduce((sum, p) => sum + (p.status === "Completed" ? (p.episodes || 1) : (p.currentEpisode || 0)), 0);

// Manga aggregates
const manReading = mangaPages.filter(p => p.status === "Currently Reading").length;
const manCompleted = mangaPages.filter(p => p.status === "Completed").length;
const manOnHold = mangaPages.filter(p => p.status === "On Hold").length;
const manDropped = mangaPages.filter(p => p.status === "Dropped").length;
const manPlan = mangaPages.filter(p => p.status === "Plan to Read").length;
const manTotal = manReading + manCompleted + manOnHold + manDropped + manPlan;

const manRated = mangaPages.filter(p => getRating(p) > 0);
const manMean = manRated.length ? (manRated.reduce((sum, p) => sum + getRating(p), 0) / manRated.length).toFixed(2) : "0.00";

const manChaps = mangaPages.reduce((sum, p) => sum + (p.status === "Completed" ? (p.chapters || 0) : (p.currentChapter || 0)), 0);
const manVols = mangaPages.reduce((sum, p) => sum + (p.status === "Completed" ? (p.volumes || 0) : (p.currentVolume || 0)), 0);
const manDays = ((manChaps * 5) / 1440).toFixed(1);

// Game aggregates
const gamePlaying = gamePages.filter(p => p.status === "Currently Playing").length;
const gameCompleted = gamePages.filter(p => p.status === "Completed").length;
const gameDropped = gamePages.filter(p => p.status === "Dropped").length;
const gamePlan = gamePages.filter(p => p.status === "Plan to Play").length;
const gameTotal = gamePlaying + gameCompleted + gameDropped + gamePlan;

const gameRated = gamePages.filter(p => getRating(p) > 0);
const gameMean = gameRated.length ? (gameRated.reduce((sum, p) => sum + getRating(p), 0) / gameRated.length).toFixed(2) : "0.00";
const gamePlaytime = gamePages.reduce((sum, p) => sum + (parseInt(p.playTime) || parseInt(p.playtime) || 0), 0);
const gameDays = (gamePlaytime / 24).toFixed(1);

// Series aggregates
const serWatching = seriesPages.filter(p => p.status === "Currently Watching").length;
const serCompleted = seriesPages.filter(p => p.status === "Completed").length;
const serOnHold = seriesPages.filter(p => p.status === "On Hold").length;
const serDropped = seriesPages.filter(p => p.status === "Dropped").length;
const serPlan = seriesPages.filter(p => p.status === "Plan to Watch").length;
const serTotal = serWatching + serCompleted + serOnHold + serDropped + serPlan;

const serRated = seriesPages.filter(p => getRating(p) > 0);
const serMean = serRated.length ? (serRated.reduce((sum, p) => sum + getRating(p), 0) / serRated.length).toFixed(2) : "0.00";

let serMin = 0;
seriesPages.forEach(p => {
  const eps = p.status === "Completed" ? (p.episodes || 1) : (p.currentEpisode || 0);
  const dur = p.duration ? (typeof p.duration === "number" ? p.duration : (parseInt(String(p.duration).match(/\d+/)) || 45)) : 45;
  serMin += eps * dur;
});
const serDays = (serMin / 1440).toFixed(1);
const serEps = seriesPages.reduce((sum, p) => sum + (p.status === "Completed" ? (p.episodes || 1) : (p.currentEpisode || 0)), 0);

// Movie aggregates
const movWatching = moviePages.filter(p => p.status === "Currently Watching").length;
const movCompleted = moviePages.filter(p => p.status === "Completed").length;
const movOnHold = moviePages.filter(p => p.status === "On Hold").length;
const movDropped = moviePages.filter(p => p.status === "Dropped").length;
const movPlan = moviePages.filter(p => p.status === "Plan to Watch").length;
const movTotal = movWatching + movCompleted + movOnHold + movDropped + movPlan;

const movRated = moviePages.filter(p => getRating(p) > 0);
const movMean = movRated.length ? (movRated.reduce((sum, p) => sum + getRating(p), 0) / movRated.length).toFixed(2) : "0.00";

let movMin = 0;
moviePages.forEach(p => {
  if (p.status === "Completed") {
    const dur = p.duration ? (typeof p.duration === "number" ? p.duration : (parseInt(String(p.duration).match(/\d+/)) || 100)) : 100;
    movMin += dur;
  }
});
const movDays = (movMin / 1440).toFixed(1);

// Helper for Proportional Progress Bar
function makeProgressBar(watching, completed, onhold, dropped, plantowatch) {
  const total = watching + completed + onhold + dropped + plantowatch;
  if (total === 0) return `<div class="progress-bar-empty"></div>`;
  
  const wPct = ((watching / total) * 100).toFixed(1);
  const cPct = ((completed / total) * 100).toFixed(1);
  const oPct = ((onhold / total) * 100).toFixed(1);
  const dPct = ((dropped / total) * 100).toFixed(1);
  const pPct = ((plantowatch / total) * 100).toFixed(1);
  
  return `
    <div class="progress-bar-container">
      ${watching > 0 ? `<div class="progress-segment watching" style="width: ${wPct}%;" title="Watching/Reading: ${watching} (${wPct}%)"></div>` : ''}
      ${completed > 0 ? `<div class="progress-segment completed" style="width: ${cPct}%;" title="Completed: ${completed} (${cPct}%)"></div>` : ''}
      ${onhold > 0 ? `<div class="progress-segment onhold" style="width: ${oPct}%;" title="On-Hold: ${onhold} (${oPct}%)"></div>` : ''}
      ${dropped > 0 ? `<div class="progress-segment dropped" style="width: ${dPct}%;" title="Dropped: ${dropped} (${dPct}%)"></div>` : ''}
      ${plantowatch > 0 ? `<div class="progress-segment plantowatch" style="width: ${pPct}%;" title="Plan to Watch/Read: ${plantowatch} (${pPct}%)"></div>` : ''}
    </div>
  `;
}

// Helper to sort plain JavaScript arrays by dynamic dates descending
function sortDescByDate(arr, dateExtractor) {
  return [...arr].sort((a, b) => {
    const valA = dateExtractor(a);
    const valB = dateExtractor(b);
    const dateA = valA ? new Date(valA) : new Date(0);
    const dateB = valB ? new Date(valB) : new Date(0);
    return dateB - dateA;
  });
}

// Active Consuming Shelf (Watching, Reading, Playing)
const activeMediaList = sortDescByDate(
  allPages.filter(p => 
    p.status === "Currently Watching" ||
    p.status === "Currently Reading" ||
    p.status === "Currently Playing"
  ),
  p => p.lastWatched || p.file.mtime
).slice(0, 6);

let activeShelfCards = "";
if (activeMediaList.length === 0) {
  activeShelfCards = `<div class="empty-shelf-placeholder">No active media in progress. Pick something from your trackers below!</div>`;
} else {
  activeMediaList.forEach(p => {
    const titleText = p.englishTitle || p.title || p.file.name;
    const coverUrl = p.image || "https://static.wikia.nocookie.net/obluda/images/f/ff/Johan.png/revision/latest?cb=20250427000122";
    
    let progressText = "Active";
    let catBadge = "MEDIA";
    let badgeClass = "badge-media";
    
    if (p.file.folder === "anime" || p.subType === "anime-movie" || p.file.folder === "anime movies") {
      progressText = `Ep. ${p.currentEpisode || 0} / ${p.episodes || '?'}`;
      catBadge = "ANIME";
      badgeClass = "badge-anime";
    } else if (p.file.folder === "manga") {
      progressText = `Ch. ${p.currentChapter || 0} / ${p.chapters || '?'}`;
      catBadge = "MANGA";
      badgeClass = "badge-manga";
    } else if (p.file.folder === "games") {
      const pt = p.playTime || p.playtime;
      progressText = pt ? `Played ${pt}h` : "Active";
      catBadge = "GAME";
      badgeClass = "badge-game";
    } else if (p.file.folder === "series") {
      progressText = `Ep. ${p.currentEpisode || 0} / ${p.episodes || '?'}`;
      catBadge = "SERIES";
      badgeClass = "badge-series";
    } else if (p.file.folder === "movies") {
      progressText = "Movie";
      catBadge = "MOVIE";
      badgeClass = "badge-movie";
    }
    
    activeShelfCards += `
      <a class="internal-link shelf-card" href="${p.file.path}" style="background-image: url('${coverUrl}');">
        <div class="card-gradient"></div>
        <div class="card-badge ${badgeClass}">${catBadge}</div>
        <div class="card-content">
          <div class="card-title">${titleText}</div>
          <div class="card-progress">${progressText}</div>
        </div>
      </a>
    `;
  });
}

// Recently Completed Shelf
const completedMediaList = sortDescByDate(
  allPages.filter(p => p.status === "Completed"),
  p => p.dateCompleted || p.file.mtime
).slice(0, 6);

let completedShelfCards = "";
if (completedMediaList.length === 0) {
  completedShelfCards = `<div class="empty-shelf-placeholder">No completed media. Time to finish something!</div>`;
} else {
  completedMediaList.forEach(p => {
    const titleText = p.englishTitle || p.title || p.file.name;
    const coverUrl = p.image || "https://images.unsplash.com/photo-1607604276583-eef5d076aa5f?w=300";
    const rating = p.personalRating > 0 ? `★ ${p.personalRating}/10` : 'Unrated';
    
    completedShelfCards += `
      <a class="internal-link shelf-card" href="${p.file.path}" style="background-image: url('${coverUrl}');">
        <div class="card-gradient"></div>
        <div class="card-badge badge-rating">${rating}</div>
        <div class="card-content">
          <div class="card-title">${titleText}</div>
        </div>
      </a>
    `;
  });
}

// Recent Anime Updates list
const recentAnimeUpdates = sortDescByDate(animePages, p => p.lastWatched || p.file.mtime).slice(0, 3);
let recentAnimeUpdatesHTML = "";
recentAnimeUpdates.forEach(p => {
  const titleText = p.englishTitle || p.title || p.file.name;
  const coverUrl = p.image || "https://images.unsplash.com/photo-1607604276583-eef5d076aa5f?w=100";
  const statusText = p.status || "Plan to Watch";
  
  let progressStr = "";
  if (p.status === "Currently Watching") {
    progressStr = `• Watching ${p.currentEpisode || 0}/${p.episodes || '?'}`;
  } else if (p.status === "Completed") {
    progressStr = `• Completed ${p.episodes || 1}/${p.episodes || 1}`;
  } else {
    progressStr = `• ${statusText}`;
  }
  
  const ratingStr = p.personalRating > 0 ? `• Scored ${p.personalRating}` : "• Scored -";
  const relativeTime = moment(p.lastWatched || p.file.mtime).calendar();
  
  recentAnimeUpdatesHTML += `
    <div class="update-row">
      <img src="${coverUrl}" class="update-thumb" />
      <div class="update-meta">
        <a class="internal-link update-title" href="${p.file.path}">${titleText}</a>
        <div class="update-details">${statusText} ${progressStr} ${ratingStr}</div>
      </div>
      <div class="update-time">${relativeTime}</div>
    </div>
  `;
});

// Recent Manga Updates list
const recentMangaUpdates = sortDescByDate(mangaPages, p => p.lastWatched || p.file.mtime).slice(0, 3);
let recentMangaUpdatesHTML = "";
recentMangaUpdates.forEach(p => {
  const titleText = p.englishTitle || p.title || p.file.name;
  const coverUrl = p.image || "https://images.unsplash.com/photo-1607604276583-eef5d076aa5f?w=100";
  const statusText = p.status || "Plan to Read";
  
  let progressStr = "";
  if (p.status === "Currently Reading") {
    progressStr = `• Reading ${p.currentChapter || 0}/${p.chapters || '?'}`;
  } else if (p.status === "Completed") {
    progressStr = `• Completed ${p.chapters || 0}/${p.chapters || 0}`;
  } else {
    progressStr = `• ${statusText}`;
  }
  
  const ratingStr = p.personalRating > 0 ? `• Scored ${p.personalRating}` : "• Scored -";
  const relativeTime = moment(p.lastWatched || p.file.mtime).calendar();
  
  recentMangaUpdatesHTML += `
    <div class="update-row">
      <img src="${coverUrl}" class="update-thumb" />
      <div class="update-meta">
        <a class="internal-link update-title" href="${p.file.path}">${titleText}</a>
        <div class="update-details">${statusText} ${progressStr} ${ratingStr}</div>
      </div>
      <div class="update-time">${relativeTime}</div>
    </div>
  `;
});

// Recent Game Updates list
const recentGameUpdates = sortDescByDate(gamePages, p => p.dateStarted || p.file.mtime).slice(0, 3);
let recentGameUpdatesHTML = "";
recentGameUpdates.forEach(p => {
  const titleText = p.englishTitle || p.title || p.file.name;
  const coverUrl = p.image || "https://images.unsplash.com/photo-1607604276583-eef5d076aa5f?w=100";
  const statusText = p.status || "Plan to Play";
  const ratingStr = p.personalRating > 0 ? `• Scored ${p.personalRating}` : "• Scored -";
  const relativeTime = moment(p.dateStarted || p.file.mtime).calendar();
  
  recentGameUpdatesHTML += `
    <div class="update-row">
      <img src="${coverUrl}" class="update-thumb" />
      <div class="update-meta">
        <a class="internal-link update-title" href="${p.file.path}">${titleText}</a>
        <div class="update-details">${statusText} ${ratingStr}</div>
      </div>
      <div class="update-time">${relativeTime}</div>
    </div>
  `;
});

// Recent Series Updates list
const recentSeriesUpdates = sortDescByDate(seriesPages, p => p.lastWatched || p.file.mtime).slice(0, 3);
let recentSeriesUpdatesHTML = "";
recentSeriesUpdates.forEach(p => {
  const titleText = p.englishTitle || p.title || p.file.name;
  const coverUrl = p.image || "https://images.unsplash.com/photo-1607604276583-eef5d076aa5f?w=100";
  const statusText = p.status || "Plan to Watch";
  
  let progressStr = "";
  if (p.status === "Currently Watching") {
    progressStr = `• Watching ${p.currentEpisode || 0}/${p.episodes || '?'}`;
  } else if (p.status === "Completed") {
    progressStr = `• Completed ${p.episodes || 1}/${p.episodes || 1}`;
  } else {
    progressStr = `• ${statusText}`;
  }
  
  const ratingStr = p.personalRating > 0 ? `• Scored ${p.personalRating}` : "• Scored -";
  const relativeTime = moment(p.lastWatched || p.file.mtime).calendar();
  
  recentSeriesUpdatesHTML += `
    <div class="update-row">
      <img src="${coverUrl}" class="update-thumb" />
      <div class="update-meta">
        <a class="internal-link update-title" href="${p.file.path}">${titleText}</a>
        <div class="update-details">${statusText} ${progressStr} ${ratingStr}</div>
      </div>
      <div class="update-time">${relativeTime}</div>
    </div>
  `;
});

// Recent Movie Updates list
const recentMovieUpdates = sortDescByDate(moviePages, p => p.lastWatched || p.file.mtime).slice(0, 3);
let recentMovieUpdatesHTML = "";
recentMovieUpdates.forEach(p => {
  const titleText = p.englishTitle || p.title || p.file.name;
  const coverUrl = p.image || "https://images.unsplash.com/photo-1607604276583-eef5d076aa5f?w=100";
  const statusText = p.status || "Plan to Watch";
  const ratingStr = p.personalRating > 0 ? `• Scored ${p.personalRating}` : "• Scored -";
  const relativeTime = moment(p.lastWatched || p.file.mtime).calendar();
  
  recentMovieUpdatesHTML += `
    <div class="update-row">
      <img src="${coverUrl}" class="update-thumb" />
      <div class="update-meta">
        <a class="internal-link update-title" href="${p.file.path}">${titleText}</a>
        <div class="update-details">${statusText} ${ratingStr}</div>
      </div>
      <div class="update-time">${relativeTime}</div>
    </div>
  `;
});

// Final HTML Template Injection
dv.container.innerHTML = `
<style>
/* Force the Obsidian preview sizer and rendered container to take the entire screen width */
.markdown-preview-view.media-dashboard .markdown-preview-sizer,
.markdown-rendered.media-dashboard,
.media-dashboard .markdown-source-view.mod-cm6 .cm-editor {
  max-width: 100% !important;
  width: 100% !important;
  padding-left: 12px !important;
  padding-right: 12px !important;
}

.obs-media-dashboard {
  --bg-primary: #0a0a0c;
  --bg-secondary: #111116;
  --bg-tertiary: #191922;
  --accent: #ff6b35;
  --accent-rgb: 255, 107, 53;
  --accent-muted: rgba(255, 107, 53, 0.15);
  --text-main: #f1f2f6;
  --text-muted: #7f8fa6;
  --border-color: rgba(255, 255, 255, 0.05);
  --font-stack: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  
  font-family: var(--font-stack);
  background-color: var(--bg-primary);
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='56' height='100' viewBox='0 0 56 100'%3E%3Cpath d='M28 66L0 50L0 16L28 0L56 16L56 50L28 66zm0 2L56 82L56 98L28 98L0 98L0 82L28 68z' fill='%23ff6b35' fill-opacity='0.02' stroke='%23ff6b35' stroke-opacity='0.08' stroke-width='1.2'/%3E%3C/svg%3E");
  color: var(--text-main);
  padding: 24px;
  border-radius: 12px;
  border: 1px solid var(--border-color);
  display: flex;
  gap: 24px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5);
  margin-top: 10px;
  width: 100%;
  box-sizing: border-box;
}

@media (max-width: 1024px) {
  .obs-media-dashboard {
    flex-direction: column;
  }
  .dashboard-sidebar {
    width: 100% !important;
  }
}

/* Sidebar Styling */
.dashboard-sidebar {
  width: 260px;
  flex-shrink: 0;
  display: flex;
  flex-direction: column;
  background: var(--bg-secondary);
  border: 1px solid var(--border-color);
  border-radius: 10px;
  padding: 20px;
  box-sizing: border-box;
}
.sidebar-header {
  font-size: 14px;
  font-weight: bold;
  letter-spacing: 1px;
  text-transform: uppercase;
  color: var(--text-main);
  margin-bottom: 16px;
  display: flex;
  align-items: center;
  gap: 6px;
}
.status-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--accent);
  box-shadow: 0 0 8px var(--accent);
  display: inline-block;
}
.avatar-frame {
  position: relative;
  width: 100%;
  border-radius: 8px;
  overflow: hidden;
  border: 2px solid var(--border-color);
  aspect-ratio: 3/4;
  margin-bottom: 12px;
}
.avatar-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;
}
.avatar-frame:hover .avatar-image {
  transform: scale(1.05);
}
.avatar-social {
  display: flex;
  justify-content: space-between;
  background: rgba(0,0,0,0.4);
  padding: 6px 12px;
  border-radius: 6px;
  margin-bottom: 16px;
  border: 1px solid var(--border-color);
}
.social-icon {
  font-size: 14px;
  color: var(--text-muted);
  cursor: pointer;
  transition: color 0.2s;
}
.social-icon:hover {
  color: var(--accent);
}
.sidebar-info-row {
  display: flex;
  justify-content: space-between;
  font-size: 12px;
  padding: 6px 0;
  border-bottom: 1px dashed var(--border-color);
}
.sidebar-info-label {
  color: var(--text-muted);
}
.sidebar-info-val {
  font-weight: 500;
  color: var(--text-main);
}
.list-button-group {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px;
  margin: 16px 0;
}
.list-pill-btn {
  display: block;
  text-align: center;
  background: var(--bg-tertiary);
  border: 1px solid var(--border-color);
  color: var(--text-main) !important;
  font-weight: bold;
  font-size: 11px;
  padding: 8px 0;
  border-radius: 20px;
  text-decoration: none !important;
  transition: all 0.2s ease;
  box-shadow: 0 2px 5px rgba(0,0,0,0.2);
}
.list-pill-btn:hover {
  border-color: var(--accent);
  background: var(--accent-muted);
  box-shadow: 0 4px 10px rgba(var(--accent-rgb), 0.2);
  transform: translateY(-1px);
}

/* Sidebar Menu */
.sidebar-menu {
  display: flex;
  flex-direction: column;
  gap: 4px;
  margin-top: 10px;
}
.menu-item {
  display: block;
  padding: 8px 12px;
  font-size: 12.5px;
  color: var(--text-muted) !important;
  text-decoration: none !important;
  border-left: 2px solid transparent;
  transition: all 0.2s;
  border-radius: 0 4px 4px 0;
}
.menu-item:hover, .menu-item.active {
  color: var(--text-main) !important;
  background: rgba(255,255,255,0.02);
  border-left-color: var(--accent);
}
.menu-row {
  display: flex;
  justify-content: space-between;
  padding: 6px 12px;
  font-size: 12px;
  color: var(--text-muted);
}
.menu-row-val {
  font-weight: bold;
  color: var(--text-main);
}
.menu-row-val.highlight {
  color: var(--accent);
}

/* Friends Avatar */
.friend-avatar {
  width: 42px;
  height: 42px;
  border-radius: 50%;
  object-fit: cover;
  border: 2px solid var(--border-color);
  transition: all 0.2s;
  cursor: pointer;
}
.friend-avatar:hover {
  border-color: var(--accent);
  transform: translateY(-2px);
}

/* Main Panel Styling */
.dashboard-main {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 24px;
  min-width: 0;
}
.dashboard-banner {
  width: 100%;
  height: 220px;
  border-radius: 10px;
  background-image: url('https://cdn.myanimelist.net/images/clubs/2/233075.jpg');
  background-size: cover;
  background-position: center 20%;
  border: 1px solid var(--border-color);
  position: relative;
  box-shadow: inset 0 -80px 100px rgba(0,0,0,0.8), 0 4px 15px rgba(0,0,0,0.3);
}
.banner-title {
  position: absolute;
  bottom: 20px;
  left: 24px;
  font-size: 24px;
  font-weight: 800;
  letter-spacing: 0.5px;
  text-shadow: 0 2px 10px rgba(0,0,0,0.8);
}
.banner-badge {
  position: absolute;
  top: 16px;
  right: 16px;
  background: rgba(0,0,0,0.6);
  border: 1px solid var(--border-color);
  backdrop-filter: blur(8px);
  padding: 4px 10px;
  border-radius: 4px;
  font-size: 11px;
  color: var(--text-muted);
}

/* Section Styling */
.section-container {
  display: flex;
  flex-direction: column;
  gap: 12px;
}
.section-header-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 6px;
}
.section-title-badge {
  background: var(--bg-secondary);
  border: 1px solid var(--border-color);
  padding: 8px 16px;
  border-radius: 6px;
  font-size: 13px;
  font-weight: bold;
  color: var(--accent);
  letter-spacing: 0.5px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.2);
}
.section-nav-links {
  display: flex;
  gap: 12px;
  font-size: 11px;
}
.sec-link {
  color: var(--text-muted) !important;
  text-decoration: none !important;
  transition: color 0.2s;
}
.sec-link:hover {
  color: var(--accent) !important;
}

/* Card Shelves Styling */
.visual-shelf-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(130px, 1fr));
  gap: 12px;
}
.shelf-card {
  position: relative;
  overflow: hidden;
  border-radius: 8px;
  aspect-ratio: 2.3/3.2;
  background-size: cover;
  background-position: center;
  border: 1px solid var(--border-color);
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  text-decoration: none !important;
  transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
  box-shadow: 0 4px 10px rgba(0,0,0,0.4);
  cursor: pointer;
}
.shelf-card:hover {
  transform: translateY(-6px);
  box-shadow: 0 8px 20px rgba(var(--accent-rgb), 0.15);
  border-color: var(--accent);
}
.card-gradient {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  background: linear-gradient(to top, rgba(0,0,0,0.92) 0%, rgba(0,0,0,0.3) 50%, rgba(0,0,0,0) 100%);
  z-index: 1;
}
.card-badge {
  position: absolute;
  top: 8px;
  right: 8px;
  font-size: 9px;
  font-weight: 900;
  padding: 3px 6px;
  border-radius: 4px;
  z-index: 2;
  box-shadow: 0 2px 4px rgba(0,0,0,0.3);
  letter-spacing: 0.5px;
}
.badge-anime { background-color: #ff6b35; color: #fff; }
.badge-manga { background-color: #264380; color: #fff; }
.badge-game { background-color: #2db039; color: #fff; }
.badge-series { background-color: #9b59b6; color: #fff; }
.badge-movie { background-color: #e74c3c; color: #fff; }
.badge-rating { background-color: #f1c40f; color: #111; }
.card-content {
  padding: 10px;
  z-index: 2;
  position: relative;
}
.card-title {
  font-size: 12px;
  font-weight: bold;
  color: var(--text-main);
  line-height: 1.25;
  margin-bottom: 2px;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
}
.card-progress {
  font-size: 10px;
  color: var(--accent);
  font-weight: 600;
}
.empty-shelf-placeholder {
  grid-column: 1 / -1;
  text-align: center;
  color: var(--text-muted);
  padding: 32px;
  background: rgba(255,255,255,0.01);
  border-radius: 8px;
  border: 1px dashed var(--border-color);
  font-size: 12px;
}

/* Statistics Layout */
.stats-card {
  background: var(--bg-secondary);
  border: 1px solid var(--border-color);
  border-radius: 10px;
  padding: 20px;
  display: grid;
  grid-template-columns: 1.1fr 0.9fr;
  gap: 24px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}
@media (max-width: 768px) {
  .stats-card {
    grid-template-columns: 1fr;
  }
}
.stats-header-row {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  border-bottom: 1px solid var(--border-color);
  padding-bottom: 8px;
  margin-bottom: 12px;
}
.stats-title {
  font-size: 15px;
  font-weight: bold;
  color: var(--text-main);
}
.stats-overview-block {
  display: flex;
  gap: 20px;
  margin-bottom: 12px;
}
.stats-ov-item {
  display: flex;
  flex-direction: column;
}
.stats-ov-lbl {
  font-size: 11px;
  color: var(--text-muted);
  text-transform: uppercase;
}
.stats-ov-val {
  font-size: 18px;
  font-weight: 800;
  color: var(--text-main);
}
.stats-ov-val.accent {
  color: var(--accent);
}

/* Proportional Progress Bar styling */
.progress-bar-container {
  display: flex;
  height: 9px;
  border-radius: 5px;
  overflow: hidden;
  background: rgba(0,0,0,0.4);
  margin: 12px 0 16px 0;
  border: 1px solid rgba(255,255,255,0.02);
}
.progress-segment {
  height: 100%;
  cursor: pointer;
  transition: opacity 0.2s;
}
.progress-segment:hover {
  opacity: 0.85;
}
.progress-segment.watching { background-color: #2db039; }
.progress-segment.completed { background-color: #264380; }
.progress-segment.onhold { background-color: #f1c40f; }
.progress-segment.dropped { background-color: #a12f2f; }
.progress-segment.plantowatch { background-color: #7d7d7d; }

/* Dynamic breakdown Grid */
.breakdown-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  row-gap: 8px;
  column-gap: 16px;
  font-size: 12px;
}
.breakdown-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.dot-lbl {
  display: flex;
  align-items: center;
  gap: 8px;
  color: var(--text-muted);
}
.color-dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  display: inline-block;
}
.dot-val {
  font-weight: bold;
  color: var(--text-main);
}

/* Update Row Styling */
.update-row {
  display: flex;
  gap: 12px;
  align-items: center;
  padding: 8px 0;
  border-bottom: 1px solid rgba(255,255,255,0.03);
}
.update-row:last-child {
  border-bottom: none;
  padding-bottom: 0;
}
.update-thumb {
  width: 38px;
  height: 52px;
  object-fit: cover;
  border-radius: 4px;
  border: 1px solid var(--border-color);
  flex-shrink: 0;
}
.update-meta {
  flex: 1;
  min-width: 0;
}
.update-title {
  font-size: 12.5px;
  font-weight: bold;
  color: var(--text-main) !important;
  text-decoration: none !important;
  display: block;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  margin-bottom: 2px;
}
.update-title:hover {
  color: var(--accent) !important;
}
.update-details {
  font-size: 10.5px;
  color: var(--text-muted);
}
.update-time {
  font-size: 10.5px;
  color: var(--text-muted);
  text-align: right;
  white-space: nowrap;
}
</style>

<div class="obs-media-dashboard">
  <!-- Left Column: Profile Sidebar -->
  <div class="dashboard-sidebar">
    <div class="sidebar-header">
      <span class="status-dot"></span>
      <span>SENPAI778's Profile</span>
    </div>
    
    <div class="avatar-frame">
      <img src="https://static.wikia.nocookie.net/obluda/images/f/ff/Johan.png/revision/latest?cb=20250427000122" class="avatar-image" alt="Johan Liebert" />
    </div>
    
    <div class="avatar-social">
      <span class="social-icon">💬</span>
      <span class="social-icon">✉️</span>
      <span class="social-icon">👤➕</span>
      <span class="social-social">🎁</span>
    </div>
    
    <div class="sidebar-info-row">
      <span class="sidebar-info-label">Last Online</span>
      <span class="sidebar-info-val">Today, 10:53 AM</span>
    </div>
    <div class="sidebar-info-row">
      <span class="sidebar-info-label">Joined</span>
      <span class="sidebar-info-val">Oct 10, 2021</span>
    </div>
    
    <div class="list-button-group">
      <a class="list-pill-btn internal-link" href="Anime View.base">Anime List</a>
      <a class="list-pill-btn internal-link" href="Manga View.base">Manga List</a>
      <a class="list-pill-btn internal-link" href="Game View.base">Game List</a>
      <a class="list-pill-btn internal-link" href="Movie View.base">Movie List</a>
      <a class="list-pill-btn internal-link" style="grid-column: span 2;" href="Series View.base">Series List</a>
    </div>
    
    <div class="sidebar-menu">
      <div class="menu-item active">Statistics</div>
      <a class="menu-item" href="#anime-stats-section">📺 Anime Statistics</a>
      <a class="menu-item" href="#manga-stats-section">📖 Manga Statistics</a>
      <a class="menu-item" href="#game-stats-section">🎮 Game Statistics</a>
      <a class="menu-item" href="#series-stats-section">🍿 Series Statistics</a>
      <a class="menu-item" href="#movie-stats-section">🎥 Movie Statistics</a>
      
      <div style="height: 1px; background: var(--border-color); margin: 8px 0;"></div>
      
      <div class="menu-row">
        <span>Forum Posts</span>
        <span class="menu-row-val highlight">1</span>
      </div>
      <div class="menu-row">
        <span>Reviews</span>
        <span class="menu-row-val">0</span>
      </div>
      <div class="menu-row">
        <span>Interest Stacks</span>
        <span class="menu-row-val">0</span>
      </div>
      <div class="menu-row">
        <span>Clubs</span>
        <span class="menu-row-val highlight">8</span>
      </div>
    </div>
    
    <!-- Friends Grid -->
    <div style="margin-top: 20px;">
      <div style="font-size: 11px; font-weight: bold; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 10px;">Friends (2)</div>
      <div style="display: flex; gap: 10px;">
        <div style="text-align: center; width: 44px;">
          <img src="https://cdn.myanimelist.net/images/characters/9/310307.jpg" class="friend-avatar" title="Luffy" />
          <div style="font-size: 9px; color: var(--text-muted); text-overflow: ellipsis; overflow: hidden; white-space: nowrap; margin-top: 3px;">Luffy</div>
        </div>
        <div style="text-align: center; width: 44px;">
          <img src="https://cdn.myanimelist.net/images/characters/9/393282.jpg" class="friend-avatar" title="Tanjirou" />
          <div style="font-size: 9px; color: var(--text-muted); text-overflow: ellipsis; overflow: hidden; white-space: nowrap; margin-top: 3px;">Tanjirou</div>
        </div>
      </div>
    </div>
  </div>
  
  <!-- Right Column: Media panels -->
  <div class="dashboard-main">
    <!-- Banner -->
    <div class="dashboard-banner">
      <div class="banner-badge">Egghead/Wano Arc</div>
      <div class="banner-title">🌌 HOME MEDIA DASHBOARD</div>
    </div>
    
    <!-- Section: Currently Watching/Reading/Playing -->
    <div class="section-container">
      <div class="section-header-row">
        <div class="section-title-badge">🚀 CURRENTLY CONSUMING</div>
      </div>
      <div class="visual-shelf-grid">
        ${activeShelfCards}
      </div>
    </div>
    
    <!-- Section: Recently Completed -->
    <div class="section-container">
      <div class="section-header-row">
        <div class="section-title-badge">⏱️ RECENTLY COMPLETED MEDIA</div>
      </div>
      <div class="visual-shelf-grid">
        ${completedShelfCards}
      </div>
    </div>
    
    <!-- Section: Anime Statistics -->
    <div class="section-container" id="anime-stats-section">
      <div class="section-header-row">
        <div class="section-title-badge">📺 ANIME STATISTICS</div>
        <div class="section-nav-links">
          <a class="sec-link internal-link" href="anime/">All Anime Stats</a>
          <span style="color: var(--border-color);">|</span>
          <a class="sec-link internal-link" href="movies/">Anime Movies</a>
        </div>
      </div>
      <div class="stats-card">
        <!-- Left: breakdown -->
        <div>
          <div class="stats-overview-block">
            <div class="stats-ov-item">
              <span class="stats-ov-lbl">Days watched</span>
              <span class="stats-ov-val accent">${aniDays}</span>
            </div>
            <div class="stats-ov-item">
              <span class="stats-ov-lbl">Mean Score</span>
              <span class="stats-ov-val">${aniMean}</span>
            </div>
          </div>
          
          ${makeProgressBar(aniWatching, aniCompleted, aniOnHold, aniDropped, aniPlan)}
          
          <div class="breakdown-grid">
            <div class="breakdown-row">
              <span class="dot-lbl"><span class="color-dot" style="background-color: #2db039;"></span>Watching</span>
              <span class="dot-val">${aniWatching}</span>
            </div>
            <div class="breakdown-row">
              <span class="dot-lbl">Total Entries</span>
              <span class="dot-val">${aniTotal}</span>
            </div>
            <div class="breakdown-row">
              <span class="dot-lbl"><span class="color-dot" style="background-color: #264380;"></span>Completed</span>
              <span class="dot-val">${aniCompleted}</span>
            </div>
            <div class="breakdown-row">
              <span class="dot-lbl">Episodes Watched</span>
              <span class="dot-val">${aniEps}</span>
            </div>
            <div class="breakdown-row">
              <span class="dot-lbl"><span class="color-dot" style="background-color: #f1c40f;"></span>On-Hold</span>
              <span class="dot-val">${aniOnHold}</span>
            </div>
            <div></div>
            <div class="breakdown-row">
              <span class="dot-lbl"><span class="color-dot" style="background-color: #a12f2f;"></span>Dropped</span>
              <span class="dot-val">${aniDropped}</span>
            </div>
            <div></div>
            <div class="breakdown-row">
              <span class="dot-lbl"><span class="color-dot" style="background-color: #7d7d7d;"></span>Plan to Watch</span>
              <span class="dot-val">${aniPlan}</span>
            </div>
          </div>
        </div>
        
        <!-- Right: updates -->
        <div>
          <div class="stats-header-row" style="margin-bottom: 8px;">
            <div style="font-size: 11.5px; font-weight: bold; color: var(--text-muted); text-transform: uppercase;">Last Anime Updates</div>
          </div>
          <div style="display: flex; flex-direction: column;">
            ${recentAnimeUpdatesHTML}
          </div>
        </div>
      </div>
    </div>
    
    <!-- Section: Manga Statistics -->
    <div class="section-container" id="manga-stats-section">
      <div class="section-header-row">
        <div class="section-title-badge">📖 MANGA STATISTICS</div>
        <div class="section-nav-links">
          <a class="sec-link internal-link" href="manga/">All Manga Stats</a>
        </div>
      </div>
      <div class="stats-card">
        <!-- Left: breakdown -->
        <div>
          <div class="stats-overview-block">
            <div class="stats-ov-item">
              <span class="stats-ov-lbl">Days Read</span>
              <span class="stats-ov-val accent">${manDays}</span>
            </div>
            <div class="stats-ov-item">
              <span class="stats-ov-lbl">Mean Score</span>
              <span class="stats-ov-val">${manMean}</span>
            </div>
          </div>
          
          ${makeProgressBar(manReading, manCompleted, manOnHold, manDropped, manPlan)}
          
          <div class="breakdown-grid">
            <div class="breakdown-row">
              <span class="dot-lbl"><span class="color-dot" style="background-color: #2db039;"></span>Reading</span>
              <span class="dot-val">${manReading}</span>
            </div>
            <div class="breakdown-row">
              <span class="dot-lbl">Total Entries</span>
              <span class="dot-val">${manTotal}</span>
            </div>
            <div class="breakdown-row">
              <span class="dot-lbl"><span class="color-dot" style="background-color: #264380;"></span>Completed</span>
              <span class="dot-val">${manCompleted}</span>
            </div>
            <div class="breakdown-row">
              <span class="dot-lbl">Chapters Read</span>
              <span class="dot-val">${manChaps}</span>
            </div>
            <div class="breakdown-row">
              <span class="dot-lbl"><span class="color-dot" style="background-color: #f1c40f;"></span>On-Hold</span>
              <span class="dot-val">${manOnHold}</span>
            </div>
            <div class="breakdown-row">
              <span class="dot-lbl">Volumes Read</span>
              <span class="dot-val">${manVols}</span>
            </div>
            <div class="breakdown-row">
              <span class="dot-lbl"><span class="color-dot" style="background-color: #a12f2f;"></span>Dropped</span>
              <span class="dot-val">${manDropped}</span>
            </div>
            <div></div>
            <div class="breakdown-row">
              <span class="dot-lbl"><span class="color-dot" style="background-color: #7d7d7d;"></span>Plan to Read</span>
              <span class="dot-val">${manPlan}</span>
            </div>
          </div>
        </div>
        
        <!-- Right: updates -->
        <div>
          <div class="stats-header-row" style="margin-bottom: 8px;">
            <div style="font-size: 11.5px; font-weight: bold; color: var(--text-muted); text-transform: uppercase;">Last Manga Updates</div>
          </div>
          <div style="display: flex; flex-direction: column;">
            ${recentMangaUpdatesHTML}
          </div>
        </div>
      </div>
    </div>

    <!-- Section: Game Statistics -->
    <div class="section-container" id="game-stats-section">
      <div class="section-header-row">
        <div class="section-title-badge">🎮 GAME STATISTICS</div>
        <div class="section-nav-links">
          <a class="sec-link internal-link" href="games/">All Games</a>
        </div>
      </div>
      <div class="stats-card">
        <!-- Left: breakdown -->
        <div>
          <div class="stats-overview-block">
            <div class="stats-ov-item">
              <span class="stats-ov-lbl">Days Played</span>
              <span class="stats-ov-val accent">${gameDays}</span>
            </div>
            <div class="stats-ov-item">
              <span class="stats-ov-lbl">Mean Score</span>
              <span class="stats-ov-val">${gameMean}</span>
            </div>
          </div>
          
          ${makeProgressBar(gamePlaying, gameCompleted, 0, gameDropped, gamePlan)}
          
          <div class="breakdown-grid">
            <div class="breakdown-row">
              <span class="dot-lbl"><span class="color-dot" style="background-color: #2db039;"></span>Playing</span>
              <span class="dot-val">${gamePlaying}</span>
            </div>
            <div class="breakdown-row">
              <span class="dot-lbl">Total Entries</span>
              <span class="dot-val">${gameTotal}</span>
            </div>
            <div class="breakdown-row">
              <span class="dot-lbl"><span class="color-dot" style="background-color: #264380;"></span>Completed</span>
              <span class="dot-val">${gameCompleted}</span>
            </div>
            <div></div>
            <div class="breakdown-row">
              <span class="dot-lbl"><span class="color-dot" style="background-color: #a12f2f;"></span>Dropped</span>
              <span class="dot-val">${gameDropped}</span>
            </div>
            <div></div>
            <div class="breakdown-row">
              <span class="dot-lbl"><span class="color-dot" style="background-color: #7d7d7d;"></span>Plan to Play</span>
              <span class="dot-val">${gamePlan}</span>
            </div>
          </div>
        </div>
        
        <!-- Right: updates -->
        <div>
          <div class="stats-header-row" style="margin-bottom: 8px;">
            <div style="font-size: 11.5px; font-weight: bold; color: var(--text-muted); text-transform: uppercase;">Last Game Updates</div>
          </div>
          <div style="display: flex; flex-direction: column;">
            ${recentGameUpdatesHTML}
          </div>
        </div>
      </div>
    </div>
    
    <!-- Section: Series Statistics -->
    <div class="section-container" id="series-stats-section">
      <div class="section-header-row">
        <div class="section-title-badge">🍿 SERIES STATISTICS</div>
        <div class="section-nav-links">
          <a class="sec-link internal-link" href="Series View.base">All Series Stats</a>
        </div>
      </div>
      <div class="stats-card">
        <!-- Left: breakdown -->
        <div>
          <div class="stats-overview-block">
            <div class="stats-ov-item">
              <span class="stats-ov-lbl">Days watched</span>
              <span class="stats-ov-val accent">${serDays}</span>
            </div>
            <div class="stats-ov-item">
              <span class="stats-ov-lbl">Mean Score</span>
              <span class="stats-ov-val">${serMean}</span>
            </div>
          </div>
          
          ${makeProgressBar(serWatching, serCompleted, serOnHold, serDropped, serPlan)}
          
          <div class="breakdown-grid">
            <div class="breakdown-row">
              <span class="dot-lbl"><span class="color-dot" style="background-color: #2db039;"></span>Watching</span>
              <span class="dot-val">${serWatching}</span>
            </div>
            <div class="breakdown-row">
              <span class="dot-lbl">Total Entries</span>
              <span class="dot-val">${serTotal}</span>
            </div>
            <div class="breakdown-row">
              <span class="dot-lbl"><span class="color-dot" style="background-color: #264380;"></span>Completed</span>
              <span class="dot-val">${serCompleted}</span>
            </div>
            <div class="breakdown-row">
              <span class="dot-lbl">Episodes Watched</span>
              <span class="dot-val">${serEps}</span>
            </div>
            <div class="breakdown-row">
              <span class="dot-lbl"><span class="color-dot" style="background-color: #f1c40f;"></span>On-Hold</span>
              <span class="dot-val">${serOnHold}</span>
            </div>
            <div></div>
            <div class="breakdown-row">
              <span class="dot-lbl"><span class="color-dot" style="background-color: #a12f2f;"></span>Dropped</span>
              <span class="dot-val">${serDropped}</span>
            </div>
            <div></div>
            <div class="breakdown-row">
              <span class="dot-lbl"><span class="color-dot" style="background-color: #7d7d7d;"></span>Plan to Watch</span>
              <span class="dot-val">${serPlan}</span>
            </div>
          </div>
        </div>
        
        <!-- Right: updates -->
        <div>
          <div class="stats-header-row" style="margin-bottom: 8px;">
            <div style="font-size: 11.5px; font-weight: bold; color: var(--text-muted); text-transform: uppercase;">Last Series Updates</div>
          </div>
          <div style="display: flex; flex-direction: column;">
            ${recentSeriesUpdatesHTML}
          </div>
        </div>
      </div>
    </div>

    <!-- Section: Movie Statistics -->
    <div class="section-container" id="movie-stats-section">
      <div class="section-header-row">
        <div class="section-title-badge">🎥 MOVIE STATISTICS</div>
        <div class="section-nav-links">
          <a class="sec-link internal-link" href="Movie View.base">All Movie Stats</a>
        </div>
      </div>
      <div class="stats-card">
        <!-- Left: breakdown -->
        <div>
          <div class="stats-overview-block">
            <div class="stats-ov-item">
              <span class="stats-ov-lbl">Days watched</span>
              <span class="stats-ov-val accent">${movDays}</span>
            </div>
            <div class="stats-ov-item">
              <span class="stats-ov-lbl">Mean Score</span>
              <span class="stats-ov-val">${movMean}</span>
            </div>
          </div>
          
          ${makeProgressBar(movWatching, movCompleted, movOnHold, movDropped, movPlan)}
          
          <div class="breakdown-grid">
            <div class="breakdown-row">
              <span class="dot-lbl"><span class="color-dot" style="background-color: #2db039;"></span>Watching</span>
              <span class="dot-val">${movWatching}</span>
            </div>
            <div class="breakdown-row">
              <span class="dot-lbl">Total Entries</span>
              <span class="dot-val">${movTotal}</span>
            </div>
            <div class="breakdown-row">
              <span class="dot-lbl"><span class="color-dot" style="background-color: #264380;"></span>Completed</span>
              <span class="dot-val">${movCompleted}</span>
            </div>
            <div></div>
            <div class="breakdown-row">
              <span class="dot-lbl"><span class="color-dot" style="background-color: #f1c40f;"></span>On-Hold</span>
              <span class="dot-val">${movOnHold}</span>
            </div>
            <div></div>
            <div class="breakdown-row">
              <span class="dot-lbl"><span class="color-dot" style="background-color: #a12f2f;"></span>Dropped</span>
              <span class="dot-val">${movDropped}</span>
            </div>
            <div></div>
            <div class="breakdown-row">
              <span class="dot-lbl"><span class="color-dot" style="background-color: #7d7d7d;"></span>Plan to Watch</span>
              <span class="dot-val">${movPlan}</span>
            </div>
          </div>
        </div>
        
        <!-- Right: updates -->
        <div>
          <div class="stats-header-row" style="margin-bottom: 8px;">
            <div style="font-size: 11.5px; font-weight: bold; color: var(--text-muted); text-transform: uppercase;">Last Movie Updates</div>
          </div>
          <div style="display: flex; flex-direction: column;">
            ${recentMovieUpdatesHTML}
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
`;
```
