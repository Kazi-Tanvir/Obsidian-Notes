---
tags:
- nextjs
- forms
- server-actions
---
# Server Actions

## What's the Actual Use?
Server Actions allow you to write functions that run on the server but can be called directly from your client-side components. This eliminates the need to manually create an API route and use `fetch()` just to submit a form or update a database.

## Real-Life Analogy
Imagine you want to change your address at the bank. Traditional API: You fill out a form, put it in an envelope, mail it to the bank, and wait for them to process it. Server Action: The bank manager is standing right next to you; you tell them the new address, and they update the computer immediately for you.

## Other Common Use Cases
- Deleting a post or comment in a social media app
- Updating a user's profile settings
- Adding items to a database-backed shopping cart

## Documentation & Code
Define actions in a separate file with `"use server"` or at the top of a server component function.

```jsx
// 1. Define the Action (e.g., in actions.js)
"use server";

export async function createPost(formData) {
  const title = formData.get("title");
  // Logic to save 'title' to Database...
  console.log(`Saved post: ${title}`);
}

// 2. Use the Action in a Component
export default function PostForm() {
  return (
    <form action={createPost}>
      <input name="title" type="text" placeholder="Enter title" />
      <button type="submit">Create Post</button>
    </form>
  );
}
```