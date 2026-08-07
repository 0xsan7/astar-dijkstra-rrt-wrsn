import numpy as np
import json
import matplotlib.pyplot as plt
from matplotlib import rcParams
import os

rcParams['font.family'] = 'serif'
rcParams['font.size'] = 11

class GraphGenerator:
    def __init__(self, results_file="../results/data/complete_results.json"):
        with open(results_file, 'r') as f:
            self.results = json.load(f)
        self.node_counts = [10, 25, 50, 100]
        self.output_dir = "../results/graphs"
        os.makedirs(self.output_dir, exist_ok=True)
    
    def generate_all_graphs(self):
        print("Generating complete comparison graphs with log scale...")
        self.graph_path_length_no_obstacles()
        self.graph_path_length_with_obstacles()
        self.graph_computation_time_no_obstacles()
        self.graph_computation_time_with_obstacles()
        print(f"✅ All graphs saved to {self.output_dir}")
    
    def graph_path_length_no_obstacles(self):
        fig, ax = plt.subplots(figsize=(12, 6))
        
        x = np.arange(len(self.node_counts))
        width = 0.25
        
        astar_distances = [self.results[str(nc)]["no_obstacles"]["A*"]["mean_distance"] for nc in self.node_counts]
        dijkstra_distances = [self.results[str(nc)]["no_obstacles"]["Dijkstra"]["mean_distance"] for nc in self.node_counts]
        rrt_distances = [self.results[str(nc)]["no_obstacles"]["RRT"]["mean_distance"] for nc in self.node_counts]
        
        ax.bar(x - width, astar_distances, width, label="A*", color="skyblue")
        ax.bar(x, dijkstra_distances, width, label="Dijkstra", color="coral")
        ax.bar(x + width, rrt_distances, width, label="RRT", color="lightgreen")
        
        ax.set_xlabel("Number of Nodes")
        ax.set_ylabel("Path Length (m)")
        ax.set_title("Path Length Comparison - No Obstacles")
        ax.set_xticks(x)
        ax.set_xticklabels(self.node_counts)
        ax.legend()
        ax.grid(axis='y', alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(f"{self.output_dir}/1_path_length_no_obstacles.png", dpi=300, bbox_inches='tight')
        plt.close()
        print("✓ Graph 1: Path Length (No Obstacles)")
    
    def graph_path_length_with_obstacles(self):
        fig, ax = plt.subplots(figsize=(12, 6))
        
        x = np.arange(len(self.node_counts))
        width = 0.25
        
        astar_distances = [self.results[str(nc)]["with_obstacles"]["A*"]["mean_distance"] for nc in self.node_counts]
        dijkstra_distances = [self.results[str(nc)]["with_obstacles"]["Dijkstra"]["mean_distance"] for nc in self.node_counts]
        rrt_distances = [self.results[str(nc)]["with_obstacles"]["RRT"]["mean_distance"] for nc in self.node_counts]
        
        ax.bar(x - width, astar_distances, width, label="A*", color="skyblue")
        ax.bar(x, dijkstra_distances, width, label="Dijkstra", color="coral")
        ax.bar(x + width, rrt_distances, width, label="RRT", color="lightgreen")
        
        ax.set_xlabel("Number of Nodes")
        ax.set_ylabel("Path Length (m)")
        ax.set_title("Path Length Comparison - With Obstacles")
        ax.set_xticks(x)
        ax.set_xticklabels(self.node_counts)
        ax.legend()
        ax.grid(axis='y', alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(f"{self.output_dir}/2_path_length_with_obstacles.png", dpi=300, bbox_inches='tight')
        plt.close()
        print("✓ Graph 2: Path Length (With Obstacles)")
    
    def graph_computation_time_no_obstacles(self):
        fig, ax = plt.subplots(figsize=(12, 6))
        
        x = np.arange(len(self.node_counts))
        width = 0.25
        
        astar_times = [self.results[str(nc)]["no_obstacles"]["A*"]["mean_time"] for nc in self.node_counts]
        dijkstra_times = [self.results[str(nc)]["no_obstacles"]["Dijkstra"]["mean_time"] for nc in self.node_counts]
        rrt_times = [self.results[str(nc)]["no_obstacles"]["RRT"]["mean_time"] for nc in self.node_counts]
        
        ax.bar(x - width, astar_times, width, label="A*", color="skyblue")
        ax.bar(x, dijkstra_times, width, label="Dijkstra", color="coral")
        ax.bar(x + width, rrt_times, width, label="RRT", color="lightgreen")
        
        ax.set_xlabel("Number of Nodes")
        ax.set_ylabel("Computation Time (ms) - LOG SCALE")
        ax.set_title("Computation Time Comparison - No Obstacles (All Algorithms Visible)")
        ax.set_xticks(x)
        ax.set_xticklabels(self.node_counts)
        ax.set_yscale('log')
        ax.legend()
        ax.grid(axis='y', alpha=0.3, which='both')
        
        plt.tight_layout()
        plt.savefig(f"{self.output_dir}/3_computation_time_no_obstacles.png", dpi=300, bbox_inches='tight')
        plt.close()
        print("✓ Graph 3: Computation Time (No Obstacles) - LOG SCALE")
    
    def graph_computation_time_with_obstacles(self):
        fig, ax = plt.subplots(figsize=(12, 6))
        
        x = np.arange(len(self.node_counts))
        width = 0.25
        
        astar_times = [self.results[str(nc)]["with_obstacles"]["A*"]["mean_time"] for nc in self.node_counts]
        dijkstra_times = [self.results[str(nc)]["with_obstacles"]["Dijkstra"]["mean_time"] for nc in self.node_counts]
        rrt_times = [self.results[str(nc)]["with_obstacles"]["RRT"]["mean_time"] for nc in self.node_counts]
        
        ax.bar(x - width, astar_times, width, label="A*", color="skyblue")
        ax.bar(x, dijkstra_times, width, label="Dijkstra", color="coral")
        ax.bar(x + width, rrt_times, width, label="RRT", color="lightgreen")
        
        ax.set_xlabel("Number of Nodes")
        ax.set_ylabel("Computation Time (ms) - LOG SCALE")
        ax.set_title("Computation Time Comparison - With Obstacles (All Algorithms Visible)")
        ax.set_xticks(x)
        ax.set_xticklabels(self.node_counts)
        ax.set_yscale('log')
        ax.legend()
        ax.grid(axis='y', alpha=0.3, which='both')
        
        plt.tight_layout()
        plt.savefig(f"{self.output_dir}/4_computation_time_with_obstacles.png", dpi=300, bbox_inches='tight')
        plt.close()
        print("✓ Graph 4: Computation Time (With Obstacles) - LOG SCALE")

if __name__ == "__main__":
    generator = GraphGenerator()
    generator.generate_all_graphs()
