---
tags: [api-admin, announcements, broadcast, create, delete, backend]
---

# Admin API: Announcements Manager

This endpoint handles administrator-only operations to create, edit, list, and delete system-wide batch-targeted announcements, located at `src/app/api/admin/announcements/route.ts`.

- **File Link**: [route.ts](file:///d:/02_CODE/04_TEST/Routine/src/app/api/admin/announcements/route.ts)
- **Backlinks**: [[index]], [[component_admin_panel]], [[admin_api]], [[api_announcements]]

---

## 1. GET `/api/admin/announcements`

- **Purpose**: Lists all registered announcements in the system, sorted descending by creation timestamp.
- **Authentication**: Required (`Admin` role check)
- **Difference from User API**: Returns the entire list (including expired notices) so administrators can manage or archive old broadcasts from the control panel dashboard.
- **Success Response JSON**:
  ```json
  [
    {
      "id": 4,
      "title": "Semester Exams Schedule",
      "body": "Midterms begin next week. Wear formal attire.",
      "university": "University of Dhaka",
      "courseName": "BSSE-18",
      "expiresAt": "2026-07-15",
      "createdAt": "2026-07-04T04:19:24.000Z"
    }
  ]
  ```

---

## 2. POST `/api/admin/announcements`

- **Purpose**: Publishes a new broadcast alert or edits an existing message.
- **Authentication**: Required (`Admin` role check)
- **JSON Payload Parameters**:
  - `id` (`Int`, Optional): Announcement database identifier. If provided, edits the matching notice.
  - `title` (`String`, Required): Title heading.
  - `body` (`String` formatted as text, Required): Main announcement body text.
  - `university` & `courseName` (`String`, Optional): Specific target filters. If omitted, sends globally to all registered student dashboards.
  - `expiresAt` (`String` format `"YYYY-MM-DD"`, Optional): Date when the alert automatically hides. If omitted, persists permanently.
- **Tag Normalization**: Runs `normalizeTag()` on target tags before committing.

---

## 3. DELETE `/api/admin/announcements`

- **Purpose**: Wipes an announcement from the database.
- **Authentication**: Required (`Admin` role check)
- **URL Query Parameters**:
  - `id` (`Int`, Required): Record key to delete.
- **Success Response JSON**:
  ```json
  { "success": true }
  ```

---

## 4. Source Code

Here is the complete implementation of `src/app/api/admin/announcements/route.ts`:

```typescript
import { NextRequest, NextResponse } from 'next/server';
import { requireAdmin } from '@/lib/auth';
import { prisma } from '@/lib/prisma';
import { normalizeTag } from '@/lib/utils';

// GET: List all announcements (admin view — shows all including expired)
export async function GET() {
  try {
    await requireAdmin();

    const announcements = await prisma.announcement.findMany({
      orderBy: { createdAt: 'desc' },
    });

    return NextResponse.json(announcements);
  } catch (error: any) {
    if (error.message === 'Forbidden: Admin access required') {
      return NextResponse.json({ error: 'Forbidden' }, { status: 403 });
    }
    if (error.message === 'Unauthorized: No authenticated user') {
      return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    }
    console.error('Error fetching announcements:', error);
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}

// POST: Create or update an announcement
export async function POST(req: NextRequest) {
  try {
    await requireAdmin();

    const { id, title, body, university, courseName, expiresAt } = await req.json();

    if (!title || !body) {
      return NextResponse.json({ error: 'Title and body are required' }, { status: 400 });
    }

    const normUni = university ? normalizeTag(university) : null;
    const normCourse = courseName ? normalizeTag(courseName) : null;

    if (id) {
      const updated = await prisma.announcement.update({
        where: { id: parseInt(id) },
        data: {
          title,
          body,
          university: normUni,
          courseName: normCourse,
          expiresAt: expiresAt || null,
        },
      });
      return NextResponse.json(updated);
    } else {
      const created = await prisma.announcement.create({
        data: {
          title,
          body,
          university: normUni,
          courseName: normCourse,
          expiresAt: expiresAt || null,
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
    console.error('Error saving announcement:', error);
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}

// DELETE: Remove an announcement
export async function DELETE(req: NextRequest) {
  try {
    await requireAdmin();

    const { searchParams } = new URL(req.url);
    const id = parseInt(searchParams.get('id') || '');

    if (!id) {
      return NextResponse.json({ error: 'Announcement ID is required' }, { status: 400 });
    }

    await prisma.announcement.delete({ where: { id } });
    return NextResponse.json({ success: true });
  } catch (error: any) {
    if (error.message === 'Forbidden: Admin access required') {
      return NextResponse.json({ error: 'Forbidden' }, { status: 403 });
    }
    if (error.message === 'Unauthorized: No authenticated user') {
      return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    }
    console.error('Error deleting announcement:', error);
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}
```
