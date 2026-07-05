---
tags: [api-user, init, bootstrap, backend]
---

# User API: Init (Bootstrap Payload)

This endpoint acts as the single bootstrap fetch loader of the application, located at `src/app/api/init/route.ts`. It packages the student profile, registered courses, weekly schedule templates, resolved calendar grids, and notifications into a single response.

- **File Link**: [route.ts](file:///d:/02_CODE/04_TEST/Routine/src/app/api/init/route.ts)
- **Backlinks**: [[index]], [[home_page]], [[api]], [[ARCHITECTURE]], [[api_calendar]], [[api_announcements]]

---

## 1. Endpoint Configuration

- **HTTP Method**: `GET`
- **Route URL**: `/api/init`
- **Authentication**: Required (`User` session check)
- **URL Parameters**:
  - `startDate` (`YYYY-MM-DD`, Required): Start date of the calendar resolution range.
  - `endDate` (`YYYY-MM-DD`, Required): End date of the calendar resolution range.
  - `todayDate` (`YYYY-MM-DD`, Required): Student's local current day string (used to filter expired notices).

---

## 2. Server Controller Logic

The API processes database operations in two parallel phases:

### Phase 1: Parallel Fetching
Retrieves 8 data arrays simultaneously using `Promise.all` to minimize roundtrips:
1. Active User profile info and associated non-archived courses.
2. User's recurring Weekly Slots.
3. Daily class overrides within the query date range.
4. Personal vacations matching the range.
5. Global holidays matching the student's primary tag configurations (university/course).
6. Saved attendance logs.
7. User's secondary tag subscriptions.
8. Unexpired announcements matching the student's tags.

### Phase 2: Boundary & Schedule Resolution
- Merges global academic holidays and personal vacations into a unified date-to-vacation lookup map.
- Filters out weekly slots for archived courses.
- Expands weekly slots for each date in the range, applying semester boundaries for admin-managed courses, overriding details if a `DailyClass` record exists, and looking up logged attendance.
- Appends standalone custom class instances (`isExtra: true`) and sorts all class items chronologically by `startTime`.

---

## 3. JSON Success Response Schema

```json
{
  "user": {
    "id": 1,
    "clerkId": "user_2iY...",
    "name": "Jane Doe",
    "email": "jane@example.com",
    "color": "#2b6cb0",
    "role": "user",
    "university": "University of Dhaka",
    "courseName": "BSSE-18",
    "courseStartDate": "2026-01-01",
    "createdAt": "2026-07-04T04:19:24.000Z"
  },
  "courses": [
    {
      "id": 5,
      "userId": 1,
      "subjectId": "CSE-1101",
      "subjectName": "Structured Programming",
      "subjectCode": "CSE-1101",
      "teacherName": "Dr. Rahman",
      "source": "admin"
    }
  ],
  "weeklySlots": [
    {
      "id": 12,
      "userId": 1,
      "courseId": 5,
      "dayOfWeek": "MONDAY",
      "startTime": "08:30",
      "endTime": "10:00",
      "room": "304-A"
    }
  ],
  "calendarData": {
    "userInfo": { "id": 1, "name": "Jane Doe", "color": "#2b6cb0" },
    "semesters": [],
    "dates": {
      "2026-07-06": {
        "dayName": "MONDAY",
        "vacationType": null,
        "classes": [
          {
            "id": "template-12-2026-07-06",
            "weeklySlotId": 12,
            "courseId": 5,
            "startTime": "08:30",
            "endTime": "10:00",
            "room": "304-A",
            "status": "SCHEDULED",
            "attendanceStatus": "PRESENT"
          }
        ]
      }
    }
  },
  "announcements": []
}
```

---

## 4. Implementation Code Breakdown

The bootstrap logic in `src/app/api/init/route.ts` runs through the following phases:

### Phase 1: Query Setup & Batch Parallel Querying
Authenticates the user and triggers concurrent database reads for student details, slots, logs, vacations, and notices.

```typescript
import { NextResponse } from 'next/server';
import { getAuthenticatedUser } from '@/lib/auth';
import { prisma } from '@/lib/prisma';

// Helper to get day name from a date string (YYYY-MM-DD)
function getDayOfWeek(dateStr: string): string {
  const [year, month, day] = dateStr.split('-').map(Number);
  const date = new Date(year, month - 1, day);
  const days = ['SUNDAY', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY'];
  return days[date.getDay()];
}

export async function GET(request: Request) {
  try {
    const user = await getAuthenticatedUser();
    const { searchParams } = new URL(request.url);
    const startDateStr = searchParams.get('startDate');
    const endDateStr = searchParams.get('endDate');
    const todayDateStr = searchParams.get('todayDate');

    if (!startDateStr || !endDateStr || !todayDateStr) {
      return NextResponse.json(
        { error: 'Missing required parameters: startDate, endDate, todayDate' },
        { status: 400 }
      );
    }

    const userId = user.id;

    // Generate all dates in the calendar range
    const start = new Date(startDateStr);
    const end = new Date(endDateStr);
    const dates: string[] = [];
    const temp = new Date(start);
    while (temp <= end) {
      dates.push(temp.toISOString().split('T')[0]);
      temp.setDate(temp.getDate() + 1);
    }

    const today = new Date().toISOString().split('T')[0];

    // CONCURRENT QUERY EXECUTION
    const [
      fullUser,
      weeklySlots,
      overrides,
      vacations,
      globalVacations,
      attendance,
      secondaryTags,
      announcements,
    ] = await Promise.all([
      prisma.user.findUnique({
        where: { id: userId },
        include: { courses: { where: { isArchived: false } } },
      }),
      prisma.weeklySlot.findMany({
        where: { userId },
        include: { course: true },
      }),
      prisma.dailyClass.findMany({
        where: {
          userId,
          date: { gte: startDateStr, lte: endDateStr },
        },
        include: { course: true },
      }),
      prisma.vacation.findMany({
        where: {
          userId,
          date: { gte: startDateStr, lte: endDateStr },
        },
      }),
      prisma.globalVacation.findMany({
        where: {
          date: { gte: startDateStr, lte: endDateStr },
          OR: [
            { university: null, courseName: null },
            { university: '', courseName: '' },
            { university: '', courseName: null },
            { university: null, courseName: '' },
            ...(user.university
              ? [
                  { university: user.university, courseName: null },
                  { university: user.university, courseName: '' },
                  ...(user.courseName
                    ? [{ university: user.university, courseName: user.courseName }]
                    : []),
                ]
              : []),
          ],
        },
      }),
      prisma.attendance.findMany({
        where: {
          userId,
          date: { gte: startDateStr, lte: endDateStr },
        },
      }),
      prisma.userSecondaryTag.findMany({
        where: { userId },
      }),
      prisma.announcement.findMany({
        where: {
          AND: [
            {
              OR: [
                { university: null, courseName: null },
                ...(user.university
                  ? [
                      { university: user.university, courseName: null },
                      ...(user.courseName
                        ? [
                            { university: null, courseName: user.courseName },
                            { university: user.university, courseName: user.courseName },
                          ]
                        : []),
                    ]
                  : []),
              ],
            },
            {
              OR: [{ expiresAt: null }, { expiresAt: { gte: today } }],
            },
          ],
        },
        orderBy: { createdAt: 'desc' },
      }),
    ]);

    if (!fullUser) {
      return NextResponse.json({ error: 'User not found' }, { status: 404 });
    }
```

---

### Phase 2: Active Semester Boundaries & Course Tag Resolution
Resolves active semesters according to secondary student tag criteria, then queries global blueprints matching the target CSE/EEE subjects.

```typescript
    const userTags = [
      { university: fullUser.university, courseName: fullUser.courseName },
      ...secondaryTags.map((t) => ({ university: t.university, courseName: t.courseName })),
    ].filter((t) => t.university || t.courseName);

    const orConditions: any[] = [{ university: '', courseName: '' }];
    if (userTags.length > 0) {
      userTags.forEach((tag) => {
        orConditions.push({
          university: tag.university,
          courseName: tag.courseName,
        });
      });
    }

    const adminSubjectIds = fullUser.courses
      .filter((c) => c.source === 'admin')
      .map((c) => c.subjectId);

    const [semesters, globalCourses] = await Promise.all([
      prisma.semester.findMany({
        where: { isActive: true, OR: orConditions },
      }),
      adminSubjectIds.length > 0
        ? prisma.globalCourse.findMany({
            where: { subjectId: { in: adminSubjectIds } },
          })
        : Promise.resolve([]),
    ]);

    // Construct tag mapping directory helper
    const courseTagMap = new Map<number, { university: string; courseName: string }>();
    fullUser.courses.forEach((c) => {
      if (c.source === 'admin') {
        const gc = globalCourses.find((g) => g.subjectId === c.subjectId);
        if (gc) {
          courseTagMap.set(c.id, { university: gc.university, courseName: gc.courseName });
        }
      }
    });
```

---

### Phase 3: Grid Expansion & Class Override Matching
Loops over the calendar range dates, mapping weekly slot templates to dates while checking vacation rules, active ranges, semester bounds, and overriding statuses.

```typescript
    // Merge personal & global vacations into lookup map
    const vacationMap = new Map<string, { type: string; description?: string | null }>();
    globalVacations.forEach((v) => {
      vacationMap.set(v.date, { type: v.type, description: v.description });
    });
    vacations.forEach((v) => {
      vacationMap.set(v.date, { type: v.type, description: v.description });
    });

    const activeCourseIds = new Set(fullUser.courses.map((c) => c.id));
    const activeWeeklySlots = weeklySlots.filter((s) => activeCourseIds.has(s.courseId));

    const calendarDates: Record<string, any> = {};

    for (const dateStr of dates) {
      const dayName = getDayOfWeek(dateStr);
      const dayVacation = vacationMap.get(dateStr);
      const dayVacationType = dayVacation?.type || null;

      const dayTemplates = activeWeeklySlots.filter((s) => {
        if (s.dayOfWeek !== dayName) return false;
        if (s.activeFrom && dateStr < s.activeFrom) return false;
        if (s.activeUntil && dateStr > s.activeUntil) return false;
        if (!s.activeFrom && dateStr < fullUser.courseStartDate) return false;
        return true;
      });

      const dateOverrides = overrides.filter((o) => o.date === dateStr);
      const activeClasses: any[] = [];

      for (const slot of dayTemplates) {
        const course = fullUser.courses.find((c) => c.id === slot.courseId);
        if (course?.archivedAt && dateStr > course.archivedAt) continue;

        // Semester restrictions check
        if (course && course.source === 'admin') {
          const tags = courseTagMap.get(course.id);
          if (tags) {
            const matchingSemesters = semesters.filter(
              (s) => s.university === tags.university && s.courseName === tags.courseName
            );
            if (matchingSemesters.length > 0) {
              const isWithinSemester = matchingSemesters.some(
                (s) => dateStr >= s.startDate && dateStr <= s.endDate
              );
              if (!isWithinSemester) continue;
            }
          }
        }

        const override = dateOverrides.find((o) => o.weeklySlotId === slot.id);

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
          date: dateStr,
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

        const att = attendance.find(
          (a) =>
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
```

---

### Phase 4: Extra Classes Resolution & Response Packing
Incorporates ad-hoc extra slots, orders classes chronologically, and returns the assembled bootstrap response payload.

```typescript
      // Process extra classes
      const extraClasses = dateOverrides.filter((o) => o.isExtra);
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
          date: dateStr,
        };

        const att = attendance.find(
          (a) =>
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

      activeClasses.sort((a, b) => a.startTime.localeCompare(b.startTime));

      calendarDates[dateStr] = {
        dayName,
        vacationType: dayVacationType,
        vacationDescription: dayVacation?.description || null,
        classes: activeClasses,
      };
    }

    return NextResponse.json({
      user: fullUser,
      courses: fullUser.courses,
      weeklySlots,
      calendarData: {
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
        dates: calendarDates,
      },
      announcements,
    });
  } catch (error: any) {
    if (error.message === 'Unauthorized: No authenticated user') {
      return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    }
    console.error('Error in /api/init bootstrap:', error);
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}
```

