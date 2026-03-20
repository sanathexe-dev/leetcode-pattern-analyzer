import React from 'react';
import { PieChart, Pie, Cell, ResponsiveContainer, BarChart, Bar, XAxis, YAxis, Tooltip } from 'recharts';

const StatsDashboard = ({ data }) => {
  // Mocking "Solved" data for the visual - in a real app, 
  // you'd pull this from the backend dataset
  const pieData = [
    { name: 'Easy', value: 40, color: '#00b8a3' },
    { name: 'Medium', value: 35, color: '#ffc01e' },
    { name: 'Hard', value: 25, color: '#ef4743' },
  ];

  const barData = data.weak_topics?.map(topic => ({
    name: topic,
    score: Math.floor(Math.random() * 40) + 10 // Representing your "weak" score
  }));

  return (
    <div className="stats-container">
      {/* Solved Problems Pie Chart */}
      <div className="card glass chart-card">
        <h4>Submission Distribution</h4>
        <ResponsiveContainer width="100%" height="100%">
          <PieChart>
            <Pie
              data={pieData}
              innerRadius={60}
              outerRadius={80}
              paddingAngle={5}
              dataKey="value"
            >
              {pieData.map((entry, index) => (
                <Cell key={`cell-${index}`} fill={entry.color} />
              ))}
            </Pie>
            <Tooltip />
          </PieChart>
        </ResponsiveContainer>
      </div>

      {/* Topic Strength Bar Chart */}
      <div className="card glass chart-card">
        <h4>Weak Topic Frequency</h4>
        <ResponsiveContainer width="100%" height="100%">
          <BarChart data={barData}>
            <XAxis dataKey="name" stroke="#94a3b8" fontSize={12} />
            <YAxis hide />
            <Tooltip cursor={{fill: 'transparent'}} />
            <Bar dataKey="score" fill="#38bdf8" radius={[4, 4, 0, 0]} />
          </BarChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
};

export default StatsDashboard;