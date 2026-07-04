---
tags: [api, admin, overview, index, backend]
---

# API Directory: Administrator-Only Endpoints

This document registers all backend APIs reserved for system administrators. Access to these endpoints is restricted, and each has a dedicated documentation sheet explaining its functionality.

- **Backlink**: [[index]], [[ARCHITECTURE]], [[api]]

---

## 1. Directory of Endpoints

| HTTP Method | Route URL | Target File Backlink | Description |
| :--- | :--- | :--- | :--- |
| **POST** | `/api/daily-class/description` | [[api_daily_class_description]] | Updates descriptions/notes for single class instances (user or override). |
| **GET / POST** | `/api/admin/analytics` | [[api_admin_analytics]] | Computes cross-student and class-wide attendance averages. |
| **GET/POST/DEL** | `/api/admin/announcements` | [[api_admin_announcements]] | Manages global broadcast announcements. |
| **GET** | `/api/admin/export` | [[api_admin_export]] | Dumps all system global schedules (courses, slots, overrides) to a backup JSON file. |
| **POST** | `/api/admin/import` | [[api_admin_import]] | Restores or imports database configurations from a global backup file. |
| **GET/POST/DEL** | `/api/admin/global-courses` | [[api_admin_global_courses]] | Configures shared master course template registries. |
| **GET/POST/DEL** | `/api/admin/global-slots` | [[api_admin_global_slots]] | Configures recurring master weekly timetable slots. |
| **GET/POST/DEL** | `/api/admin/global-overrides` | [[api_admin_global_overrides]] | Inserts schedule modifications that apply to all matching students. |
| **GET/POST/DEL** | `/api/admin/global-vacations` | [[api_admin_global_vacations]] | Schedules holidays applying to specific tag groupings. |
| **GET/POST/DEL** | `/api/admin/semesters` | [[api_admin_semesters]] | Defines academic term date scopes for global schedule generation. |
| **GET / POST** | `/api/admin/suggestions` | [[api_admin_suggestions]] | Processes student schedule change suggestions (Approve/Reject actions). |
| **GET/POST/DEL** | `/api/admin/users` | [[api_admin_users]] | Registers and manages student accounts, secondary tags, and roles. |
| **GET / POST** | `/api/admin/push-sync` | [[api_admin_push_sync]] | Coordinates force updates of course templates to matching student files. |

---

## 2. Administrator Access Control
- Every route registered under `/api/admin/` requires admin privileges.
- In backend controllers, this check is enforced at the start of request processing:
  ```typescript
  import { requireAdmin } from '@/lib/auth';
  
  export async function POST(req: NextRequest) {
    try {
      // Throws error immediately if role !== 'admin'
      const adminUser = await requireAdmin(); 
      // ... proceed with admin operations ...
    } catch (error: any) {
      if (error.message === 'Forbidden: Admin access required') {
        return NextResponse.json({ error: 'Forbidden' }, { status: 403 });
      }
      return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    }
  }
  ```
- **Reference**: [[lib_auth]]
