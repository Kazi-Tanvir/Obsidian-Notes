---
tags: [api-admin, suggestions, review, approve, reject, backend]
---

# Admin API: Suggestions Audit Board

This endpoint enables administrators to inspect modification proposals suggested by students and process approvals or rejections, located at `src/app/api/admin/suggestions/route.ts`.

- **File Link**: [route.ts](file:///d:/02_CODE/04_TEST/Routine/src/app/api/admin/suggestions/route.ts)
- **Backlinks**: [[index]], [[component_admin_panel]], [[admin_api]], [[api_suggestions]]

---

## 1. GET `/api/admin/suggestions`

- **Purpose**: Lists all student schedule suggestions.
- **Authentication**: Required (`Admin` role check)
- **URL Query Parameters**:
  - `status` (`String`, Optional): Filter by suggestion status (`"PENDING"`, `"APPROVED"`, `"REJECTED"`).
- **Sorting Order**: Returns `PENDING` suggestions first, followed by resolved ones sorted descending by creation date.

---

## 2. POST `/api/admin/suggestions`

- **Purpose**: Approves or rejects a suggestion.
- **Authentication**: Required (`Admin` role check)
- **JSON Payload Parameters**:
  - `suggestionId` (`String`/`Int`, Required): Record identifier.
  - `action` (`String`, Required): Either `"approve"` or `"reject"`.

### Decision Logic:
- **`reject`**: Updates the `ClassSuggestion` status to `"REJECTED"`.
- **`approve`**:
  1. **Create Global Daily Override**: Creates or updates a `GlobalDailyOverride` record matching the suggestion's target `globalCourseId` and `date`.
  2. **Audit Student Subscriptions**: Queries all student courses matching the `subjectId` where `source === 'admin'` and `isArchived === false`.
  3. **Calendar Override Insertion**:
     - Determines the weekday name (e.g. `"MONDAY"`) from the target date.
     - Loops through each student course and matching weekly slots.
     - Creates or updates a personal `DailyClass` override record for each student matching the slot times, room, group, and reason (marked as `"Approved user suggestion"`).
  4. **Set Approved Status**: Updates the `ClassSuggestion` status to `"APPROVED"`.

---

## 3. Implementation Code Breakdown

The source code in `src/app/api/admin/suggestions/route.ts` is divided into three key steps:

### Phase 1: GET Request (Fetch Suggestions)
Pulls all suggestions, sorting by pending items first and then descending by creation date.

```typescript
import { NextRequest, NextResponse } from 'next/server';
import { requireAdmin } from '@/lib/auth';
import { prisma } from '@/lib/prisma';

export async function GET(req: NextRequest) {
  try {
    await requireAdmin();

    const { searchParams } = new URL(req.url);
    const statusFilter = searchParams.get('status');

    const where: any = {};
    if (statusFilter) {
      where.status = statusFilter;
    }

    const suggestions = await prisma.classSuggestion.findMany({
      where,
      include: {
        globalCourse: {
          select: {
            id: true,
            subjectId: true,
            subjectName: true,
            subjectCode: true,
            university: true,
            courseName: true,
          },
        },
      },
      orderBy: [
        { status: 'asc' }, // PENDING first
        { createdAt: 'desc' },
      ],
    });

    return NextResponse.json(suggestions);
  } catch (error: any) {
    if (error.message === 'Forbidden: Admin access required') {
      return NextResponse.json({ error: 'Forbidden' }, { status: 403 });
    }
    if (error.message === 'Unauthorized: No authenticated user') {
      return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    }
    console.error('Error fetching suggestions:', error);
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}
```

---

### Phase 2: POST Request - Validation and Rejection Decisions
Verifies administrator authorization, validates inputs, and processes simple rejections directly.

```typescript
export async function POST(req: NextRequest) {
  try {
    await requireAdmin();

    const { suggestionId, action } = await req.json();

    if (!suggestionId || !action) {
      return NextResponse.json({ error: 'Missing required fields: suggestionId, action' }, { status: 400 });
    }

    if (!['approve', 'reject'].includes(action)) {
      return NextResponse.json({ error: 'Action must be "approve" or "reject"' }, { status: 400 });
    }

    const suggestion = await prisma.classSuggestion.findUnique({
      where: { id: parseInt(suggestionId) },
      include: {
        globalCourse: {
          include: { weeklySlots: true },
        },
      },
    });

    if (!suggestion) {
      return NextResponse.json({ error: 'Suggestion not found' }, { status: 404 });
    }

    if (suggestion.status !== 'PENDING') {
      return NextResponse.json({ error: 'This suggestion has already been processed' }, { status: 400 });
    }

    if (action === 'reject') {
      const updated = await prisma.classSuggestion.update({
        where: { id: suggestion.id },
        data: { status: 'REJECTED' },
      });
      return NextResponse.json({ success: true, suggestion: updated, action: 'rejected' });
    }
```

---

### Phase 3: POST Request - Approvals & Student Overrides Propagation
Upserts the `GlobalDailyOverride` record based on suggestion parameters and propagates updates to student diaries.

```typescript
    // === APPROVE FLOW ===
    const overrideStatus = suggestion.suggestedStatus;
    const override = await prisma.globalDailyOverride.upsert({
      where: {
        globalCourseId_date: {
          globalCourseId: suggestion.globalCourseId,
          date: suggestion.date,
        },
      },
      create: {
        globalCourseId: suggestion.globalCourseId,
        date: suggestion.date,
        status: overrideStatus,
        newStartTime: overrideStatus === 'RESCHEDULED' ? suggestion.newStartTime : null,
        newEndTime: overrideStatus === 'RESCHEDULED' ? suggestion.newEndTime : null,
        newRoom: suggestion.newRoom,
        description: suggestion.reason ? `[User Suggestion] ${suggestion.reason}` : '[User Suggestion] Approved',
      },
      update: {
        status: overrideStatus,
        newStartTime: overrideStatus === 'RESCHEDULED' ? suggestion.newStartTime : null,
        newEndTime: overrideStatus === 'RESCHEDULED' ? suggestion.newEndTime : null,
        newRoom: suggestion.newRoom,
        description: suggestion.reason ? `[User Suggestion] ${suggestion.reason}` : '[User Suggestion] Approved',
      },
    });

    // Find subscribed student course copies
    const userCourses = await prisma.course.findMany({
      where: {
        subjectId: suggestion.globalCourse.subjectId,
        source: 'admin',
        isArchived: false,
      },
      include: {
        weeklySlots: true,
      },
    });

    const dateObj = new Date(suggestion.date + 'T00:00:00');
    const dayNames = ['SUNDAY', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY'];
    const dayOfWeek = dayNames[dateObj.getDay()];

    let overridesApplied = 0;

    for (const course of userCourses) {
      const matchingSlots = course.weeklySlots.filter(s => s.dayOfWeek === dayOfWeek && s.source !== 'personal');

      for (const slot of matchingSlots) {
        const existing = await prisma.dailyClass.findFirst({
          where: {
            userId: course.userId,
            courseId: course.id,
            date: suggestion.date,
            weeklySlotId: slot.id,
          },
        });

        if (existing) {
          await prisma.dailyClass.update({
            where: { id: existing.id },
            data: {
              status: overrideStatus,
              startTime: overrideStatus === 'RESCHEDULED' && suggestion.newStartTime ? suggestion.newStartTime : slot.startTime,
              endTime: overrideStatus === 'RESCHEDULED' && suggestion.newEndTime ? suggestion.newEndTime : slot.endTime,
              room: suggestion.newRoom || slot.room,
              description: suggestion.reason ? `[Suggestion] ${suggestion.reason}` : '[Suggestion] Approved',
            },
          });
        } else {
          await prisma.dailyClass.create({
            data: {
              userId: course.userId,
              courseId: course.id,
              weeklySlotId: slot.id,
              date: suggestion.date,
              startTime: overrideStatus === 'RESCHEDULED' && suggestion.newStartTime ? suggestion.newStartTime : slot.startTime,
              endTime: overrideStatus === 'RESCHEDULED' && suggestion.newEndTime ? suggestion.newEndTime : slot.endTime,
              room: suggestion.newRoom || slot.room,
              group: slot.group,
              status: overrideStatus,
              isExtra: false,
              description: suggestion.reason ? `[Suggestion] ${suggestion.reason}` : null,
            },
          });
        }
        overridesApplied++;
      }
    }

    const updated = await prisma.classSuggestion.update({
      where: { id: suggestion.id },
      data: { status: 'APPROVED' },
    });

    return NextResponse.json({
      success: true,
      suggestion: updated,
      action: 'approved',
      overridesApplied,
      studentsAffected: userCourses.length,
    });
  } catch (error: any) {
    if (error.message === 'Forbidden: Admin access required') {
      return NextResponse.json({ error: 'Forbidden' }, { status: 403 });
    }
    if (error.message === 'Unauthorized: No authenticated user') {
      return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    }
    console.error('Error processing suggestion:', error);
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}
```

