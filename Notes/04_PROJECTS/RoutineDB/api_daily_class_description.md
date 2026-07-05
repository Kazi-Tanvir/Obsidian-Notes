---
tags: [api-user, api-admin, description, overrides, class-notes, backend]
---

# API: Class Session Note Editor

This endpoint adds, updates, or deletes a description note for a specific class instance, located at `src/app/api/daily-class/description/route.ts`.

- **File Link**: [route.ts](file:///d:/02_CODE/04_TEST/Routine/src/app/api/daily-class/description/route.ts)
- **Backlinks**: [[index]], [[component_modals]], [[api]], [[admin_api]]

---

## 1. Endpoint Configuration

- **HTTP Method**: `POST`
- **Route URL**: `/api/daily-class/description`
- **Authentication**: Required (`User` session check)

---

## 2. Dynamic Override Instantiation Logic

The API supports updating notes for both pre-existing overrides and default template sessions:

### A. Case 1: Pre-existing Class Override (has `dailyClassId`)
- Parses string identifiers that may contain frontend prefixes (e.g. replacing `"override-14"` or `"extra-8"` into an integer `14` or `8`).
- Verifies student ownership of the override record.
- Commits the updated description directly to the record. If the text is empty, resets the field to `null`.

### B. Case 2: Template Slot (no `dailyClassId` yet)
- If the session is generated from a weekly slot and has no override record, the client sends:
  - `{ weeklySlotId, courseId, date, description }`
- The API queries the template weekly slot parameters (`startTime`, `endTime`, `room`, `group`).
- Instantiates a new `DailyClass` override record in the database, sets its status to `"SCHEDULED"`, copies all slot properties, and writes the custom description. This converts a template instance into a concrete database override record.

---

## 3. Implementation Code Breakdown

The source code in `src/app/api/daily-class/description/route.ts` is split into two logical paths:

### Phase 1: Existing Overrides Updates
If `dailyClassId` is present in the request body, parses prefixes and updates the record directly after validating ownership checks.

```typescript
import { NextResponse } from 'next/server';
import { getAuthenticatedUser } from '@/lib/auth';
import { prisma } from '@/lib/prisma';

export async function POST(request: Request) {
  try {
    const user = await getAuthenticatedUser();
    const body = await request.json();
    const { dailyClassId, weeklySlotId, courseId, date, description } = body;

    // Case 1. If dailyClassId is specified, directly update it
    if (dailyClassId) {
      const dbId = typeof dailyClassId === 'string' && dailyClassId.startsWith('override-')
        ? parseInt(dailyClassId.replace('override-', ''))
        : typeof dailyClassId === 'string' && dailyClassId.startsWith('extra-')
        ? parseInt(dailyClassId.replace('extra-', ''))
        : parseInt(dailyClassId);

      const existingClass = await prisma.dailyClass.findFirst({
        where: { id: dbId, userId: user.id },
      });

      if (!existingClass) {
        return NextResponse.json({ error: 'Daily class instance not found' }, { status: 404 });
      }

      const updated = await prisma.dailyClass.update({
        where: { id: dbId },
        data: { description: description || null },
      });

      return NextResponse.json(updated);
    }
```

---

### Phase 2: Template Slots Promotion & Notes Saving
If `dailyClassId` is missing but `weeklySlotId`, `courseId`, and `date` are present, promotes the recurring template slot to a concrete database override record and attaches the description.

```typescript
    // Case 2. If weeklySlotId and date are specified, find or create the override
    if (weeklySlotId && date && courseId) {
      const slotId = parseInt(weeklySlotId);
      const cId = parseInt(courseId);

      // Check if override already exists
      const existingOverride = await prisma.dailyClass.findFirst({
        where: {
          userId: user.id,
          weeklySlotId: slotId,
          date,
        },
      });

      if (existingOverride) {
        const updated = await prisma.dailyClass.update({
          where: { id: existingOverride.id },
          data: { description: description || null },
        });
        return NextResponse.json(updated);
      }

      // Fetch weekly slot properties
      const slot = await prisma.weeklySlot.findFirst({
        where: { id: slotId, userId: user.id },
      });

      if (!slot) {
        return NextResponse.json({ error: 'Weekly slot not found' }, { status: 404 });
      }

      // Promote slot to DailyClass override record and attach description
      const created = await prisma.dailyClass.create({
        data: {
          userId: user.id,
          courseId: cId,
          weeklySlotId: slotId,
          date,
          startTime: slot.startTime,
          endTime: slot.endTime,
          room: slot.room || '',
          group: slot.group || '',
          status: 'SCHEDULED',
          isExtra: false,
          description: description || null,
        },
      });

      return NextResponse.json(created);
    }

    return NextResponse.json({ error: 'Missing required parameters' }, { status: 400 });
  } catch (error: any) {
    if (error.message === 'Unauthorized: No authenticated user') {
      return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    }
    console.error('Error saving class description:', error);
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}
```

