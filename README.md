# Comparative Analysis of Pathfinding Algorithms for Mobile Charging Vehicle Routing in Wireless Sensor Networks

## Abstract

This research compares three pathfinding algorithms for optimizing Mobile Charging Vehicle (MCV) trajectory planning in Wireless Sensor Networks (WRSN). The study evaluates A*, Dijkstra, and Rapidly-Exploring Random Tree (RRT) algorithms across multiple network sizes (10-150 nodes) with and without obstacle constraints.

## Research Objective

To determine which pathfinding algorithm provides optimal performance for MCV routing in WRSN, considering both path optimality and computational efficiency.

## Methodology

### Algorithms Evaluated

1. A* Algorithm: Goal-aware heuristic search
2. Dijkstra Algorithm: Systematic uniform-cost search
3. RRT: Rapidly-Exploring Random Tree

### Experimental Setup

- Grid: 100 x 100 meters (10 x 10 cells)
- Nodes: 10, 25, 50, 100, 150
- Scenarios: Without obstacles, With random obstacles
- Trials: 5 independent runs per configuration

## Installation

```bash
git clone https://github.com/0xsan7/astar-dijkstra-rrt-wrsn.git
cd astar-dijkstra-rrt-wrsn
pip install numpy matplotlib
```

## Usage

```bash
cd code
python3 algorithm_astar.py
python3 algorithm_dijkstra.py
python3 algorithm_rrt.py
python3 test_algorithms.py
python3 generate_graphs.py
```

## Author

Santiago (0xsan7)

## Institution

NIT Goa, Department of Computer Science and Engineering

## License

MIT License
