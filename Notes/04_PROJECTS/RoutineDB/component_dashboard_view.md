---
tags: [ui, component, today, class-list, attendance, frontend]
---

# UI Component: Dashboard View

This component renders the `📔 Today's Sheet` tab, located at `src/components/DashboardView.tsx`. It displays active announcements, today's schedule, sick-day/holiday notifications, and a summary of academic record stats in a dual-page layout separated by a central spiral binder.

- **File Link**: [DashboardView.tsx](file:///d:/02_CODE/04_TEST/Routine/src/components/DashboardView.tsx)
- **Backlinks**: [[index]], [[home_page]], [[DESIGN]], [[api_init]], [[api_attendance]]

---

## 1. Props Schema

The component expects the following typed arguments from the parent layout:

```typescript
interface DashboardViewProps {
  user: any;                                                       // Authenticated user object
  currentDate: string;                                             // ISO string representation of today ("YYYY-MM-DD")
  todayClasses: any[];                                             // Resolved array of session instances for today
  todayVacation: { type: string | null; description?: string | null } | null; // Holiday or sick day override configuration
  toggleAttendance: (classItem: any, date: string, status: string) => void; // Event trigger to record attendance status
  setSelectedClass: (classItem: any) => void;                      // State setter to update target context modal
  setShowSubjectModal: (show: boolean) => void;                    // Controller to show/hide session editor modal
  analyticsData: any;                                              // Statistics calculations payload
  openCustomClassModal: (dateStr?: string) => void;                // Event trigger to open extra classes model
  announcements: any[];                                            // List of unexpired announcements matching tags
}
```

---

## 2. Layout Structure

### Top announcements board
- Automatically displays matching admin announcements. Renders at most three announcements at once.

### Left page: Today's Schedule
- **Holiday Override**: If `todayVacation.type === 'VACATION'`, replaces the schedule list with a custom banner detailing the holiday.
- **Sick-Day Override**: If `todayVacation.type === 'ABSENT_DAY'`, marks all sessions as absent and displays a warning note.
- **Dynamic List**: Renders active classes sorted chronologically. Each card shows the subject code, group tags, class status (Rescheduled/Cancelled), classroom number, and custom teacher notes.
- **Interactive Checkbox Controls**: Check mark (PRESENT) and X mark (ABSENT) buttons allow recording logs without opening details modal.

### Right page: Academic Record & Statistics
- **Academic Info**: Displays university name, course tag, course start date, and user role inside a sketchy decorated note block.
- **Scorecard Widgets**: Renders wobbly boxes summarizing current attendance rate, total held sessions, present counts, and absent counts.

---

## 3. Source Code

Here is the complete implementation of `src/components/DashboardView.tsx`:

```tsx
'use client';

import React, { useState } from 'react';
import { BookOpen, Clock, MapPin, Check, X, Calendar, GraduationCap, Award, Megaphone, AlertTriangle } from 'lucide-react';

interface DashboardViewProps {
  user: any;
  currentDate: string;
  todayClasses: any[];
  todayVacation: { type: string | null; description?: string | null } | null;
  toggleAttendance: (classItem: any, date: string, status: string) => void;
  setSelectedClass: (classItem: any) => void;
  setShowSubjectModal: (show: boolean) => void;
  analyticsData: any;
  openCustomClassModal: (dateStr?: string) => void;
  announcements: any[];
}

export default function DashboardView({
  user,
  currentDate,
  todayClasses,
  todayVacation,
  toggleAttendance,
  setSelectedClass,
  setShowSubjectModal,
  analyticsData,
  openCustomClassModal,
  announcements
}: DashboardViewProps) {
  const userColor = user?.color || '#2b6cb0';
  const vacationType = todayVacation?.type || null;

  // Announcements visibility toggle (local UI state only)
  const [showAnnouncements, setShowAnnouncements] = useState(true);

  return (
    <div className="notebook-binder">
      {/* Announcements Banner */}
      {announcements.length > 0 && showAnnouncements && (
        <div style={{ marginBottom: '1rem', width: '100%' }}>
          {announcements.slice(0, 3).map(a => (
            <div key={a.id} className="wobbly-box" style={{ padding: '0.6rem 1rem', marginBottom: '0.5rem', background: '#fffff0', borderLeft: '6px solid #d69e2e' }}>
              <div className="flex-between">
                <div className="flex-row" style={{ gap: '0.3rem' }}>
                  <Megaphone size={14} style={{ color: '#d69e2e' }} />
                  <span className="sketchy-heading" style={{ fontSize: '0.95rem' }}>{a.title}</span>
                </div>
                {a.expiresAt && <span className="handwritten" style={{ fontSize: '0.75rem', color: '#718096' }}>Expires: {a.expiresAt}</span>}
              </div>
              <p className="handwritten" style={{ fontSize: '0.9rem', color: '#4a5568', marginTop: '0.2rem' }}>{a.body}</p>
            </div>
          ))}
          {announcements.length > 3 && (
            <p className="handwritten" style={{ fontSize: '0.8rem', color: '#718096', textAlign: 'center' }}>+{announcements.length - 3} more announcements</p>
          )}
        </div>
      )}

      {/* LEFT PAGE: TODAY'S CLASSES */}
      <div className="notebook-page paper-lined">
        <div className="tape-decor"></div>
        
        <div className="flex-between mb-4 flex-wrap mobile-stack" style={{ gap: '0.8rem' }}>
          <div>
            <span className="highlight-yellow handwritten" style={{ fontSize: '1.2rem', fontWeight: 'bold' }}>
              {user?.courseName || 'No Course Tag Set'}
            </span>
            <h2 className="sketchy-heading" style={{ fontSize: '1.6rem', marginTop: '0.4rem', color: userColor }}>
              📌 Today&apos;s Schedule
            </h2>
          </div>
          <div className="mobile-stack" style={{ textAlign: 'right' }}>
            <p className="handwritten" style={{ fontSize: '1.1rem' }}>Today&apos;s Date</p>
            <p className="sketchy-heading" style={{ fontSize: '0.9rem', color: '#718096' }}>{currentDate}</p>
          </div>
        </div>

        {/* Today's Classes List */}
        <div className="mt-4" style={{ minHeight: '300px' }}>
          <div className="flex-between mb-4" style={{ borderBottom: '1px dashed var(--ink-charcoal)', paddingBottom: '0.5rem', flexWrap: 'wrap', gap: '0.5rem' }}>
            <span className="handwritten" style={{ fontSize: '1.2rem', color: '#4a5568', fontWeight: 'bold' }}>Today&apos;s Sessions</span>
            <button 
              onClick={() => openCustomClassModal(currentDate)}
              className="sketchy-btn sketchy-btn-accent"
              style={{ fontSize: '0.8rem', padding: '0.2rem 0.5rem', boxShadow: '1.5px 2px 0px var(--ink-charcoal)' }}
            >
              + Add Custom Class
            </button>
          </div>

          {vacationType === 'VACATION' ? (
            <div style={{ padding: '2rem 1rem', textDecoration: 'none', textAlign: 'center' }}>
              <p className="handwritten" style={{ fontSize: '2rem', color: '#c53030' }}>🎉 Vacation Day!</p>
              <p className="handwritten" style={{ fontSize: '1.3rem', color: '#4a5568' }}>
                All classes are cancelled for today: <strong>{todayVacation?.description || 'Holiday'}</strong>
              </p>
            </div>
          ) : vacationType === 'ABSENT_DAY' ? (
            <div style={{ padding: '2rem 1rem', textAlign: 'center' }}>
              <p className="handwritten" style={{ fontSize: '2.0rem', color: '#9b2c2c' }}>🤒 Sick Day (Full-Day Absent)</p>
              <p className="handwritten" style={{ fontSize: '1.3rem', color: '#4a5568' }}>
                All scheduled classes are marked absent: <strong>{todayVacation?.description || 'Absent'}</strong>
              </p>
            </div>
          ) : todayClasses.length === 0 ? (
            <p className="handwritten" style={{ fontSize: '1.5rem', color: '#718096', textAlign: 'center', padding: '3rem 0' }}>
              No classes scheduled for today.
            </p>
          ) : (
            <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
              {todayClasses.map((c: any) => (
                <div 
                  key={c.id} 
                  className="wobbly-box flex-between mobile-class-card" 
                  style={{ 
                    borderLeft: `8px solid ${userColor}`, 
                    background: '#ffffff',
                    padding: '0.8rem 1.2rem',
                    cursor: 'pointer'
                  }}
                  onClick={() => {
                    setSelectedClass(c);
                    setShowSubjectModal(true);
                  }}
                >
                  <div style={{ flex: 1, marginRight: '1rem' }}>
                    <div className="flex-row">
                      <span className="sketchy-heading" style={{ fontSize: '1rem', fontWeight: 'bold' }}>{c.course.subjectCode}</span>
                      {c.group && <span className="highlight-yellow handwritten" style={{ fontSize: '1rem' }}>({c.group})</span>}
                      {c.status === 'RESCHEDULED' && <span className="highlight-pink handwritten" style={{ fontSize: '0.9rem', color: '#c05621' }}>Rescheduled</span>}
                      {c.status === 'CANCELLED' && <span className="highlight-pink handwritten" style={{ fontSize: '0.9rem', color: '#718096' }}>Cancelled</span>}
                      {c.description && c.description.startsWith('[Admin]') && (
                        <span style={{ display: 'inline-flex', alignItems: 'center', gap: '0.1rem', fontSize: '0.65rem', padding: '0.1rem 0.3rem', borderRadius: '3px', backgroundColor: '#fed7d7', color: '#9b2c2c' }}>
                          <AlertTriangle size={8} /> Admin Override
                        </span>
                      )}
                    </div>
                    <p className="handwritten" style={{ fontSize: '1.3rem', color: '#4a5568', marginTop: '0.1rem' }}>{c.course.subjectName}</p>
                    <div className="flex-row mt-4" style={{ fontSize: '0.9rem', color: '#718096', flexWrap: 'wrap', gap: '0.3rem' }}>
                      <span className="flex-row"><Clock size={12} /> {c.startTime} - {c.endTime}</span>
                      <span className="flex-row"><MapPin size={12} /> Room {c.room || 'TBA'}</span>
                    </div>

                    {/* Class Description Note */}
                    {c.description && (
                      <p 
                        className="handwritten" 
                        style={{ 
                          fontSize: '0.95rem', 
                          margin: '0.4rem 0 0 0', 
                          padding: '0.2rem 0.5rem', 
                          background: '#fef08a', 
                          borderRadius: '4px',
                          borderLeft: '3px solid #d97706',
                          display: 'inline-block'
                        }}
                      >
                        📝 Note: {c.description}
                      </p>
                    )}
                  </div>

                  {/* Log Attendance Directly */}
                  <div className="flex-row mobile-attendance-row" onClick={(e) => e.stopPropagation()}>
                    <button 
                      onClick={() => toggleAttendance(c, currentDate, 'PRESENT')}
                      className={`sketchy-btn mobile-touch-target ${c.attendanceStatus === 'PRESENT' ? 'class-status-present' : ''}`}
                      style={{ padding: '0.3rem 0.6rem', border: '1px solid #718096', boxShadow: 'none' }}
                      title="Mark Present"
                      disabled={c.status === 'CANCELLED'}
                    >
                      <Check size={14} />
                    </button>
                    <button 
                      onClick={() => toggleAttendance(c, currentDate, 'ABSENT')}
                      className={`sketchy-btn mobile-touch-target ${c.attendanceStatus === 'ABSENT' ? 'class-status-absent' : ''}`}
                      style={{ padding: '0.3rem 0.6rem', border: '1px solid #718096', boxShadow: 'none' }}
                      title="Mark Absent"
                      disabled={c.status === 'CANCELLED'}
                    >
                      <X size={14} />
                    </button>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>

        {/* Overall Attendance Footer */}
        <div style={{ marginTop: '3rem', borderTop: '2px dashed var(--ink-charcoal)', paddingTop: '1.5rem' }}>
          <div className="flex-between">
            <span className="sketchy-heading" style={{ fontSize: '1.1rem' }}>Overall Attendance</span>
            <span className="highlight-green handwritten" style={{ fontSize: '1.4rem', fontWeight: 'bold' }}>
              {analyticsData?.summary?.overallPercentage !== undefined ? `${analyticsData.summary.overallPercentage}%` : '100%'}
            </span>
          </div>
        </div>
      </div>

      {/* CENTER SPIRAL BINDER RINGS */}
      <div className="notebook-spiral">
        <div className="spiral-ring"></div>
        <div className="spiral-ring"></div>
        <div className="spiral-ring"></div>
        <div className="spiral-ring"></div>
        <div className="spiral-ring"></div>
        <div className="spiral-ring"></div>
        <div className="spiral-ring"></div>
        <div className="spiral-ring"></div>
        <div className="spiral-ring"></div>
        <div className="spiral-ring"></div>
      </div>

      {/* RIGHT PAGE: USER QUICK STATS & PROFILE */}
      <div className="notebook-page paper-lined">
        <div className="tape-decor"></div>

        <div className="flex-between mb-4 flex-wrap mobile-stack" style={{ gap: '0.8rem' }}>
          <div>
            <span className="highlight-yellow handwritten" style={{ fontSize: '1.2rem', fontWeight: 'bold' }}>
              Student Profile Sheet
            </span>
            <h2 className="sketchy-heading" style={{ fontSize: '1.6rem', marginTop: '0.4rem', color: userColor }}>
              🧑‍🎓 {user?.name || 'Academic Record'}
            </h2>
          </div>
        </div>

        {/* User profile information card */}
        <div className="wobbly-box mt-4" style={{ background: '#ffffff', padding: '1.2rem' }}>
          <div className="tape-decor-angle"></div>
          <h3 className="sketchy-heading" style={{ fontSize: '1rem', marginBottom: '0.8rem', color: '#4a5568' }}>
            📋 Academic Registration Tags
          </h3>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '0.8rem' }} className="handwritten mobile-profile-info">
            <div className="flex-row" style={{ fontSize: '1.1rem' }}>
              <GraduationCap size={16} /> <strong>University:</strong> {user?.university || 'Not specified (Set in Profile Settings)'}
            </div>
            <div className="flex-row" style={{ fontSize: '1.1rem' }}>
              <BookOpen size={16} /> <strong>Course Name:</strong> {user?.courseName || 'Not specified (Set in Profile Settings)'}
            </div>
            <div className="flex-row" style={{ fontSize: '1.1rem' }}>
              <Calendar size={16} /> <strong>Course Start Date:</strong> {user?.courseStartDate || '2026-01-01'}
            </div>
            <div className="flex-row" style={{ fontSize: '1.1rem' }}>
              <Award size={16} /> <strong>Role Account:</strong> {user?.role ? user.role.toUpperCase() : 'USER'}
            </div>
          </div>
        </div>

        {/* Attendance statistics widgets */}
        <div style={{ marginTop: '2.5rem' }}>
          <h3 className="sketchy-heading mb-4" style={{ fontSize: '1.1rem' }}>📊 Attendance Scorecard</h3>
          {analyticsData ? (
            <div className="analytics-summary-grid" style={{ gridTemplateColumns: 'repeat(2, 1fr)', gap: '1rem' }}>
              <div className="wobbly-box" style={{ padding: '0.8rem', textAlign: 'center', background: '#f0fff4' }}>
                <p className="handwritten" style={{ fontSize: '1rem' }}>Attendance Rate</p>
                <p className="sketchy-heading" style={{ fontSize: '1.6rem', color: '#2f855a' }}>
                  {analyticsData.summary?.overallPercentage || 100}%
                </p>
              </div>
              <div className="wobbly-box" style={{ padding: '0.8rem', textAlign: 'center', background: '#ebf8ff' }}>
                <p className="handwritten" style={{ fontSize: '1rem' }}>Sessions Held</p>
                <p className="sketchy-heading" style={{ fontSize: '1.6rem', color: '#2b6cb0' }}>
                  {analyticsData.summary?.totalClassesHeld || 0}
                </p>
              </div>
              <div className="wobbly-box" style={{ padding: '0.8rem', textAlign: 'center', background: '#f0f4f8' }}>
                <p className="handwritten" style={{ fontSize: '1rem' }}>Present Count</p>
                <p className="sketchy-heading" style={{ fontSize: '1.6rem', color: '#4a5568' }}>
                  {analyticsData.summary?.totalPresent || 0}
                </p>
              </div>
              <div className="wobbly-box" style={{ padding: '0.8rem', textAlign: 'center', background: '#fff5f5' }}>
                <p className="handwritten" style={{ fontSize: '1rem' }}>Absent Count</p>
                <p className="sketchy-heading" style={{ fontSize: '1.6rem', color: '#c53030' }}>
                  {analyticsData.summary?.totalAbsent || 0}
                </p>
              </div>
            </div>
          ) : (
            <p className="handwritten" style={{ textAlign: 'center', color: '#718096', padding: '1rem 0' }}>No attendance history loaded.</p>
          )}
        </div>

        {/* Motivational handwritten note */}
        <div style={{ marginTop: '2rem', borderTop: '2px dashed var(--ink-charcoal)', paddingTop: '1.5rem', textAlign: 'center' }}>
          <p className="handwritten highlight-yellow" style={{ fontSize: '1.1rem', transform: 'rotate(-1deg)', display: 'inline-block', padding: '0.3rem 1rem' }}>
            ✏️ Keep tracking! Consistent attendance leads to academic excellence. 🚀
          </p>
        </div>
      </div>
    </div>
  );
}
```
