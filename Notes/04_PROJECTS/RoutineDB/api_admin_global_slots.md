---
tags: [api-admin, slots, template, weekly-slots, backend]
---

# Admin API: Master Slots Template Manager

This endpoint handles administrator-only operations to configure weekly slots inside global course templates, located at `src/app/api/admin/global-slots/route.ts`.

- **File Link**: [route.ts](file:///d:/02_CODE/04_TEST/Routine/src/app/api/admin/global-slots/route.ts)
- **Backlinks**: [[index]], [[component_admin_panel]], [[admin_api]], [[api_admin_global_courses]]

---

## 1. GET `/api/admin/global-slots`

- **Purpose**: Lists global weekly slots template records.
- **Authentication**: Required (`Admin` role check)
- **URL Query Parameters**:
  - `globalCourseId` (`Int`, Optional): If provided, filters results to weekly slots belonging to that course.
- **Success Response JSON**:
  ```json
  [
    {
      "id": 8,
      "globalCourseId": 1,
      "dayOfWeek": "SUNDAY",
      "startTime": "08:00",
      "endTime": "09:30",
      "room": "205-IIT",
      "group": "A"
    }
  ]
  ```

---

## 2. POST `/api/admin/global-slots`

- **Purpose**: Schedules a new recurring slot template inside a global course, or updates details on an existing slot.
- **Authentication**: Required (`Admin` role check)
- **JSON Payload Parameters**:
  - `id` (`Int`, Optional): Record identifier key (triggers update flow).
  - `globalCourseId` (`Int`, Required): Parent global course identifier.
  - `dayOfWeek` (`String`, Required): Day enum (e.g. `"SUNDAY"`).
  - `startTime` & `endTime` (`String` format `"HH:MM"`, Required).
  - `room` & `group` strings.

---

## 3. DELETE `/api/admin/global-slots`

- **Purpose**: Deletes a global slot template from the course schedule blueprint.
- **Authentication**: Required (`Admin` role check)
- **URL Query Parameters**:
  - `id` (`Int`, Required): Unique identifier key of the slot record.
- **Success Response JSON**:
  ```json
  { "success": true }
  ```

---

## 4. Implementation Code Breakdown

The source code in `src/app/api/admin/global-slots/route.ts` is divided into three parts:

### Phase 1: GET Request (Fetch Slots)
Queries all global slots, with an optional filter for `globalCourseId`.

```typescript
import { NextResponse } from 'next/server';
import { requireAdmin } from '@/lib/auth';
import { prisma } from '@/lib/prisma';

export async function GET(request: Request) {
  try {
    await requireAdmin();
    const { searchParams } = new URL(request.url);
    const globalCourseId = searchParams.get('globalCourseId');

    const slots = await prisma.globalWeeklySlot.findMany({
      where: globalCourseId ? { globalCourseId: parseInt(globalCourseId) } : {},
      orderBy: [
        { dayOfWeek: 'asc' },
        { startTime: 'asc' },
      ],
    });
    return NextResponse.json(slots);
  } catch (error: any) {
    if (error.message.includes('Unauthorized') || error.message.includes('Forbidden')) {
      return NextResponse.json({ error: error.message }, { status: 403 });
    }
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}
```

---

### Phase 2: POST Request (Create/Edit Slot Template)
Validates fields and inserts or updates a global weekly slot template.

```typescript
export async function POST(request: Request) {
  try {
    await requireAdmin();
    const body = await request.json();
    const { id, globalCourseId, dayOfWeek, startTime, endTime, room, group } = body;

    if (!globalCourseId || !dayOfWeek || !startTime || !endTime) {
      return NextResponse.json({ error: 'Missing required fields' }, { status: 400 });
    }

    const slotData = {
      globalCourseId: parseInt(globalCourseId),
      dayOfWeek,
      startTime,
      endTime,
      room: room || '',
      group: group || '',
    };

    if (id) {
      // Update existing slot template
      const updated = await prisma.globalWeeklySlot.update({
        where: { id: parseInt(id) },
        data: slotData,
      });
      return NextResponse.json(updated);
    } else {
      // Create new slot template
      const created = await prisma.globalWeeklySlot.create({
        data: slotData,
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
```

---

### Phase 3: DELETE Request (Remove Slot Blueprint)
Deletes the weekly template slot from the database.

```typescript
export async function DELETE(request: Request) {
  try {
    await requireAdmin();
    const { searchParams } = new URL(request.url);
    const id = searchParams.get('id');
    if (!id) return NextResponse.json({ error: 'Missing ID' }, { status: 400 });

    await prisma.globalWeeklySlot.delete({
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

