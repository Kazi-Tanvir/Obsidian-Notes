---
tags: [api-user, attendance, stats, history, backend]
---

# User API: Attendance Analytics & Logger

This endpoint compiles paginated attendance history tables, calculates subject percentages, and logs attendance updates (Present/Absent checks), located at `src/app/api/attendance/route.ts`.

- **File Link**: [route.ts](file:///d:/02_CODE/04_TEST/Routine/src/app/api/attendance/route.ts)
- **Backlinks**: [[index]], [[component_analytics_view]], [[api]]

---

## 1. GET `/api/attendance`

- **Purpose**: Computes attendance summaries (held counts, present rates) for a date range and compiles paginated logs.
- **Authentication**: Required (`User` session check)
- **URL Query Parameters**:
  - `startDate` & `endDate` (`YYYY-MM-DD`, Optional): Defaults to the past 30 days.
  - `page` (`Int`, Optional): Defaults to `1`.
  - `pageSize` (`Int`, Optional): Page size limit, defaults to `50`.

### A. Core Statistical Rules
1. **Future Capping**: The `endDate` parameter is capped at today's date (`endDate = min(endDate, today)`). Future scheduled classes must never affect average rates.
2. **Holiday Exclusion**: If a global or personal holiday (`VACATION`) falls on a date, sessions on that day are excluded from held counts.
3. **Sick-Day Overrides**: If a sick day (`ABSENT_DAY`) falls on a date, all classes are automatically counted as `ABSENT`.
4. **Cancellation Exclusions**: If a class is cancelled (via `DailyClass` status `"CANCELLED"` or the `Attendance` record status `"CANCELLED"`), it is excluded from held counts.

### B. Output Payload Structure
Returns:
- **`range`**: Start and end query bounds.
- **`summary`**: Overall totals (held, present, absent, cancelled, overall percentage rate).
- **`subjects`**: Array of subject breakdowns (held count, present, absent, cancelled, subject-specific percentage rate).
- **`classHistory`**: Chronological log array of session cards (paginated).
- **`historyPagination`**: Pagination metadata.

---

## 2. POST `/api/attendance`

- **Purpose**: Logs a Present, Absent, or Cancelled check.
- **Authentication**: Required (`User` session check)
- **JSON Payload Parameters**:
  - `courseId` (`String` / `Int`, Required)
  - `date` (`YYYY-MM-DD`, Required)
  - `status` (`String`, Required): `"PRESENT"`, `"ABSENT"`, or `"CANCELLED"`.
  - `weeklySlotId` (`String` / `Int`, Optional)
  - `dailyClassId` (`String` / `Int`, Optional)
- **Logic**: Upserts the attendance record by checking matching constraints on `userId`, `courseId`, `date`, `weeklySlotId`, and `dailyClassId`.

---

## 3. Implementation Code Breakdown

The source code in `src/app/api/attendance/route.ts` is divided into logical phases:

### Phase 1: Imports & Weekday Helper
Imports ORM modules and handles date conversion to day name strings.

```typescript
import { NextResponse } from 'next/server';
import { getAuthenticatedUser } from '@/lib/auth';
import { prisma } from '@/lib/prisma';

// Helper to determine day name
function getDayOfWeek(dateStr: string): string {
  const [year, month, day] = dateStr.split('-').map(Number);
  const date = new Date(year, month - 1, day);
  const days = ['SUNDAY', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY'];
  return days[date.getDay()];
}
```

---

### Phase 2: GET Request - Student Information and Date Ranges Capping
Pulls user configurations and sets date range filters. Checks that the calculations end date does not extend past today, preventing future classes from affecting stats.

```typescript
export async function GET(request: Request) {
  try {
    const user = await getAuthenticatedUser();
    const { searchParams } = new URL(request.url);
    const startDateStr = searchParams.get('startDate');
    const endDateStr = searchParams.get('endDate');

    const student = await prisma.user.findUnique({
      where: { id: user.id },
      include: {
        courses: {
          where: { isArchived: false },
          include: {
            weeklySlots: true,
          }
        }
      }
    });

    if (!student) {
      return NextResponse.json({ error: 'User not found' }, { status: 404 });
    }

    const secondaryTags = await prisma.userSecondaryTag.findMany({
      where: { userId: user.id }
    });

    const userTags = [
      { university: student.university, courseName: student.courseName },
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

    const adminSubjectIds = student.courses
      .filter(c => c.source === 'admin')
      .map(c => c.subjectId);

    const globalCourses = adminSubjectIds.length > 0
      ? await prisma.globalCourse.findMany({
          where: { subjectId: { in: adminSubjectIds } }
        })
      : [];

    const courseTagMap = new Map<number, { university: string; courseName: string }>();
    student.courses.forEach(c => {
      if (c.source === 'admin') {
        const gc = globalCourses.find(g => g.subjectId === c.subjectId);
        if (gc) {
          courseTagMap.set(c.id, { university: gc.university, courseName: gc.courseName });
        }
      }
    });

    // Date range preparation
    let startStr = startDateStr;
    let endStr = endDateStr;
    if (!startStr || !endStr) {
      const today = new Date();
      endStr = today.toISOString().split('T')[0];
      const oneMonthAgo = new Date();
      oneMonthAgo.setMonth(oneMonthAgo.getMonth() - 1);
      startStr = oneMonthAgo.toISOString().split('T')[0];
    }

    // CAP END DATE TO TODAY (No future class metrics allowed)
    const todayStr = new Date().toISOString().split('T')[0];
    if (endStr > todayStr) {
      endStr = todayStr;
    }

    const whereClause: any = { userId: user.id };
    if (startStr && endStr) {
      whereClause.date = { gte: startStr, lte: endStr };
    }
```

---

### Phase 3: GET Request - Database Records Loading & Vacation Maps Builder
Pulls vacations, overrides, and logs, then builds holiday indexes.

```typescript
    const vacations = await prisma.vacation.findMany({ where: whereClause });
    const dailyClasses = await prisma.dailyClass.findMany({ where: whereClause });
    const attendances = await prisma.attendance.findMany({ where: whereClause });

    // Global vacations from admin
    const globalVacations = await prisma.globalVacation.findMany({
      where: {
        date: { gte: startStr, lte: endStr },
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

    const start = new Date(startStr);
    const end = new Date(endStr);
    const dates: string[] = [];
    const temp = new Date(start);
    while (temp <= end) {
      dates.push(temp.toISOString().split('T')[0]);
      temp.setDate(temp.getDate() + 1);
    }

    // Build vacation map (personal overrides global)
    const vacationMap = new Map<string, string>();
    globalVacations.forEach(v => vacationMap.set(v.date, v.type));
    vacations.forEach(v => vacationMap.set(v.date, v.type));

    // Pagination configuration
    const page = parseInt(searchParams.get('page') || '1');
    const pageSize = parseInt(searchParams.get('pageSize') || '50');

    // Initialize stats
    let totalClassesHeld = 0;
    let totalPresent = 0;
    let totalAbsent = 0;
    let totalCancelled = 0;

    const courseStats: Record<string, { held: number; present: number; absent: number; cancelled: number; courseId: number; subjectName: string; subjectCode: string }> = {};
    const courseMap = new Map<number, { subjectName: string; subjectCode: string; subjectId: string }>();
    student.courses.forEach(c => {
      courseStats[c.id] = {
        held: 0, present: 0, absent: 0, cancelled: 0,
        courseId: c.id, subjectName: c.subjectName, subjectCode: c.subjectCode
      };
      courseMap.set(c.id, { subjectName: c.subjectName, subjectCode: c.subjectCode, subjectId: c.subjectId });
    });

    const allClassHistory: Array<{
      date: string;
      courseId: number;
      subjectCode: string;
      subjectName: string;
      startTime: string;
      endTime: string;
      room: string | null;
      status: string;
      isExtra: boolean;
    }> = [];
```

---

### Phase 4: GET Request - Date Iterations Loop (Template slots & overrides)
Resolves every date in the range, applying filters for semesters, archived courses, holiday types, and cancellation overrides.

```typescript
    for (const dateStr of dates) {
      const dayName = getDayOfWeek(dateStr);
      const dayVacationType = vacationMap.get(dateStr);

      if (dayVacationType === 'VACATION') continue;

      const dayTemplates = student.courses.flatMap(c => {
        if (c.archivedAt && dateStr > c.archivedAt) return [];

        if (c.source === 'admin') {
          const tags = courseTagMap.get(c.id);
          if (tags) {
            const matchingSemesters = semesters.filter(s => 
              s.university === tags.university && 
              s.courseName === tags.courseName
            );
            if (matchingSemesters.length > 0) {
              const isWithinSemester = matchingSemesters.some(s => 
                dateStr >= s.startDate && dateStr <= s.endDate
              );
              if (!isWithinSemester) return [];
            }
          }
        }

        return c.weeklySlots.filter(s => {
          if (s.dayOfWeek !== dayName) return false;
          if (s.activeFrom && dateStr < s.activeFrom) return false;
          if (s.activeUntil && dateStr > s.activeUntil) return false;
          if (!s.activeFrom && dateStr < student.courseStartDate) return false;
          return true;
        });
      });
      const dateOverrides = dailyClasses.filter(o => o.date === dateStr);

      for (const slot of dayTemplates) {
        if (!courseStats[slot.courseId]) continue;
        const override = dateOverrides.find(o => o.weeklySlotId === slot.id);
        let status = 'SCHEDULED';
        if (override) status = override.status;

        const courseInfo = courseMap.get(slot.courseId);

        // Check if class is cancelled via override status
        if (status === 'CANCELLED') {
          totalCancelled++;
          courseStats[slot.courseId].cancelled++;
          allClassHistory.push({
            date: dateStr,
            courseId: slot.courseId,
            subjectCode: courseInfo?.subjectCode || '',
            subjectName: courseInfo?.subjectName || '',
            startTime: override?.startTime || slot.startTime,
            endTime: override?.endTime || slot.endTime,
            room: override?.room || slot.room,
            status: 'CANCELLED',
            isExtra: false,
          });
          continue;
        }

        let attStatus: string | null = null;
        if (dayVacationType === 'ABSENT_DAY') {
          attStatus = 'ABSENT';
        } else {
          const att = attendances.find(a => 
            a.courseId === slot.courseId && a.date === dateStr &&
            (override ? a.dailyClassId === override.id : a.weeklySlotId === slot.id)
          );
          if (att) attStatus = att.status;
        }

        // Treat class as cancelled if attendance record is CANCELLED
        if (attStatus === 'CANCELLED') {
          totalCancelled++;
          courseStats[slot.courseId].cancelled++;
          allClassHistory.push({
            date: dateStr,
            courseId: slot.courseId,
            subjectCode: courseInfo?.subjectCode || '',
            subjectName: courseInfo?.subjectName || '',
            startTime: override?.startTime || slot.startTime,
            endTime: override?.endTime || slot.endTime,
            room: override?.room || slot.room,
            status: 'CANCELLED',
            isExtra: false,
          });
          continue;
        }

        totalClassesHeld++;
        courseStats[slot.courseId].held++;
        const resolvedStatus = attStatus === 'PRESENT' ? 'PRESENT' : attStatus === 'ABSENT' ? 'ABSENT' : 'UNMARKED';
        if (attStatus === 'PRESENT') { totalPresent++; courseStats[slot.courseId].present++; }
        else if (attStatus === 'ABSENT') { totalAbsent++; courseStats[slot.courseId].absent++; }

        allClassHistory.push({
          date: dateStr,
          courseId: slot.courseId,
          subjectCode: courseInfo?.subjectCode || '',
          subjectName: courseInfo?.subjectName || '',
          startTime: override?.startTime || slot.startTime,
          endTime: override?.endTime || slot.endTime,
          room: override?.room || slot.room,
          status: resolvedStatus,
          isExtra: false,
        });
      }
```

---

### Phase 5: GET Request - Extra Classes Resolution, Sorting, & Pagination
Processes custom extra class instances, sorts histories chronologically, and returns paginated statistics.

```typescript
      // Process extra classes
      const extraClasses = dateOverrides.filter(o => o.isExtra);
      for (const extra of extraClasses) {
        if (!courseStats[extra.courseId]) continue;
        const courseInfo = courseMap.get(extra.courseId);

        if (extra.status === 'CANCELLED') {
          totalCancelled++;
          courseStats[extra.courseId].cancelled++;
          allClassHistory.push({
            date: dateStr,
            courseId: extra.courseId,
            subjectCode: courseInfo?.subjectCode || '',
            subjectName: courseInfo?.subjectName || '',
            startTime: extra.startTime,
            endTime: extra.endTime,
            room: extra.room,
            status: 'CANCELLED',
            isExtra: true,
          });
          continue;
        }

        let attStatus: string | null = null;
        if (dayVacationType === 'ABSENT_DAY') {
          attStatus = 'ABSENT';
        } else {
          const att = attendances.find(a => 
            a.courseId === extra.courseId && a.date === dateStr && a.dailyClassId === extra.id
          );
          if (att) attStatus = att.status;
        }

        if (attStatus === 'CANCELLED') {
          totalCancelled++;
          courseStats[extra.courseId].cancelled++;
          allClassHistory.push({
            date: dateStr,
            courseId: extra.courseId,
            subjectCode: courseInfo?.subjectCode || '',
            subjectName: courseInfo?.subjectName || '',
            startTime: extra.startTime,
            endTime: extra.endTime,
            room: extra.room,
            status: 'CANCELLED',
            isExtra: true,
          });
          continue;
        }

        totalClassesHeld++;
        courseStats[extra.courseId].held++;
        const resolvedStatus = attStatus === 'PRESENT' ? 'PRESENT' : attStatus === 'ABSENT' ? 'ABSENT' : 'UNMARKED';
        if (attStatus === 'PRESENT') { totalPresent++; courseStats[extra.courseId].present++; }
        else if (attStatus === 'ABSENT') { totalAbsent++; courseStats[extra.courseId].absent++; }

        allClassHistory.push({
          date: dateStr,
          courseId: extra.courseId,
          subjectCode: courseInfo?.subjectCode || '',
          subjectName: courseInfo?.subjectName || '',
          startTime: extra.startTime,
          endTime: extra.endTime,
          room: extra.room,
          status: resolvedStatus,
          isExtra: true,
        });
      }
    }

    // Compile metrics and averages
    const overallPercentage = totalClassesHeld > 0 ? Math.round((totalPresent / totalClassesHeld) * 100) : 100;

    const subjectsData = Object.values(courseStats).map(s => ({
      ...s,
      percentage: s.held > 0 ? Math.round((s.present / s.held) * 100) : 100
    }));

    // Sort by date descending
    allClassHistory.sort((a, b) => {
      const dateCmp = b.date.localeCompare(a.date);
      if (dateCmp !== 0) return dateCmp;
      return a.startTime.localeCompare(b.startTime);
    });

    // Paginate response data
    const totalHistoryItems = allClassHistory.length;
    const totalPages = Math.ceil(totalHistoryItems / pageSize);
    const startIdx = (page - 1) * pageSize;
    const paginatedHistory = allClassHistory.slice(startIdx, startIdx + pageSize);

    return NextResponse.json({
      range: { start: startStr, end: endStr },
      summary: { totalClassesHeld, totalPresent, totalAbsent, totalCancelled, overallPercentage },
      subjects: subjectsData,
      classHistory: paginatedHistory,
      historyPagination: { page, pageSize, totalItems: totalHistoryItems, totalPages },
    });

  } catch (error: any) {
    if (error.message === 'Unauthorized: No authenticated user') {
      return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    }
    console.error('Error fetching attendance stats:', error);
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}
```

---

### Phase 6: POST Request - Toggle Attendance Logger
Upserts the database log row storing whether the student attended a specific session.

```typescript
export async function POST(request: Request) {
  try {
    const user = await getAuthenticatedUser();
    const body = await request.json();
    const { courseId, date, status, weeklySlotId, dailyClassId } = body;

    if (!courseId || !date || !status) {
      return NextResponse.json({ error: 'Missing required fields' }, { status: 400 });
    }

    const cId = parseInt(courseId);
    const wsId = weeklySlotId ? parseInt(weeklySlotId) : null;
    const dcId = dailyClassId ? parseInt(dailyClassId) : null;

    const existing = await prisma.attendance.findFirst({
      where: {
        userId: user.id,
        courseId: cId,
        date,
        weeklySlotId: wsId,
        dailyClassId: dcId,
      },
    });

    let attendance;
    if (existing) {
      attendance = await prisma.attendance.update({
        where: { id: existing.id },
        data: { status },
      });
    } else {
      attendance = await prisma.attendance.create({
        data: {
          userId: user.id,
          courseId: cId,
          date,
          status,
          weeklySlotId: wsId,
          dailyClassId: dcId,
        },
      });
    }

    return NextResponse.json(attendance);
  } catch (error: any) {
    if (error.message === 'Unauthorized: No authenticated user') {
      return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    }
    console.error('Error updating attendance:', error);
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}
```
