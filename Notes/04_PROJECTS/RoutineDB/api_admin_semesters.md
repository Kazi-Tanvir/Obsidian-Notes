---
tags: [api-admin, semesters, term-dates, validation, backend]
---

# Admin API: Academic Semesters Manager

This endpoint handles administrator-only term scheduling operations (declaring semester start and end boundary dates for batch tags), located at `src/app/api/admin/semesters/route.ts`.

- **File Link**: [route.ts](file:///d:/02_CODE/04_TEST/Routine/src/app/api/admin/semesters/route.ts)
- **Backlinks**: [[index]], [[component_admin_panel]], [[admin_api]], [[api_calendar]]

---

## 1. GET `/api/admin/semesters`

- **Purpose**: Lists semester configurations, sorted descending by start date (most recent first).
- **Authentication**: Required (`Admin` role check)
- **URL Query Parameters**:
  - `university` & `courseName` (`String`, Optional): Filters results to semesters defined for those tag groupings.
- **Success Response JSON**:
  ```json
  [
    {
      "id": 1,
      "name": "Spring 2026",
      "startDate": "2026-01-10",
      "endDate": "2026-06-15",
      "university": "University of Dhaka",
      "courseName": "BSSE-18",
      "isActive": true
    }
  ]
  ```

---

## 2. POST `/api/admin/semesters`

- **Purpose**: Creates a new academic term registry or edits date scopes on an existing block.
- **Authentication**: Required (`Admin` role check)
- **JSON Payload Parameters**:
  - `id` (`Int`, Optional): Record database identifier (triggers edit flow).
  - `name` (`String`, Required): Semester tag title (e.g. `"Spring 2026"`).
  - `startDate` & `endDate` (`YYYY-MM-DD` strings, Required).
  - `university` & `courseName` (`String`, Optional): Subscribed batch tags.
  - `isActive` (`Boolean`, Optional): Defaults to `true`.
- **Validation Rules**:
  - **Date ordering check**: Validates that `startDate` is equal to or chronologically before `endDate`. Returns a `400 Bad Request` if bounds are reversed.
  - **Deduplication Gate**: Catches database collisions if the name and tag filters overlap with a pre-existing semester (Prisma compound unique index exception `P2002`).

---

## 3. DELETE `/api/admin/semesters`

- **Purpose**: Deletes a semester definition block.
- **Authentication**: Required (`Admin` role check)
- **URL Query Parameters**:
  - `id` (`Int`, Required): Unique record key.
- **Success Response JSON**:
  ```json
  { "success": true }
  ```

---

## 4. Implementation Code Breakdown

The source code in `src/app/api/admin/semesters/route.ts` is divided into three key REST operations:

### Phase 1: GET Request (Fetch Semesters)
Lists semesters, with optional tag filters for `university` and `courseName`.

```typescript
import { NextRequest, NextResponse } from 'next/server';
import { requireAdmin } from '@/lib/auth';
import { prisma } from '@/lib/prisma';
import { normalizeTag } from '@/lib/utils';

export async function GET(req: NextRequest) {
  try {
    await requireAdmin();

    const { searchParams } = new URL(req.url);
    const university = searchParams.get('university');
    const courseName = searchParams.get('courseName');

    const where: any = {};
    if (university !== null) where.university = normalizeTag(university);
    if (courseName !== null) where.courseName = normalizeTag(courseName);

    const semesters = await prisma.semester.findMany({
      where,
      orderBy: { startDate: 'desc' },
    });

    return NextResponse.json(semesters);
  } catch (error: any) {
    if (error.message === 'Forbidden: Admin access required') {
      return NextResponse.json({ error: 'Forbidden' }, { status: 403 });
    }
    if (error.message === 'Unauthorized: No authenticated user') {
      return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    }
    console.error('Error fetching semesters:', error);
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}
```

---

### Phase 2: POST Request (Create/Edit Semester)
Validates that `startDate <= endDate`, normalizes tags, and handles compound index collision checks.

```typescript
export async function POST(req: NextRequest) {
  try {
    await requireAdmin();

    const { id, name, startDate, endDate, university, courseName, isActive } = await req.json();

    if (!name || !startDate || !endDate) {
      return NextResponse.json({ error: 'Name, start date, and end date are required' }, { status: 400 });
    }

    if (startDate > endDate) {
      return NextResponse.json({ error: 'Start date must be before end date' }, { status: 400 });
    }

    const normUni = normalizeTag(university);
    const normCourse = normalizeTag(courseName);

    if (id) {
      // Update existing semester configuration
      const updated = await prisma.semester.update({
        where: { id: parseInt(id) },
        data: {
          name,
          startDate,
          endDate,
          university: normUni,
          courseName: normCourse,
          isActive: isActive !== undefined ? isActive : true,
        },
      });
      return NextResponse.json(updated);
    } else {
      // Create new semester configuration
      const created = await prisma.semester.create({
        data: {
          name,
          startDate,
          endDate,
          university: normUni,
          courseName: normCourse,
          isActive: isActive !== undefined ? isActive : true,
        },
      });
      return NextResponse.json(created);
    }
  } catch (error: any) {
    if (error.message === 'Forbidden: Admin access required') {
      return NextResponse.json({ error: 'Forbidden' }, { status: 403 });
    }
    if (error.message === 'Unauthorized: No authenticated user') {
      return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    }
    if (error.code === 'P2002') {
      // Handles compound key collisions gracefully
      return NextResponse.json({ error: 'A semester with this name and tags already exists' }, { status: 400 });
    }
    console.error('Error saving semester:', error);
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}
```

---

### Phase 3: DELETE Request (Remove Semester)
Removes the semester calendar boundaries block.

```typescript
export async function DELETE(req: NextRequest) {
  try {
    await requireAdmin();

    const { searchParams } = new URL(req.url);
    const id = parseInt(searchParams.get('id') || '');

    if (!id) {
      return NextResponse.json({ error: 'Semester ID is required' }, { status: 400 });
    }

    await prisma.semester.delete({ where: { id } });
    return NextResponse.json({ success: true });
  } catch (error: any) {
    if (error.message === 'Forbidden: Admin access required') {
      return NextResponse.json({ error: 'Forbidden' }, { status: 403 });
    }
    if (error.message === 'Unauthorized: No authenticated user') {
      return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    }
    console.error('Error deleting semester:', error);
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}
```
