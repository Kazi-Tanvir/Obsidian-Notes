---
tags: [api-user, profile, update, backend]
---

# User API: Profile Manager

This endpoint handles personal profile retrievals and customization settings, located at `src/app/api/user/route.ts`.

- **File Link**: [route.ts](file:///d:/02_CODE/04_TEST/Routine/src/app/api/user/route.ts)
- **Backlinks**: [[index]], [[home_page]], [[api]], [[lib_auth]]

---

## 1. GET `/api/user`

- **Purpose**: Retrieves the detailed profile of the active authenticated user, including their active courses directory.
- **Authentication**: Required (`User` session check)
- **Success Response JSON**:
  ```json
  {
    "id": 1,
    "clerkId": "user_abc123",
    "name": "Alice Smith",
    "email": "alice@univ.edu",
    "color": "#3182ce",
    "role": "user",
    "university": "University of Dhaka",
    "courseName": "BSSE-18",
    "courseStartDate": "2026-01-01",
    "createdAt": "2026-07-04T04:19:24.000Z",
    "courses": []
  }
  ```

---

## 2. POST `/api/user`

- **Purpose**: Commits updates to theme colors, name parameters, and course/university registration tags.
- **Authentication**: Required (`User` session check)
- **JSON Payload Parameters**:
  - `name` (`String`, Optional): Updated user display name.
  - `color` (`String`, Optional): Hex theme color code (e.g. `"#3182ce"`).
  - `courseStartDate` (`String` format `"YYYY-MM-DD"`, Optional): Date when slot calendar resolution starts.
  - `university` (`String`, Optional): Targets primary batch synchronization tag.
  - `courseName` (`String`, Optional): Targets primary course synchronization tag.
- **Tag Normalization**: Handled using `normalizeTag()` before committing writes to database fields.
- **Success Response JSON**: Returns the updated user record object.

---

## 3. Source Code

Here is the complete implementation of `src/app/api/user/route.ts`:

```typescript
import { NextResponse } from 'next/server';
import { getAuthenticatedUser } from '@/lib/auth';
import { prisma } from '@/lib/prisma';
import { normalizeTag } from '@/lib/utils';

// GET: Return the current authenticated user's profile
export async function GET() {
  try {
    const user = await getAuthenticatedUser();
    
    const fullUser = await prisma.user.findUnique({
      where: { id: user.id },
      include: {
        courses: {
          where: { isArchived: false },
        },
      },
    });

    return NextResponse.json(fullUser);
  } catch (error: any) {
    if (error.message === 'Unauthorized: No authenticated user') {
      return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    }
    console.error('Error fetching user:', error);
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}

// POST: Update the current user's profile settings
export async function POST(request: Request) {
  try {
    const user = await getAuthenticatedUser();
    const body = await request.json();
    const { courseStartDate, color, name, university, courseName } = body;

    const updateData: any = {};
    if (courseStartDate !== undefined) updateData.courseStartDate = courseStartDate;
    if (color !== undefined) updateData.color = color;
    if (name !== undefined) updateData.name = name;
    if (university !== undefined) updateData.university = normalizeTag(university);
    if (courseName !== undefined) updateData.courseName = normalizeTag(courseName);

    const updated = await prisma.user.update({
      where: { id: user.id },
      data: updateData,
    });

    return NextResponse.json(updated);
  } catch (error: any) {
    if (error.message === 'Unauthorized: No authenticated user') {
      return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    }
    console.error('Error updating user:', error);
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}
```
