---
tags: [api-user, courses, soft-delete, archive, backend]
---

# User API: Personal Course Manager

This endpoint handles personal courses (subjects) configuration, updates, and soft-archiving procedures, located at `src/app/api/courses/route.ts`.

- **File Link**: [route.ts](file:///d:/02_CODE/04_TEST/Routine/src/app/api/courses/route.ts)
- **Backlinks**: [[index]], [[component_setup_view]], [[api]]

---

## 1. GET `/api/courses`

- **Purpose**: Lists all active courses (where `isArchived: false`) associated with the active student, sorted alphabetically by `subjectId`.
- **Authentication**: Required (`User` session check)
- **Success Response JSON**:
  ```json
  [
    {
      "id": 5,
      "userId": 1,
      "subjectId": "CSE-1101",
      "subjectName": "Structured Programming",
      "subjectCode": "CSE-1101",
      "teacherName": "Dr. Rahman",
      "teacherCode": "SR",
      "teacherContact": "TBA",
      "teacherEmail": "sr@univ.edu",
      "source": "personal",
      "isArchived": false,
      "archivedAt": null
    }
  ]
  ```

---

## 2. POST `/api/courses`

- **Purpose**: Creates a new course card or edits properties of an existing course.
- **Authentication**: Required (`User` session check)
- **JSON Payload Parameters**:
  - `id` (`Int`, Optional): Database key parameter. If provided, edits the matching course.
  - `subjectId` (`String`, Required): Custom subject key tag (e.g. `"CSE-1101"`).
  - `subjectName` (`String`, Required): Subject title.
  - `subjectCode` (`String`, Required).
  - Instructor optional parameters: `teacherName`, `teacherCode`, `teacherContact`, `teacherEmail`.
- **Logic**:
  - **Edit Mode**: Verifies student ownership check before updating.
  - **Creation Mode**: If the course ID tag (`subjectId`) already exists and is soft-archived, **restores it** (sets `isArchived: false`, resets `archivedAt` to `null`, and overrides variables) instead of failing or inserting duplicate records.

---

## 3. DELETE `/api/courses`

- **Purpose**: Hides a course from upcoming schedule calculations, or wipes its records from database tables.
- **Authentication**: Required (`User` session check)
- **URL Query Parameters**:
  - `id` (`Int`, Required): Unique course ID database integer.
  - `hard` (`Boolean`, Optional): Defaults to `false`.
- **Logic**:
  - **Soft Delete (Default)**: Updates `isArchived: true` and writes today's ISO date string to `archivedAt`. Timetable slots are ignored for resolution boundaries on dates after this date, preserving historical attendance records.
  - **Hard Delete (`hard=true`)**: Wipes the database row completely. (Triggers cascade deletions on slots, overrides, and logs).

---

## 4. Implementation Code Breakdown

The backend implementation at `src/app/api/courses/route.ts` is divided into three REST operations:

### Phase 1: GET Request (Active Courses List)
Fetches all non-archived courses for the student, sorted alphabetically by code index.

```typescript
import { NextResponse } from 'next/server';
import { getAuthenticatedUser } from '@/lib/auth';
import { prisma } from '@/lib/prisma';

export async function GET() {
  try {
    const user = await getAuthenticatedUser();
    
    const courses = await prisma.course.findMany({
      where: { userId: user.id, isArchived: false },
      orderBy: { subjectId: 'asc' },
    });
    
    return NextResponse.json(courses);
  } catch (error: any) {
    if (error.message === 'Unauthorized: No authenticated user') {
      return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    }
    console.error('Error fetching courses:', error);
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}
```

---

### Phase 2: POST Request (Create, Edit or Restore)
Handles creating new courses, updates fields for existing courses, and automatically un-archives matching soft-deleted courses if they are re-registered.

```typescript
export async function POST(request: Request) {
  try {
    const user = await getAuthenticatedUser();
    const body = await request.json();
    const {
      id,
      subjectId,
      subjectName,
      subjectCode,
      teacherName,
      teacherCode,
      teacherContact,
      teacherEmail,
    } = body;

    if (!subjectId || !subjectName || !subjectCode) {
      return NextResponse.json({ error: 'Missing required fields' }, { status: 400 });
    }

    if (id) {
      // Edit existing course — verify ownership
      const existing = await prisma.course.findFirst({
        where: { id: parseInt(id), userId: user.id },
      });
      if (!existing) {
        return NextResponse.json({ error: 'Course not found' }, { status: 404 });
      }

      const updatedCourse = await prisma.course.update({
        where: { id: parseInt(id) },
        data: {
          subjectId,
          subjectName,
          subjectCode,
          teacherName: teacherName || '',
          teacherCode: teacherCode || '',
          teacherContact: teacherContact || '',
          teacherEmail: teacherEmail || '',
        },
      });
      return NextResponse.json(updatedCourse);
    } else {
      // Create new course — check duplicate subjectId first
      const existing = await prisma.course.findUnique({
        where: {
          userId_subjectId: {
            userId: user.id,
            subjectId,
          },
        },
      });

      if (existing) {
        if (existing.isArchived) {
          // Unarchive the course instead of creating a duplicate row
          const restored = await prisma.course.update({
            where: { id: existing.id },
            data: {
              isArchived: false,
              archivedAt: null,
              subjectName,
              subjectCode,
              teacherName: teacherName || '',
              teacherCode: teacherCode || '',
              teacherContact: teacherContact || '',
              teacherEmail: teacherEmail || '',
            },
          });
          return NextResponse.json(restored);
        }
        return NextResponse.json({ error: `Subject ID ${subjectId} already exists` }, { status: 400 });
      }

      const newCourse = await prisma.course.create({
        data: {
          userId: user.id,
          subjectId,
          subjectName,
          subjectCode,
          teacherName: teacherName || '',
          teacherCode: teacherCode || '',
          teacherContact: teacherContact || '',
          teacherEmail: teacherEmail || '',
        },
      });
      return NextResponse.json(newCourse, { status: 201 });
    }
  } catch (error: any) {
    if (error.message === 'Unauthorized: No authenticated user') {
      return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    }
    console.error('Error creating/updating course:', error);
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}
```

---

### Phase 3: DELETE Request (Soft vs Hard Deletions)
Handles course soft-deletion (setting `isArchived: true` to preserve historic records for attendance reports) or hard-deletion (fully purging the database records).

```typescript
export async function DELETE(request: Request) {
  try {
    const user = await getAuthenticatedUser();
    const { searchParams } = new URL(request.url);
    const id = searchParams.get('id');
    const hardDelete = searchParams.get('hard') === 'true';

    if (!id) {
      return NextResponse.json({ error: 'Missing course ID' }, { status: 400 });
    }

    // Verify course ownership
    const course = await prisma.course.findFirst({
      where: { id: parseInt(id), userId: user.id },
    });
    if (!course) {
      return NextResponse.json({ error: 'Course not found' }, { status: 404 });
    }

    if (hardDelete) {
      // Hard delete — removes everything including historical database relations
      await prisma.course.delete({
        where: { id: parseInt(id) },
      });
    } else {
      // Soft delete — archive the course, preserving historical data
      const today = new Date();
      const dateStr = today.toISOString().split('T')[0];
      
      await prisma.course.update({
        where: { id: parseInt(id) },
        data: {
          isArchived: true,
          archivedAt: dateStr,
        },
      });
    }

    return NextResponse.json({ success: true });
  } catch (error: any) {
    if (error.message === 'Unauthorized: No authenticated user') {
      return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    }
    console.error('Error deleting course:', error);
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}
```

