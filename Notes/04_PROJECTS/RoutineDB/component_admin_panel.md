---
tags: [ui, component, admin, panel, forms, sub-views, frontend]
---

# UI Component: Admin Panel Dashboard

This component represents the core administration interface rendered in the `/admin` path, located at `src/components/AdminPanel.tsx`. It divides operations into 9 sub-tabs to coordinate database templates, user accounts, overrides, holidays, semesters, suggestions, broadcasts, analytics, and backup files.

- **File Link**: [AdminPanel.tsx](file:///d:/02_CODE/04_TEST/Routine/src/components/AdminPanel.tsx)
- **Backlinks**: [[index]], [[admin_page]], [[DESIGN]], [[api_admin_push_sync]], [[api_admin_suggestions]]

---

## 1. Props Schema & Tab Coordination

The component takes the active user object as props and manages sub-tabs internally using a local state string:

```typescript
interface AdminPanelProps {
  user: any; // Checked active admin user
}

export default function AdminPanel({ user }: AdminPanelProps) {
  const [subTab, setSubTab] = useState<'courses' | 'vacations' | 'users' | 'semesters' | 'announcements' | 'overrides' | 'analytics' | 'export-import' | 'suggestions'>('courses');
  // ... state configurations ...
}
```

---

## 2. Technical Details of the 9 Admin Sub-Panels

### A. Global Course Templates (`courses`)
- **Action**: Manages `GlobalCourse` templates and nested slots `GlobalWeeklySlot`.
- **Sync System**: Admins configure global timetables and can call a preview calculation of matching students before triggering a **Push Sync** operation which propagates changes to all matching students.

### B. Global Overrides (`overrides`)
- **Action**: Declares single-instance overrides for template schedules (e.g. reschedule classes due to weather).
- **Behavior**: Auto-creates `GlobalDailyOverride` records and pushes `DailyClass` overrides into student calendars.

### C. Global Vacations (`vacations`)
- **Action**: Manages system holidays or absent days.
- **Rules**: Holidays can target specific universities or courses, or apply globally if university/course tags are null.

### D. Semester Boundaries (`semesters`)
- **Action**: Defines academic calendars start/end dates.
- **Behavior**: Used to restrict generation of global schedule slots within term windows.

### E. User Suggestions Box (`suggestions`)
- **Action**: Lists user-submitted schedule modifications.
- **Logic**: Renders "Approve" and "Reject" actions:
  - **Approve**: Calls `/api/admin/suggestions` to create `GlobalDailyOverride` blocks, pushes overrides to matching students, and updates the suggestion status to `APPROVED`.
  - **Reject**: Updates status to `REJECTED`.

### F. Announcements Broadcast (`announcements`)
- **Action**: Writes notices targeted by university/course name filters.

### G. Users Registry (`users`)
- **Action**: Lists all registered accounts in the local DB. Allows updating roles (e.g. promoting users to admin) or correcting student university/course tags.

### H. Analytics Scorecards (`analytics`)
- **Action**: Renders overall metrics or student-specific grids, calculating average attendance rates across different batches.

### I. Database Backups (`export-import`)
- **Action**: Triggers complete database dumps (excluding critical auth data) or restores records from backup files.

---

## 3. Key Core API Handlers (Reusable Reference Blocks)

### Push Synchronization Callback
Triggered when admins push global course schedule modifications to student binders:
```typescript
const handlePushSync = async () => {
  if (!confirm('Push these template schedules to all matching students? This will overwrite their current schedules.')) return;
  setIsPushing(true);
  try {
    const res = await fetch('/api/admin/push-sync', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        globalCourseId: selectedCourseId,
        university: templateFilterUniversity,
        courseName: templateFilterCourseName,
        updateMode: pushSyncMode, // 'merge' or 'replace'
      }),
    });
    if (res.ok) {
      alert('Schedule pushed to students successfully!');
    }
  } catch (err: any) {
    alert('Push failed: ' + err.message);
  } finally {
    setIsPushing(false);
  }
};
```

### Suggestion Approval Callback
Triggered when approving a student rescheduling request:
```typescript
const handleProcessSuggestion = async (suggestionId: number, action: 'approve' | 'reject') => {
  setIsProcessingSuggestion(true);
  try {
    const res = await fetch('/api/admin/suggestions', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ suggestionId, action }),
    });
    if (res.ok) {
      alert(`Suggestion successfully ${action}d!`);
      fetchSuggestions(); // refresh list
    }
  } catch (err: any) {
    alert('Processing failed: ' + err.message);
  } finally {
    setIsProcessingSuggestion(false);
  }
};
```
