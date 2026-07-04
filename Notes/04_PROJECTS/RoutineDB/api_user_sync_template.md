---
tags: [api-user, sync, template, courses, slots, backend]
---

# User API: Schedule Sync Engine

This endpoint allows students to pull and synchronize global template schedules matching their university and course tags into their personal schedule binders, located at `src/app/api/user/sync-template/route.ts`.

- **File Link**: [route.ts](file:///d:/02_CODE/04_TEST/Routine/src/app/api/user/sync-template/route.ts)
- **Backlinks**: [[index]], [[home_page]], [[api]], [[api_admin_push_sync]], [[lib_utils]]

---

## 1. Endpoint Configuration

- **HTTP Method**: `POST`
- **Route URL**: `/api/user/sync-template`
- **Authentication**: Required (`User` session check)

---

## 2. Sync Logic Workflow

1. **Gathers User Tags**: Fetches the user's primary tags (`university`, `courseName`) and all registered secondary tag records.
2. **Tag Verification**: Returns a `400 Bad Request` if no tags are configured in the user profile.
3. **Template Lookup**: Queries the `GlobalCourse` table matching any tag pairs (university/course) or fetching universal templates (empty university + courseName).
4. **Course Synchronization**:
   - For each matching global template, checks if the course is already in the user's registry.
   - If missing: Creates the user-level course with details, setting `source: 'admin'`.
   - If present: Updates the metadata, resets `isArchived` to `false`, and nullifies `archivedAt` (force restoration).
5. **Slots Merge Operations**:
   - Loops through template weekly slot items. Matches with existing slots by day and time.
   - If missing: Inserts the new slot, setting `source: 'admin'`.
   - If present: Updates room numbers and group configurations if the admin template changed.

---

## 3. JSON Success Response Schema

```json
{
  "success": true,
  "coursesSynced": 3,
  "slotsSynced": 8
}
```

---

## 4. Source Code

Here is the complete implementation of `src/app/api/user/sync-template/route.ts`:

```typescript
import { NextResponse } from 'next/server';
import { getAuthenticatedUser } from '@/lib/auth';
import { prisma } from '@/lib/prisma';

// POST: Sync/Import global courses and slots template to the authenticated user's profile
// Only syncs courses matching the user's primary + secondary tags
export async function POST() {
  try {
    const user = await getAuthenticatedUser();

    // Get user's tags (primary + secondary)
    const secondaryTags = await prisma.userSecondaryTag.findMany({
      where: { userId: user.id },
    });

    const userTags = [
      { university: user.university, courseName: user.courseName },
      ...secondaryTags.map(t => ({ university: t.university, courseName: t.courseName })),
    ].filter(t => t.university || t.courseName);

    if (userTags.length === 0) {
      return NextResponse.json(
        { error: 'Please set your university and course tags in your profile before syncing.' },
        { status: 400 }
      );
    }

    // Build OR conditions to match global courses by any of the user's tags
    const orConditions = userTags.map(tag => {
      const condition: any = {};
      if (tag.university) condition.university = tag.university;
      if (tag.courseName) condition.courseName = tag.courseName;
      return condition;
    });

    // Also include universal courses (empty university + courseName)
    orConditions.push({ university: '', courseName: '' });

    // Fetch matching global courses and their weekly slots
    const globalCourses = await prisma.globalCourse.findMany({
      where: { OR: orConditions },
      include: { weeklySlots: true },
    });

    if (globalCourses.length === 0) {
      return NextResponse.json({
        success: true,
        coursesSynced: 0,
        slotsSynced: 0,
        message: 'No matching templates found for your course tags.',
      });
    }

    let coursesSynced = 0;
    let slotsSynced = 0;

    for (const gc of globalCourses) {
      // Check if user already has this course
      let localCourse = await prisma.course.findUnique({
        where: {
          userId_subjectId: {
            userId: user.id,
            subjectId: gc.subjectId,
          },
        },
      });

      if (!localCourse) {
        // Create new course for the user
        localCourse = await prisma.course.create({
          data: {
            userId: user.id,
            subjectId: gc.subjectId,
            subjectName: gc.subjectName,
            subjectCode: gc.subjectCode,
            teacherName: gc.teacherName,
            teacherCode: gc.teacherCode,
            teacherContact: gc.teacherContact,
            teacherEmail: gc.teacherEmail,
            source: 'admin',
            isArchived: false,
          },
        });
        coursesSynced++;
      } else {
        // Update details if changed and ensure it is not archived
        localCourse = await prisma.course.update({
          where: { id: localCourse.id },
          data: {
            subjectName: gc.subjectName,
            subjectCode: gc.subjectCode,
            teacherName: gc.teacherName,
            teacherCode: gc.teacherCode,
            teacherContact: gc.teacherContact,
            teacherEmail: gc.teacherEmail,
            source: 'admin',
            isArchived: false,
            archivedAt: null,
          },
        });
        coursesSynced++;
      }

      // Sync weekly slots for this course (merge mode — add missing, update existing)
      for (const gs of gc.weeklySlots) {
        const existingSlot = await prisma.weeklySlot.findFirst({
          where: {
            userId: user.id,
            courseId: localCourse.id,
            dayOfWeek: gs.dayOfWeek,
            startTime: gs.startTime,
            endTime: gs.endTime,
          },
        });

        if (!existingSlot) {
          await prisma.weeklySlot.create({
            data: {
              userId: user.id,
              courseId: localCourse.id,
              dayOfWeek: gs.dayOfWeek,
              startTime: gs.startTime,
              endTime: gs.endTime,
              room: gs.room,
              group: gs.group,
              source: 'admin',
            },
          });
          slotsSynced++;
        } else {
          // Update room/group if they changed in the global template
          await prisma.weeklySlot.update({
            where: { id: existingSlot.id },
            data: {
              room: gs.room,
              group: gs.group,
              source: 'admin',
            },
          });
        }
      }
    }

    return NextResponse.json({
      success: true,
      coursesSynced,
      slotsSynced,
    });
  } catch (error: any) {
    if (error.message === 'Unauthorized: No authenticated user') {
      return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    }
    console.error('Error syncing template:', error);
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}
```
