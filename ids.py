class IDS:
    def __init__(self, map_matrix, start, end, terrain_costs):
        """
        Initializes the IDS class.
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

    def ids_search(self):
        """Executes the IDS search and returns the cost and the path."""
        print(f"Starting IDS from {self.start} to {self.end}")

        # Validate start and end positions
        if not self.is_valid(self.start[0], self.start[1]):
            print(f"Error: Start point {self.start} is invalid.")
            return float('inf'), []

        if not self.is_valid(self.end[0], self.end[1]):
            print(f"Error: End point {self.end} is invalid.")
            return float('inf'), []

        depth = 0
        while True:
            print(f"Searching with depth limit {depth}")
            cost, path = self.dls(self.start, depth, set(), 0, [])
            if path is not None:  # If a solution is found
                print(f"Solution found at depth {depth}")
                return cost, path
            depth += 1  # Increment depth for the next iteration

    def dls(self, current, depth, visited, current_cost, path):
        """
        Depth-Limited Search (DLS) recursive helper.
        :param current: Current position as (x, y).
        :param depth: Current depth limit.
        :param visited: Set of visited positions.
        :param current_cost: Accumulated cost to reach this point.
        :param path: Path taken so far.
        :return: (cost, path) if goal is found, or (None, None) if not.
        """
        if depth < 0:
            return None, None  # Depth limit exceeded

        if current == self.end:
            return current_cost, path + [current]  # Goal reached

        visited.add(current)
        path.append(current)

        for dx, dy in self.directions:
            neighbor_x = current[0] + dx
            neighbor_y = current[1] + dy
            neighbor = (neighbor_x, neighbor_y)

            if neighbor not in visited and self.is_valid(neighbor_x, neighbor_y):
                terrain = self.map_matrix[neighbor_y][neighbor_x]
                terrain_cost = self.terrain_costs[terrain]

                # Explore the neighbor
                result_cost, result_path = self.dls(
                    neighbor,
                    depth - 1,
                    visited.copy(),
                    current_cost + terrain_cost,
                    path.copy(),
                )

                if result_path is not None:  # Solution found in recursion
                    return result_cost, result_path

        return None, None  # No solution found at this depth
