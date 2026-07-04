---
tags: [ui, component, calendar, scheduler, grid, frontend]
---

# UI Component: Calendar View

This component manages the interactive scheduler tab `📅 Calendar Grid`, located at `src/components/CalendarView.tsx`. It displays schedules in three different layout configurations (Daily, Weekly, and Monthly) and supports logging vacation ranges or inserting extra custom sessions.

- **File Link**: [CalendarView.tsx](file:///d:/02_CODE/04_TEST/Routine/src/components/CalendarView.tsx)
- **Backlinks**: [[index]], [[home_page]], [[DESIGN]], [[api_calendar]], [[component_modals]]

---

## 1. Props Schema

The component interacts with the calendar state variables configured in the parent route controller:

```typescript
interface CalendarViewProps {
  user: any;                                                       // Student metadata
  calendarMode: 'daily' | 'weekly' | 'monthly';                    // Zoom layouts trigger state
  setCalendarMode: (mode: 'daily' | 'weekly' | 'monthly') => void; // Layout switcher event handler
  viewDate: string;                                                // Main focal date ("YYYY-MM-DD")
  setViewDate: (date: string) => void;                             // Focal date updater
  calendarData: any;                                               // Resolved schedule dates dataset
  currentDate: string;                                             // System today date string
  setSelectedClass: (c: any) => void;                              // Context setter for details modal
  setShowSubjectModal: (show: boolean) => void;                    // Controller to show/hide session editor
  setVacationData: (data: any) => void;                            // Form data setter for vacations
  setShowVacationModal: (show: boolean) => void;                   // Controller to show/hide vacation model
  getReadableDate: (dateStr: string) => string;                    // String date formatter
  toggleAttendance: (classItem: any, date: string, status: string) => void; // Event trigger to update logs
  openCustomClassModal: (dateStr?: string) => void;                // Event trigger to schedule extras
}
```

---

## 2. Layout & Positioning Algorithms

### Hourly Decimal Conversion (`timeToDecimal`)
To position session blocks accurately in a weekly timeline layout, a utility function translates time strings (e.g. `"10:30"`) into float percentages (e.g. `10.5` hours):
```typescript
function timeToDecimal(timeStr: string): number {
  if (!timeStr) return 8;
  const [hours, minutes] = timeStr.split(':').map(Number);
  return hours + minutes / 60;
}
```
This is mapped to style layouts using pixel heights:
```css
height: (endTimeDecimal - startTimeDecimal) * heightPerHour;
top: (startTimeDecimal - START_HOUR) * heightPerHour;
```

### Event Theme Styles (`getEventCardStyle`)
Maps dynamic background/border colors according to real-time status attributes:
- **PRESENT**: Green background (`#def7ec`), dark green borders (`#03543f`).
- **ABSENT**: Pink background (`#fde8e8`), dark red borders (`#9b1c1c`), title strikethrough.
- **CANCELLED**: Grey transparent background (`#f3f4f6`), grey borders (`#4b5563`), title strikethrough.
- **RESCHEDULED**: Yellow background (`#fef3c7`), dark yellow borders (`#d97706`).
- **SCHEDULED**: Clear white background, bordered with user's theme color choice (`user.color`).

---

## 3. Rendering Modes

### A. Daily view
- Renders today's list in detailed card formats.
- Highlights academic tag groups and shows notices if today falls under vacation tags.

### B. Weekly grid
- Renders a 7-day grid columns set (Sunday to Saturday).
- Sessions are rendered inside relative divs positioned using `timeToDecimal`.
- Displays semester boundary indicator banners (e.g., "Spring 2026 Starts" or "Spring 2026 Ends") directly on transition dates.

### C. Monthly view
- Renders standard 7-column calendar grids padding days of surrounding months to fill rows.
- Each date square renders tiny indicator rows summarizing classes or listing vacations.
- Double-clicking a date cell immediately redirects to its Daily schedule sheet.
