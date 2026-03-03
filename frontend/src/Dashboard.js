import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Dashboard({ onLogout }) {
  const [input, setInput] = useState('');
  
  // Persistencia de datos en el navegador
  const [results, setResults] = useState(() => {
    const saved = localStorage.getItem('spam_results');
    return saved ? JSON.parse(saved) : [];
  });
  
  const [stats, setStats] = useState(() => {
    const saved = localStorage.getItem('spam_stats');
    return saved ? JSON.parse(saved) : { total: 0, spam: 0, ham: 0 };
  });

  useEffect(() => {
    localStorage.setItem('spam_results', JSON.stringify(results));
    localStorage.setItem('spam_stats', JSON.stringify(stats));
  }, [results, stats]);

  const handleAnalyze = async () => {
    const lines = input.split('\n').filter(line => line.trim() !== '');
    for (const text of lines) {
      try {
        const response = await axios.post('http://localhost:8000/predict', { text });
        const data = response.data;
        setResults(prev => [data, ...prev]);
        setStats(prev => ({
          total: prev.total + 1,
          spam: data.resultado === 'Spam' ? prev.spam + 1 : prev.spam,
          ham: data.resultado === 'No Spam' ? prev.ham + 1 : prev.ham
        }));
      } catch (error) { console.error("Error API:", error); }
    }
    setInput('');
  };

  const clearHistory = () => {
    setResults([]);
    setStats({ total: 0, spam: 0, ham: 0 });
    localStorage.removeItem('spam_results');
    localStorage.removeItem('spam_stats');
  };

  return (
    <div className="container">
      <header style={{display: 'flex', justifyContent: 'space-between'}}>
        <h1>Panel de Control IA</h1>
        <button onClick={onLogout} className="btn-logout">Cerrar Sesión</button>
      </header>

      <div className="dashboard">
        <div className="card">Total: {stats.total}</div>
        <div className="card green">Ham: {stats.ham}</div>
        <div className="card red">Spam: {stats.spam}</div>
      </div>

      <main>
        <textarea 
          value={input} 
          onChange={(e) => setInput(e.target.value)}
          placeholder="Pega mensajes aquí..."
        />
        <div className="actions">
          <button onClick={handleAnalyze}>Analizar Ahora</button>
          <button onClick={clearHistory} className="btn-clear">Limpiar Todo</button>
        </div>

        <table>
          <thead>
            <tr><th>Mensaje</th><th>Resultado</th><th>Confianza</th></tr>
          </thead>
          <tbody>
            {results.map((res, i) => (
              <tr key={i}>
                <td>{res.mensaje}</td>
                <td><span className={res.resultado === 'Spam' ? 'tag-spam' : 'tag-ham'}>{res.resultado}</span></td>
                <td>{(res.confianza * 100).toFixed(2)}%</td>
              </tr>
            ))}
          </tbody>
        </table>
      </main>
    </div>
  );
}

export default Dashboard;