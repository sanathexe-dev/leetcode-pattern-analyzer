import { useState } from "react";
import UsernameInput from "./components/UsernameInput";
import Results from "./components/Results";
import { analyzeUser } from "./services/api";
import "./App.css";

function App() {
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleAnalyze = async (username) => {
    setLoading(true);
    setResult(null); 
    const data = await analyzeUser(username);
    setResult(data);
    setLoading(false);
  };

  return (
    <div className="app-container">
      <div className="blob"></div>

      {/* TOP STATS BAR */}
      {!loading && result && (
        <div className="top-stats-bar">
          {/* LEFT SIDE: World Rank */}
          <div className="stat-box glass">
            <span className="label">World Rank</span>
            <span className="value">#{result.ranking?.toLocaleString()}</span>
          </div>

          {/* RIGHT SIDE: Total & Difficulty */}
          <div className="stat-box glass">
            <div className="difficulty-row">
              <div className="diff total-display">
                <span className="label">TOTAL</span> 
                <span className="total-count">{result.total_solved || 0}</span>
              </div>
              
              <div className="divider">|</div>

              <div className="diff easy"><span>E</span> {result.solved?.Easy || 0}</div>
              <div className="diff med"><span>M</span> {result.solved?.Medium || 0}</div>
              <div className="diff hard"><span>H</span> {result.solved?.Hard || 0}</div>
            </div>
          </div>
        </div>
      )}

      <header className="glass-header">
        <h1>LeetCode <span className="text-gradient">Pattern Analyzer</span></h1>
        <p className="subtitle">Identify your gaps. Master the patterns.</p>
        <UsernameInput onSubmit={handleAnalyze} disabled={loading} />
      </header>

      <main className="content">
        {loading ? (
          <div className="loader-container">
            <div className="spinner"></div>
            <p>Scanning LeetCode profile...</p>
          </div>
        ) : (
          result && <Results data={result} />
        )}
      </main>
    </div>
  );
}

export default App;