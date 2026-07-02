import numpy as np
import json
import csv
from grid_base import GridBase
from algorithm_astar import AStarAlgorithm
from algorithm_dijkstra import DijkstraAlgorithm
from algorithm_rrt import RRTAlgorithm

class AlgorithmComparison:
    """
    Comprehensive testing framework for all three algorithms
    """
    
    def __init__(self):
        self.results = {}
        self.node_counts = [10, 25, 50, 100]
        self.num_trials = 3
    
    def run_full_comparison(self):
        """Run complete comparison"""
        
        print("=" * 70)
        print("COMPREHENSIVE PATHFINDING ALGORITHM COMPARISON")
        print("=" * 70)
        
        for node_count in self.node_counts:
            print("\n" + "=" * 70)
            print("Testing with " + str(node_count) + " nodes")
            print("=" * 70)
            
            print("\nTest 1: WITHOUT OBSTACLES")
            print("-" * 70)
            no_obs_results = self.test_configuration(node_count, obstacle_count=0)
            
            print("\nTest 2: WITH RANDOM OBSTACLES")
            print("-" * 70)
            with_obs_results = self.test_configuration(node_count, obstacle_count=15)
            
            self.results[node_count] = {
                "no_obstacles": no_obs_results,
                "with_obstacles": with_obs_results
            }
    
    def test_configuration(self, node_count, obstacle_count):
        """Test one configuration"""
        
        results_per_algorithm = {}
        
        algorithms = [
            ("A*", AStarAlgorithm),
            ("RRT", RRTAlgorithm)
        ]
        
        # Add Dijkstra only for small node counts
        if node_count <= 25:
            algorithms.insert(1, ("Dijkstra", DijkstraAlgorithm))
        
        for algo_name, AlgoClass in algorithms:
            print("\nTesting " + algo_name + " algorithm...")
            
            distances = []
            times = []
            
            for trial in range(self.num_trials):
                grid = GridBase(grid_size=10, area_size=100, 
                               num_nodes=node_count, seed=trial + 100)
                
                if obstacle_count > 0:
                    grid.add_random_obstacles(obstacle_count=obstacle_count, seed=trial)
                
                algorithm = AlgoClass(grid)
                result = algorithm.visit_all_nodes()
                
                distances.append(result.distance)
                times.append(result.computation_time)
            
            mean_distance = np.mean(distances)
            std_distance = np.std(distances)
            mean_time = np.mean(times)
            std_time = np.std(times)
            
            efficiency = mean_distance / mean_time if mean_time > 0 else 0
            
            results_per_algorithm[algo_name] = {
                "mean_distance": mean_distance,
                "std_distance": std_distance,
                "mean_time": mean_time,
                "std_time": std_time,
                "efficiency": efficiency,
                "trials": distances
            }
            
            print("  Mean distance: {:.1f}m (std: {:.1f}m)".format(mean_distance, std_distance))
            print("  Mean time: {:.2f}ms (std: {:.2f}ms)".format(mean_time, std_time))
            print("  Efficiency: {:.2f}".format(efficiency))
        
        return results_per_algorithm
    
    def print_summary(self):
        """Print summary of all results"""
        
        print("\n\n" + "=" * 70)
        print("SUMMARY: PATH LENGTH COMPARISON")
        print("=" * 70)
        
        print("\nWithout Obstacles:")
        print("-" * 70)
        self._print_table("no_obstacles")
        
        print("\n\nWith Random Obstacles:")
        print("-" * 70)
        self._print_table("with_obstacles")
    
    def _print_table(self, scenario):
        """Print comparison table"""
        
        print("{:<10} {:<15} {:<15} {:<15}".format(
            "Nodes", "A*", "Dijkstra", "RRT"))
        print("-" * 70)
        
        for node_count in self.node_counts:
            if node_count not in self.results:
                continue
            
            results = self.results[node_count][scenario]
            
            astar_dist = results["A*"]["mean_distance"]
            dijkstra_dist = results.get("Dijkstra", {}).get("mean_distance", 0)
            rrt_dist = results["RRT"]["mean_distance"]
            
            if dijkstra_dist > 0:
                print("{:<10} {:<15.1f} {:<15.1f} {:<15.1f}".format(
                    node_count, astar_dist, dijkstra_dist, rrt_dist))
            else:
                print("{:<10} {:<15.1f} {:<15} {:<15.1f}".format(
                    node_count, astar_dist, "N/A", rrt_dist))
    
    def save_results_csv(self):
        """Save results to CSV"""
        
        csv_file = "../results/data/results_summary.csv"
        
        with open(csv_file, 'w', newline='') as f:
            writer = csv.writer(f)
            
            writer.writerow(["Node Count", "Scenario", "Algorithm", 
                           "Mean Distance (m)", "Std Distance (m)",
                           "Mean Time (ms)", "Std Time (ms)", "Efficiency"])
            
            for node_count in self.node_counts:
                if node_count not in self.results:
                    continue
                
                for scenario in ["no_obstacles", "with_obstacles"]:
                    results = self.results[node_count][scenario]
                    
                    for algo_name in ["A*", "Dijkstra", "RRT"]:
                        if algo_name not in results:
                            continue
                            
                        algo_results = results[algo_name]
                        
                        writer.writerow([
                            node_count,
                            scenario,
                            algo_name,
                            "{:.2f}".format(algo_results["mean_distance"]),
                            "{:.2f}".format(algo_results["std_distance"]),
                            "{:.2f}".format(algo_results["mean_time"]),
                            "{:.2f}".format(algo_results["std_time"]),
                            "{:.2f}".format(algo_results["efficiency"])
                        ])
        
        print("\nResults saved to: " + csv_file)
    
    def save_results_json(self):
        """Save detailed results to JSON"""
        
        json_file = "../results/data/detailed_results.json"
        
        with open(json_file, 'w') as f:
            json.dump(self.results, f, indent=2)
        
        print("Detailed results saved to: " + json_file)


if __name__ == "__main__":
    comparison = AlgorithmComparison()
    comparison.run_full_comparison()
    comparison.print_summary()
    comparison.save_results_csv()
    comparison.save_results_json()
    
    print("\n" + "=" * 70)
    print("TESTING COMPLETE")
    print("=" * 70)
