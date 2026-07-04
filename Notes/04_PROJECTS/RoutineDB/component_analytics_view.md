---
tags: [ui, component, analytics, stats, attendance, frontend]
---

# UI Component: Analytics View

This component manages the attendance scorecard dashboard and history logs rendered in `📊 Attendance Stats`, located at `src/components/AnalyticsView.tsx`. It provides forms to query statistics over custom ranges, breakdown rates per subject (flagging rates below 75% in pink highlight), and review paginated historic records.

- **File Link**: [AnalyticsView.tsx](file:///d:/02_CODE/04_TEST/Routine/src/components/AnalyticsView.tsx)
- **Backlinks**: [[index]], [[home_page]], [[DESIGN]], [[api_attendance]]

---

## 1. Props Schema

The component triggers query recalculations binding state models inside the main home route:

```typescript
interface AnalyticsViewProps {
  user: any;                                                       // User settings payload
  analyticsData: any;                                              // Statistics calculation dataset
  customRange: { start: string; end: string };                     // Current active query date range
  setCustomRange: (range: { start: string; end: string }) => void; // Range state setter
  handleCalculateCustom: (e: React.FormEvent) => void;              // Recalculate event submit handler
  isCalculatingCustom: boolean;                                    // Loading indicator state
  onLoadHistoryPage?: (page: number) => void;                      // Paginated history navigator
}
```

---

## 2. Key Interface Modules

### A. Date Range Period Form
- Renders start date and end date input selectors (defaulting to the current month range).
- Triggers `GET /api/attendance?startDate=...&endDate=...` to pull recalculations.

### B. Summary Scorecards
- Renders overall attendance percentage, total class instances held, count of present sessions, absent sessions, and cancelled sessions.

### C. Subject Breakdown Table
- Lists all active courses.
- Renders class stats per subject: held sessions, present counts, absent counts, and cancelled counts.
- **Academic Warning Rule**: If a subject's attendance rate falls below **75%**, the rate percentage cell background is highlighted using `.hl-pink` (red warning) instead of `.hl-green` (safe).

### D. Detailed History Logs (Collapsible)
- Users toggle a checkbox to expand the detailed chronological attendance log sheet.
- Supports client-side dropdown filtering by Course subject and Status (`PRESENT`, `ABSENT`, `CANCELLED`, `UNMARKED`).
- Coordinates paginated footer navigators (`Prev` and `Next` buttons) mapping to database query bounds.

---

## 3. Source Code

Here is the complete implementation of `src/components/AnalyticsView.tsx`:

```tsx
'use client';

import React, { useState } from 'react';

interface AnalyticsViewProps {
  user: any;
  analyticsData: any;
  customRange: { start: string; end: string };
  setCustomRange: (range: { start: string; end: string }) => void;
  handleCalculateCustom: (e: React.FormEvent) => void;
  isCalculatingCustom: boolean;
  onLoadHistoryPage?: (page: number) => void;
}

export default function AnalyticsView({
  user,
  analyticsData,
  customRange,
  setCustomRange,
  handleCalculateCustom,
  isCalculatingCustom,
  onLoadHistoryPage
}: AnalyticsViewProps) {
  const userColor = user?.color || '#2b6cb0';

  // Class history filters (client-side filtering of current page)
  const [historyFilterCourse, setHistoryFilterCourse] = useState<string>('all');
  const [historyFilterStatus, setHistoryFilterStatus] = useState<string>('all');
  const [showHistory, setShowHistory] = useState(false);

  // Get unique courses from history for filter dropdown
  const historyEntries = analyticsData?.classHistory || [];
  const uniqueCourses = Array.from(
    new Set(historyEntries.map((h: any) => h.courseId))
  ).map((courseId: any) => {
    const entry = historyEntries.find((h: any) => h.courseId === courseId);
    return { courseId, subjectCode: entry?.subjectCode, subjectName: entry?.subjectName };
  });

  // Apply client-side filters on the current page
  const filteredHistory = historyEntries.filter((h: any) => {
    if (historyFilterCourse !== 'all' && String(h.courseId) !== historyFilterCourse) return false;
    if (historyFilterStatus !== 'all' && h.status !== historyFilterStatus) return false;
    return true;
  });

  const pagination = analyticsData?.historyPagination;

  const statusColors: Record<string, { bg: string; color: string; label: string }> = {
    PRESENT: { bg: 'rgba(187, 247, 208, 0.6)', color: '#22543d', label: '✅ Present' },
    ABSENT: { bg: 'rgba(254, 202, 202, 0.6)', color: '#9b2c2c', label: '❌ Absent' },
    CANCELLED: { bg: 'rgba(226, 232, 240, 0.6)', color: '#718096', label: '🚫 Cancelled' },
    UNMARKED: { bg: 'rgba(254, 235, 200, 0.6)', color: '#975a16', label: '⏳ Unmarked' },
  };

  return (
    <div className="wobbly-box" style={{ background: '#ffffff', padding: '2rem' }}>
      <div className="analytics-header mb-6 mobile-stack">
        <div className="flex-row flex-wrap mobile-stack" style={{ gap: '0.8rem' }}>
          <h2 className="sketchy-heading" style={{ fontSize: '1.5rem', color: userColor }}>📊 Attendance Statistics</h2>
          <span className="highlight-yellow handwritten" style={{ fontSize: '1.1rem', fontWeight: 'bold' }}>
            {user?.name || 'My Record'}
          </span>
        </div>

        {/* Custom period query form */}
        <form onSubmit={handleCalculateCustom} className="range-picker-form wobbly-box mobile-stack" style={{ padding: '0.4rem 1rem', background: '#f7fafc', boxShadow: 'none' }}>
          <span className="handwritten" style={{ fontSize: '1.1rem' }}>From:</span>
          <input 
            type="date" 
            value={customRange.start} 
            onChange={(e) => setCustomRange({ ...customRange, start: e.target.value })}
            className="wobbly-input"
            style={{ width: '150px', padding: '0.2rem 0.4rem', fontSize: '1rem' }}
          />
          <span className="handwritten" style={{ fontSize: '1.1rem' }}>To:</span>
          <input 
            type="date" 
            value={customRange.end} 
            onChange={(e) => setCustomRange({ ...customRange, end: e.target.value })}
            className="wobbly-input"
            style={{ width: '150px', padding: '0.2rem 0.4rem', fontSize: '1rem' }}
          />
          <button type="submit" className="sketchy-btn sketchy-btn-accent" disabled={isCalculatingCustom}>
            {isCalculatingCustom ? 'Recalculating...' : 'Get Average'}
          </button>
        </form>
      </div>

      {analyticsData ? (
        <div>
          {/* Overall stats widgets */}
          <div className="analytics-summary-grid mb-4">
            <div className="wobbly-box" style={{ padding: '1rem', textAlign: 'center' }}>
              <p className="handwritten" style={{ fontSize: '1.1rem' }}>Overall Percentage</p>
              <p className="sketchy-heading" style={{ fontSize: 'clamp(1.3rem, 5vw, 1.8rem)', color: '#2f855a' }}>
                {analyticsData.summary.overallPercentage}%
              </p>
            </div>
            <div className="wobbly-box" style={{ padding: '1rem', textAlign: 'center' }}>
              <p className="handwritten" style={{ fontSize: '1.1rem' }}>Classes Held</p>
              <p className="sketchy-heading" style={{ fontSize: 'clamp(1.3rem, 5vw, 1.8rem)' }}>{analyticsData.summary.totalClassesHeld}</p>
            </div>
            <div className="wobbly-box" style={{ padding: '1rem', textAlign: 'center' }}>
              <p className="handwritten" style={{ fontSize: '1.1rem' }}>Total Present</p>
              <p className="sketchy-heading" style={{ fontSize: 'clamp(1.3rem, 5vw, 1.8rem)', color: '#2b6cb0' }}>{analyticsData.summary.totalPresent}</p>
            </div>
            <div className="wobbly-box" style={{ padding: '1rem', textAlign: 'center' }}>
              <p className="handwritten" style={{ fontSize: '1.1rem' }}>Total Absent</p>
              <p className="sketchy-heading" style={{ fontSize: 'clamp(1.3rem, 5vw, 1.8rem)', color: '#c53030' }}>{analyticsData.summary.totalAbsent}</p>
            </div>
            <div className="wobbly-box" style={{ padding: '1rem', textAlign: 'center' }}>
              <p className="handwritten" style={{ fontSize: '1.1rem' }}>Total Cancelled</p>
              <p className="sketchy-heading" style={{ fontSize: 'clamp(1.3rem, 5vw, 1.8rem)', color: '#718096' }}>{analyticsData.summary.totalCancelled}</p>
            </div>
          </div>

          {/* Subject Breakdown List */}
          <div className="wobbly-box" style={{ padding: '1.5rem' }}>
            <h3 className="sketchy-heading mb-4" style={{ fontSize: '1.2rem' }}>📚 Attendance Per Subject</h3>
            <div className="scroll-hint-x" style={{ overflowX: 'auto', width: '100%' }}>
              <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left', minWidth: '650px' }}>
                <thead>
                  <tr style={{ borderBottom: '2px solid var(--ink-charcoal)' }}>
                    <th style={{ padding: '0.6rem 0.4rem', fontFamily: 'var(--font-sketch)' }}>Code</th>
                    <th style={{ padding: '0.6rem 0.4rem', fontFamily: 'var(--font-sketch)' }}>Subject Name</th>
                    <th style={{ padding: '0.6rem 0.4rem', fontFamily: 'var(--font-sketch)' }}>Classes Held</th>
                    <th style={{ padding: '0.6rem 0.4rem', fontFamily: 'var(--font-sketch)' }}>Attended</th>
                    <th style={{ padding: '0.6rem 0.4rem', fontFamily: 'var(--font-sketch)' }}>Absent</th>
                    <th style={{ padding: '0.6rem 0.4rem', fontFamily: 'var(--font-sketch)' }}>Cancelled</th>
                    <th style={{ padding: '0.6rem 0.4rem', fontFamily: 'var(--font-sketch)' }}>Rate</th>
                  </tr>
                </thead>
                <tbody>
                  {analyticsData.subjects.map((s: any) => (
                    <tr key={s.courseId} style={{ borderBottom: '1px dashed #cbd5e0' }}>
                      <td style={{ padding: '0.8rem 0.4rem', fontWeight: 'bold' }}>{s.subjectCode}</td>
                      <td style={{ padding: '0.8rem 0.4rem' }} className="handwritten">{s.subjectName}</td>
                      <td style={{ padding: '0.8rem 0.4rem' }}>{s.held}</td>
                      <td style={{ padding: '0.8rem 0.4rem', color: '#2b6cb0' }}>{s.present}</td>
                      <td style={{ padding: '0.8rem 0.4rem', color: '#c53030' }}>{s.absent}</td>
                      <td style={{ padding: '0.8rem 0.4rem', color: '#718096' }}>{s.cancelled}</td>
                      <td style={{ padding: '0.8rem 0.4rem' }}>
                        <span 
                          className="highlight-green handwritten" 
                          style={{ 
                            fontSize: '1.1rem', 
                            fontWeight: 'bold',
                            backgroundColor: s.percentage < 75 ? 'rgba(254, 202, 202, 0.6)' : 'rgba(187, 247, 208, 0.6)',
                            color: s.percentage < 75 ? '#c53030' : '#22543d'
                          }}
                        >
                          {s.percentage}%
                        </span>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>

          {/* Collapsible History Logs list */}
          <div style={{ marginTop: '2.5rem' }}>
            <div style={{ display: 'flex', gap: '0.5rem', alignItems: 'center' }}>
              <input 
                type="checkbox" 
                id="showHistoryCheck" 
                checked={showHistory} 
                onChange={(e) => setShowHistory(e.target.checked)} 
                style={{ width: '16px', height: '16px', cursor: 'pointer' }}
              />
              <label htmlFor="showHistoryCheck" className="sketchy-heading" style={{ fontSize: '1.1rem', cursor: 'pointer' }}>
                🔍 Show Detailed Session Logs List
              </label>
            </div>

            {showHistory && (
              <div className="wobbly-box mt-4" style={{ padding: '1.5rem' }}>
                {/* Filters */}
                <div className="flex-between mb-4 flex-wrap mobile-stack" style={{ gap: '1rem', borderBottom: '1px dashed var(--ink-charcoal)', paddingBottom: '1rem' }}>
                  <div className="flex-row flex-wrap" style={{ gap: '0.8rem' }}>
                    <span className="handwritten" style={{ fontSize: '1.1rem' }}>Filter Subject:</span>
                    <select 
                      value={historyFilterCourse} 
                      onChange={(e) => setHistoryFilterCourse(e.target.value)}
                      className="wobbly-input" 
                      style={{ width: '160px', padding: '0.2rem', fontSize: '1rem', fontFamily: 'var(--font-hand)' }}
                    >
                      <option value="all">All Subjects</option>
                      {uniqueCourses.map((uc: any) => (
                        <option key={uc.courseId} value={String(uc.courseId)}>{uc.subjectCode}</option>
                      ))}
                    </select>

                    <span className="handwritten" style={{ fontSize: '1.1rem' }}>Status:</span>
                    <select 
                      value={historyFilterStatus} 
                      onChange={(e) => setHistoryFilterStatus(e.target.value)}
                      className="wobbly-input" 
                      style={{ width: '160px', padding: '0.2rem', fontSize: '1rem', fontFamily: 'var(--font-hand)' }}
                    >
                      <option value="all">All Statuses</option>
                      <option value="PRESENT">Present</option>
                      <option value="ABSENT">Absent</option>
                      <option value="CANCELLED">Cancelled</option>
                      <option value="UNMARKED">Unmarked</option>
                    </select>
                  </div>

                  {pagination && (
                    <span className="handwritten" style={{ fontSize: '1.1rem' }}>
                      Page {pagination.page} of {pagination.totalPages} ({pagination.totalCount} logs)
                    </span>
                  )}
                </div>

                {/* History Table */}
                <div style={{ overflowX: 'auto' }}>
                  <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left', minWidth: '600px' }}>
                    <thead>
                      <tr style={{ borderBottom: '2px solid var(--ink-charcoal)' }}>
                        <th style={{ padding: '0.6rem 0.4rem', fontFamily: 'var(--font-sketch)' }}>Date</th>
                        <th style={{ padding: '0.6rem 0.4rem', fontFamily: 'var(--font-sketch)' }}>Subject</th>
                        <th style={{ padding: '0.6rem 0.4rem', fontFamily: 'var(--font-sketch)' }}>Time Slot</th>
                        <th style={{ padding: '0.6rem 0.4rem', fontFamily: 'var(--font-sketch)' }}>Room</th>
                        <th style={{ padding: '0.6rem 0.4rem', fontFamily: 'var(--font-sketch)' }}>Log Status</th>
                      </tr>
                    </thead>
                    <tbody>
                      {filteredHistory.length === 0 ? (
                        <tr>
                          <td colSpan={5} className="handwritten" style={{ textAlign: 'center', padding: '2rem 0', color: '#718096' }}>
                            No matching session history entries.
                          </td>
                        </tr>
                      ) : (
                        filteredHistory.map((h: any, index: number) => (
                          <tr key={index} style={{ borderBottom: '1px dashed #cbd5e0' }}>
                            <td style={{ padding: '0.8rem 0.4rem', fontFamily: 'monospace' }}>{h.date}</td>
                            <td style={{ padding: '0.8rem 0.4rem' }}>
                              <strong>{h.subjectCode}</strong> <span className="handwritten" style={{ color: '#718096', fontSize: '0.95rem' }}>({h.subjectName})</span>
                            </td>
                            <td style={{ padding: '0.8rem 0.4rem' }}>{h.startTime} - {h.endTime}</td>
                            <td style={{ padding: '0.8rem 0.4rem' }}>{h.room || 'TBA'}</td>
                            <td style={{ padding: '0.8rem 0.4rem' }}>
                              <span 
                                className="handwritten" 
                                style={{ 
                                  padding: '0.2rem 0.5rem', 
                                  borderRadius: '4px',
                                  backgroundColor: statusColors[h.status]?.bg || '#edf2f7',
                                  color: statusColors[h.status]?.color || '#4a5568',
                                  fontWeight: 'bold'
                                }}
                              >
                                {statusColors[h.status]?.label || h.status}
                              </span>
                            </td>
                          </tr>
                        ))
                      )}
                    </tbody>
                  </table>
                </div>

                {/* Pagination Controls */}
                {pagination && pagination.totalPages > 1 && onLoadHistoryPage && (
                  <div className="flex-between mt-6">
                    <button 
                      onClick={() => onLoadHistoryPage(pagination.page - 1)}
                      disabled={pagination.page <= 1}
                      className="sketchy-btn"
                      style={{ padding: '0.3rem 0.8rem' }}
                    >
                      👈 Prev Page
                    </button>
                    <button 
                      onClick={() => onLoadHistoryPage(pagination.page + 1)}
                      disabled={pagination.page >= pagination.totalPages}
                      className="sketchy-btn"
                      style={{ padding: '0.3rem 0.8rem' }}
                    >
                      Next Page 👉
                    </button>
                  </div>
                )}
              </div>
            )}
          </div>
        </div>
      ) : (
        <p className="handwritten" style={{ textAlign: 'center', color: '#718096', padding: '2rem 0' }}>No statistics loaded.</p>
      )}
    </div>
  );
}
```
