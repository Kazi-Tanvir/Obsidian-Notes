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
