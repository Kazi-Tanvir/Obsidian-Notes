---
tags:
  - portfolio
  - nextjs
  - design/neobrutalism
  - mysql

date: 2026-04-17
---

# Kazi Tanvir - Portfolio Project

> [!abstract] Overview
> This repository contains the source code for my dynamic, neobrutalist portfolio website. It is built using modern web technologies to ensure high performance, security, and a stunning visual experience.

---

## 🎨 Design Details & Theme

The project employs a [[Neobrutalism]] design aesthetic. This style is characterized by bold typography, high-contrast colors, distinct borders, and flat, hard shadows instead of soft, diffused ones.

> [!info] Core Themes & Variables
> - **Color Palette:** > 	- **Primary:** Yellow (`#ffe600`) as the main background and accent.
> 	- **Secondary Accents:** Hero Background Pink (`#ff57c3`), About Background Cyan (`#00d1ff`), and Milestone Background Orange (`#ff9100`).
> 	- **Surfaces/Text:** High contrast black (`#000000`) and white (`#ffffff`).
> - **Typography:** > 	- **Headlines:** `Space Grotesk` (with `Arial Black` fallback).
> 	- **Body Text:** `Manrope`.
> - **Visuals:** Defined in `src/app/globals.css` using custom [[Tailwind CSS]] v4 variables (`@theme`).

### Responsiveness & Structural Adjustments
To ensure the Neobrutalist design scales cleanly:
- **Scaling Borders:** The main `<body>` wrapper has a `4px` black border on mobile that scales up to an `8px` border on medium (`md:`) screens and above.
- **Dynamic Shadows:** Custom utility classes (`.neo-shadow`, `.neo-shadow-sm`, `.neo-shadow-lg`). On mobile, these cast a smaller shadow (e.g., `4px 4px`). Using a media query (`@media (min-width: 768px)`), shadows enlarge on desktop displays (e.g., `8px 8px`) to emphasize depth.
- **Text Strokes:** Custom `.text-stroke` class provides a `3px` text shadow on mobile, scaling to `4px` on larger screens.

---

## ⚙️ Functionality & Application Logic

This application is built on **[[Next.js]] (App Router)**. It provides a static-first front end combined with powerful server-side functionality.

### Key Logic Areas
1. **Server Actions **(`src/app/actions.ts`): - Replaces traditional REST API endpoints. Form submissions and Admin CRUD operations directly call server functions.
   - Cache invalidation (`revalidatePath`) ensures the static frontend immediately reflects database changes without a hard refresh.
2. **Secure Admin Dashboard:**
   - Protected `/admin` routes.
   - **Authentication:** Uses [[JWT|JSON Web Tokens]] signed via the `jose` package. Passwords are securely hashed via `bcryptjs`.
   - Sets an `admin_token` HTTP-only cookie upon login to manage Projects, Skills, Education, Reviews, and Messages.
3. **Contact Form Handling:**
   - Generates a UUID for every message.
   - Securely stores submissions directly into the MySQL database.

---

## 🗄️ Database Integration

A [[MySQL]] database is utilized to store all dynamic content, making the portfolio completely manageable via the Admin UI.

- **Connection & Setup:** Handled through `src/lib/db.ts` using the `mysql2` package.
- **Connection Pool:** Uses `mysql.createPool` via the `DATABASE_URL` environment variable to reuse connections, preventing server overload.

> [!database] Schema Tables
> Complete schema and sample data found in `db_dump.sql`.

| Table       | Description                                                                                           |
| :---------- | :---------------------------------------------------------------------------------------------------- |
| `admin`     | Stores the administrative credentials (username, hashed password).                                    |
| `project`   | Stores project details (UUID, title, description, tags [JSON], image URLs, category, external links). |
| `skill`     | Manages displayed technical skills and their respective icon references.                              |
| `review`    | Stores client testimonials.                                                                           |
| `education` | Tracks educational history and active status.                                                         |
| `message`   | Captures incoming contact form submissions (UUID, name, email, payload).                              |

---

## 📦 Required Packages

### Core Framework & UI
- `next` `(^16.2.1-canary.45)`: Core React framework for SSR, App Router, and Server Actions.
- `react` & `react-dom` `(^19.0.0)`: Foundational UI libraries.
- `lucide-react`: Clean, SVG-based icons.
- `motion`: (Framer Motion) Production-ready animation library for micro-interactions.

### Styling
- `tailwindcss` `(^4.1.14)` & `@tailwindcss/postcss`: Utility-first CSS framework (Version 4).
- `postcss` & `autoprefixer`: CSS processors for applying Tailwind and vendor prefixes.

### Backend & Database
- `mysql2`: High-performance MySQL driver with Promise support (critical for async/await Server Actions).
- `bcryptjs`: Hashes admin passwords and securely compares them during login.
- `jose`: Lightweight, dependency-free JWT library for session management.
- `dotenv`: Loads `.env` variables into `process.env`.

---

## 🚀 How to Run the Project Locally

> [!tip] Setup Checklist
> Use the checklist below to track your local deployment progress.

- [ ] **1. Prerequisites:** Ensure Node.js (v18+) and a local/remote MySQL Server are running.
- [ ] **2. Environment Setup:** Create a `.env` file in the root directory:
```env
# Database connection string
DATABASE_URL="mysql://username:password@localhost:3306/portfoliodb"

# Secret key for signing Admin JWT tokens
ADMIN_SECRET="your_very_secure_secret_string"
```
- [ ]  **3. Database Initialization:** Import the SQL dump to create tables and the default admin account:
```bash
mysql -u your_username -p portfoliodb < db_dump.sql
```
> [!warning] Security Note
> Default admin credentials are `Username: admin` / `Password: admin123`. **Update this by hashing your own password if deploying.**
- [ ] **4. Installation & Startup:** Run the following commands in your terminal:
```bash
npm install
npm run dev
```
- [ ] **5. Access:** The application will be accessible at `http://localhost:3000`.