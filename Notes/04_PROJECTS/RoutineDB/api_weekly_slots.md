---
tags: [api-user, slots, timetable, override-cleanup, backend]
---

# User API: Weekly Recurring Timetable Slots

This endpoint manages the weekly recurring schedules templates assigned to courses, located at `src/app/api/weekly-slots/route.ts`.

- **File Link**: [route.ts](file:///d:/02_CODE/04_TEST/Routine/src/app/api/weekly-slots/route.ts)
- **Backlinks**: [[index]], [[component_setup_view]], [[api]], [[api_calendar]]

---

## 1. GET `/api/weekly-slots`

- **Purpose**: Lists all weekly slots configured by the active user, embedding course relational titles.
- **Authentication**: Required (`User` session check)
- **Success Response JSON**:
  ```json
  [
    {
      "id": 12,
      "userId": 1,
      "courseId": 5,
      "dayOfWeek": "MONDAY",
      "startTime": "08:30",
      "endTime": "10:00",
      "room": "304-A",
      "group": "Group A",
      "activeFrom": null,
      "activeUntil": null,
      "source": "personal",
      "course": {
        "id": 5,
        "subjectId": "CSE-1101",
        "subjectName": "Structured Programming",
        "subjectCode": "CSE-1101"
      }
    }
  ]
  ```

---

## 2. POST `/api/weekly-slots`

- **Purpose**: Schedules a new recurring slot or edits parameters on an existing template.
- **Authentication**: Required (`User` session check)
- **JSON Payload Parameters**:
  - `id` (`Int`, Optional): Database key. If provided, triggers edit actions.
  - `courseId` (`Int`, Required): Relational course key.
  - `dayOfWeek` (`String`, Required): Day enum (e.g. `"MONDAY"`).
  - `startTime` & `endTime` (`String` format `"HH:MM"`, Required).
  - `room` & `group` strings.
  - `activeFrom` & `activeUntil` (`YYYY-MM-DD` strings, Optional).
  - `updateMode` (`String`, Optional): Mode is either `"future"` (default) or `"all"`. Determines how past/future overrides are scrubbed.
- **Form Actions & DailyClass Overrides Cleanup**:
  - Verifies ownership of both parent course and slot items.
  - When editing a slot, the system cleans up previously generated `DailyClass` overrides linked to this slot:
    - **`all`**: Deletes all generated overrides in the database, reverting the entire historical calendar back to template defaults.
    - **`future`**: Retains historical logs (for attendance records integrity) but deletes overrides on dates after today (`date > today`), forcing the calendar engine to resolve modifications using the updated weekly slot structure from tomorrow onwards.

---

## 3. DELETE `/api/weekly-slots`

- **Purpose**: Deletes a weekly template slot.
- **Authentication**: Required (`User` session check)
- **URL Query Parameters**:
  - `id` (`Int`, Required): Slot record key.
- **Validation**: Verifies slot ownership.
- **Success Response JSON**:
  ```json
  { "success": true }
  ```

---

## 4. Source Code

Here is the complete implementation of `src/app/api/weekly-slots/route.ts`:

```typescript
import { NextResponse } from 'next/server';
import { getAuthenticatedUser } from '@/lib/auth';
import { prisma } from '@/lib/prisma';

// GET: Fetch weekly slots for the authenticated user
export async function GET() {
  try {
    const user = await getAuthenticatedUser();

    const slots = await prisma.weeklySlot.findMany({
      where: { userId: user.id },
      include: {
        course: true,
      },
    });

    return NextResponse.json(slots);
  } catch (error: any) {
    if (error.message === 'Unauthorized: No authenticated user') {
      return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    }
    console.error('Error fetching weekly slots:', error);
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}

// POST: Create or edit a weekly slot for the authenticated user
export async function POST(request: Request) {
  try {
    const user = await getAuthenticatedUser();
    const body = await request.json();
    const { id, courseId, dayOfWeek, startTime, endTime, room, group, updateMode, activeFrom, activeUntil } = body;

    if (!courseId || !dayOfWeek || !startTime || !endTime) {
      return NextResponse.json({ error: 'Missing required fields' }, { status: 400 });
    }

    // Verify course ownership
    const course = await prisma.course.findFirst({
      where: { id: parseInt(courseId), userId: user.id },
    });
    if (!course) {
      return NextResponse.json({ error: 'Course not found' }, { status: 404 });
    }

    if (id) {
      // Verify slot ownership
      const existingSlot = await prisma.weeklySlot.findFirst({
        where: { id: parseInt(id), userId: user.id },
      });
      if (!existingSlot) {
        return NextResponse.json({ error: 'Slot not found' }, { status: 404 });
      }

      const updatedSlot = await prisma.weeklySlot.update({
        where: { id: parseInt(id) },
        data: {
          courseId: parseInt(courseId),
          dayOfWeek,
          startTime,
          endTime,
          room: room || '',
          group: group || '',
          activeFrom: activeFrom || null,
          activeUntil: activeUntil || null,
        },
      });

      // Handle DailyClass cleanup based on updateMode
      const mode = updateMode || 'future'; // default to 'future'
      const todayStr = new Date().toISOString().split('T')[0];

      if (mode === 'all') {
        // Entire timeline: delete ALL DailyClass records tied to this slot
        await prisma.dailyClass.deleteMany({
          where: { weeklySlotId: parseInt(id), userId: user.id },
        });
      } else {
        // Future only: delete only future DailyClass records tied to this slot
        await prisma.dailyClass.deleteMany({
          where: {
            weeklySlotId: parseInt(id),
            userId: user.id,
            date: { gt: todayStr },
          },
        });
      }

      return NextResponse.json(updatedSlot);
    } else {
      const newSlot = await prisma.weeklySlot.create({
        data: {
          userId: user.id,
          courseId: parseInt(courseId),
          dayOfWeek,
          startTime,
          endTime,
          room: room || '',
          group: group || '',
          activeFrom: activeFrom || null,
          activeUntil: activeUntil || null,
        },
      });
      return NextResponse.json(newSlot, { status: 201 });
    }
  } catch (error: any) {
    if (error.message === 'Unauthorized: No authenticated user') {
      return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    }
    console.error('Error creating/updating weekly slot:', error);
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}

// DELETE: Remove a weekly slot (verify ownership)
export async function DELETE(request: Request) {
  try {
    const user = await getAuthenticatedUser();
    const { searchParams } = new URL(request.url);
    const id = searchParams.get('id');

    if (!id) {
      return NextResponse.json({ error: 'Missing slot ID' }, { status: 400 });
    }

    const slot = await prisma.weeklySlot.findFirst({
      where: { id: parseInt(id), userId: user.id },
    });
    if (!slot) {
      return NextResponse.json({ error: 'Slot not found' }, { status: 404 });
    }

    await prisma.weeklySlot.delete({
      where: { id: parseInt(id) },
    });

    return NextResponse.json({ success: true });
  } catch (error: any) {
    if (error.message === 'Unauthorized: No authenticated user') {
      return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    }
    console.error('Error deleting weekly slot:', error);
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}
```
