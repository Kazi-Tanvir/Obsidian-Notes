---
tags: [api-user, vacations, holidays, sick-leave, backend]
---

# User API: Personal Vacation Planner

This endpoint manages student personal sick leave blocks and holiday periods, located at `src/app/api/vacations/route.ts`.

- **File Link**: [route.ts](file:///d:/02_CODE/04_TEST/Routine/src/app/api/vacations/route.ts)
- **Backlinks**: [[index]], [[component_calendar_view]], [[api]], [[api_calendar]]

---

## 1. GET `/api/vacations`

- **Purpose**: Lists all personal vacations registered to the active student, sorted chronologically.
- **Authentication**: Required (`User` session check)
- **Success Response JSON**:
  ```json
  [
    {
      "id": 8,
      "userId": 1,
      "date": "2026-07-10",
      "type": "VACATION",
      "description": "Sick day"
    }
  ]
  ```

---

## 2. POST `/api/vacations`

- **Purpose**: Registers a vacation day, a range of holiday dates, or clears previously registered blocks.
- **Authentication**: Required (`User` session check)
- **JSON Payload Parameters**:
  - `date` (`String` format `"YYYY-MM-DD"`, Required): Start date of the vacation block.
  - `endDate` (`String` format `"YYYY-MM-DD"`, Optional): End date of the vacation block. If omitted, defaults to the start date (1-day duration).
  - `type` (`String`, Required): `"VACATION"`, `"ABSENT_DAY"`, or `"NONE"`.
  - `description` (`String`, Optional): Vacation description.
- **Logic**:
  - Automatically calculates the full array of dates in the range between `date` and `endDate` using `getDatesInRange()`.
  - **Clearing Mode (`type === "NONE"` or falsy)**: Deletes any existing vacation rows matching this user and the target dates, reverting the calendar dates back to standard session tracking.
  - **Upsert Mode**: Upserts `Vacation` rows in the database, mapping matching records by `(userId, date)` unique constraint key.

---

## 3. DELETE `/api/vacations`

- **Purpose**: Deletes a personal vacation row.
- **Authentication**: Required (`User` session check)
- **URL Query Parameters**:
  - `id` (`Int`, Required): Vacation record identifier.
- **Validation**: Verifies vacation ownership before deleting the row.
- **Success Response JSON**:
  ```json
  { "success": true }
  ```

---

## 4. Implementation Code Breakdown

The source code in `src/app/api/vacations/route.ts` is divided into three REST handler parts:

### Phase 1: Range Helper & GET Request (Fetch Holidays)
Computes dates lists inside ranges, and fetches active vacations for the student.

```typescript
import { NextResponse } from 'next/server';
import { getAuthenticatedUser } from '@/lib/auth';
import { prisma } from '@/lib/prisma';

// Helper to get dates between start and end
function getDatesInRange(startStr: string, endStr: string): string[] {
  const start = new Date(startStr);
  const end = new Date(endStr);
  const dates: string[] = [];
  const temp = new Date(start);
  while (temp <= end) {
    dates.push(temp.toISOString().split('T')[0]);
    temp.setDate(temp.getDate() + 1);
  }
  return dates;
}

export async function GET() {
  try {
    const user = await getAuthenticatedUser();

    const vacations = await prisma.vacation.findMany({
      where: { userId: user.id },
      orderBy: { date: 'asc' },
    });

    return NextResponse.json(vacations);
  } catch (error: any) {
    if (error.message === 'Unauthorized: No authenticated user') {
      return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    }
    console.error('Error fetching vacations:', error);
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}
```

---

### Phase 2: POST Request (Create Vacation Block)
Processes updates for a range of dates. If `type === 'NONE'`, removes vacation days, else upserts vacation metadata dates in loop parameters.

```typescript
export async function POST(request: Request) {
  try {
    const user = await getAuthenticatedUser();
    const body = await request.json();
    const { date, endDate, type, description } = body;

    if (!date) {
      return NextResponse.json({ error: 'Missing required parameters' }, { status: 400 });
    }

    const startStr = date;
    const endStr = endDate || date;
    const dates = getDatesInRange(startStr, endStr);
    const results = [];

    for (const currentDate of dates) {
      if (type === 'NONE' || !type) {
        // Clear vacation dates
        const existing = await prisma.vacation.findUnique({
          where: {
            userId_date: {
              userId: user.id,
              date: currentDate
            }
          }
        });
        if (existing) {
          await prisma.vacation.delete({ where: { id: existing.id } });
        }
      } else {
        // Upsert vacation properties
        const vacation = await prisma.vacation.upsert({
          where: {
            userId_date: {
              userId: user.id,
              date: currentDate
            }
          },
          update: { type, description: description || '' },
          create: {
            userId: user.id,
            date: currentDate,
            type,
            description: description || ''
          }
        });
        results.push(vacation);
      }
    }

    return NextResponse.json({ success: true, count: dates.length, results });
  } catch (error: any) {
    if (error.message === 'Unauthorized: No authenticated user') {
      return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    }
    console.error('Error saving vacations:', error);
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}
```

---

### Phase 3: DELETE Request (Remove Vacation Entry)
Deletes a vacation record by checking student ownership details.

```typescript
export async function DELETE(request: Request) {
  try {
    const user = await getAuthenticatedUser();
    const { searchParams } = new URL(request.url);
    const id = searchParams.get('id');

    if (!id) {
      return NextResponse.json({ error: 'Missing vacation ID' }, { status: 400 });
    }

    // Verify ownership
    const vacation = await prisma.vacation.findFirst({
      where: { id: parseInt(id), userId: user.id },
    });
    if (!vacation) {
      return NextResponse.json({ error: 'Vacation not found' }, { status: 404 });
    }

    await prisma.vacation.delete({ where: { id: parseInt(id) } });
    return NextResponse.json({ success: true });
  } catch (error: any) {
    if (error.message === 'Unauthorized: No authenticated user') {
      return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    }
    console.error('Error deleting vacation:', error);
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}
```

