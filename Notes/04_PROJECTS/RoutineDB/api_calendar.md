---
tags: [api-user, calendar, scheduler, overrides, backend]
---

# User API: Calendar & Overrides Resolver

This endpoint resolves the active timetable schedule for any date range, expanding weekly slot templates and mapping holiday, sick day, cancellation, and rescheduling overrides, located at `src/app/api/calendar/route.ts`.

- **File Link**: [route.ts](file:///d:/02_CODE/04_TEST/Routine/src/app/api/calendar/route.ts)
- **Backlinks**: [[index]], [[home_page]], [[component_calendar_view]], [[api]], [[ARCHITECTURE]]

---

## 1. GET `/api/calendar`

- **Purpose**: Generates the list of scheduled class sessions for each date in a range, resolving template slots and applying holidays, overrides, and attendance statuses.
- **Authentication**: Required (`User` session check)
- **URL Query Parameters**:
  - `startDate` (`YYYY-MM-DD`, Required)
  - `endDate` (`YYYY-MM-DD`, Required)
- **Algorithmic Flow**: Refer to the flowchart in [[ARCHITECTURE]] for a visual breakdown of how dates, slots, semesters, and overrides are evaluated.

### Output JSON Shape:
```json
{
  "userInfo": {
    "id": 1,
    "name": "Jane Doe",
    "color": "#2b6cb0",
    "role": "user",
    "university": "DU",
    "courseName": "BSSE-18",
    "courseStartDate": "2026-01-01"
  },
  "semesters": [],
  "dates": {
    "2026-07-06": {
      "dayName": "MONDAY",
      "vacationType": null,
      "vacationDescription": null,
      "classes": [
        {
          "id": "template-12-2026-07-06",
          "weeklySlotId": 12,
          "dailyClassId": null,
          "courseId": 5,
          "startTime": "08:30",
          "endTime": "10:00",
          "room": "304-A",
          "group": "Group A",
          "status": "SCHEDULED",
          "isExtra": false,
          "description": null,
          "attendanceStatus": "PRESENT",
          "userId": 1,
          "date": "2026-07-06",
          "course": {
            "id": 5,
            "subjectId": "CSE-1101",
            "subjectName": "Structured Programming",
            "subjectCode": "CSE-1101"
          }
        }
      ]
    }
  }
}
```

---

## 2. POST `/api/calendar`

- **Purpose**: Creates or updates a local override (e.g. canceling or rescheduling a session) or inserts a custom one-off class instance (`isExtra: true`).
- **Authentication**: Required (`User` session check)
- **JSON Payload Parameters**:
  - `courseId` (`Int`, Required): Course identifier.
  - `weeklySlotId` (`Int`, Optional): Required if overriding a template recurring slot. Leave empty for custom extra sessions.
  - `date` (`String` format `"YYYY-MM-DD"`, Required): Target date.
  - `startTime` & `endTime` (`String` format `"HH:MM"`, Required).
  - `room` & `group` strings.
  - `status` (`String`, Optional): `"SCHEDULED"`, `"RESCHEDULED"`, or `"CANCELLED"`.
  - `isExtra` (`Boolean`, Optional): Set to `true` to declare a new standalone class session.
  - `description` (`String`, Optional): Notes displayed on the class card.
- **Logic**:
  - Verifies student course ownership.
  - Inserts or updates the `DailyClass` database row.
  - **Attendance Synchronization**: If the override status is `"CANCELLED"`, the endpoint automatically inserts or updates a matching `Attendance` log with status `"CANCELLED"`, ensuring calculations do not flag the session as unmarked or absent.

---

## 3. Implementation Code Breakdown

The source code in `src/app/api/calendar/route.ts` is structured as follows:

### Phase 1: Imports and Date-Weekday Helper
Imports dependencies and translates date strings to Day Name strings (e.g. `"MONDAY"`), matching template days in local timezone contexts.

```typescript
import { NextResponse } from 'next/server';
import { getAuthenticatedUser } from '@/lib/auth';
import { prisma } from '@/lib/prisma';

// Helper to get day name from a date string (YYYY-MM-DD)
// Note: We force interpretation in local time to avoid timezone shifts
function getDayOfWeek(dateStr: string): string {
  const [year, month, day] = dateStr.split('-').map(Number);
  const date = new Date(year, month - 1, day);
  const days = ['SUNDAY', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY'];
  return days[date.getDay()];
}
```

---

### Phase 2: GET Request - Initialization and Database Queries
Queries user configuration parameters, vacations (personal & global), slots, overrides, and attendance logs.

```typescript
export async function GET(request: Request) {
  try {
    const user = await getAuthenticatedUser();
    const { searchParams } = new URL(request.url);
    const startDateStr = searchParams.get('startDate'); // YYYY-MM-DD
    const endDateStr = searchParams.get('endDate'); // YYYY-MM-DD

    if (!startDateStr || !endDateStr) {
      return NextResponse.json({ error: 'Missing date range parameters' }, { status: 400 });
    }

    const userId = user.id;
    const start = new Date(startDateStr);
    const end = new Date(endDateStr);
    
    // Generate all dates in the range
    const dates: string[] = [];
    const temp = new Date(start);
    while (temp <= end) {
      dates.push(temp.toISOString().split('T')[0]);
      temp.setDate(temp.getDate() + 1);
    }

    // Query data for this user
    const fullUser = await prisma.user.findUnique({
      where: { id: userId },
      include: { courses: { where: { isArchived: false } } }
    });
    if (!fullUser) {
      return NextResponse.json({ error: 'User not found' }, { status: 404 });
    }

    const weeklySlots = await prisma.weeklySlot.findMany({
      where: { userId },
      include: { course: true }
    });

    const overrides = await prisma.dailyClass.findMany({
      where: {
        userId,
        date: { gte: startDateStr, lte: endDateStr }
      },
      include: { course: true }
    });

    // Personal vacations
    const vacations = await prisma.vacation.findMany({
      where: {
        userId,
        date: { gte: startDateStr, lte: endDateStr }
      }
    });

    // Global vacations (from admin) — match by user's university/courseName tags
    const globalVacations = await prisma.globalVacation.findMany({
      where: {
        date: { gte: startDateStr, lte: endDateStr },
        OR: [
          { university: null, courseName: null },
          { university: '', courseName: '' },
          { university: '', courseName: null },
          { university: null, courseName: '' },
          ...(user.university ? [
            { university: user.university, courseName: null },
            { university: user.university, courseName: '' },
            ...(user.courseName ? [{ university: user.university, courseName: user.courseName }] : []),
          ] : []),
        ]
      }
    });

    const attendance = await prisma.attendance.findMany({
      where: {
        userId,
        date: { gte: startDateStr, lte: endDateStr }
      }
    });
```

---

### Phase 3: GET Request - Tag Resolution & Active Semester Filtering
Gathers secondary department tags to find matching admin semester term boundaries.

```typescript
    // Merge personal & global vacations (personal takes precedence)
    const vacationMap = new Map<string, { type: string; description?: string | null }>();
    globalVacations.forEach(v => {
      vacationMap.set(v.date, { type: v.type, description: v.description });
    });
    vacations.forEach(v => {
      vacationMap.set(v.date, { type: v.type, description: v.description });
    });

    // Fetch active semesters matching user primary/secondary tags
    const secondaryTags = await prisma.userSecondaryTag.findMany({
      where: { userId }
    });

    const userTags = [
      { university: fullUser.university, courseName: fullUser.courseName },
      ...secondaryTags.map(t => ({ university: t.university, courseName: t.courseName }))
    ].filter(t => t.university || t.courseName);

    const orConditions: any[] = [{ university: '', courseName: '' }];
    if (userTags.length > 0) {
      userTags.forEach(tag => {
        orConditions.push({
          university: tag.university,
          courseName: tag.courseName,
        });
      });
    }

    const semesters = await prisma.semester.findMany({
      where: {
        isActive: true,
        OR: orConditions
      }
    });

    const adminSubjectIds = fullUser.courses
      .filter(c => c.source === 'admin')
      .map(c => c.subjectId);

    const globalCourses = adminSubjectIds.length > 0
      ? await prisma.globalCourse.findMany({
          where: { subjectId: { in: adminSubjectIds } }
        })
      : [];

    const courseTagMap = new Map<number, { university: string; courseName: string }>();
    fullUser.courses.forEach(c => {
      if (c.source === 'admin') {
        const gc = globalCourses.find(g => g.subjectId === c.subjectId);
        if (gc) {
          courseTagMap.set(c.id, { university: gc.university, courseName: gc.courseName });
        }
      }
    });

    // Filter weekly slots for non-archived courses
    const activeCourseIds = new Set(fullUser.courses.map(c => c.id));
    const activeWeeklySlots = weeklySlots.filter(s => activeCourseIds.has(s.courseId));

    const responseData: any = {
      userInfo: {
        id: fullUser.id,
        name: fullUser.name,
        color: fullUser.color,
        role: fullUser.role,
        university: fullUser.university,
        courseName: fullUser.courseName,
        courseStartDate: fullUser.courseStartDate,
      },
      semesters,
      dates: {} as Record<string, any>
    };
```

---

### Phase 4: GET Request - Calendar Grid Resolution Loop
Iterates through all dates in the range, checks template boundaries, applies semester rules, overrides metadata, and checks attendance details.

```typescript
    // Resolve for each date
    for (const dateStr of dates) {
      const dayName = getDayOfWeek(dateStr);
      const dayVacation = vacationMap.get(dateStr);
      const dayVacationType = dayVacation?.type || null;

      // Get template slots for this day of week
      const dayTemplates = activeWeeklySlots.filter(s => {
        if (s.dayOfWeek !== dayName) return false;
        if (s.activeFrom && dateStr < s.activeFrom) return false;
        if (s.activeUntil && dateStr > s.activeUntil) return false;
        if (!s.activeFrom && dateStr < fullUser.courseStartDate) return false;
        return true;
      });

      const dateOverrides = overrides.filter(o => o.date === dateStr);
      const activeClasses: any[] = [];

      // Process template slots
      for (const slot of dayTemplates) {
        const course = fullUser.courses.find(c => c.id === slot.courseId);
        if (course?.archivedAt && dateStr > course.archivedAt) continue;

        // Check if course is admin-pushed and has semester restrictions
        if (course && course.source === 'admin') {
          const tags = courseTagMap.get(course.id);
          if (tags) {
            const matchingSemesters = semesters.filter(s => 
              s.university === tags.university && 
              s.courseName === tags.courseName
            );
            
            if (matchingSemesters.length > 0) {
              const isWithinSemester = matchingSemesters.some(s => 
                dateStr >= s.startDate && dateStr <= s.endDate
              );
              if (!isWithinSemester) continue;
            }
          }
        }

        const override = dateOverrides.find(o => o.weeklySlotId === slot.id);
        
        let classItem: any = {
          id: `template-${slot.id}-${dateStr}`,
          weeklySlotId: slot.id,
          dailyClassId: null,
          courseId: slot.courseId,
          course: slot.course,
          startTime: slot.startTime,
          endTime: slot.endTime,
          room: slot.room,
          group: slot.group,
          status: 'SCHEDULED',
          isExtra: false,
          description: null,
          attendanceStatus: null,
          userId,
          date: dateStr
        };

        if (override) {
          classItem.id = `override-${override.id}`;
          classItem.dailyClassId = override.id;
          classItem.startTime = override.startTime;
          classItem.endTime = override.endTime;
          classItem.room = override.room;
          classItem.group = override.group;
          classItem.status = override.status;
          classItem.description = override.description;
        }

        // Resolve attendance status
        const att = attendance.find(a => 
          a.courseId === slot.courseId &&
          a.date === dateStr &&
          (override ? a.dailyClassId === override.id : a.weeklySlotId === slot.id)
        );

        if (dayVacationType === 'VACATION') {
          classItem.attendanceStatus = 'VACATION';
        } else if (dayVacationType === 'ABSENT_DAY') {
          classItem.attendanceStatus = 'ABSENT';
        } else if (classItem.status === 'CANCELLED') {
          classItem.attendanceStatus = 'CANCELLED';
        } else if (att) {
          classItem.attendanceStatus = att.status;
        }

        activeClasses.push(classItem);
      }

      // Process extra classes
      const extraClasses = dateOverrides.filter(o => o.isExtra);
      for (const extra of extraClasses) {
        let classItem: any = {
          id: `extra-${extra.id}`,
          weeklySlotId: null,
          dailyClassId: extra.id,
          courseId: extra.courseId,
          course: extra.course,
          startTime: extra.startTime,
          endTime: extra.endTime,
          room: extra.room,
          group: extra.group,
          status: extra.status,
          isExtra: true,
          description: extra.description,
          attendanceStatus: null,
          userId,
          date: dateStr
        };

        const att = attendance.find(a => 
          a.courseId === extra.courseId &&
          a.date === dateStr &&
          a.dailyClassId === extra.id
        );

        if (dayVacationType === 'VACATION') {
          classItem.attendanceStatus = 'VACATION';
        } else if (dayVacationType === 'ABSENT_DAY') {
          classItem.attendanceStatus = 'ABSENT';
        } else if (classItem.status === 'CANCELLED') {
          classItem.attendanceStatus = 'CANCELLED';
        } else if (att) {
          classItem.attendanceStatus = att.status;
        }

        activeClasses.push(classItem);
      }

      // Sort classes chronologically
      activeClasses.sort((a, b) => a.startTime.localeCompare(b.startTime));

      responseData.dates[dateStr] = {
        dayName,
        vacationType: dayVacationType,
        vacationDescription: dayVacation?.description || null,
        classes: activeClasses
      };
    }

    return NextResponse.json(responseData);
  } catch (error: any) {
    if (error.message === 'Unauthorized: No authenticated user') {
      return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    }
    console.error('Error in calendar resolution GET:', error);
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}
```

---

### Phase 5: POST Request - Schedule Overrides & Attendance Sync
Inserts or updates a local class override (`DailyClass`). If the class is cancelled, automatically inserts/updates a matching `Attendance` record with status `"CANCELLED"`.

```typescript
export async function POST(request: Request) {
  try {
    const user = await getAuthenticatedUser();
    const body = await request.json();
    const {
      courseId,
      weeklySlotId,
      date,
      startTime,
      endTime,
      room,
      group,
      status,
      isExtra,
      description
    } = body;

    if (!courseId || !date || !startTime || !endTime) {
      return NextResponse.json({ error: 'Missing required override fields' }, { status: 400 });
    }

    // Verify course ownership
    const course = await prisma.course.findFirst({
      where: { id: parseInt(courseId), userId: user.id },
    });
    if (!course) {
      return NextResponse.json({ error: 'Course not found' }, { status: 404 });
    }

    let existingOverride = null;
    if (weeklySlotId) {
      existingOverride = await prisma.dailyClass.findFirst({
        where: {
          userId: user.id,
          weeklySlotId: parseInt(weeklySlotId),
          date
        }
      });
    }

    let dailyClass;
    if (existingOverride) {
      dailyClass = await prisma.dailyClass.update({
        where: { id: existingOverride.id },
        data: {
          startTime,
          endTime,
          room: room || '',
          group: group || '',
          status,
          description: description || null,
        }
      });
    } else {
      dailyClass = await prisma.dailyClass.create({
        data: {
          userId: user.id,
          courseId: parseInt(courseId),
          weeklySlotId: weeklySlotId ? parseInt(weeklySlotId) : null,
          date,
          startTime,
          endTime,
          room: room || '',
          group: group || '',
          status: status || 'SCHEDULED',
          isExtra: !!isExtra,
          description: description || null,
        }
      });
    }

    // If cancelled, sync attendance
    if (status === 'CANCELLED') {
      const existingAtt = await prisma.attendance.findFirst({
        where: {
          userId: user.id,
          courseId: parseInt(courseId),
          date,
          weeklySlotId: weeklySlotId ? parseInt(weeklySlotId) : null,
          dailyClassId: dailyClass.id
        }
      });

      if (existingAtt) {
        await prisma.attendance.update({
          where: { id: existingAtt.id },
          data: { status: 'CANCELLED' }
        });
      } else {
        await prisma.attendance.create({
          data: {
            userId: user.id,
            courseId: parseInt(courseId),
            date,
            weeklySlotId: weeklySlotId ? parseInt(weeklySlotId) : null,
            dailyClassId: dailyClass.id,
            status: 'CANCELLED'
          }
        });
      }
    }

    return NextResponse.json(dailyClass);
  } catch (error: any) {
    if (error.message === 'Unauthorized: No authenticated user') {
      return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    }
    console.error('Error saving calendar override:', error);
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}
```

