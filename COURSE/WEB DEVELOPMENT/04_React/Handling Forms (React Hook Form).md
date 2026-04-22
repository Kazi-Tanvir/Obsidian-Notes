---
tags:
- react
- forms
- validation
---
# Handling Forms (React Hook Form)

## What's the Actual Use?
React Hook Form is a library that simplifies form management and validation in React. It significantly reduces the amount of code needed compared to manual state management (controlled components) and improves performance by reducing unnecessary re-renders.

## Real-Life Analogy
Managing a form manually is like having a person watch every single keypress and update a ledger for each one (`useState`). React Hook Form is like giving the user a clipboard; they fill everything out on their own, and only when they hand the clipboard to you (submit) do you check the data and process it.

## Other Common Use Cases
- Complex multi-step registration forms
- Real-time form validation (email format, password strength)
- Handling dynamic form fields (adding/removing inputs)

## Documentation & Code
Use the `useForm` hook to register inputs and handle submissions.

```jsx
import { useForm } from 'react-hook-form';

export default function SimpleForm() {
  // register: connects input to the library
  // handleSubmit: wraps your submit function
  // formState: contains errors and other metadata
  const { register, handleSubmit, formState: { errors } } = useForm();

  const onSubmit = (data) => {
    console.log("Form Data:", data);
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <label>Email</label>
      {/* Register input with validation rules */}
      <input {...register("email", { required: "Email is required" })} />
      {errors.email && <span>{errors.email.message}</span>}

      <label>Password</label>
      <input 
        type="password" 
        {...register("password", { minLength: { value: 6, message: "Too short" } })} 
      />
      {errors.password && <span>{errors.password.message}</span>}

      <button type="submit">Submit</button>
    </form>
  );
}
```