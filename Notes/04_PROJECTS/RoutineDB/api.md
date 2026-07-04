---
tags: [api, user, overview, index, backend]
---

# API Directory: Student-Facing Endpoints

This document lists all user-facing backend API routes for the Routine Planner. Each route has a dedicated documentation file outlining schemas, code blocks, and response properties.

- **Backlink**: [[index]], [[ARCHITECTURE]], [[admin_api]]

---

## 1. Directory of Endpoints

| HTTP Method | Route URL | Target File Backlink | Description |
| :--- | :--- | :--- | :--- |
| **GET** | `/api/init` | [[api_init]] | Single-call app bootstrapper payload generator. |
| **GET / POST** | `/api/user` | [[api_user]] | Retrieves profile attributes or commits theme and primary tag updates. |
| **GET/POST/DEL** | `/api/user/secondary-tags` | [[api_user_secondary_tags]] | Manages student subscriptions to secondary course/university tags. |
| **POST** | `/api/user/sync-template` | [[api_user_sync_template]] | Synchronizes student schedule with the admin-defined course template. |
| **GET** | `/api/user/export` | [[api_user_export]] | Dumps all student schedule records (attendance, vacations) to a JSON file. |
| **POST** | `/api/user/import` | [[api_user_import]] | Restores or merges student schedule records from a backed-up JSON file. |
| **GET/POST/DEL** | `/api/courses` | [[api_courses]] | Add, edit, or soft-archive personal subject codes. |
| **GET/POST/DEL** | `/api/weekly-slots` | [[api_weekly_slots]] | Configures template weekly recurring timetable schedule items. |
| **GET / POST** | `/api/calendar` | [[api_calendar]] | GET resolves date grids (expanding slots with overrides); POST commits local overrides. |
| **GET / POST** | `/api/attendance` | [[api_attendance]] | Retrieves paginated attendance list or logs present/absent checks. |
| **GET/POST/DEL** | `/api/vacations` | [[api_vacations]] | Manages sick leave days and personal vacation periods. |
| **POST** | `/api/suggestions` | [[api_suggestions]] | Submits class rescheduling/cancellation requests to administrative review boards. |
| **GET** | `/api/announcements` | [[api_announcements]] | Retrieves broadcasts matching the student's primary/secondary tags. |

---

## 2. Core Authentication Policy
- All student-facing API routes check for valid authentication sessions.
- In backend controllers, session mapping is executed using:
  ```typescript
  import { getAuthenticatedUser } from '@/lib/auth';
  const user = await getAuthenticatedUser();
  const userId = user.id; // local incremental database integer ID
  ```
- If a request is made with an invalid/missing Clerk session token, `getAuthenticatedUser()` throws an error, causing the API to respond with a `401 Unauthorized` status.
- **Reference**: [[lib_auth]]
