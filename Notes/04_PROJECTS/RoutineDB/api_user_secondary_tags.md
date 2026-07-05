---
tags: [api-user, tags, secondary, subscription, backend]
---

# User API: Secondary Subscriptions Manager

This endpoint handles secondary subscription tags matching additional courses or universities, located at `src/app/api/user/secondary-tags/route.ts`.

- **File Link**: [route.ts](file:///d:/02_CODE/04_TEST/Routine/src/app/api/user/secondary-tags/route.ts)
- **Backlinks**: [[index]], [[component_setup_view]], [[api]]

---

## 1. GET `/api/user/secondary-tags`

- **Purpose**: Lists all secondary subscription tags assigned to the active user.
- **Authentication**: Required (`User` session check)
- **Success Response JSON**:
  ```json
  [
    {
      "id": 2,
      "userId": 1,
      "university": "Dhaka University",
      "courseName": "IIT-10"
    }
  ]
  ```

---

## 2. POST `/api/user/secondary-tags`

- **Purpose**: Subscribes to an additional university and course tag pair.
- **Authentication**: Required (`User` session check)
- **JSON Payload Parameters**:
  - `university` (`String`, Optional): Secondary university filter tag.
  - `courseName` (`String`, Required): Secondary course name tag.
- **Validations & Constraints**:
  - Requires a valid `courseName`.
  - Blocks requests if the tags match the user's primary tags.
  - Handles MySQL unique indexing warnings. If the student has already registered the tag combination, returns `400 Bad Request` catching the Prisma unique index code `P2002`.
- **Success Response JSON**: Returns the newly created tag record.

---

## 3. DELETE `/api/user/secondary-tags`

- **Purpose**: Unsubscribes from a secondary university/course tag.
- **Authentication**: Required (`User` session check)
- **URL Query Parameters**:
  - `id` (`Int`, Required): Unique ID of the secondary tag record.
- **Validation**: Verifies that the tag record exists and belongs to the authenticated user before deletion.
- **Success Response JSON**:
  ```json
  { "success": true }
  ```

---

## 4. Implementation Code Breakdown

The source code in `src/app/api/user/secondary-tags/route.ts` is split into three key handlers:

### Phase 1: GET Request (Fetch Secondary Tags List)
Lists all secondary tag subscriptions for the authenticated student.

```typescript
import { NextRequest, NextResponse } from 'next/server';
import { getAuthenticatedUser } from '@/lib/auth';
import { prisma } from '@/lib/prisma';
import { normalizeTag } from '@/lib/utils';

export async function GET() {
  try {
    const user = await getAuthenticatedUser();

    const tags = await prisma.userSecondaryTag.findMany({
      where: { userId: user.id },
      orderBy: { id: 'asc' },
    });

    return NextResponse.json(tags);
  } catch (error: any) {
    if (error.message === 'Unauthorized: No authenticated user') {
      return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    }
    console.error('Error fetching secondary tags:', error);
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}
```

---

### Phase 2: POST Request (Subscribe to Additional Tag Pair)
Checks that the tag is not already primary, normalizes casing rules, and creates a secondary tag subscription entry.

```typescript
export async function POST(req: NextRequest) {
  try {
    const user = await getAuthenticatedUser();
    const { university: rawUniversity, courseName: rawCourseName } = await req.json();
    const university = rawUniversity ? normalizeTag(rawUniversity) : '';
    const courseName = normalizeTag(rawCourseName);

    if (!courseName) {
      return NextResponse.json({ error: 'Tag name (courseName) is required' }, { status: 400 });
    }

    // Check if same as primary tag
    if (university && user.university === university && user.courseName === courseName) {
      return NextResponse.json({ error: 'This is already your primary tag' }, { status: 400 });
    }

    const tag = await prisma.userSecondaryTag.create({
      data: {
        userId: user.id,
        university,
        courseName,
      },
    });

    return NextResponse.json(tag);
  } catch (error: any) {
    if (error.message === 'Unauthorized: No authenticated user') {
      return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    }
    if (error.code === 'P2002') {
      return NextResponse.json({ error: 'This tag already exists' }, { status: 400 });
    }
    console.error('Error adding secondary tag:', error);
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}
```

---

### Phase 3: DELETE Request (Remove Tag Subscription)
Validates record ownership, and deletes the secondary tag record.

```typescript
export async function DELETE(req: NextRequest) {
  try {
    const user = await getAuthenticatedUser();
    const { searchParams } = new URL(req.url);
    const id = parseInt(searchParams.get('id') || '');

    if (!id) {
      return NextResponse.json({ error: 'Tag ID is required' }, { status: 400 });
    }

    // Verify ownership
    const tag = await prisma.userSecondaryTag.findFirst({
      where: { id, userId: user.id },
    });

    if (!tag) {
      return NextResponse.json({ error: 'Tag not found' }, { status: 404 });
    }

    await prisma.userSecondaryTag.delete({
      where: { id },
    });

    return NextResponse.json({ success: true });
  } catch (error: any) {
    if (error.message === 'Unauthorized: No authenticated user') {
      return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    }
    console.error('Error deleting secondary tag:', error);
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}
```

