---
tags: [api-user, suggestions, overrides, collective-agreement, backend]
---

# User API: Schedule Modification Suggestions

This endpoint manages student-initiated suggestions for modifying global templates (e.g. asking to cancel or reschedule an admin course due to exams), located at `src/app/api/suggestions/route.ts`.

- **File Link**: [route.ts](file:///d:/02_CODE/04_TEST/Routine/src/app/api/suggestions/route.ts)
- **Backlinks**: [[index]], [[component_modals]], [[api]], [[api_admin_suggestions]]

---

## 1. GET `/api/suggestions`

- **Purpose**: Retrieves all suggestions submitted by or supported by the active user, limited to the 50 most recent items.
- **Authentication**: Required (`User` session check)
- **Logic**: Filters rows where the student's ID is stored within the JSON string field `suggestedByUserIds` (`contains String(user.id)`).

---

## 2. POST `/api/suggestions`

- **Purpose**: Creates a new suggestion or registers agreement with an existing reschedule/cancel request.
- **Authentication**: Required (`User` session check)
- **JSON Payload Parameters**:
  - `date` (`String` format `"YYYY-MM-DD"`, Required): Class date.
  - `suggestedStatus` (`String`, Required): `"CANCELLED"` or `"RESCHEDULED"`.
  - `courseId` or `subjectId` (`String`/`Int`, Optional): Identifies the target class course.
  - `reason` (`String`, Optional): Student description.
- **Logic & User Consolidation Rules**:
  - **Scope Limitation**: Verifies that the target course exists in the database and is admin-managed (`source === 'admin'`). Returns `400 Bad Request` if attempting to modify a personal custom course.
  - **Duplicate Check**: Checks if a suggestion has already been submitted for this `globalCourseId` and `date`:
    - **If New**: Creates a suggestion row, initializing the JSON arrays `suggestedByUserIds` and `suggestedByNames` with the student's details.
    - **If Existing**: Consolidates votes. If the student has not yet voted, appends their `userId` and `name` to the existing JSON arrays, logs their feedback text (`existingReason | User: newReason`), and updates the latest proposed status.

---

## 3. Implementation Code Breakdown

The source code in `src/app/api/suggestions/route.ts` is divided into three key steps:

### Phase 1: GET Request (Fetch Student's Suggestions)
Pulls suggestions that include the active user's ID within the `suggestedByUserIds` JSON array, limiting results to 50 items.

```typescript
import { NextRequest, NextResponse } from 'next/server';
import { getAuthenticatedUser } from '@/lib/auth';
import { prisma } from '@/lib/prisma';

export async function GET() {
  try {
    const user = await getAuthenticatedUser();

    const suggestions = await prisma.classSuggestion.findMany({
      where: {
        suggestedByUserIds: { contains: String(user.id) }
      },
      include: {
        globalCourse: {
          select: { subjectId: true, subjectName: true, subjectCode: true, university: true, courseName: true }
        }
      },
      orderBy: { createdAt: 'desc' },
      take: 50,
    });

    return NextResponse.json(suggestions);
  } catch (error: any) {
    if (error.message === 'Unauthorized: No authenticated user') {
      return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    }
    console.error('Error fetching suggestions:', error);
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}
```

---

### Phase 2: POST Request - Course Verification Gate
Validates that suggestions are only allowed for admin-managed courses, translating local courses to global blueprints.

```typescript
export async function POST(req: NextRequest) {
  try {
    const user = await getAuthenticatedUser();
    const { courseId, subjectId, date, suggestedStatus, reason, startTime, endTime } = await req.json();

    if (!date || !suggestedStatus) {
      return NextResponse.json({ error: 'Missing required fields: date, suggestedStatus' }, { status: 400 });
    }

    // Find the global course corresponding to this user's admin course
    let globalCourse = null;

    if (subjectId) {
      // Find by subjectId directly
      globalCourse = await prisma.globalCourse.findFirst({
        where: { subjectId },
      });
    }

    if (!globalCourse && courseId) {
      // Fallback: find user's local course, get its subjectId, then find global course template
      const localCourse = await prisma.course.findFirst({
        where: { id: parseInt(courseId), userId: user.id, source: 'admin' },
      });
      if (localCourse) {
        globalCourse = await prisma.globalCourse.findFirst({
          where: { subjectId: localCourse.subjectId },
        });
      }
    }

    if (!globalCourse) {
      return NextResponse.json(
        { error: 'This course is not admin-managed. Suggestions can only be made for admin-pushed courses.' },
        { status: 400 }
      );
    }
```

---

### Phase 3: POST Request - Vote Consolidation Upsert
If a suggestion for this course and date already exists, appends the user details and reasons, consolidates the status, and updates the row. Otherwise, creates a new suggestion.

```typescript
    // Check if a suggestion already exists for this globalCourse + date
    const existing = await prisma.classSuggestion.findUnique({
      where: {
        globalCourseId_date: {
          globalCourseId: globalCourse.id,
          date,
        },
      },
    });

    if (existing) {
      // Add this user to the suggestion if not already present
      const existingUserIds: number[] = JSON.parse(existing.suggestedByUserIds);
      const existingNames: string[] = JSON.parse(existing.suggestedByNames);

      if (!existingUserIds.includes(user.id)) {
        existingUserIds.push(user.id);
        existingNames.push(user.name);

        const updated = await prisma.classSuggestion.update({
          where: { id: existing.id },
          data: {
            suggestedByUserIds: JSON.stringify(existingUserIds),
            suggestedByNames: JSON.stringify(existingNames),
            // Update reason (append new user comment)
            reason: reason
              ? (existing.reason ? `${existing.reason} | ${user.name}: ${reason}` : `${user.name}: ${reason}`)
              : existing.reason,
            suggestedStatus: suggestedStatus || existing.suggestedStatus,
          },
          include: {
            globalCourse: {
              select: { subjectId: true, subjectName: true, subjectCode: true }
            }
          },
        });

        return NextResponse.json(updated);
      } else {
        // User already suggested this — update their reason
        const updated = await prisma.classSuggestion.update({
          where: { id: existing.id },
          data: {
            suggestedStatus: suggestedStatus || existing.suggestedStatus,
            reason: reason
              ? (existing.reason ? `${existing.reason} | ${user.name}: ${reason}` : `${user.name}: ${reason}`)
              : existing.reason,
          },
          include: {
            globalCourse: {
              select: { subjectId: true, subjectName: true, subjectCode: true }
            }
          },
        });
        return NextResponse.json(updated);
      }
    } else {
      // Create new suggestion
      const suggestion = await prisma.classSuggestion.create({
        data: {
          globalCourseId: globalCourse.id,
          date,
          suggestedStatus,
          reason: reason ? `${user.name}: ${reason}` : null,
          suggestedByUserIds: JSON.stringify([user.id]),
          suggestedByNames: JSON.stringify([user.name]),
        },
        include: {
          globalCourse: {
            select: { subjectId: true, subjectName: true, subjectCode: true }
          }
        },
      });

      return NextResponse.json(suggestion);
    }
  } catch (error: any) {
    if (error.message === 'Unauthorized: No authenticated user') {
      return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    }
    console.error('Error creating suggestion:', error);
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}
```
