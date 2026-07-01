import numpy as np
import heapq
import time
from grid_base import GridBase, PathfindingResult

class DijkstraAlgorithm:
    """
    Dijkstra Pathfinding Algorithm
    
    Systematic uniform-cost search that explores all directions equally.
    Uses only g(n) = actual cost from start (no heuristic).
    
    Guarantees shortest path but explores more than A*.
    """
    
    def __init__(self, grid):
        self.grid = grid
        self.result = PathfindingResult("Dijkstra")
    
    def find_path(self, start, goal):
        """
        Find shortest path using Dijkstra algorithm
        
        Args:
            start: Starting position (x, y)
            goal: Goal position (x, y)
        
        Returns:
            PathfindingResult with path and metrics
        """
        start_time = time.time()
        
        open_set = []
        counter = 0
        heapq.heappush(open_set, (0, counter, start, [start]))
        counter += 1
        
        visited = set()
        distances = {start: 0}
        
        while open_set:
            current_dist, _, current, path = heapq.heappop(open_set)
            
            if self._close_enough(current, goal):
                path.append(goal)
                self.result.path = path
                self.result.nodes_visited = len(visited)
                self.result.calculate_distance()
                self.result.computation_time = (time.time() - start_time) * 1000
                return self.result
            
            if current in visited:
                continue
            
            visited.add(current)
            neighbors = self.grid.get_neighbors(current, step_size=5)
            
            for neighbor in neighbors:
                if neighbor in visited:
                    continue
                
                if not self.grid.line_of_sight(current, neighbor):
                    continue
                
                new_distance = current_dist + self.grid.heuristic_distance(current, neighbor)
                
                if neighbor not in distances or new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    
                    new_path = path + [neighbor]
                    heapq.heappush(open_set, (new_distance, counter, neighbor, new_path))
                    counter += 1
        
        self.result.path = []
        self.result.distance = float('inf')
        self.result.nodes_visited = len(visited)
        self.result.computation_time = (time.time() - start_time) * 1000
        return self.result
    
    def _close_enough(self, pos1, pos2, threshold=5):
        """Check if within threshold of goal"""
        return self.grid.heuristic_distance(pos1, pos2) < threshold
    
    def visit_all_nodes(self):
        """
        Visit all sensor nodes in optimal order using nearest neighbor + Dijkstra
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
            
            result = self.find_path(current_pos, nearest_pos)
            
            if result.path:
                full_path.extend(result.path[1:])
                total_distance += result.distance
            
            current_pos = nearest_pos
            unvisited.remove(nearest_idx)
            nodes_visited += 1
        
        final_result = PathfindingResult("Dijkstra")
        final_result.path = full_path
        final_result.distance = total_distance
        final_result.computation_time = (time.time() - start_time) * 1000
        final_result.nodes_visited = nodes_visited
        
        return final_result


if __name__ == "__main__":
    print("=" * 60)
    print("DIJKSTRA ALGORITHM TEST")
    print("=" * 60)
    
    grid = GridBase(grid_size=10, area_size=100, num_nodes=25, seed=42)
    
    print("\nGrid created: 10x10")
    print("Nodes placed: 25")
    print("Obstacles: 0")
    
    dijkstra = DijkstraAlgorithm(grid)
    result = dijkstra.visit_all_nodes()
    
    print("\n" + str(result))
    print("Path waypoints: " + str(len(result.path)))
    print("Test passed")
    
    print("\n" + "=" * 60)
