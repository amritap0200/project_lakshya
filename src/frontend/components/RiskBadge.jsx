import React from 'react';
import en from '../localization/phrases_en.json';
import kn from '../localization/phrases_kn.json';

/**
 * RiskBadge
 * Displays the bilingual risk classification card.
 * Props: score (object from /analyze), lang ('en' | 'kn')
 */
export default function RiskBadge({ score, lang }) {
  if (!score) return null;
  const phrases = lang === 'kn' ? kn : en;
  const label   = score.label || 'LOW RISK';
  const data    = phrases[label] || phrases['LOW RISK'];

  return (
    <div style={{
      border:       `2px solid ${score.color}`,
      borderRadius: 8,
      padding:      20,
      marginTop:    20,
      maxWidth:     600,
    }}>
      <div style={{ fontSize: 22, fontWeight: 'bold', color: score.color }}>
        {data.badge}
      </div>
      <div style={{ fontSize: 32, fontWeight: 'bold', margin: '8px 0' }}>
        {score.score}/100
      </div>
      <p style={{ margin: '8px 0' }}>{data.summary}</p>
      <p style={{ fontSize: 12, opacity: 0.7 }}>{data.fir_note}</p>
    </div>
  );
}
