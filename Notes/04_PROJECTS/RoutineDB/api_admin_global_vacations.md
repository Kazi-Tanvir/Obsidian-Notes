---
tags: [api-admin, vacations, holidays, targeting, backend]
---

# Admin API: Master Vacations Manager

This endpoint handles administrator-only configurations to manage global and batch-targeted holiday vacation schedules, located at `src/app/api/admin/global-vacations/route.ts`.

- **File Link**: [route.ts](file:///d:/02_CODE/04_TEST/Routine/src/app/api/admin/global-vacations/route.ts)
- **Backlinks**: [[index]], [[component_admin_panel]], [[admin_api]], [[api_vacations]]

---

## 1. GET `/api/admin/global-vacations`

- **Purpose**: Lists all global vacations in the system.
- **Authentication**: Required (`Admin` role check)
- **Success Response JSON**:
  ```json
  [
    {
      "id": 3,
      "date": "2026-07-06",
      "type": "VACATION",
      "description": "Eid-ul-Fitr Holiday",
      "university": "University of Dhaka",
      "courseName": "BSSE-18"
    }
  ]
  ```

---

## 2. POST `/api/admin/global-vacations`

- **Purpose**: Publishes a holiday or declares absent periods for specific batch groupings (or globally).
- **Authentication**: Required (`Admin` role check)
- **JSON Payload Parameters**:
  - `id` (`Int`, Optional): Record identifier key (updates matching record).
  - `date` (`String` format `"YYYY-MM-DD"`, Required): Start date of the holiday period.
  - `endDate` (`String` format `"YYYY-MM-DD"`, Optional): End date of the vacation period (defaults to the start date).
  - `type` (`String`, Optional): Defaults to `"VACATION"`.
  - `description` (`String`, Optional).
  - `university` & `courseName` (`String`, Optional): Batch target filters. If omitted (or null), the vacation applies globally to all students in the database.

### Logic:
- If `id` is present: Updates the record details.
- If creating new: Generates all dates in the range using `getDatesInRange()`. For each date, checks for existing records matching the specific `(date, university, courseName)` combination:
  - If existing: Updates the type and description.
  - If new: Inserts a new `GlobalVacation` row.

---

## 3. DELETE `/api/admin/global-vacations`

- **Purpose**: Deletes a global holiday record.
- **Authentication**: Required (`Admin` role check)
- **URL Query Parameters**:
  - `id` (`Int`, Required): Record identifier key to wipe.
- **Success Response JSON**:
  ```json
  { "success": true }
  ```

---

## 4. Source Code

Here is the complete implementation of `src/app/api/admin/global-vacations/route.ts`:

```typescript
import { NextResponse } from 'next/server';
import { requireAdmin } from '@/lib/auth';
import { prisma } from '@/lib/prisma';
import { normalizeTag } from '@/lib/utils';

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

// GET: Fetch all global vacations
export async function GET() {
  try {
    await requireAdmin();
    const vacations = await prisma.globalVacation.findMany({
      orderBy: { date: 'asc' },
    });
    return NextResponse.json(vacations);
  } catch (error: any) {
    if (error.message.includes('Unauthorized') || error.message.includes('Forbidden')) {
      return NextResponse.json({ error: error.message }, { status: 403 });
    }
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}

// POST: Create/update a global vacation
export async function POST(request: Request) {
  try {
    await requireAdmin();
    const body = await request.json();
    const { id, date, endDate, type, description, university, courseName } = body;

    if (!date) {
      return NextResponse.json({ error: 'Missing date' }, { status: 400 });
    }

    const normUniversity = university ? normalizeTag(university) : null;
    const normCourseName = courseName ? normalizeTag(courseName) : null;

    if (id) {
      const updated = await prisma.globalVacation.update({
        where: { id: parseInt(id) },
        data: {
          date,
          type: type || 'VACATION',
          description: description || '',
          university: normUniversity,
          courseName: normCourseName,
        },
      });
      return NextResponse.json(updated);
    } else {
      const startStr = date;
      const endStr = endDate || date;
      const dates = getDatesInRange(startStr, endStr);

      const results = [];
      for (const currentDate of dates) {
        // Find if vacation with same date/univ/course combination already exists
        const existing = await prisma.globalVacation.findFirst({
          where: {
            date: currentDate,
            university: normUniversity,
            courseName: normCourseName,
          },
        });

        if (existing) {
          const updated = await prisma.globalVacation.update({
            where: { id: existing.id },
            data: {
              type: type || 'VACATION',
              description: description || '',
            }
          });
          results.push(updated);
        } else {
          const created = await prisma.globalVacation.create({
            data: {
              date: currentDate,
              type: type || 'VACATION',
              description: description || '',
              university: normUniversity,
              courseName: normCourseName,
            },
          });
          results.push(created);
        }
      }
      return NextResponse.json({ success: true, count: dates.length, results }, { status: 201 });
    }
  } catch (error: any) {
    if (error.message.includes('Unauthorized') || error.message.includes('Forbidden')) {
      return NextResponse.json({ error: error.message }, { status: 403 });
    }
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}

// DELETE: Delete a global vacation
export async function DELETE(request: Request) {
  try {
    await requireAdmin();    const { searchParams } = new URL(request.url);
    const id = searchParams.get('id');
    if (!id) return NextResponse.json({ error: 'Missing ID' }, { status: 400 });

    await prisma.globalVacation.delete({
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
