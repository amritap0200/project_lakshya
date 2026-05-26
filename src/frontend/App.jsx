import React, { useState } from 'react';
import RiskBadge from './components/RiskBadge';
import ClusterGraph from './components/ClusterGraph';

export default function App() {
  const [file, setFile]       = useState(null);
  const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(false);
  const [lang, setLang]       = useState('en'); // 'en' | 'kn'

  const handleAnalyze = async () => {
    if (!file) return;
    setLoading(true);
    const form = new FormData();
    form.append('file', file);
    const res  = await fetch('http://localhost:8000/analyze', { method: 'POST', body: form });
    const data = await res.json();
    setResults(data);
    setLoading(false);
  };

  return (
    <div style={{ padding: 40, fontFamily: 'monospace', background: '#0a0e1a', color: '#e8eaf6', minHeight: '100vh' }}>
      <h1>🔍 Project LAKSHYA</h1>
      <p>APK Forensic Triage — CIDECODE 2026</p>

      {!results ? (
        <div>
          <input type="file" accept=".apk" onChange={e => setFile(e.target.files[0])} />
          <button onClick={handleAnalyze} disabled={!file || loading} style={{ marginLeft: 12 }}>
            {loading ? 'Analyzing...' : 'Run Analysis'}
          </button>
        </div>
      ) : (
        <div>
          <button onClick={() => setLang(lang === 'en' ? 'kn' : 'en')}>
            Switch to {lang === 'en' ? 'ಕನ್ನಡ' : 'English'}
          </button>
          <RiskBadge score={results.score} lang={lang} />
          <ClusterGraph cluster={results.cluster} />
          {/* TODO: add BehaviorTimeline, DNAMatchCard, FIRExportButton components */}
          <button onClick={() => setResults(null)} style={{ marginTop: 24 }}>Analyze another</button>
        </div>
      )}
    </div>
  );
}
