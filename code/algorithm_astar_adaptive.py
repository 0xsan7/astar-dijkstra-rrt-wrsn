"""
Adaptive A* Algorithm with Dynamic Heuristic Weighting

Novel contribution: A* with obstacle-density-aware heuristic weight
Adapts heuristic strength based on local obstacle density
"""

import math
from grid_base import GridBase, PathfindingResult

class AdaptiveAStarAlgorithm:
    """
    A* with adaptive heuristic weight based on obstacle density.
    
    Innovation: Instead of static heuristic, weight increases when obstacles present.
    f(n) = g(n) + w(obstacle_density) * h(n)
    """
    
    def __init__(self, grid):
        self.grid = grid
        self.start_time = None
        self.end_time = None
    
    def calculate_local_obstacle_density(self, x, y, radius=5):
        """Calculate obstacle density in local neighborhood"""
        obstacles = 0
        total_cells = 0
        
        for dx in range(-radius, radius + 1):
            for dy in range(-radius, radius + 1):
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.grid.grid_size and 0 <= ny < self.grid.grid_size:
                    total_cells += 1
                    if self.grid.grid[ny][nx] == 1:  # 1 = obstacle
                        obstacles += 1
        
        if total_cells == 0:
            return 0
        return obstacles / total_cells
    
    def calculate_adaptive_weight(self, obstacle_density):
        """
        Calculate dynamic heuristic weight based on obstacle density.
        
        w = 1.0 + 2.0 * density
        
        No obstacles: w = 1.0 (normal A*)
        High obstacles: w = 3.0 (trust heuristic more)
        """
        return 1.0 + (2.0 * obstacle_density)
    
    def heuristic(self, pos, goal):
        """Euclidean distance heuristic"""
        return math.sqrt((pos[0] - goal[0])**2 + (pos[1] - goal[1])**2)
    
    def visit_all_nodes(self):
        """Execute adaptive A* to visit all nodes"""
        import time
        self.start_time = time.time()
        
        total_distance = 0
        visited_nodes = set()
        current_pos = tuple(self.grid.nodes[0])
        visited_nodes.add(0)
        
        waypoints = [current_pos]
        
        # Visit all nodes
        while len(visited_nodes) < len(self.grid.nodes):
            # Find nearest unvisited node
            nearest_node = None
            nearest_distance = float('inf')
            
            for i, node in enumerate(self.grid.nodes):
                if i not in visited_nodes:
                    dist = self.heuristic(current_pos, tuple(node))
                    if dist < nearest_distance:
                        nearest_distance = dist
                        nearest_node = i
            
            # Calculate adaptive weight for this region
            obstacle_density = self.calculate_local_obstacle_density(
                int(current_pos[0]), int(current_pos[1])
            )
            weight = self.calculate_adaptive_weight(obstacle_density)
            
            # Find path to nearest node using adaptive A*
            path = self._adaptive_astar_search(
                current_pos, 
                tuple(self.grid.nodes[nearest_node]),
                weight
            )
            
            if path:
                for waypoint in path[1:]:
                    waypoints.append(waypoint)
                    total_distance += self.heuristic(current_pos, waypoint)
                    current_pos = waypoint
            
            visited_nodes.add(nearest_node)
        
        self.end_time = time.time()
        computation_time = (self.end_time - self.start_time) * 1000
        
        return PathfindingResult(
            distance=total_distance,
            waypoints=waypoints,
            computation_time=computation_time
        )
    
    def _adaptive_astar_search(self, start, goal, weight):
        """A* search with adaptive heuristic weight"""
        import heapq
        
        open_set = [(0, start)]
        came_from = {}
        g_score = {start: 0}
        
        iterations = 0
        max_iterations = 1000
        
        while open_set and iterations < max_iterations:
            iterations += 1
            _, current = heapq.heappop(open_set)
            
            if current == goal:
                path = [current]
                while current in came_from:
                    current = came_from[current]
                    path.append(current)
                return path[::-1]
            
            # 8-directional movement
            for dx, dy in [(-5, -5), (-5, 0), (-5, 5), (0, -5), 
                          (0, 5), (5, -5), (5, 0), (5, 5)]:
                neighbor = (current[0] + dx, current[1] + dy)
                
                # Check bounds
                grid_x, grid_y = int(neighbor[0] // 10), int(neighbor[1] // 10)
                if not (0 <= grid_x < self.grid.grid_size and 
                       0 <= grid_y < self.grid.grid_size):
                    continue
                
                # Check obstacles
                if self.grid.grid[grid_y][grid_x] == 1:
                    continue
                
                tentative_g = g_score[current] + math.sqrt(dx**2 + dy**2)
                
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    
                    # ADAPTIVE WEIGHT HERE
                    h = weight * self.heuristic(neighbor, goal)
                    f = tentative_g + h
                    
                    heapq.heappush(open_set, (f, neighbor))
        
        return None
