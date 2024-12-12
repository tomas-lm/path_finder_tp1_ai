class Greedy:
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

    def manhattan_distance(self, x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)

    def greedy_search(self):
        if not self.is_valid(self.start[0], self.start[1]):
            print(f"Error: Start point {self.start} is invalid.")
            return [], float('inf')

        if not self.is_valid(self.end[0], self.end[1]):
            print(f"Error: End point {self.end} is invalid.")
            return [], float('inf')

        current = self.start
        path = [current]
        total_cost = 0
        visited = set()

        while current != self.end:
            if current in visited:
                return path, float('inf')
            
            visited.add(current)
            neighbors = []

            for dx, dy in self.directions:
                neighbor_x, neighbor_y = current[0] + dx, current[1] + dy
                if self.is_valid(neighbor_x, neighbor_y):
                    h = self.manhattan_distance(neighbor_x, neighbor_y, self.end[0], self.end[1])
                    neighbors.append(((neighbor_x, neighbor_y), h))

            if not neighbors:
                return path, float('inf')

            next_move = min(neighbors, key=lambda x: x[1])[0]
            path.append(next_move)
            total_cost += self.terrain_costs[self.map_matrix[next_move[1]][next_move[0]]]
            current = next_move

        print(f"{total_cost} {', '.join(map(str, path))}")
        return path, total_cost
