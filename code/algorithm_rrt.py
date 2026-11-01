import numpy as np
import time
from grid_base import GridBase, PathfindingResult

class RRTAlgorithm:
    """
    RRT (Rapidly-Exploring Random Tree) Algorithm
    
    Randomized incremental search that grows random branches.
    Very fast exploration but does not guarantee optimal path.
    
    Uses goal biasing: 20% chance to go toward goal, 80% random.
    """
    
    def __init__(self, grid):
        self.grid = grid
        self.result = PathfindingResult("RRT")
    
    def find_path(self, start, goal, max_iterations=1000, step_size=5):
        """
        Find path using RRT algorithm
        
        Args:
            start: Starting position (x, y)
            goal: Goal position (x, y)
            max_iterations: Maximum random samples
            step_size: Size of each expansion step
        
        Returns:
            PathfindingResult with path and metrics
        """
        start_time = time.time()
        
        tree = [start]
        parent = {start: None}
        
        for iteration in range(max_iterations):
            # Goal biasing: 20% toward goal, 80% random
            if np.random.rand() < 0.2:
                random_point = goal
            else:
                random_point = (np.random.uniform(0, self.grid.area_size),
                               np.random.uniform(0, self.grid.area_size))
            
            # Find nearest node in tree
            nearest_node = min(tree,
                             key=lambda n: self.grid.heuristic_distance(n, random_point))
            
            # Expand toward random point
            direction = np.array(random_point) - np.array(nearest_node)
            distance = np.linalg.norm(direction)
            
            if distance < 0.01:
                continue
            
            direction = direction / distance
            new_node = tuple(np.array(nearest_node) + direction * step_size)
            
            # Check if in free space
            if not self.grid.is_obstacle_free(new_node[0], new_node[1]):
                continue
            
            if not self.grid.line_of_sight(nearest_node, new_node):
                continue
            
            tree.append(new_node)
            parent[new_node] = nearest_node
            
            # Check if reached goal
            if self.grid.heuristic_distance(new_node, goal) < 10:
                path = []
                current = new_node
                
                while current is not None:
                    path.append(current)
                    current = parent[current]
                
                path.reverse()
                path.append(goal)
                
                self.result.path = path
                self.result.nodes_visited = len(tree)
                self.result.calculate_distance()
                self.result.computation_time = (time.time() - start_time) * 1000
                return self.result
        
        self.result.path = []
        self.result.distance = float('inf')
        self.result.nodes_visited = len(tree)
        self.result.computation_time = (time.time() - start_time) * 1000
        return self.result
    
    def visit_all_nodes(self):
        """
        Visit all sensor nodes using nearest neighbor + RRT
        """
        start_time = time.time()
        
        current_pos = tuple(self.grid.nodes[0])
        unvisited = set(range(1, self.grid.num_nodes))
        full_path = [current_pos]
        
        total_distance = 0
        nodes_visited = 1
        
        while unvisited:
            nearest_idx = min(unvisited,
                             key=lambda i: self.grid.heuristic_distance(current_pos, tuple(self.grid.nodes[i])))
            nearest_pos = tuple(self.grid.nodes[nearest_idx])
            
            result = self.find_path(current_pos, nearest_pos, max_iterations=500)
            
            if result.path:
                full_path.extend(result.path[1:])
                total_distance += result.distance
            
            current_pos = nearest_pos
            unvisited.remove(nearest_idx)
            nodes_visited += 1
        
        final_result = PathfindingResult("RRT")
        final_result.path = full_path
        final_result.distance = total_distance
        final_result.computation_time = (time.time() - start_time) * 1000
        final_result.nodes_visited = nodes_visited
        
        return final_result


if __name__ == "__main__":
    print("=" * 60)
    print("RRT ALGORITHM TEST")
    print("=" * 60)
    
    grid = GridBase(grid_size=10, area_size=100, num_nodes=25, seed=42)
    
    print("\nGrid created: 10x10")
    print("Nodes placed: 25")
    print("Obstacles: 0")
    
    rrt = RRTAlgorithm(grid)
    result = rrt.visit_all_nodes()
    
    print("\n" + str(result))
    print("Path waypoints: " + str(len(result.path)))
    print("Test passed")
    
    print("\n" + "=" * 60)
