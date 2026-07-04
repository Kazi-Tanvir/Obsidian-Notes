---
tags: [api-user, announcements, broadcast, tag-filtering, backend]
---

# User API: Announcements Broadcasts

This endpoint handles retrievals of admin broadcast announcements targeting the student's registered batch tag categories, located at `src/app/api/announcements/route.ts`.

- **File Link**: [route.ts](file:///d:/02_CODE/04_TEST/Routine/src/app/api/announcements/route.ts)
- **Backlinks**: [[index]], [[component_dashboard_view]], [[api]], [[api_admin_announcements]]

---

## 1. Endpoint Configuration

- **HTTP Method**: `GET`
- **Route URL**: `/api/announcements`
- **Authentication**: Required (`User` session check)

---

## 2. Dynamic Tag-Targeting Logic

Rather than showing all system messages to every student, the controller filters announcements dynamically:

1. **Tag Pair Consolidation**: Combines the student's primary tags (`university`, `courseName`) and all registered secondary tag records into a list of tag pairs.
2. **Matching Parameters**: Builds a database query matching announcements under these OR filters:
   - Universal broadcasts (where `university: null` and `courseName: null`).
   - University-wide alerts (where `university` matches, and `courseName` is null).
   - Course-wide alerts (where `courseName` matches, and `university` is null).
   - Exact departmental matches (where both tags match a pair).
3. **Expiration check**: Compares `expiresAt` with today's ISO date string. If the notice has expired, it is filtered out.
4. **Ordering**: Sorted with the newest items first (`createdAt: 'desc'`).

---

## 3. Source Code

Here is the complete implementation of `src/app/api/announcements/route.ts`:

```typescript
import { NextResponse } from 'next/server';
import { getAuthenticatedUser } from '@/lib/auth';
import { prisma } from '@/lib/prisma';

// GET: Fetch announcements matching the current user's tags (non-expired only)
export async function GET() {
  try {
    const user = await getAuthenticatedUser();
    const today = new Date().toISOString().split('T')[0];

    // Get user's secondary tags
    const secondaryTags = await prisma.userSecondaryTag.findMany({
      where: { userId: user.id },
    });

    // Build all tag pairs for the user
    const tagPairs: Array<{ university: string; courseName: string }> = [];
    if (user.university && user.courseName) {
      tagPairs.push({ university: user.university, courseName: user.courseName });
    }
    for (const tag of secondaryTags) {
      tagPairs.push({ university: tag.university, courseName: tag.courseName });
    }

    // Build OR conditions for tag matching
    const tagConditions: any[] = [
      // Global announcements (no targeting)
      { university: null, courseName: null },
    ];

    for (const tp of tagPairs) {
      // Match university only
      tagConditions.push({ university: tp.university, courseName: null });
      // Match courseName only
      tagConditions.push({ university: null, courseName: tp.courseName });
      // Match exact combo
      tagConditions.push({ university: tp.university, courseName: tp.courseName });
    }

    const announcements = await prisma.announcement.findMany({
      where: {
        AND: [
          { OR: tagConditions },
          {
            OR: [
              { expiresAt: null },
              { expiresAt: { gte: today } },
            ],
          },
        ],
      },
      orderBy: { createdAt: 'desc' },
    });

    return NextResponse.json(announcements);
  } catch (error: any) {
    if (error.message === 'Unauthorized: No authenticated user') {
      return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    }
    console.error('Error fetching user announcements:', error);
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}
```
