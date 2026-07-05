---
tags: [api-admin, import, backup, database, backend]
---

# Admin API: Database Master Importer

This endpoint parses and imports system-wide global templates, holiday schedules, and broadcasts from a JSON master backup file, located at `src/app/api/admin/import/route.ts`.

- **File Link**: [route.ts](file:///d:/02_CODE/04_TEST/Routine/src/app/api/admin/import/route.ts)
- **Backlinks**: [[index]], [[component_admin_panel]], [[admin_api]], [[api_admin_export]]

---

## 1. Endpoint Configuration

- **HTTP Method**: `POST`
- **Route URL**: `/api/admin/import`
- **Authentication**: Required (`Admin` role check)
- **URL Query Parameters**:
  - `mode` (`String`, Optional): Mode is either `"merge"` (default, upserts parameters and deduplicates records) or `"replace"` (wipes all existing global templates first).

---

## 2. Dependency-Safe Restoration Workflow

### A. Phase 1: Wiping Data (`mode === 'replace'`)
To avoid foreign key constraint violations during a full database reset, tables are cleared in strict dependency order:
1. `GlobalCourse` (deleting a course automatically triggers cascades in MySQL that wipe child tables `GlobalWeeklySlot` and `GlobalDailyOverride`).
2. `GlobalVacation` table.
3. `Semester` boundary conditions.
4. `Announcement` broadcast items.

### B. Phase 2: Compound Key Upsert Mapping
To prevent duplicate key collisions, records are imported using Prisma `upsert` queries targeting unique index groupings:
- **Global Courses**: Matches by compound key index `@@unique([subjectId, university, courseName])`.
- **Global Slots**: Deduplicates items using composite check on `(globalCourseId, dayOfWeek, startTime)`.
- **Global Overrides**: Upserts by `@@unique([globalCourseId, date])`.
- **Global Vacations**: Upserts by `@@unique([date, university, courseName])`.
- **Semesters**: Upserts by `@@unique([name, university, courseName])`.
- **Announcements**: Checks if a notice matching `(title, university, courseName)` already exists. If not, inserts the record.

---

## 3. Implementation Code Breakdown

The source code in `src/app/api/admin/import/route.ts` is divided into the following phases:

### Phase 1: Authentication and Header Validation
Verifies admin permission checks and validates backup file export metadata formats.

```typescript
import { NextRequest, NextResponse } from 'next/server';
import { requireAdmin } from '@/lib/auth';
import { prisma } from '@/lib/prisma';

export async function POST(req: NextRequest) {
  try {
    await requireAdmin();

    const { searchParams } = new URL(req.url);
    const mode = searchParams.get('mode') === 'replace' ? 'replace' : 'merge';
    const body = await req.json();

    // Validate export file
    if (body.exportType !== 'admin') {
      return NextResponse.json(
        { error: 'Invalid export file: exportType must be "admin". Did you mean to use the user import?' },
        { status: 400 }
      );
    }
    if (!body.version) {
      return NextResponse.json({ error: 'Invalid export file: missing version' }, { status: 400 });
    }

    const {
      globalCourses: exportedCourses = [],
      globalVacations: exportedVacations = [],
      semesters: exportedSemesters = [],
      announcements: exportedAnnouncements = [],
    } = body;

    const counts = {
      courses: 0,
      slots: 0,
      overrides: 0,
      vacations: 0,
      semesters: 0,
      announcements: 0,
    };
```

---

### Phase 2: Dependency-Ordered Cleanups (Replace Mode)
If `mode === 'replace'`, deletes global courses, vacations, semesters, and announcements. The deletions in `globalCourse` cascade to nested slots and overrides.

```typescript
    if (mode === 'replace') {
      // Delete everything in dependency order
      await prisma.globalCourse.deleteMany({});
      await prisma.globalVacation.deleteMany({});
      await prisma.semester.deleteMany({});
      await prisma.announcement.deleteMany({});
    }
```

---

### Phase 3: Global Courses & Nested Templates Import
Upserts courses using compound target keys `(subjectId, university, courseName)`, then imports slots and date overrides nested under the resolved course.

```typescript
    // Import global courses (with nested slots and overrides)
    for (const c of exportedCourses) {
      if (!c.subjectId || !c.university || c.courseName === undefined) continue;

      // Upsert the global course by its unique key
      const course = await prisma.globalCourse.upsert({
        where: {
          subjectId_university_courseName: {
            subjectId: c.subjectId,
            university: c.university,
            courseName: c.courseName,
          },
        },
        create: {
          subjectId: c.subjectId,
          subjectName: c.subjectName || '',
          subjectCode: c.subjectCode || '',
          teacherName: c.teacherName || '',
          teacherCode: c.teacherCode || '',
          teacherContact: c.teacherContact || '',
          teacherEmail: c.teacherEmail || '',
          university: c.university,
          courseName: c.courseName,
        },
        update: {
          subjectName: c.subjectName || '',
          subjectCode: c.subjectCode || '',
          teacherName: c.teacherName || '',
          teacherCode: c.teacherCode || '',
          teacherContact: c.teacherContact || '',
          teacherEmail: c.teacherEmail || '',
        },
      });
      counts.courses++;

      // Import weekly slots
      for (const s of (c.slots || [])) {
        if (!s.dayOfWeek || !s.startTime) continue;
        const existingSlot = await prisma.globalWeeklySlot.findFirst({
          where: {
            globalCourseId: course.id,
            dayOfWeek: s.dayOfWeek,
            startTime: s.startTime,
          },
        });
        if (!existingSlot) {
          await prisma.globalWeeklySlot.create({
            data: {
              globalCourseId: course.id,
              dayOfWeek: s.dayOfWeek,
              startTime: s.startTime,
              endTime: s.endTime || s.startTime,
              room: s.room || null,
              group: s.group || null,
            },
          });
          counts.slots++;
        }
      }

      // Import nested overrides
      for (const o of (c.overrides || [])) {
        if (!o.date || !o.status) continue;
        await prisma.globalDailyOverride.upsert({
          where: {
            globalCourseId_date: {
              globalCourseId: course.id,
              date: o.date,
            },
          },
          create: {
            globalCourseId: course.id,
            date: o.date,
            status: o.status,
            newStartTime: o.newStartTime || null,
            newEndTime: o.newEndTime || null,
            newRoom: o.newRoom || null,
            description: o.description || null,
          },
          update: {
            status: o.status,
            newStartTime: o.newStartTime || null,
            newEndTime: o.newEndTime || null,
            newRoom: o.newRoom || null,
            description: o.description || null,
          },
        });
        counts.overrides++;
      }
    }
```

---

### Phase 4: Global Vacations, Semesters & Broadcasts Import
Restores remaining metadata tables, and returns counts of imported entries.

```typescript
    // Import global vacations — upsert by (date, university, courseName)
    for (const v of exportedVacations) {
      if (!v.date || !v.type) continue;
      await prisma.globalVacation.upsert({
        where: {
          date_university_courseName: {
            date: v.date,
            university: v.university || null,
            courseName: v.courseName || null,
          },
        },
        create: {
          date: v.date,
          type: v.type,
          description: v.description || null,
          university: v.university || null,
          courseName: v.courseName || null,
        },
        update: {
          type: v.type,
          description: v.description || null,
        },
      });
      counts.vacations++;
    }

    // Import semesters — upsert by (name, university, courseName)
    for (const s of exportedSemesters) {
      if (!s.name || !s.startDate || !s.endDate) continue;
      await prisma.semester.upsert({
        where: {
          name_university_courseName: {
            name: s.name,
            university: s.university || '',
            courseName: s.courseName || '',
          },
        },
        create: {
          name: s.name,
          startDate: s.startDate,
          endDate: s.endDate,
          university: s.university || '',
          courseName: s.courseName || '',
          isActive: s.isActive ?? true,
        },
        update: {
          startDate: s.startDate,
          endDate: s.endDate,
          isActive: s.isActive ?? true,
        },
      });
      counts.semesters++;
    }

    // Import announcements — deduplicate by title and tags
    for (const a of exportedAnnouncements) {
      if (!a.title || !a.body) continue;

      const existing = await prisma.announcement.findFirst({
        where: {
          title: a.title,
          university: a.university || null,
          courseName: a.courseName || null,
        },
      });

      if (!existing) {
        await prisma.announcement.create({
          data: {
            title: a.title,
            body: a.body,
            university: a.university || null,
            courseName: a.courseName || null,
            expiresAt: a.expiresAt || null,
          },
        });
        counts.announcements++;
      }
    }

    return NextResponse.json({
      success: true,
      mode,
      imported: counts,
    });
  } catch (error: any) {
    if (error.message === 'Forbidden: Admin access required') {
      return NextResponse.json({ error: 'Forbidden' }, { status: 403 });
    }
    if (error.message === 'Unauthorized: No authenticated user') {
      return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    }
    console.error('Error importing admin data:', error);
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}
```

