---
tags: [ui, page, home, dashboard, state-management, client, frontend]
---

# Page: Home / Main Dashboard Controller

This page acts as the main controller for authenticated students, located at `src/app/page.tsx` and mapped to `/`. It manages the state, loads student configuration files, coordinates active views (tabs), and triggers overlays (modals).

- **File Link**: [page.tsx](file:///d:/02_CODE/04_TEST/Routine/src/app/page.tsx)
- **Backlinks**: [[index]], [[ARCHITECTURE]], [[DESIGN]], [[component_dashboard_view]], [[component_calendar_view]], [[component_setup_view]], [[component_analytics_view]]

---

## 1. State Management Core

The page maintains the state that feeds into all rendering sub-views:

```typescript
// Active Navigation Tab
const [activeTab, setActiveTab] = useState<'dashboard' | 'calendar' | 'courses' | 'analytics' | 'settings'>('dashboard');

// Session & Configuration State
const [user, setUser] = useState<any>(null);
const [isLoadingUser, setIsLoadingUser] = useState(true);
const [currentDate, setCurrentDate] = useState<string>('');

// Roster Data
const [courses, setCourses] = useState<any[]>([]);
const [weeklySlots, setWeeklySlots] = useState<any[]>([]);
const [calendarData, setCalendarData] = useState<any>(null);
const [analyticsData, setAnalyticsData] = useState<any>(null);
const [announcements, setAnnouncements] = useState<any[]>([]);
```

---

## 2. Bootstrapping Lifecycle

On initial component mount, the controller triggers a single bootstrap request `/api/init` to prevent waterfall requests:

```typescript
useEffect(() => {
  const today = new Date();
  const yyyy = today.getFullYear();
  const mm = String(today.getMonth() + 1).padStart(2, '0');
  const dd = String(today.getDate()).padStart(2, '0');
  const todayStr = `${yyyy}-${mm}-${dd}`;
  
  setCurrentDate(todayStr);
  setViewDate(todayStr);

  const startOfMonth = `${yyyy}-${mm}-01`;
  setCustomRange({ start: startOfMonth, end: todayStr });

  fetchInitData(todayStr);
}, []);

const fetchInitData = async (todayStr: string) => {
  setIsLoadingUser(true);
  try {
    const focusDate = new Date(todayStr);
    const day = focusDate.getDay();
    const diff = focusDate.getDate() - day;
    const sun = new Date(focusDate);
    sun.setDate(diff);
    const startStr = sun.toISOString().split('T')[0];
    const sat = new Date(sun);
    sat.setDate(sun.getDate() + 6);
    const endStr = sat.toISOString().split('T')[0];

    const res = await fetch(`/api/init?startDate=${startStr}&endDate=${endStr}&todayDate=${todayStr}`);
    if (res.ok) {
      const data = await res.json();
      setUser(data.user);
      setCourses(data.courses);
      setWeeklySlots(data.weeklySlots);
      setCalendarData(data.calendarData);
      setAnnouncements(data.announcements);
    }
  } catch (err) {
    console.error('Connection error during app bootstrap:', err);
  } finally {
    setIsLoadingUser(false);
  }
};
```

---

## 3. Custom Scrolling Lock

When modals open, the controller locks the HTML viewport body scroll to prevent secondary background panning, particularly on mobile touch displays:

```typescript
useEffect(() => {
  const isAnyModalOpen = showSubjectModal || showOverrideModal || showVacationModal || showAddCourseModal || showAddSlotModal || showCustomClassModal;
  if (isAnyModalOpen) {
    document.body.style.overflow = 'hidden';
    document.body.style.position = 'fixed';
    document.body.style.width = '100%';
    document.body.style.top = `-${window.scrollY}px`;
  } else {
    const scrollY = document.body.style.top;
    document.body.style.overflow = '';
    document.body.style.position = '';
    document.body.style.width = '';
    document.body.style.top = '';
    if (scrollY) {
      window.scrollTo(0, parseInt(scrollY || '0') * -1);
    }
  }
}, [showSubjectModal, showOverrideModal, showVacationModal, showAddCourseModal, showAddSlotModal, showCustomClassModal]);
```

---

## 4. Key Actions & Operations

- **Tab Switching**: Coordinates tab changes and lazy-loads analytics data on the first transition to `#analytics`.
- **Attendance Logging**: Handles real-time logs by POSTing slots/override references to `/api/attendance`.
- **Admin-Template Synchronization**: Students call `POST /api/user/sync-template` to pull changes matching their tags into their courses sheet.
- **Export & Import Actions**: Handles triggers for JSON exporter / parser widgets.

---

## 5. UI Structure Overview

The header houses navigation tabs (`📔 Today's Sheet`, `📅 Calendar Grid`, `⚙️ Timetable Setup`, `📊 Attendance Stats`, `🛠️ Settings`) alongside Clerk's `<UserButton>` menu. Underneath the header, the page dynamically mounts:
- `<DashboardView>` (for today's timeline)
- `<CalendarView>` (for grid view)
- `<SetupView>` (for management)
- `<AnalyticsView>` (for reports)
- Modals collection wrappers (`SubjectModal`, `OverrideModal`, etc.)
