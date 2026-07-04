---
tags: [lib, utility, string-helpers, normalization, backend]
---

# Code Library: UI & String Utilities

This module contains shared text formatting and helper functions, located at `src/lib/utils.ts`.

- **File Link**: [utils.ts](file:///d:/02_CODE/04_TEST/Routine/src/lib/utils.ts)
- **Backlinks**: [[index]], [[SCHEMA]], [[api_user_sync_template]], [[api_admin_push_sync]]

---

## Technical Details

To ensure consistency in user secondary tag grouping, all course tags and university names must be normalized before matching or database insertion. The `normalizeTag()` function does the following:
- Sanitizes input values (safely handles `null`/`undefined`).
- Trims leading and trailing whitespaces.
- Replaces multiple consecutive space characters with a single standard space.

---

## Source Code

Here is the complete implementation of `src/lib/utils.ts`:

```typescript
/**
 * Normalizes user/course tags by trimming whitespace and replacing
 * multiple consecutive spaces with a single space.
 */
export function normalizeTag(tag: string | null | undefined): string {
  if (!tag) return '';
  return tag.trim().replace(/\s+/g, ' ');
}
```
