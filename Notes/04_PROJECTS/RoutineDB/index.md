---
tags: [index, documentation, map-of-content, toc]
---

# Routine Planner Documentation: Master Index

Welcome to the Developer Documentation database for the Routine Planner application. This vault is organized with a flat structure using Obsidian tags and backlinks to make discovery and navigation simple.

---

## 🗺️ Architectural Core

- **[[ARCHITECTURE]]** - System design, auth routing, request flow, and calendar engine.
- **[[DESIGN]]** - Fonts, typography, CSS style variables, and hand-drawn UI classes.
- **[[SCHEMA]]** - Database relational model diagram (ERD) and fields definitions.

---

## 🖥️ Next.js Page Routes

- **[[layout]]** - App Shell, Clerk Auth Provider, and CSS styles bootstrapping.
- **[[home_page]]** - Dashboard core controller (`/`) and active view tab manager.
- **[[admin_page]]** - Administrator entrance controller (`/admin`) and permissions check.
- **[[signin_page]]** - Sign-in route wrapping Clerk auth interface.
- **[[signup_page]]** - Sign-up route wrapping Clerk auth interface.

---

## 🎨 UI Component Views

- **[[component_dashboard_view]]** - Renders the daily routine sheet and announcements board.
- **[[component_calendar_view]]** - Grid views for schedules (Daily, Weekly, Monthly).
- **[[component_setup_view]]** - Interface for personal courses list and slots.
- **[[component_analytics_view]]** - Attendance logs and aggregate target charts.
- **[[component_admin_panel]]** - Complete admin view and its 9 administration tabs.
- **[[component_modals]]** - Overlay modals for slot forms, override setups, vacations, and extras.

---

## ⚙️ Core Libraries & Middlewares

- **[[lib_auth]]** - Helper for user caching, automatic profile initialization, and role verification.
- **[[lib_prisma]]** - Singleton instantiation script for Prisma client.
- **[[lib_utils]]** - String manipulation and tag normalization helpers.
- **[[proxy_middleware]]** - Clerk middleware protection rules and path matching.

---

## 🔌 API Route Registers

- **[[api]]** - Overview directory of user-facing API routes.
- **[[admin_api]]** - Overview directory of admin-only API templates.

### User API Routes
- **[[api_init]]** - Single GET bootstrap endpoint for the dashboard.
- **[[api_user]]** - User profile information settings.
- **[[api_user_secondary_tags]]** - Multi-tag secondary subscription handlers.
- **[[api_user_sync_template]]** - Synchronization triggers for administrative templates.
- **[[api_user_export]]** - Personal data JSON exporter.
- **[[api_user_import]]** - Personal data JSON importer.
- **[[api_courses]]** - Personal course manager.
- **[[api_weekly_slots]]** - Recurring slots scheduler.
- **[[api_calendar]]** - Calendar overrides resolver and local adjustments logger.
- **[[api_attendance]]** - Attendance toggler and logs history.
- **[[api_vacations]]** - Personal vacation planner.
- **[[api_suggestions]]** - Administrative schedule modification suggestions.
- **[[api_announcements]]** - Tag-filtered announcements retriever.

### Admin API Routes
- **[[api_daily_class_description]]** - Instance description editor.
- **[[api_admin_users]]** - Registry control directory of registered accounts.
- **[[api_admin_global_courses]]** - Core course template definitions.
- **[[api_admin_global_slots]]** - Recurring weekly slot templates.
- **[[api_admin_global_overrides]]** - Schedule adjustment global definitions.
- **[[api_admin_global_vacations]]** - National and academic holiday scheduler.
- **[[api_admin_semesters]]** - Academic term dates manager.
- **[[api_admin_announcements]]** - Announcement broadcaster.
- **[[api_admin_suggestions]]** - Suggestions dashboard reviewer.
- **[[api_admin_export]]** - Global DB backup template.
- **[[api_admin_import]]** - Database restoration setup.
- **[[api_admin_analytics]]** - Cross-student attendance analytics.
- **[[api_admin_push_sync]]** - Push template synchronization coordinator.

---

## 🏷️ Vault Tag Index
- `#architecture` — Top-level system architecture configurations.
- `#database` — Relational databases schema definitions.
- `#theme` — Styling parameters and sketch variables.
- `#ui-page` — Entry level page file controllers.
- `#ui-component` — Modular client components.
- `#lib` — Backend logic helper utilities.
- `#api-overview` — Overview files for API route folders.
- `#api-user` — Detailed backend routes for student interactions.
- `#api-admin` — Detailed backend routes for administrator features.
