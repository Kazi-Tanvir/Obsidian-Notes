---
tags: [api-admin, analytics, aggregate, student-records, backend]
---

# Admin API: Cross-Student Attendance Analytics

This endpoint compiles database attendance statistics for administrators to audit batch averages or review performance metrics for individual students, located at `src/app/api/admin/analytics/route.ts`.

- **File Link**: [route.ts](file:///d:/02_CODE/04_TEST/Routine/src/app/api/admin/analytics/route.ts)
- **Backlinks**: [[index]], [[component_admin_panel]], [[admin_api]]

---

## 1. Endpoint Configuration

- **HTTP Method**: `GET`
- **Route URL**: `/api/admin/analytics`
- **Authentication**: Required (`Admin` role check)
- **URL Query Parameters**:
  - `startDate` & `endDate` (`YYYY-MM-DD`, Required): Calculations date range window.
  - `view` (`String`, Required): Mode is either `"aggregate"` (course averages) or `"per-student"` (scorecard breakdown list).
  - `university` & `courseName` (`String`, Optional): Batch filter tag parameters.
  - `subjectId` (`String`, Optional): Filter results to a single course ID key.

---

## 2. Calculation Modes

### A. View: `aggregate` (Batch Course Averages)
- Loops through matching attendance logs and groups metrics by `subjectId`.
- Computes:
  - Total Present, Absent, and Cancelled counts.
  - Student Count (number of distinct users attending this subject).
  - **Attendance Rate**:
    $$\text{Rate} = \text{round}\left(\frac{\text{Present}}{\text{Present} + \text{Absent}} \times 100\right)$$

### B. View: `per-student` (Individual Scorecards list)
- Group metrics by student `userId`.
- For each student:
  - Generates a nested course breakdown array showing Present/Absent metrics and rates per subject.
  - Computes the student's overall attendance rate across all registered courses.
  - Returns the list sorted alphabetically by student name.

---

## 3. Source Code

Here is the complete implementation of `src/app/api/admin/analytics/route.ts`:

```typescript
import { NextRequest, NextResponse } from 'next/server';
import { requireAdmin } from '@/lib/auth';
import { prisma } from '@/lib/prisma';

// GET: Admin attendance analytics — aggregate or per-student
export async function GET(req: NextRequest) {
  try {
    await requireAdmin();

    const { searchParams } = new URL(req.url);
    const university = searchParams.get('university') || '';
    const courseName = searchParams.get('courseName') || '';
    const startDate = searchParams.get('startDate') || '';
    const endDate = searchParams.get('endDate') || '';
    const view = searchParams.get('view') || 'aggregate'; // 'aggregate' or 'per-student'
    const courseSubjectId = searchParams.get('subjectId') || '';

    if (!startDate || !endDate) {
      return NextResponse.json({ error: 'startDate and endDate are required' }, { status: 400 });
    }

    // Build user filter based on tags
    const userFilter: any = {};
    if (university) userFilter.university = university;
    if (courseName) userFilter.courseName = courseName;

    // Find matching users
    const users = await prisma.user.findMany({
      where: { ...userFilter, role: 'user' },
      select: { id: true, name: true, email: true, university: true, courseName: true },
    });

    const userIds = users.map(u => u.id);

    if (userIds.length === 0) {
      return NextResponse.json({ 
        view,
        totalStudents: 0,
        courses: [],
        students: [],
      });
    }

    // Build attendance filter
    const attendanceFilter: any = {
      userId: { in: userIds },
      date: { gte: startDate, lte: endDate },
    };

    // Get all attendance records
    const attendanceRecords = await prisma.attendance.findMany({
      where: attendanceFilter,
      include: {
        course: { select: { subjectId: true, subjectName: true, subjectCode: true, source: true } },
        user: { select: { id: true, name: true, email: true } },
      },
    });

    // Optionally filter by specific course
    const filteredRecords = courseSubjectId
      ? attendanceRecords.filter(a => a.course.subjectId === courseSubjectId)
      : attendanceRecords;

    if (view === 'aggregate') {
      // Group by course — compute aggregate stats
      const courseMap = new Map<string, { 
        subjectId: string; 
        subjectName: string; 
        subjectCode: string;
        totalPresent: number; 
        totalAbsent: number; 
        totalCancelled: number;
        studentCount: number;
        students: Set<number>;
      }>();

      for (const record of filteredRecords) {
        const key = record.course.subjectId;
        if (!courseMap.has(key)) {
          courseMap.set(key, {
            subjectId: record.course.subjectId,
            subjectName: record.course.subjectName,
            subjectCode: record.course.subjectCode,
            totalPresent: 0,
            totalAbsent: 0,
            totalCancelled: 0,
            studentCount: 0,
            students: new Set(),
          });
        }
        const entry = courseMap.get(key)!;
        entry.students.add(record.userId);
        if (record.status === 'PRESENT') entry.totalPresent++;
        else if (record.status === 'ABSENT') entry.totalAbsent++;
        else if (record.status === 'CANCELLED') entry.totalCancelled++;
      }

      const courses = Array.from(courseMap.values()).map(entry => ({
        subjectId: entry.subjectId,
        subjectName: entry.subjectName,
        subjectCode: entry.subjectCode,
        totalPresent: entry.totalPresent,
        totalAbsent: entry.totalAbsent,
        totalCancelled: entry.totalCancelled,
        studentCount: entry.students.size,
        attendanceRate: entry.totalPresent + entry.totalAbsent > 0
          ? Math.round((entry.totalPresent / (entry.totalPresent + entry.totalAbsent)) * 100)
          : 0,
      }));

      return NextResponse.json({
        view: 'aggregate',
        totalStudents: users.length,
        dateRange: { startDate, endDate },
        courses,
      });
    } else {
      // Per-student view
      const studentMap = new Map<number, {
        id: number;
        name: string;
        email: string;
        courses: Map<string, { 
          subjectId: string; 
          subjectCode: string; 
          present: number; 
          absent: number; 
          cancelled: number 
        }>;
      }>();

      for (const record of filteredRecords) {
        if (!studentMap.has(record.userId)) {
          studentMap.set(record.userId, {
            id: record.user.id,
            name: record.user.name,
            email: record.user.email,
            courses: new Map(),
          });
        }

        const student = studentMap.get(record.userId)!;
        const courseKey = record.course.subjectId;

        if (!student.courses.has(courseKey)) {
          student.courses.set(courseKey, {
            subjectId: record.course.subjectId,
            subjectCode: record.course.subjectCode,
            present: 0,
            absent: 0,
            cancelled: 0,
          });
        }

        const courseStats = student.courses.get(courseKey)!;
        if (record.status === 'PRESENT') courseStats.present++;
        else if (record.status === 'ABSENT') courseStats.absent++;
        else if (record.status === 'CANCELLED') courseStats.cancelled++;
      }

      const students = Array.from(studentMap.values()).map(student => ({
        id: student.id,
        name: student.name,
        email: student.email,
        courses: Array.from(student.courses.values()).map(c => ({
          ...c,
          attendanceRate: c.present + c.absent > 0
            ? Math.round((c.present / (c.present + c.absent)) * 100)
            : 0,
        })),
        overallRate: (() => {
          let totalPresent = 0;
          let totalAbsent = 0;
          for (const c of student.courses.values()) {
            totalPresent += c.present;
            totalAbsent += c.absent;
          }
          return totalPresent + totalAbsent > 0
            ? Math.round((totalPresent / (totalPresent + totalAbsent)) * 100)
            : 0;
        })(),
      }));

      return NextResponse.json({
        view: 'per-student',
        totalStudents: users.length,
        dateRange: { startDate, endDate },
        students: students.sort((a, b) => a.name.localeCompare(b.name)),
      });
    }
  } catch (error: any) {
    if (error.message === 'Forbidden: Admin access required') {
      return NextResponse.json({ error: 'Forbidden' }, { status: 403 });
    }
    if (error.message === 'Unauthorized: No authenticated user') {
      return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    }
    console.error('Error fetching admin analytics:', error);
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}
```
