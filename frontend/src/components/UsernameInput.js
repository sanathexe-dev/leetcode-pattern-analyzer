import React, { useState } from "react";

function UsernameInput({ onSubmit, disabled }) {
  const [username, setUsername] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault(); 
    if (username.trim()) {
      onSubmit(username.trim());
    }
  };

  return (
    <form className="input-wrapper" onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="LeetCode Username..."
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        disabled={disabled}
      />
      <button type="submit" disabled={disabled || !username.trim()}>
        Analyze
      </button>
    </form>
  );
}

export default UsernameInput;