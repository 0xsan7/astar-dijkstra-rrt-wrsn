# Path Planning for Wireless Rechargeable Sensor Networks

Research internship work at **National Institute of Technology Goa (NIT Goa)** by **Santiago Jerald**, exploring A*, Dijkstra and RRT for mobile charging vehicle navigation in wireless rechargeable sensor networks (WRSNs).

## Scope

This repository preserves the original internship implementation, methodology notes, recorded measurements and graphs. It documents simulation-based exploration of route planning; it does not report hardware deployment or establish general algorithm superiority.

The later horizon-aware charging scheduling study, unpublished manuscript, associated source code and experimental evidence are maintained separately in a private repository while the paper is under preparation.

## Repository structure

| Path | Contents |
| --- | --- |
| `code/` | Original internship path-planning scripts |
| `docs/` | Historical methodology, results and analysis notes |
| `results/data/` | Recorded internship measurements |
| `results/graphs/` | Internship plots |

## Interpretation of historical results

The scripts and records are retained as internship research artifacts. Later review identified limitations in the legacy implementations and experimental interpretations. The original observations do not establish linear A* scaling, exponential Dijkstra complexity, globally optimal continuous paths or general real-time suitability of RRT. Timing depends on the implementation, workload and execution environment.

## Running the scripts

Review the selected script and its input paths in `code/` before running it. Use an isolated Python environment and the dependencies actually imported by that script. No universal runner or clean-environment test guarantee is claimed for this historical collection.

## Research status and attribution

This is a record of exploratory internship work, not an accepted publication. Consult the retained license and source attributions for reuse terms. Institutional endorsement and additional authorship are not implied.
