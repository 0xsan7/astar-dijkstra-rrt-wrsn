# Comparative Analysis of Pathfinding Algorithms for MCV Routing in WRSN

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

A comprehensive comparative analysis of A*, Dijkstra, and RRT pathfinding algorithms for Mobile Charging Vehicle routing in Wireless Sensor Networks.

## Overview

This research evaluates three pathfinding algorithms across network sizes (10-100 nodes) with and without obstacles.

| Algorithm | Path Quality | Speed | Best For |
|-----------|-------------|-------|----------|
| A* | Optimal | 20-30ms | Production |
| Dijkstra | Optimal | 4-8 seconds | Theory |
| RRT | Suboptimal | <15ms | Real-time |

## Key Results

- **A*:** Shortest paths, scales linearly, optimal for WRSN
- **Dijkstra:** Optimal but exponential scaling, impractical beyond 25 nodes
- **RRT:** Fastest, suboptimal paths, suitable for real-time

## Repository Structure

astar-dijkstra-rrt-wrsn/
├── README.md
├── LICENSE
├── requirements.txt
├── RESEARCH_REPORT.pdf
├── code/
│   ├── grid_base.py
│   ├── algorithm_astar.py
│   ├── algorithm_dijkstra.py
│   ├── algorithm_rrt.py
│   ├── test_algorithms.py
│   └── generate_graphs.py
├── results/
│   ├── data/
│   │   ├── results_summary.csv
│   │   └── detailed_results.json
│   └── graphs/
│       ├── 01_path_length_no_obstacles_all_three.png
│       ├── 02_path_length_with_obstacles_all_three.png
│       ├── 03_dijkstra_vs_astar.png
│       ├── 04_computation_time_all.png
│       └── 05_efficiency_all_three.png
└── docs/
├── METHODOLOGY.md
└── RESULTS.md

## Quick Start

```bash
git clone https://github.com/0xsan7/astar-dijkstra-rrt-wrsn.git
cd astar-dijkstra-rrt-wrsn
pip install -r requirements.txt
cd code
python3 test_algorithms.py
```

## Documentation

- [RESEARCH_REPORT.pdf](./RESEARCH_REPORT.pdf) - Full research report
- [docs/METHODOLOGY.md](./docs/METHODOLOGY.md) - Research methodology
- [docs/RESULTS.md](./docs/RESULTS.md) - Detailed results analysis

## Key Findings

**A* is optimal for WRSN MCV routing.** It achieves shortest paths with practical computation times (< 50ms at 100 nodes) and scales linearly.

**Dijkstra is impractical.** While theoretically optimal, it requires 4+ seconds on 10 nodes and scales exponentially, making it unsuitable for real-time WRSN applications.

**RRT is best for real-time.** Extremely fast (< 14ms) but produces suboptimal paths (10-35% longer than A*).

## Technologies

- Python 3.8+
- NumPy, Matplotlib
- Custom grid-based implementation

## References

1. Hart, P. E., Nilsson, N. J., & Raphael, B. (1968). A formal basis for the heuristic determination of minimum cost paths.
2. Dijkstra, E. W. (1959). A note on two problems in connexion with graphs.
3. LaValle, S. M. (2006). Planning algorithms.
4. Shi, W., Zhang, Y., & Zhang, Q. (2021). Energy-efficient data gathering with autonomous vehicles in WRSN.

## License

MIT License - see LICENSE file

## Author

Santiago (0xsan7)  
Computer Science Student  
SRM University-AP  

Research Internship:  
NIT Goa, Department of Computer Science and Engineering  
Advisor: Dr. S Mini

Status: ongoing 
