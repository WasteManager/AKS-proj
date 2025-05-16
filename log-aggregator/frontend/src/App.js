import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [level, setLevel] = useState('');
  const [logs, setLogs] = useState([]);

  const searchLogs = async () => {
    const res = await axios.get(`/api/search`, { params: { level } });
    setLogs(res.data);
  };

  return (
    <div>
      <h1>Log Dashboard</h1>
      <input value={level} onChange={e => setLevel(e.target.value)} placeholder="Log level (e.g., INFO)" />
      <button onClick={searchLogs}>Search</button>
      <ul>
        {logs.map((log, idx) => (
          <li key={idx}>{log.timestamp} - {log.level}: {log.message}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
