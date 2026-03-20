function Results({ data }) {
  if (!data) return null;

  return (
    <div className="results-grid">
      <section className="card glass">
        <div className="card-header">
          <span className="icon">📉</span>
          <h3>Growth Areas</h3>
        </div>
        <div className="topic-tags">
          {data.weak_topics?.map((topic, i) => (
            <span key={i} className="tag-weak">{topic}</span>
          ))}
        </div>
      </section>

      <section className="card glass lg-col-2">
        <div className="card-header">
          <span className="icon">🚀</span>
          <h3>Next Challenges</h3>
        </div>
        <div className="problem-list">
          {data.recommendations?.map((prob, i) => (
            <div key={i} className="problem-item">
              <span className="prob-title">{prob}</span>
              <a 
                href={`https://leetcode.com/problems/${prob.toLowerCase().replace(/ /g, "-")}/`}
                target="_blank"
                rel="noreferrer"
                className="solve-btn"
              >
                Solve →
              </a>
            </div>
          ))}
        </div>
      </section>
    </div>
  );
}

export default Results;