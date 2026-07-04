---
tags: [api-admin, global-courses, template, create, delete, backend]
---

# Admin API: Master Courses Template Manager

This endpoint coordinates administrative operations to manage master course templates, located at `src/app/api/admin/global-courses/route.ts`.

- **File Link**: [route.ts](file:///d:/02_CODE/04_TEST/Routine/src/app/api/admin/global-courses/route.ts)
- **Backlinks**: [[index]], [[component_admin_panel]], [[admin_api]]

---

## 1. GET `/api/admin/global-courses`

- **Purpose**: Lists all global course templates configured in the system, embedding their template weekly slots and overrides.
- **Authentication**: Required (`Admin` role check)
- **Success Response JSON**:
  ```json
  [
    {
      "id": 1,
      "subjectId": "CSE-1101",
      "subjectName": "Structured Programming",
      "subjectCode": "CSE-1101",
      "teacherName": "Dr. Rahman",
      "teacherCode": "SR",
      "teacherContact": "017...",
      "teacherEmail": "sr@univ.edu",
      "university": "University of Dhaka",
      "courseName": "BSSE-18",
      "weeklySlots": [],
      "overrides": []
    }
  ]
  ```

---

## 2. POST `/api/admin/global-courses`

- **Purpose**: Publishes a new shared template course or updates metadata details of an existing template.
- **Authentication**: Required (`Admin` role check)
- **JSON Payload Parameters**:
  - `id` (`Int`, Optional): Record identifier key (triggers update flow).
  - `subjectId` (`String`, Required): Unique subject code identifier (e.g. `"CSE-1101"`).
  - `subjectName` (`String`, Required).
  - `subjectCode` (`String`, Required).
  - `university` & `courseName` (`String`, Optional): Batch identifiers.
  - Instructor metadata: `teacherName`, `teacherCode`, `teacherContact`, `teacherEmail`.
- **Tag Normalization**: Runs `normalizeTag()` on target tags before committing.

---

## 3. DELETE `/api/admin/global-courses`

- **Purpose**: Removes a global course template from the system registry.
- **Authentication**: Required (`Admin` role check)
- **URL Query Parameters**:
  - `id` (`Int`, Required): Unique ID key of the template to delete.
- **Relational Cascades**: Database deletion cascades automatically trigger cleanups of all child tables (`GlobalWeeklySlot`, `GlobalDailyOverride`, `ClassSuggestion`).

---

## 4. Source Code

Here is the complete implementation of `src/app/api/admin/global-courses/route.ts`:

```typescript
import { NextResponse } from 'next/server';
import { requireAdmin } from '@/lib/auth';
import { prisma } from '@/lib/prisma';
import { normalizeTag } from '@/lib/utils';

// GET: List all global courses
export async function GET() {
  try {
    await requireAdmin();
    const courses = await prisma.globalCourse.findMany({
      include: { weeklySlots: true, overrides: true },
      orderBy: { subjectId: 'asc' },
    });
    return NextResponse.json(courses);
  } catch (error: any) {
    if (error.message.includes('Unauthorized') || error.message.includes('Forbidden')) {
      return NextResponse.json({ error: error.message }, { status: 403 });
    }
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}

// POST: Create/update a global course
export async function POST(request: Request) {
  try {
    await requireAdmin();
    const body = await request.json();
    const { id, subjectId, subjectName, subjectCode, teacherName, teacherCode, teacherContact, teacherEmail, university, courseName } = body;

    if (!subjectId || !subjectName || !subjectCode) {
      return NextResponse.json({ error: 'Missing required fields' }, { status: 400 });
    }

    const normUniversity = normalizeTag(university);
    const normCourseName = normalizeTag(courseName);

    if (id) {
      const updated = await prisma.globalCourse.update({
        where: { id: parseInt(id) },
        data: { subjectId, subjectName, subjectCode, teacherName: teacherName || '', teacherCode: teacherCode || '', teacherContact: teacherContact || '', teacherEmail: teacherEmail || '', university: normUniversity, courseName: normCourseName },
      });
      return NextResponse.json(updated);
    } else {
      const created = await prisma.globalCourse.create({
        data: { subjectId, subjectName, subjectCode, teacherName: teacherName || '', teacherCode: teacherCode || '', teacherContact: teacherContact || '', teacherEmail: teacherEmail || '', university: normUniversity, courseName: normCourseName },
      });
      return NextResponse.json(created, { status: 201 });
    }
  } catch (error: any) {
    if (error.message.includes('Unauthorized') || error.message.includes('Forbidden')) {
      return NextResponse.json({ error: error.message }, { status: 403 });
    }
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}

// DELETE: Remove a global course
export async function DELETE(request: Request) {
  try {
    await requireAdmin();
    const { searchParams } = new URL(request.url);
    const id = searchParams.get('id');
    if (!id) return NextResponse.json({ error: 'Missing ID' }, { status: 400 });
    await prisma.globalCourse.delete({ where: { id: parseInt(id) } });
    return NextResponse.json({ success: true });
  } catch (error: any) {
    if (error.message.includes('Unauthorized') || error.message.includes('Forbidden')) {
      return NextResponse.json({ error: error.message }, { status: 403 });
    }
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}
```
