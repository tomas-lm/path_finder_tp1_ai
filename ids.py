class IDS:
    def __init__(self, map_matrix, start, end, terrain_costs):
        self.map_matrix = map_matrix
        self.start = start
        self.end = end
        self.terrain_costs = terrain_costs
        self.rows = len(map_matrix)
        self.cols = len(map_matrix[0])
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def is_valid(self, x, y):
        if not (0 <= x < self.cols and 0 <= y < self.rows):
            return False
        terrain = self.map_matrix[y][x]
        if terrain not in self.terrain_costs:
            return False
        return terrain != '@'

    def ids_search(self):
        if not self.is_valid(self.start[0], self.start[1]):
            print(f"Error: Start point {self.start} is invalid.")
            return float('inf'), []

        if not self.is_valid(self.end[0], self.end[1]):
            print(f"Error: End point {self.end} is invalid.")
            return float('inf'), []

        depth = 0
        while True:
            cost, path = self.dls(self.start, depth, set(), 0, [])
            if path is not None:
                print(f"{cost} {', '.join(map(str, path))}")
                return cost, path
            depth += 1

    def dls(self, current, depth, visited, current_cost, path):
        if depth < 0:
            return None, None

        if current == self.end:
            return current_cost, path + [current]

        visited.add(current)
        path.append(current)

        for dx, dy in self.directions:
            neighbor_x = current[0] + dx
            neighbor_y = current[1] + dy
            neighbor = (neighbor_x, neighbor_y)

            if neighbor not in visited and self.is_valid(neighbor_x, neighbor_y):
                terrain = self.map_matrix[neighbor_y][neighbor_x]
                terrain_cost = self.terrain_costs[terrain]

                result_cost, result_path = self.dls(
                    neighbor,
                    depth - 1,
                    visited.copy(),
                    current_cost + terrain_cost,
                    path.copy(),
                )

                if result_path is not None:
                    return result_cost, result_path

        return None, None
