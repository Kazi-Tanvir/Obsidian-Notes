---
tags: [architecture, nextjs, lifecycle, systems-design, dataflow, backend]
---

# System Architecture & Lifecycle: Routine Planner

This document provides a technical overview of how the Routine Planner is structured, its authentication integration, the bootstrapping lifecycle, and the core calendar resolution engine.

---

## 1. System Context Diagram

The architecture is built on Next.js (App Router), leveraging Clerk for user management, Prisma as the ORM, and MySQL for persistence.

```mermaid
graph TD
    Client[Browser Frontend / React]
    Clerk[Clerk Auth Service]
    API[Next.js App Router API Routes]
    Prisma[Prisma Client ORM]
    DB[(MySQL Database)]

    Client -->|1. Authenticate / Retrieve Token| Clerk
    Client -->|2. Send Requests + Cookie Session| API
    API -->|3. Call clerkMiddleware / Verify Session| Clerk
    API -->|4. Query Data| Prisma
    Prisma -->|5. Connect via Database URL| DB
```

---

## 2. Bootstrapping Lifecycle (`/api/init`)

When a user visits the website, rather than triggering multiple concurrent API calls (which causes database connection spikes and screen flickering), the application fires a single bootstrap query: `GET /api/init`.

```mermaid
sequenceDiagram
    participant Browser as React Frontend
    participant API as API Route (/api/init)
    participant Clerk as Clerk SDK
    participant DB as Prisma / MySQL

    Browser->>API: GET /api/init?startDate=...&endDate=...&todayDate=...
    API->>Clerk: Get Clerk userId from session
    Clerk-->>API: returns clerkId (e.g. user_abc123)
    API->>DB: Find user in DB by clerkId
    alt User does not exist
        API->>Clerk: Fetch full profile info (name, email)
        API->>DB: Create User record (role: admin if 1st user, else user)
    end
    API->>DB: Fetch user courses, weekly slots, announcements
    API->>DB: Resolve calendar data for date range (DailyClasses, Vacations, Attendance)
    DB-->>API: Returns payload
    API-->>Browser: returns combined initialization JSON
    Note over Browser: App finishes Loading state,<br/>renders Dashboard & Schedule views.
```

- **File Backlink**: [[api_init]], [[home_page]]

---

## 3. Core Calendar Resolution Engine

The core scheduling logic lies in `src/app/api/calendar/route.ts`. The server resolves weekly recurring schedules into concrete class instances for any given range of dates (`startDate` to `endDate`).

### Algorithm Flowchart

```mermaid
flowchart TD
    Start([For each Date in Range]) --> GetDayOfWeek[Get Name of Day e.g. MONDAY]
    GetDayOfWeek --> FetchSlots[Filter user's active WeeklySlots matching Day]
    
    FetchSlots --> LoopSlots{For each Slot...}
    
    LoopSlots -- Yes --> CheckRange{Date within slot's<br/>activeFrom/activeUntil<br/>or user.courseStartDate?}
    CheckRange -- No --> NextSlot[Skip Slot] --> LoopSlots
    
    CheckRange -- Yes --> CheckSemester{Is Admin course?<br/>Has active Semester definition?}
    
    CheckSemester -- Yes --> InSemester{Is date within<br/>semester start/end?}
    InSemester -- No --> NextSlot
    InSemester -- Yes --> CheckLocalOverride{Does Local DailyClass<br/>override exist for slot?}
    CheckSemester -- No --> CheckLocalOverride
    
    CheckLocalOverride -- Yes --> ApplyOverride[Apply Override details<br/>startTime, endTime, room, status] --> ResolveAttendance
    CheckLocalOverride -- No --> ApplyTemplate[Use default template details<br/>startTime, endTime, room, status: SCHEDULED] --> ResolveAttendance
    
    ResolveAttendance[Resolve attendance status<br/>Check if logged attendance exists] --> CheckVacation{Does Global or Local<br/>Vacation exist for date?}
    
    CheckVacation -- Yes --> ForceVacationStatus[Overwrite attendance status:<br/>VACATION or ABSENT] --> RecordClass[Add to resolved list]
    CheckVacation -- No --> RecordClass
    
    RecordClass --> NextSlot
    
    LoopSlots -- No (Done) --> FetchExtraClasses[Find all DailyClass instances<br/>marked isExtra = true for Date]
    FetchExtraClasses --> LoopExtras{For each Extra...}
    LoopExtras -- Yes --> AddExtra[Append custom class to resolved list] --> LoopExtras
    LoopExtras -- No --> SortChronological[Sort list chronologically by startTime]
    SortChronological --> End([Done for Date])
```

- **File Backlink**: [[api_calendar]]
- **Details**:
  - **Semester Boundary filter**: Applied to courses synced from admin (`source = 'admin'`). Ensures class templates do not generate during summer/winter holidays or exam breaks.
  - **Vacation / Absent Day overrides**: Global vacations (declared by admin) and personal vacations (declared by student) take ultimate precedence. If a vacation falls on a date, classes are kept on the list but marked with status `VACATION` or `ABSENT`, disabling standard attendance triggers.
  - **Custom Extra Classes**: Standalone class instances (`isExtra: true`) are generated manually by the student or pushed by the admin. They bypass weekly slots.
