---
tags:
- frontend
- nextjs
- react
- server-actions
- forms
- optimistic-ui
date: 2026-08-09
---

# Day 9 - Next.js Server Actions, Mutations, Optimistic UI & Form Handling

## SECTION 1: IN-DEPTH THEORY & ARCHITECTURE

### 1. Server Actions Architecture ('use server')

**Server Actions** are asynchronous server functions executed on the server that can be invoked directly from Client Components, Server Components, or native HTML <form> elements.

- **RPC Endpoint Abstraction**: Next.js automatically generates an encrypted HTTP POST endpoint under the hood for each Server Action.

- **Progressive Enhancement**: HTML forms using Server Actions work even before JavaScript hydraes on the client.

- **Security Guardrails**: Server Actions should always validate user authentication, authorization, and input payloads (e.g. via Zod) server-side.

```javascript
// actions/user-actions.ts
```

'use server'

```javascript
import { z } from 'zod';
import { revalidateTag } from 'next/cache';
const updateUserSchema = z.object({
```

userId: z.string().uuid(),

name: z.string().min(2),

```javascript
});
export async function updateProfile(prevState: any, formData: FormData) {
// 1. Parse & Validate
const rawData = {
```

userId: formData.get('userId'),

name: formData.get('name'),

```javascript
};
const result = updateUserSchema.safeParse(rawData);
if (!result.success) {
return { success: false, errors: result.error.flatten().fieldErrors };
}
// 2. Perform DB Mutation
await db.user.update({
```

where: { id: result.data.userId },

data: { name: result.data.name },

```javascript
});
// 3. Purge Next.js Data Cache & Return State
revalidateTag('user-profile');
return { success: true, errors: {} };
}
```

### 2. Form State & Loading Management (useActionState & useFormStatus)

Managing submission state, pending loaders, and server errors is built on native React 19 / Next.js hooks:

```javascript
// components/EditProfileForm.tsx
```

'use client'

```javascript
import { useActionState } from 'react';
import { useFormStatus } from 'react-dom';
import { updateProfile } from '@/actions/user-actions';
function SubmitButton() {
const { pending } = useFormStatus();
return (
```

<button type="submit" disabled={pending}>

{pending ? 'Saving...' : 'Save Changes'}

</button>

```typescript
);
}
export function EditProfileForm({ userId }: { userId: string }) {
const [state, formAction] = useActionState(updateProfile, { success: false, errors: {} });
return (
```

<form action={formAction}>

<input type="hidden" name="userId" value={userId} />

<input type="text" name="name" placeholder="Enter new name" />

{state.errors?.name && <p className="error">{state.errors.name[0]}</p>}

<SubmitButton />

</form>

```javascript
);
}
```

### 3. Optimistic UI Updates (useOptimistic)

useOptimistic provides instant UI updates while the asynchronous Server Action runs in the background, automatically reverting if the mutation fails.

```javascript
// components/OptimisticTodoList.tsx
```

'use client'

```typescript
import { useOptimistic, useTransition } from 'react';
import { addTodoAction } from '@/actions/todo-actions';
interface Todo {
id: string;
text: string;
sending?: boolean;
}
export function OptimisticTodoList({ initialTodos }: { initialTodos: Todo[] }) {
const [isPending, startTransition] = useTransition();
const [optimisticTodos, addOptimisticTodo] = useOptimistic(
```

initialTodos,

(state, newText: string) => [

...state,

{ id: Math.random().toString(), text: newText, sending: true }

```javascript
]
);
async function handleSubmit(formData: FormData) {
const text = formData.get('text') as string;
// 1. Trigger Instant UI Update
addOptimisticTodo(text);
// 2. Execute Async Server Action inside Transition
```

startTransition(async () => {

```javascript
await addTodoAction(formData);
});
}
return (
```

<div>

<form action={handleSubmit}>

<input type="text" name="text" required />

<button type="submit">Add Todo</button>

</form>

<ul>

{optimisticTodos.map(todo => (

<li key={todo.id} style={{ opacity: todo.sending ? 0.5 : 1 }}>

{todo.text} {todo.sending && '(Saving...)'}

</li>

```javascript
))}
```

</ul>

</div>

```javascript
);
}
```

## SECTION 2: DOCUMENTATION CHEAT SHEET

| **Hook / API** | **Signature / Location** | **Description** |
| --- | --- | --- |
| **'use server'**      T | p of file or function                     D | signates file/function as a Server Action RPC endpoint |
| **useActionState** | useActionState(actionFn, initialState) | Manages form state, returned errors, and pending status |
| **useFormStatus** | const { pending, data } = useFormStatus() | Accesses status of parent <form> (Must be child component) |
| **useOptimistic** | useOptimistic(state, updateFn) | Immediately renders optimistic state while server mutation completes |
| **revalidatePath** | revalidatePath('/dashboard')              P | rges router and data cache for a route segment |

## SECTION 3: WEEKLY SYSTEM DESIGN & CODING PROBLEMS

### Problem 1: System Design (Multi-Step Form with Auto-Save & Optimistic Updates)

Design a production-grade multi-step Onboarding Wizard in Next.js App Router using Server Actions.

**Requirements**:

1.  Diagram data flow between step forms, Server Actions, and database state.

2.  Design a draft auto-save mechanism using debounced Server Actions without full page reloads.

3.  Architect an Optimistic UI state strategy that advances step indicators instantly while validating form fields server-side with Zod.

### Problem 2: End-to-End Code Implementation Challenge

Build an **Interactive Task Kanban Board Component** in Next.js App Router.

**Requirements**:

1.  Server Component (app/kanban/page.tsx) that fetches tasks from database.

2.  Server Action (updateTaskStatusAction) that updates task status (TODO -> IN_PROGRESS -> DONE), validates user permission, and calls revalidatePath('/kanban').

3.  Client Component (TaskCard.tsx) using useOptimistic to instantly move the task card across Kanban columns upon click/drag, rolling back smoothly if the Server Action throws an authorization error.

4.  Include Zod schema validation and error feedback handling.
