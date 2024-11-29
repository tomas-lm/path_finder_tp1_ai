from collections import deque

class BFS:
    def __init__(self, map_matrix, start, end, terrain_costs):
        """
        Initializes the BFS class.
        :param map_matrix: 2D matrix representing the map.
        :param start: Tuple (x, y) for the start point.
        :param end: Tuple (x, y) for the end point.
        :param terrain_costs: Dictionary of terrain costs.
        """
        self.map_matrix = map_matrix
        self.start = start
        self.end = end
        self.terrain_costs = terrain_costs
        self.rows = len(map_matrix)
        self.cols = len(map_matrix[0])
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Directions: right, down, left, up

    def is_valid(self, x, y):
        """Checks if the position is within map bounds and not a wall."""
        if not (0 <= x < self.cols and 0 <= y < self.rows):
            return False  # Out of bounds
        terrain = self.map_matrix[y][x]
        if terrain not in self.terrain_costs:
            return False  # Invalid or unknown terrain
        return terrain != '@'  # Not a wall


    def bfs_search(self):
        """Executes the BFS search and returns the cost and the path."""
        print(f"Starting BFS from {self.start} to {self.end}")
        
        # Validate start and end positions
        if not self.is_valid(self.start[0], self.start[1]):
            print(f"Error: Start point {self.start} is invalid.")
            return float('inf'), []

        if not self.is_valid(self.end[0], self.end[1]):
            print(f"Error: End point {self.end} is invalid.")
            return float('inf'), []

        # BFS initialization
        queue = deque([(self.start, 0, [self.start])])  # (current_position, cost, path)
        visited = set()  # Keeps track of visited nodes
        print(f"Initialized BFS queue with start node {self.start}")

        while queue:
            current, cost, path = queue.popleft()
            print(f"Processing node {current} with cost {cost} and path {path}")

            # Check if the goal is reached
            if current == self.end:
                print(f"Goal reached! Total cost: {cost}, Path: {path}")
                return cost, path

            # Mark the current node as visited
            visited.add(current)

            # Explore neighbors
            for dx, dy in self.directions:
                neighbor_x = current[0] + dx
                neighbor_y = current[1] + dy
                neighbor = (neighbor_x, neighbor_y)

                if neighbor not in visited and self.is_valid(neighbor_x, neighbor_y):
                    terrain = self.map_matrix[neighbor_y][neighbor_x]
                    terrain_cost = self.terrain_costs[terrain]  # `is_valid` ensures the terrain is valid
                    print(f"  Exploring neighbor {neighbor} with terrain '{terrain}' and cost {terrain_cost}")

                    queue.append((neighbor, cost + terrain_cost, path + [neighbor]))
                    print(f"    Added neighbor {neighbor} to queue with updated cost {cost + terrain_cost} and path {path + [neighbor]}")

        # If the search ends without finding a path
        print("No path found from start to goal.")
        return float('inf'), []