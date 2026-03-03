import React, { useState } from 'react';
import Login from './Login';
import Dashboard from './Dashboard';
import './App.css';

function App() {
  // Verificamos si ya hay una sesión activa en el navegador
  const [isLoggedIn, setIsLoggedIn] = useState(() => {
    return localStorage.getItem('isLoggedIn') === 'true';
  });

  const loginUser = () => {
    setIsLoggedIn(true);
    localStorage.setItem('isLoggedIn', 'true');
  };

  const logoutUser = () => {
    setIsLoggedIn(false);
    localStorage.removeItem('isLoggedIn');
  };

  return (
    <div className="App">
      {isLoggedIn ? (
        <Dashboard onLogout={logoutUser} />
      ) : (
        <Login onLogin={loginUser} />
      )}
    </div>
  );
}

export default App;