---
tags: [api-user, export, migration, database, backend]
---

# User API: Data Exporter

This endpoint generates a downloadable backup JSON dump of the student's full calendar settings, located at `src/app/api/user/export/route.ts`.

- **File Link**: [route.ts](file:///d:/02_CODE/04_TEST/Routine/src/app/api/user/export/route.ts)
- **Backlinks**: [[index]], [[component_setup_view]], [[api]], [[api_user_import]]

---

## 1. Endpoint Configuration

- **HTTP Method**: `GET`
- **Route URL**: `/api/user/export`
- **Authentication**: Required (`User` session check)
- **Response Headers**:
  - `Content-Type: application/json`
  - `Content-Disposition: attachment; filename="routine-user-export-YYYY-MM-DD.json"`

---

## 2. Serialization Architecture

To ensure backups are portable across different student accounts (or restorable if database indices change), the exporter converts relational integer database keys (`id`, `courseId`, `weeklySlotId`) into transfer-safe logical tags:

1. **Profile**: Dumps name, theme color, primary tags (university, course), and start date.
2. **Secondary Tags**: Arrays of university and course name filters.
3. **Courses**: Serializes details mapping `subjectId` (which acts as a unique string key per user) rather than database integers.
4. **Weekly Slots**: Translates `courseId` integers into `subjectId` strings.
5. **Daily Classes**: Replaces `courseId` with `subjectId`. Replaces `weeklySlotId` with a slot descriptor lookup ref containing:
   - `{ subjectId, dayOfWeek, startTime }`
6. **Attendance Logs**: Resolves slot and class keys to logical reference descriptors:
   - `{ subjectId, date, status, weeklySlotRef }`
7. **Vacations**: Dumps lists of personal vacation dates, types, and descriptions.

---

## 3. Implementation Code Breakdown

The source code in `src/app/api/user/export/route.ts` is divided into three key steps:

### Phase 1: Parallel Database Loading
Authenticates the user and fetches all user courses, slots, overrides, attendance logs, vacations, and secondary tag configurations concurrently.

```typescript
import { NextRequest, NextResponse } from 'next/server';
import { getAuthenticatedUser } from '@/lib/auth';
import { prisma } from '@/lib/prisma';

export async function GET(req: NextRequest) {
  try {
    const user = await getAuthenticatedUser();

    // Fetch all user data in parallel
    const [courses, weeklySlots, dailyClasses, attendance, vacations, secondaryTags] =
      await Promise.all([
        prisma.course.findMany({
          where: { userId: user.id },
          orderBy: { id: 'asc' },
        }),
        prisma.weeklySlot.findMany({
          where: { userId: user.id },
          orderBy: { id: 'asc' },
        }),
        prisma.dailyClass.findMany({
          where: { userId: user.id },
          orderBy: { date: 'asc' },
        }),
        prisma.attendance.findMany({
          where: { userId: user.id },
          orderBy: { date: 'asc' },
        }),
        prisma.vacation.findMany({
          where: { userId: user.id },
          orderBy: { date: 'asc' },
        }),
        prisma.userSecondaryTag.findMany({
          where: { userId: user.id },
        }),
      ]);
```

---

### Phase 2: Relational ID Reference Map Builders
Constructs maps converting foreign keys like `courseId` and `weeklySlotId` into logical string keys.

```typescript
    // Build a map from courseId → subjectId for cross-referencing
    const courseIdToSubjectId = new Map<number, string>();
    for (const c of courses) {
      courseIdToSubjectId.set(c.id, c.subjectId);
    }

    // Build a map from weeklySlotId → { subjectId, dayOfWeek, startTime }
    const slotIdToRef = new Map<number, { subjectId: string; dayOfWeek: string; startTime: string }>();
    for (const s of weeklySlots) {
      slotIdToRef.set(s.id, {
        subjectId: courseIdToSubjectId.get(s.courseId) || '',
        dayOfWeek: s.dayOfWeek,
        startTime: s.startTime,
      });
    }
```

---

### Phase 3: JSON Serialization & Data Streaming
Converts relational schemas into the backup format structure and sets JSON download file headers.

```typescript
    const exportData = {
      version: '1.0',
      exportType: 'user',
      exportedAt: new Date().toISOString(),

      profile: {
        name: user.name,
        color: user.color,
        university: user.university,
        courseName: user.courseName,
        courseStartDate: user.courseStartDate,
      },

      secondaryTags: secondaryTags.map(t => ({
        university: t.university,
        courseName: t.courseName,
      })),

      courses: courses.map(c => ({
        subjectId: c.subjectId,
        subjectName: c.subjectName,
        subjectCode: c.subjectCode,
        teacherName: c.teacherName,
        teacherCode: c.teacherCode,
        teacherContact: c.teacherContact,
        teacherEmail: c.teacherEmail,
        source: c.source,
        isArchived: c.isArchived,
        archivedAt: c.archivedAt,
      })),

      weeklySlots: weeklySlots.map(s => ({
        subjectId: courseIdToSubjectId.get(s.courseId) || '',
        dayOfWeek: s.dayOfWeek,
        startTime: s.startTime,
        endTime: s.endTime,
        room: s.room,
        group: s.group,
        activeFrom: s.activeFrom,
        activeUntil: s.activeUntil,
        source: s.source,
      })),

      dailyClasses: dailyClasses.map(d => ({
        subjectId: courseIdToSubjectId.get(d.courseId) || '',
        weeklySlotRef: d.weeklySlotId ? slotIdToRef.get(d.weeklySlotId) || null : null,
        date: d.date,
        startTime: d.startTime,
        endTime: d.endTime,
        room: d.room,
        group: d.group,
        status: d.status,
        isExtra: d.isExtra,
        description: d.description,
      })),

      attendance: attendance.map(a => ({
        subjectId: courseIdToSubjectId.get(a.courseId) || '',
        date: a.date,
        status: a.status,
        weeklySlotRef: a.weeklySlotId ? slotIdToRef.get(a.weeklySlotId) || null : null,
      })),

      vacations: vacations.map(v => ({
        date: v.date,
        type: v.type,
        description: v.description,
      })),
    };

    const json = JSON.stringify(exportData, null, 2);
    const fileName = `routine-user-export-${new Date().toISOString().split('T')[0]}.json`;

    return new NextResponse(json, {
      status: 200,
      headers: {
        'Content-Type': 'application/json',
        'Content-Disposition': `attachment; filename="${fileName}"`,
      },
    });
  } catch (error: any) {
    if (error.message === 'Unauthorized: No authenticated user') {
      return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    }
    console.error('Error exporting user data:', error);
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}
```

