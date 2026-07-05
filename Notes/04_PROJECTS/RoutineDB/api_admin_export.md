---
tags: [api-admin, export, backup, database, backend]
---

# Admin API: Database Master Exporter

This endpoint generates a master backup JSON payload of all global scheduling templates, holidays, semesters, and broadcasts in the system, located at `src/app/api/admin/export/route.ts`.

- **File Link**: [route.ts](file:///d:/02_CODE/04_TEST/Routine/src/app/api/admin/export/route.ts)
- **Backlinks**: [[index]], [[component_admin_panel]], [[admin_api]], [[api_admin_import]]

---

## 1. Endpoint Configuration

- **HTTP Method**: `GET`
- **Route URL**: `/api/admin/export`
- **Authentication**: Required (`Admin` role check)
- **Response Headers**:
  - `Content-Type: application/json`
  - `Content-Disposition: attachment; filename="routine-admin-export-YYYY-MM-DD.json"`

---

## 2. Serialization Design (Master Backups)

To safeguard user privacy and separate system configuration from student telemetry, the master exporter **completely ignores individual student tables** (User accounts, secondary tags, personal courses/slots, personal overrides, attendance logs, and vacations).

The generated JSON object contains:
1. **`exportType`**: Hardcoded to `"admin"` (used by the importer to identify master backups).
2. **`globalCourses`**: List of all shared course templates, including nested slot templates (`weeklySlots`) and global overrides.
3. **`globalVacations`**: System-wide or batch-specific holidays.
4. **`semesters`**: Active term start and end boundaries.
5. **`announcements`**: All broadcast messages.

---

## 3. Implementation Code Breakdown

The source code in `src/app/api/admin/export/route.ts` is divided into three key steps:

### Phase 1: Authentication and Parallel Database Queries
Validates administrative permissions, and queries all template tables concurrently using `Promise.all()`.

```typescript
import { NextRequest, NextResponse } from 'next/server';
import { requireAdmin } from '@/lib/auth';
import { prisma } from '@/lib/prisma';

export async function GET(req: NextRequest) {
  try {
    await requireAdmin();

    // Fetch all admin data in parallel
    const [globalCourses, globalVacations, semesters, announcements] = await Promise.all([
      prisma.globalCourse.findMany({
        include: {
          weeklySlots: {
            orderBy: { id: 'asc' },
          },
          overrides: {
            orderBy: { date: 'asc' },
          },
        },
        orderBy: { id: 'asc' },
      }),
      prisma.globalVacation.findMany({ orderBy: { date: 'asc' } }),
      prisma.semester.findMany({ orderBy: { startDate: 'asc' } }),
      prisma.announcement.findMany({ orderBy: { createdAt: 'asc' } }),
    ]);
```

---

### Phase 2: Serialization of Global Course Blueprint Templates
Constructs the backup payload structure and maps courses, recurring template weekly slots, and template date overrides.

```typescript
    const exportData = {
      version: '1.0',
      exportType: 'admin',
      exportedAt: new Date().toISOString(),

      globalCourses: globalCourses.map(c => ({
        subjectId: c.subjectId,
        subjectName: c.subjectName,
        subjectCode: c.subjectCode,
        teacherName: c.teacherName,
        teacherCode: c.teacherCode,
        teacherContact: c.teacherContact,
        teacherEmail: c.teacherEmail,
        university: c.university,
        courseName: c.courseName,
        slots: c.weeklySlots.map(s => ({
          dayOfWeek: s.dayOfWeek,
          startTime: s.startTime,
          endTime: s.endTime,
          room: s.room,
          group: s.group,
        })),
        overrides: c.overrides.map(o => ({
          date: o.date,
          status: o.status,
          newStartTime: o.newStartTime,
          newEndTime: o.newEndTime,
          newRoom: o.newRoom,
          description: o.description,
        })),
      })),
```

---

### Phase 3: Metadata Serialization and Download Streaming
Maps holidays, active terms, and system broadcasts, converting the object to a string format and returning file attachment download headers.

```typescript
      globalVacations: globalVacations.map(v => ({
        date: v.date,
        type: v.type,
        description: v.description,
        university: v.university,
        courseName: v.courseName,
      })),

      semesters: semesters.map(s => ({
        name: s.name,
        startDate: s.startDate,
        endDate: s.endDate,
        university: s.university,
        courseName: s.courseName,
        isActive: s.isActive,
      })),

      announcements: announcements.map(a => ({
        title: a.title,
        body: a.body,
        university: a.university,
        courseName: a.courseName,
        expiresAt: a.expiresAt,
      })),
    };

    const json = JSON.stringify(exportData, null, 2);
    const fileName = `routine-admin-export-${new Date().toISOString().split('T')[0]}.json`;

    return new NextResponse(json, {
      status: 200,
      headers: {
        'Content-Type': 'application/json',
        'Content-Disposition': `attachment; filename="${fileName}"`,
      },
    });
  } catch (error: any) {
    if (error.message === 'Forbidden: Admin access required') {
      return NextResponse.json({ error: 'Forbidden' }, { status: 403 });
    }
    if (error.message === 'Unauthorized: No authenticated user') {
      return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    }
    console.error('Error exporting admin data:', error);
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}
```

