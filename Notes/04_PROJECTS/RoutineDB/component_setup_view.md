---
tags: [ui, component, setup, courses, slots, frontend]
---

# UI Component: Setup View

This component manages the configurations dashboard rendered in `⚙️ Timetable Setup` and `🛠️ Settings`, located at `src/components/SetupView.tsx`. It provides form inputs for student details, color scheme selection, secondary tags subscriptions, file export/import pipelines, and custom course directories.

- **File Link**: [SetupView.tsx](file:///d:/02_CODE/04_TEST/Routine/src/components/SetupView.tsx)
- **Backlinks**: [[index]], [[home_page]], [[DESIGN]], [[api_courses]], [[api_weekly_slots]], [[api_user_secondary_tags]]

---

## 1. Props Schema

The component triggers data transformations managed by the main controller state:

```typescript
interface SetupViewProps {
  user: any;                                                       // User settings payload
  courses: any[];                                                  // Current courses array
  weeklySlots: any[];                                              // Current timetable slots array
  setCourseFormData: (data: any) => void;                          // Form binder for course details
  setShowAddCourseModal: (show: boolean) => void;                  // Add course dialog toggler
  setSlotFormData: (data: any) => void;                            // Form binder for slots details
  setShowAddSlotModal: (show: boolean) => void;                     // Add slot dialog toggler
  handleDeleteCourse: (id: number) => void;                        // Soft archive operation trigger
  handleDeleteSlot: (id: number) => void;                          // Delete slot trigger
  handleUpdateProfile: (data: any) => Promise<void>;               // POST handler for student profile
  showProfile?: boolean;                                           // Toggle display of profile forms
  showTimetable?: boolean;                                         // Toggle display of schedules setup lists
  onExport?: () => Promise<void>;                                  // JSON export callback
  onImport?: (file: File, mode: 'merge' | 'replace', importProfile: boolean) => Promise<any>; // JSON parser callback
}
```

---

## 2. Key Interface Modules

### A. Profile Form
- Allows setting Name, custom theme accent color, primary University, and primary Course Name tags.
- Includes a date input for `courseStartDate` which determines from which calendar date weekly recurring slots should begin generation.

### B. Secondary Tags Subscription
- Queries `GET /api/user/secondary-tags` on mount.
- Displays dynamic tags list. Users can add additional university/course tag pairs (e.g. for cross-department courses) to sync those schedules alongside their primary slots.

### C. Course Directory List
- Renders cards for each registered course. Shows teacher name, code, contact number, email, and whether the course is a personal custom course or synced from admin templates (`source === 'admin'`).
- Renders an **Archive** button. Soft-archives courses by setting `isArchived: true` and mapping `archivedAt` in the DB. This retains past attendance stats but hides future classes.

### D. Timetable Recurring Slots
- Categorizes slot cards by days of the week (Sunday through Saturday).
- Lists start/end times, room codes, student group targets, and active date boundaries.

### E. Backup & Migration (Export / Import)
- Contains file uploads forms to load backups or trigger JSON download exports. Supports two restoration modes:
  - **Merge**: Appends new courses and slots, bypassing duplicates.
  - **Replace**: Clears the personal schema database and overwrites with the contents of the backup file.
