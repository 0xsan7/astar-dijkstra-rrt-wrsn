import numpy as np
import json
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['font.family'] = 'serif'
rcParams['font.size'] = 11

class GraphGenerator:
    
    def __init__(self, results_file="../results/data/detailed_results.json"):
        with open(results_file, 'r') as f:
            self.results = json.load(f)
        self.node_counts = [10, 25, 50, 100]
    
    def generate_all_graphs(self):
        print("Generating comparison graphs...")
        self.graph_path_length_no_obstacles()
        self.graph_path_length_with_obstacles()
        self.graph_computation_time()
        self.graph_efficiency_comparison()
        print("All graphs generated successfully")
    
    def graph_path_length_no_obstacles(self):
        fig, ax = plt.subplots(figsize=(10, 6))
        
        astar_distances = []
        rrt_distances = []
        nodes = []
        
        for node_count in self.node_counts:
            node_count_str = str(node_count)
            if node_count_str not in self.results:
                continue
            results = self.results[node_count_str]["no_obstacles"]
            nodes.append(node_count)
            astar_distances.append(results["A*"]["mean_distance"])
            rrt_distances.append(results["RRT"]["mean_distance"])
        
        ax.plot(nodes, astar_distances, marker="o", linewidth=2, markersize=8, label="A*", color="steelblue")
        ax.plot(nodes, rrt_distances, marker="s", linewidth=2, markersize=8, label="RRT", color="seagreen")
        
        ax.set_xlabel("Number of Nodes")
        ax.set_ylabel("Path Length (meters)")
        ax.set_title("Path Length Comparison - Without Obstacles")
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig("../results/graphs/path_length_no_obstacles.png", dpi=300)
        plt.close()
        print("Saved: path_length_no_obstacles.png")
    
    def graph_path_length_with_obstacles(self):
        fig, ax = plt.subplots(figsize=(10, 6))
        
        astar_distances = []
        rrt_distances = []
        nodes = []
        
        for node_count in self.node_counts:
            node_count_str = str(node_count)
            if node_count_str not in self.results:
                continue
            results = self.results[node_count_str]["with_obstacles"]
            nodes.append(node_count)
            astar_distances.append(results["A*"]["mean_distance"])
            rrt_distances.append(results["RRT"]["mean_distance"])
        
        ax.plot(nodes, astar_distances, marker="o", linewidth=2, markersize=8, label="A*", color="steelblue")
        ax.plot(nodes, rrt_distances, marker="s", linewidth=2, markersize=8, label="RRT", color="seagreen")
        
        ax.set_xlabel("Number of Nodes")
        ax.set_ylabel("Path Length (meters)")
        ax.set_title("Path Length Comparison - With Random Obstacles")
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig("../results/graphs/path_length_with_obstacles.png", dpi=300)
        plt.close()
        print("Saved: path_length_with_obstacles.png")
    
    def graph_computation_time(self):
        fig, ax = plt.subplots(figsize=(10, 6))
        
        astar_times_no_obs = []
        astar_times_with_obs = []
        rrt_times_no_obs = []
        rrt_times_with_obs = []
        nodes = []
        
        for node_count in self.node_counts:
            node_count_str = str(node_count)
            if node_count_str not in self.results:
                continue
            
            results_no_obs = self.results[node_count_str]["no_obstacles"]
            results_with_obs = self.results[node_count_str]["with_obstacles"]
            nodes.append(node_count)
            
            astar_times_no_obs.append(results_no_obs["A*"]["mean_time"])
            astar_times_with_obs.append(results_with_obs["A*"]["mean_time"])
            rrt_times_no_obs.append(results_no_obs["RRT"]["mean_time"])
            rrt_times_with_obs.append(results_with_obs["RRT"]["mean_time"])
        
        ax.plot(nodes, astar_times_no_obs, marker="o", linewidth=2, markersize=8, label="A* (no obstacles)", color="steelblue")
        ax.plot(nodes, astar_times_with_obs, marker="o", linewidth=2, markersize=8, label="A* (with obstacles)", color="darkblue", linestyle="--")
        ax.plot(nodes, rrt_times_no_obs, marker="s", linewidth=2, markersize=8, label="RRT (no obstacles)", color="seagreen")
        ax.plot(nodes, rrt_times_with_obs, marker="s", linewidth=2, markersize=8, label="RRT (with obstacles)", color="darkgreen", linestyle="--")
        
        ax.set_xlabel("Number of Nodes")
        ax.set_ylabel("Computation Time (milliseconds)")
        ax.set_title("Computation Time Comparison")
        ax.set_yscale("log")
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig("../results/graphs/computation_time.png", dpi=300)
        plt.close()
        print("Saved: computation_time.png")
    
    def graph_efficiency_comparison(self):
        fig, ax = plt.subplots(figsize=(10, 6))
        
        astar_eff = []
        rrt_eff = []
        nodes = []
        
        for node_count in self.node_counts:
            node_count_str = str(node_count)
            if node_count_str not in self.results:
                continue
            results = self.results[node_count_str]["no_obstacles"]
            nodes.append(node_count)
            astar_eff.append(results["A*"]["efficiency"])
            rrt_eff.append(results["RRT"]["efficiency"])
        
        x = np.arange(len(nodes))
        width = 0.35
        
        ax.bar(x - width/2, astar_eff, width, label="A*", color="steelblue")
        ax.bar(x + width/2, rrt_eff, width, label="RRT", color="seagreen")
        
        ax.set_xlabel("Number of Nodes")
        ax.set_ylabel("Efficiency Score (distance per millisecond)")
        ax.set_title("Algorithm Efficiency Comparison - Without Obstacles")
        ax.set_xticks(x)
        ax.set_xticklabels(nodes)
        ax.legend()
        ax.grid(True, alpha=0.3, axis="y")
        
        plt.tight_layout()
        plt.savefig("../results/graphs/efficiency_comparison.png", dpi=300)
        plt.close()
        print("Saved: efficiency_comparison.png")


if __name__ == "__main__":
    print("=" * 70)
    print("GENERATING COMPARISON GRAPHS")
    print("=" * 70)
    generator = GraphGenerator()
    generator.generate_all_graphs()
    print("\n" + "=" * 70)
    print("GRAPH GENERATION COMPLETE")
    print("Graphs saved to: ../results/graphs/")
    print("=" * 70)
