import React, { useState } from 'react';

function Login({ onLogin }) {
  const [user, setUser] = useState('');
  const [pass, setPass] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (user === 'User' && pass === 'user123') {
      onLogin(); // Avisamos al padre que el login fue exitoso
    } else {
      alert('Credenciales incorrectas (User / user123)');
    }
  };

  return (
    <div className="login-container">
      <form className="login-card" onSubmit={handleSubmit}>
        <h2>Acceso al Sistema</h2>
        <input 
          type="text" 
          placeholder="Usuario" 
          value={user}
          onChange={e => setUser(e.target.value)} 
        />
        <input 
          type="password" 
          placeholder="Contraseña" 
          value={pass}
          onChange={e => setPass(e.target.value)} 
        />
        <button type="submit">Entrar</button>
      </form>
    </div>
  );
}

export default Login;