import React, { useState } from 'react';
import axios from 'axios';
import './App.css'; // Aquí pondrás los estilos para que se vea como el mockup

function App() {
  const [input, setInput] = useState('');
  const [results, setResults] = useState([]);
  const [stats, setStats] = useState({ total: 0, spam: 0, ham: 0 });

  const handleAnalyze = async () => {
    // Dividimos por líneas para procesar varios mensajes (según el mockup)
    const lines = input.split('\n').filter(line => line.trim() !== '');
    
    for (const text of lines) {
      try {
        const response = await axios.post('http://localhost:8000/predict', { text });
        const data = response.data;

        // Actualizamos resultados (RI-02)
        setResults(prev => [data, ...prev]);

        // Actualizamos estadísticas del Dashboard (RI-05)
        setStats(prev => ({
          total: prev.total + 1,
          spam: data.resultado === 'Spam' ? prev.spam + 1 : prev.spam,
          ham: data.resultado === 'No Spam' ? prev.ham + 1 : prev.ham
        }));
      } catch (error) {
        console.error("Error analizando el mensaje:", error);
      }
    }
  };

  return (
    <div className="container">
      <header>
        <h1>SpamDetector v1.0</h1> {/* Basado en el Mockup [cite: 87] */}
      </header>

      <div className="dashboard">
        <div className="card">Total Analizados: {stats.total}</div>
        <div className="card green">No Spam: {stats.ham}</div>
        <div className="card red">Spam Detectado: {stats.spam}</div>
      </div>

      <main>
        <h3>Entrada de Mensajes</h3>
        <p>Pega varios mensajes (uno por línea) para analizarlos.</p>
        <textarea 
          value={input} 
          onChange={(e) => setInput(e.target.value)}
          placeholder="Escribe o pega aquí tus correos..."
        />
        <button onClick={handleAnalyze}>Clasificar Mensajes</button>

        <section className="results">
          <h3>Resultados del Análisis</h3>
          <table>
            <thead>
              <tr>
                <th>Mensaje</th>
                <th>Resultado</th>
                <th>Confianza (%)</th>
              </tr>
            </thead>
            <tbody>
              {results.map((res, index) => (
                <tr key={index}>
                  <td>{res.mensaje}</td>
                  <td className={res.resultado === 'Spam' ? 'tag-spam' : 'tag-ham'}>
                    {res.resultado}
                  </td>
                  <td>{res.confianza}%</td> {/* RI-03 [cite: 29] */}
                </tr>
              ))}
            </tbody>
          </table>
        </section>
      </main>
    </div>
  );
}

export default App;