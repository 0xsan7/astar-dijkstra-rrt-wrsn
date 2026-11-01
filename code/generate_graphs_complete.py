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
        print("Generating comprehensive comparison graphs...")
        self.graph_all_three_no_obstacles()
        self.graph_all_three_with_obstacles()
        self.graph_dijkstra_comparison()
        self.graph_computation_time_all()
        self.graph_efficiency_all()
        print("All graphs generated successfully")
    
    def graph_all_three_no_obstacles(self):
        """Graph 1: All three algorithms - no obstacles"""
        fig, ax = plt.subplots(figsize=(12, 7))
        
        astar_distances = []
        dijkstra_distances = []
        rrt_distances = []
        nodes = []
        
        for node_count in self.node_counts:
            node_count_str = str(node_count)
            if node_count_str not in self.results:
                continue
            results = self.results[node_count_str]["no_obstacles"]
            nodes.append(node_count)
            astar_distances.append(results["A*"]["mean_distance"])
            if "Dijkstra" in results:
                dijkstra_distances.append(results["Dijkstra"]["mean_distance"])
            rrt_distances.append(results["RRT"]["mean_distance"])
        
        x = np.arange(len(nodes))
        width = 0.25
        
        ax.bar(x - width, astar_distances, width, label="A*", color="steelblue")
        if dijkstra_distances:
            # Pad with None for nodes without Dijkstra
            dijkstra_padded = [dijkstra_distances[0], dijkstra_distances[1], None, None]
            valid_x = [0, 1]
            valid_dijkstra = dijkstra_distances
            ax.bar(valid_x, valid_dijkstra, width, label="Dijkstra", color="coral")
        ax.bar(x + width, rrt_distances, width, label="RRT", color="seagreen")
        
        ax.set_xlabel("Number of Nodes")
        ax.set_ylabel("Path Length (meters)")
        ax.set_title("Path Length Comparison - All Three Algorithms - Without Obstacles")
        ax.set_xticks(x)
        ax.set_xticklabels(nodes)
        ax.legend()
        ax.grid(True, alpha=0.3, axis="y")
        
        plt.tight_layout()
        plt.savefig("../results/graphs/01_path_length_no_obstacles_all_three.png", dpi=300)
        plt.close()
        print("Saved: 01_path_length_no_obstacles_all_three.png")
    
    def graph_all_three_with_obstacles(self):
        """Graph 2: All three algorithms - with obstacles"""
        fig, ax = plt.subplots(figsize=(12, 7))
        
        astar_distances = []
        dijkstra_distances = []
        rrt_distances = []
        nodes = []
        
        for node_count in self.node_counts:
            node_count_str = str(node_count)
            if node_count_str not in self.results:
                continue
            results = self.results[node_count_str]["with_obstacles"]
            nodes.append(node_count)
            astar_distances.append(results["A*"]["mean_distance"])
            if "Dijkstra" in results:
                dijkstra_distances.append(results["Dijkstra"]["mean_distance"])
            rrt_distances.append(results["RRT"]["mean_distance"])
        
        x = np.arange(len(nodes))
        width = 0.25
        
        ax.bar(x - width, astar_distances, width, label="A*", color="steelblue")
        if dijkstra_distances:
            valid_x = [0, 1]
            valid_dijkstra = dijkstra_distances
            ax.bar(valid_x, valid_dijkstra, width, label="Dijkstra", color="coral")
        ax.bar(x + width, rrt_distances, width, label="RRT", color="seagreen")
        
        ax.set_xlabel("Number of Nodes")
        ax.set_ylabel("Path Length (meters)")
        ax.set_title("Path Length Comparison - All Three Algorithms - With Random Obstacles")
        ax.set_xticks(x)
        ax.set_xticklabels(nodes)
        ax.legend()
        ax.grid(True, alpha=0.3, axis="y")
        
        plt.tight_layout()
        plt.savefig("../results/graphs/02_path_length_with_obstacles_all_three.png", dpi=300)
        plt.close()
        print("Saved: 02_path_length_with_obstacles_all_three.png")
    
    def graph_dijkstra_comparison(self):
        """Graph 3: Dijkstra vs A* (head-to-head on comparable data)"""
        fig, ax = plt.subplots(figsize=(10, 6))
        
        nodes_dijkstra = [10, 25]
        astar_distances = []
        dijkstra_distances = []
        
        for node_count in nodes_dijkstra:
            node_count_str = str(node_count)
            results = self.results[node_count_str]["no_obstacles"]
            astar_distances.append(results["A*"]["mean_distance"])
            dijkstra_distances.append(results["Dijkstra"]["mean_distance"])
        
        x = np.arange(len(nodes_dijkstra))
        width = 0.35
        
        ax.bar(x - width/2, astar_distances, width, label="A*", color="steelblue")
        ax.bar(x + width/2, dijkstra_distances, width, label="Dijkstra", color="coral")
        
        ax.set_xlabel("Number of Nodes")
        ax.set_ylabel("Path Length (meters)")
        ax.set_title("Dijkstra vs A* Path Length (No Obstacles)")
        ax.set_xticks(x)
        ax.set_xticklabels(nodes_dijkstra)
        ax.legend()
        ax.grid(True, alpha=0.3, axis="y")
        
        plt.tight_layout()
        plt.savefig("../results/graphs/03_dijkstra_vs_astar.png", dpi=300)
        plt.close()
        print("Saved: 03_dijkstra_vs_astar.png")
    
    def graph_computation_time_all(self):
        """Graph 4: Computation time - all three algorithms"""
        fig, ax = plt.subplots(figsize=(12, 7))
        
        astar_times = []
        dijkstra_times = []
        rrt_times = []
        nodes = []
        
        for node_count in self.node_counts:
            node_count_str = str(node_count)
            if node_count_str not in self.results:
                continue
            results = self.results[node_count_str]["no_obstacles"]
            nodes.append(node_count)
            astar_times.append(results["A*"]["mean_time"])
            if "Dijkstra" in results:
                dijkstra_times.append(results["Dijkstra"]["mean_time"])
            rrt_times.append(results["RRT"]["mean_time"])
        
        ax.plot(nodes, astar_times, marker="o", linewidth=2.5, markersize=8, label="A*", color="steelblue")
        if dijkstra_times:
            ax.plot([10, 25], dijkstra_times, marker="^", linewidth=2.5, markersize=8, label="Dijkstra", color="coral")
        ax.plot(nodes, rrt_times, marker="s", linewidth=2.5, markersize=8, label="RRT", color="seagreen")
        
        ax.set_xlabel("Number of Nodes")
        ax.set_ylabel("Computation Time (milliseconds)")
        ax.set_title("Computation Time Comparison - All Three Algorithms - Without Obstacles")
        ax.set_yscale("log")
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig("../results/graphs/04_computation_time_all.png", dpi=300)
        plt.close()
        print("Saved: 04_computation_time_all.png")
    
    def graph_efficiency_all(self):
        """Graph 5: Efficiency - all three algorithms"""
        fig, ax = plt.subplots(figsize=(10, 6))
        
        nodes_dijkstra = [10, 25]
        astar_eff = []
        dijkstra_eff = []
        rrt_eff = []
        
        for node_count in nodes_dijkstra:
            node_count_str = str(node_count)
            results = self.results[node_count_str]["no_obstacles"]
            astar_eff.append(results["A*"]["efficiency"])
            dijkstra_eff.append(results["Dijkstra"]["efficiency"])
            rrt_eff.append(results["RRT"]["efficiency"])
        
        x = np.arange(len(nodes_dijkstra))
        width = 0.25
        
        ax.bar(x - width, astar_eff, width, label="A*", color="steelblue")
        ax.bar(x, dijkstra_eff, width, label="Dijkstra", color="coral")
        ax.bar(x + width, rrt_eff, width, label="RRT", color="seagreen")
        
        ax.set_xlabel("Number of Nodes")
        ax.set_ylabel("Efficiency Score (distance per millisecond)")
        ax.set_title("Algorithm Efficiency Comparison - Without Obstacles")
        ax.set_xticks(x)
        ax.set_xticklabels(nodes_dijkstra)
        ax.legend()
        ax.grid(True, alpha=0.3, axis="y")
        
        plt.tight_layout()
        plt.savefig("../results/graphs/05_efficiency_all_three.png", dpi=300)
        plt.close()
        print("Saved: 05_efficiency_all_three.png")


if __name__ == "__main__":
    print("=" * 70)
    print("GENERATING COMPREHENSIVE COMPARISON GRAPHS")
    print("=" * 70)
    generator = GraphGenerator()
    generator.generate_all_graphs()
    print("\n" + "=" * 70)
    print("GRAPH GENERATION COMPLETE - 5 Professional Graphs")
    print("Graphs saved to: ../results/graphs/")
    print("=" * 70)
