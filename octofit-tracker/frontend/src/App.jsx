import React from 'react'

export default function App() {
  return (
    <div style={{ fontFamily: 'system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial', padding: 20 }}>
      <h1>OctoFit Tracker — Gym Teacher Dashboard</h1>
      <p>Welcome, Coach. Use the API at <code>/api/</code> to manage students, activities and teams.</p>
      <ul>
        <li>List students: GET /api/profiles/</li>
        <li>Log activity: POST /api/activities/</li>
        <li>Teams: GET /api/teams/</li>
        <li>Leaderboard: GET /api/teams/leaderboard/</li>
      </ul>
    </div>
  )
}
