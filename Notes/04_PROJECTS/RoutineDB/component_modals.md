---
tags: [ui, component, modal, forms, overlays, frontend]
---

# UI Components: Overlay Modals Vault

This module, located at `src/components/Modals.tsx`, exports all overlay form modal overlays. They capture user configurations, manage overrides, log holidays, and update course/slot schema files.

- **File Link**: [Modals.tsx](file:///d:/02_CODE/04_TEST/Routine/src/components/Modals.tsx)
- **Backlinks**: [[index]], [[home_page]], [[component_dashboard_view]], [[component_calendar_view]], [[component_setup_view]]

---

## 1. SubjectModal (Subject Detail Sheet)
- **Purpose**: Displays comprehensive details of a selected calendar item (code, time, teacher details, and room).
- **Interactive Forms**:
  - **Class Notes**: Inline input field allows users to submit description notes (e.g. "Homework assignment due today") calling `POST /api/daily-class/description`.
  - **Attendance Toggles**: PRESENT or ABSENT markers.
  - **User Suggestion**: If the course is an admin-template course (`source === 'admin'`), users can toggle the suggestion form. This lets students suggest cancellations or reschedules to the administrator group, which POSTs to `POST /api/suggestions`.

---

## 2. OverrideModal (Single-Instance Override Form)
- **Purpose**: Allows users to override time slot parameters, cancel, or reschedule a single class instance on a specific date.
- **Form Controls**:
  - `startTime` & `endTime` (`HH:MM` time inputs).
  - `room` & `group` strings.
  - `status` dropdown: `"SCHEDULED"`, `"RESCHEDULED"`, or `"CANCELLED"`.
  - `description` notes.
- **API Target**: `POST /api/calendar` (local overrides handler).

---

## 3. VacationModal (Vacation Logging Form)
- **Purpose**: Registers a vacation range or absent block.
- **Form Controls**:
  - `date`: Start date selector.
  - `endDate`: Optional end date selector (for multi-day blocks).
  - `type` dropdown:
    - `"VACATION"`: Holiday block. Classes are marked as holiday.
    - `"ABSENT_DAY"`: Sick day block. Marks all classes as absent automatically.
  - `description` details.
- **API Target**: `POST /api/vacations`.

---

## 4. CourseModal (Add/Edit Personal Course Form)
- **Purpose**: Adds a new personal course card or updates contact card properties for instructor files.
- **Form Controls**:
  - `subjectId` (Unique ID, e.g. `"CSE-1201"`).
  - `subjectName` & `subjectCode`.
  - Instructor metadata: `teacherName`, `teacherCode`, `teacherContact`, `teacherEmail`.
- **API Target**: `POST /api/courses`.

---

## 5. SlotModal (Add/Edit Timetable Slot Form)
- **Purpose**: Configures recurring schedule templates (e.g., "This class occurs every Monday at 10 AM").
- **Form Controls**:
  - `courseId` dropdown (populates from current active courses).
  - `dayOfWeek` selector (Sunday to Saturday).
  - `startTime` & `endTime`.
  - `room` & `group` targets.
  - `activeFrom` & `activeUntil` (optional date boundaries for temporary recurring classes like tutoring).
- **API Target**: `POST /api/weekly-slots`.

---

## 6. CustomClassModal (Add Extra Class Form)
- **Purpose**: Manually inserts a custom one-off class instance on a date, bypassing standard recurring slot schemas.
- **Form Controls**:
  - `courseId` select list.
  - `date` calendar picker.
  - `startTime` & `endTime`.
  - `room` & `group` tags.
- **API Target**: `POST /api/calendar` with payload variable `{ isExtra: true }`.
