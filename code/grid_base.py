import numpy as np
import time

class GridBase:
    """
    Base class for grid-based pathfinding
    Handles grid creation, node placement, obstacle placement
    """
    
    def __init__(self, grid_size=10, area_size=100, num_nodes=25, seed=42):
        """
        Initialize grid
        
        Args:
            grid_size: Number of cells per side (10x10 grid)
            area_size: Physical area in meters (100x100)
            num_nodes: Number of sensor nodes
            seed: Random seed for reproducibility
        """
        np.random.seed(seed)
        
        self.grid_size = grid_size
        self.area_size = area_size
        self.num_nodes = num_nodes
        self.cell_size = area_size / grid_size
        
        self.grid = np.zeros((grid_size, grid_size), dtype=int)
        self.nodes = self._place_nodes()
        self.obstacles = np.array([])
    
    def _place_nodes(self):
        """Place sensor nodes randomly in grid"""
        nodes = []
        for _ in range(self.num_nodes):
            x = np.random.uniform(0, self.area_size)
            y = np.random.uniform(0, self.area_size)
            nodes.append((x, y))
        return np.array(nodes)
    
    def add_random_obstacles(self, obstacle_count=15, seed=None):
        """Add random obstacles to grid"""
        if seed is not None:
            np.random.seed(seed)
        
        obstacles = []
        for _ in range(obstacle_count):
            cell_x = np.random.randint(0, self.grid_size)
            cell_y = np.random.randint(0, self.grid_size)
            
            x = cell_x * self.cell_size
            y = cell_y * self.cell_size
            
            obstacles.append((x, y, x + self.cell_size, y + self.cell_size))
            self.grid[cell_y, cell_x] = 1
        
        self.obstacles = np.array(obstacles)
        return obstacles
    
    def is_obstacle_free(self, x, y):
        """Check if position is obstacle-free"""
        if x < 0 or x >= self.area_size or y < 0 or y >= self.area_size:
            return False
        
        cell_x = int(x / self.cell_size)
        cell_y = int(y / self.cell_size)
        
        cell_x = max(0, min(cell_x, self.grid_size - 1))
        cell_y = max(0, min(cell_y, self.grid_size - 1))
        
        return self.grid[cell_y, cell_x] == 0
    
    def line_of_sight(self, pos1, pos2):
        """Check if straight line between two points is obstacle-free"""
        x1, y1 = pos1
        x2, y2 = pos2
        
        steps = 20
        for i in range(1, steps):
            t = i / steps
            x = x1 + t * (x2 - x1)
            y = y1 + t * (y2 - y1)
            
            if not self.is_obstacle_free(x, y):
                return False
        
        return True
    
    def heuristic_distance(self, pos1, pos2):
        """Calculate Euclidean distance"""
        return np.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)
    
    def get_neighbors(self, pos, step_size=5):
        """Get neighboring positions"""
        neighbors = []
        for angle in np.linspace(0, 2*np.pi, 8, endpoint=False):
            nx = pos[0] + step_size * np.cos(angle)
            ny = pos[1] + step_size * np.sin(angle)
            
            if self.is_obstacle_free(nx, ny):
                neighbors.append((nx, ny))
        
        return neighbors
    
    def reset(self):
        """Reset grid for new test"""
        self.grid = np.zeros((self.grid_size, self.grid_size), dtype=int)
        self.obstacles = np.array([])
        self.nodes = self._place_nodes()


class PathfindingResult:
    """Store pathfinding results"""
    
    def __init__(self, algorithm_name):
        self.algorithm = algorithm_name
        self.path = None
        self.distance = 0
        self.computation_time = 0
        self.nodes_visited = 0
    
    def calculate_distance(self):
        """Calculate total distance of path"""
        if self.path is None or len(self.path) < 2:
            return 0
        
        distance = 0
        for i in range(len(self.path) - 1):
            p1 = self.path[i]
            p2 = self.path[i + 1]
            distance += np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
        
        self.distance = distance
        return distance
    
    def __str__(self):
        return (f"{self.algorithm}: "
                f"Distance={self.distance:.1f}m, "
                f"Time={self.computation_time:.2f}ms, "
                f"Nodes visited={self.nodes_visited}")


if __name__ == "__main__":
    print("=" * 60)
    print("GRID BASE TEST")
    print("=" * 60)
    
    grid = GridBase(grid_size=10, area_size=100, num_nodes=25)
    
    print("\nGrid created: 10x10")
    print("Nodes placed: " + str(len(grid.nodes)))
    print("Area size: 100x100 meters")
    
    grid.add_random_obstacles(obstacle_count=15)
    print("Obstacles added: " + str(len(grid.obstacles)))
    
    print("\nTest passed")
    print("=" * 60)
