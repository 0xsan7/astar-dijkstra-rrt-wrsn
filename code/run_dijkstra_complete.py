import numpy as np
import signal
from grid_base import GridBase
from algorithm_astar import AStarAlgorithm
from algorithm_dijkstra import DijkstraAlgorithm
from algorithm_rrt import RRTAlgorithm
import time

class TimeoutError(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutError("Timeout")

def run_with_timeout(func, timeout_seconds=60):
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(timeout_seconds)
    try:
        result = func()
        signal.alarm(0)
        return result
    except TimeoutError:
        return None

node_counts = [10, 25, 50, 100]
num_trials = 3
results = {}

for node_count in node_counts:
    print(f"\nTesting {node_count} nodes...")
    results[node_count] = {}
    
    for scenario in ["no_obstacles", "with_obstacles"]:
        results[node_count][scenario] = {}
        
        for algo_name, AlgoClass in [("A*", AStarAlgorithm), 
                                      ("Dijkstra", DijkstraAlgorithm), 
                                      ("RRT", RRTAlgorithm)]:
            distances = []
            times = []
            timed_out = False
            
            for trial in range(num_trials):
                grid = GridBase(grid_size=10, area_size=100, 
                               num_nodes=node_count, seed=trial+100)
                
                if scenario == "with_obstacles":
                    grid.add_random_obstacles(obstacle_count=15, seed=trial)
                
                algo = AlgoClass(grid)
                
                def run_algo():
                    return algo.visit_all_nodes()
                
                start = time.time()
                result = run_with_timeout(run_algo, timeout_seconds=120)
                elapsed = (time.time() - start) * 1000
                
                if result is None:
                    print(f"  {algo_name} TIMED OUT on {node_count} nodes")
                    timed_out = True
                    break
                
                distances.append(result.distance)
                times.append(result.computation_time)
            
            if not timed_out and distances:
                results[node_count][scenario][algo_name] = {
                    "mean_distance": np.mean(distances),
                    "std_distance": np.std(distances),
                    "mean_time": np.mean(times),
                    "std_time": np.std(times)
                }
                print(f"  {algo_name}: {np.mean(distances):.1f}m, {np.mean(times):.2f}ms")
            else:
                results[node_count][scenario][algo_name] = None
                print(f"  {algo_name}: TIMED OUT - recorded as N/A")

import json
with open("../results/data/complete_results.json", "w") as f:
    json.dump(results, f, indent=2)

print("\nDone! Results saved.")
