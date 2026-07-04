# Research Methodology

## Experimental Design

### Objective
Compare A*, Dijkstra, and RRT pathfinding algorithms for Mobile Charging Vehicle routing in Wireless Sensor Networks under controlled conditions.

---

## Environment Configuration

### Grid Setup
- **Dimensions:** 100m × 100m
- **Cell Structure:** 10×10 grid (100 cells total)
- **Cell Size:** 10m × 10m per cell

### Node Placement
- **Distribution:** Uniform random
- **Seeding:** Fixed seeds (100, 101, 102) for reproducibility
- **Network Sizes Tested:** 10, 25, 50, 100 nodes

### Obstacle Configuration
- **Obstacle Count:** 15 obstacles per test
- **Obstacle Density:** 15% of total grid cells
- **Scenarios:** No obstacles (baseline) + With random obstacles (realistic)

---

## Algorithm Parameters

### A* Algorithm
- Evaluation Function: f(n) = g(n) + h(n)
- Heuristic: Euclidean distance
- Step Size: 5 meters
- Goal Threshold: 5 meters

### Dijkstra Algorithm
- Evaluation Function: f(n) = g(n) only
- Heuristic: None (uniform-cost search)
- Step Size: 5 meters
- Goal Threshold: 5 meters

### RRT Algorithm
- Goal Bias: 20%
- Iteration Limit: 500 per segment
- Step Size: 5 meters

---

## Performance Metrics

1. **Path Length (meters)** - Lower is better
2. **Computation Time (milliseconds)** - Lower is better
3. **Efficiency Score** - Path Length ÷ Computation Time (Higher is better)

---

## Experimental Procedure

Test Configuration: 10, 25, 50, 100 nodes × 2 scenarios × 3 algorithms × 3 trials = 72 tests

Results are reproducible with fixed random seeds (100, 101, 102).

---

## Conclusion

This methodology enables rigorous, reproducible comparison of pathfinding algorithms for WRSN MCV routing.
