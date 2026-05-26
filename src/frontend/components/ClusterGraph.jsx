import React from 'react';

/**
 * ClusterGraph
 * Renders the NetworkX C2 infrastructure graph as an interactive SVG.
 * TODO: replace table stub with a proper force-directed graph
 *       (react-force-graph or D3 force simulation).
 * Props: cluster ({ nodes: [], edges: [] })
 */
export default function ClusterGraph({ cluster }) {
  if (!cluster || !cluster.nodes.length) return null;

  return (
    <div style={{ marginTop: 24 }}>
      <h3>C2 Infrastructure Cluster</h3>
      <table style={{ borderCollapse: 'collapse', fontSize: 12, width: '100%' }}>
        <thead>
          <tr>
            <th style={{ textAlign: 'left', padding: 6, borderBottom: '1px solid #333' }}>IOC</th>
            <th style={{ textAlign: 'left', padding: 6, borderBottom: '1px solid #333' }}>Type</th>
            <th style={{ textAlign: 'left', padding: 6, borderBottom: '1px solid #333' }}>Malicious</th>
          </tr>
        </thead>
        <tbody>
          {cluster.nodes.map(node => (
            <tr key={node.id}>
              <td style={{ padding: 6 }}>{node.id}</td>
              <td style={{ padding: 6 }}>{node.node_type}</td>
              <td style={{ padding: 6, color: node.malicious ? '#FF3B30' : '#34C759' }}>
                {node.malicious ? '⚠ YES' : '✓ NO'}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
      {/* TODO: render force-directed graph here */}
    </div>
  );
}
