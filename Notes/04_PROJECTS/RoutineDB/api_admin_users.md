---
tags: [api-admin, users, membership, roles, backend]
---

# Admin API: Student Directory & Roles Auditor

This endpoint allows administrators to manage registered user accounts, allocate administrator roles, and tag university departments, located at `src/app/api/admin/users/route.ts`.

- **File Link**: [route.ts](file:///d:/02_CODE/04_TEST/Routine/src/app/api/admin/users/route.ts)
- **Backlinks**: [[index]], [[component_admin_panel]], [[admin_api]]

---

## 1. GET `/api/admin/users`

- **Purpose**: Retrieves list of all registered student profiles in the database, sorted ascending by incremental ID.
- **Authentication**: Required (`Admin` role check)
- **Success Response JSON**:
  ```json
  [
    {
      "id": 1,
      "email": "user@gmail.com",
      "name": "Jane Doe",
      "color": "#1A5276",
      "role": "user",
      "university": "DU",
      "courseName": "BSSE-18",
      "courseStartDate": "2026-01-01",
      "createdAt": "2026-07-04T04:19:24.000Z"
    }
  ]
  ```

---

## 2. POST `/api/admin/users`

- **Purpose**: Modifies user account settings or escalates account privileges.
- **Authentication**: Required (`Admin` role check)
- **JSON Payload Parameters**:
  - `id` (`String`/`Int`, Required): Target user identifier.
  - `role` (`String`, Optional): `"user"` or `"admin"`. Can promote/demote users.
  - `university` & `courseName` (`String`, Optional): Modifies primary academic batch tags.
  - `name` (`String`, Optional).

---

## 3. DELETE `/api/admin/users`

- **Purpose**: Removes a user account and deletes all related telemetry records from the database.
- **Authentication**: Required (`Admin` role check)
- **URL Query Parameters**:
  - `id` (`Int`, Required): Record identifier key to wipe.
- **Relational Cascades**: Database constraints wipe all records linked to this user across other tables (`Course`, `WeeklySlot`, `DailyClass`, `Attendance`, `Vacation`, `UserSecondaryTag`).

---

## 4. Source Code

Here is the complete implementation of `src/app/api/admin/users/route.ts`:

```typescript
import { NextResponse } from 'next/server';
import { requireAdmin } from '@/lib/auth';
import { prisma } from '@/lib/prisma';

// GET: List all users
export async function GET() {
  try {
    await requireAdmin();
    const users = await prisma.user.findMany({
      orderBy: { id: 'asc' },
    });
    return NextResponse.json(users);
  } catch (error: any) {
    if (error.message.includes('Unauthorized') || error.message.includes('Forbidden')) {
      return NextResponse.json({ error: error.message }, { status: 403 });
    }
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}

// POST: Update user role, tags, etc.
export async function POST(request: Request) {
  try {
    await requireAdmin();
    const body = await request.json();
    const { id, role, university, courseName, name } = body;

    if (!id) {
      return NextResponse.json({ error: 'Missing user ID' }, { status: 400 });
    }

    const updateData: any = {};
    if (role !== undefined) updateData.role = role;
    if (university !== undefined) updateData.university = university;
    if (courseName !== undefined) updateData.courseName = courseName;
    if (name !== undefined) updateData.name = name;

    const updated = await prisma.user.update({
      where: { id: parseInt(id) },
      data: updateData,
    });

    return NextResponse.json(updated);
  } catch (error: any) {
    if (error.message.includes('Unauthorized') || error.message.includes('Forbidden')) {
      return NextResponse.json({ error: error.message }, { status: 403 });
    }
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}

// DELETE: Delete a user
export async function DELETE(request: Request) {
  try {
    await requireAdmin();
    const { searchParams } = new URL(request.url);
    const id = searchParams.get('id');
    if (!id) return NextResponse.json({ error: 'Missing ID' }, { status: 400 });

    await prisma.user.delete({
      where: { id: parseInt(id) },
    });
    return NextResponse.json({ success: true });
  } catch (error: any) {
    if (error.message.includes('Unauthorized') || error.message.includes('Forbidden')) {
      return NextResponse.json({ error: error.message }, { status: 403 });
    }
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}
```
