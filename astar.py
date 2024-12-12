import heapq

class AStar:
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

    def astar_search(self):
        if not self.is_valid(self.start[0], self.start[1]):
            print(f"Error: Start point {self.start} is invalid.")
            return float('inf'), []

        if not self.is_valid(self.end[0], self.end[1]):
            print(f"Error: End point {self.end} is invalid.")
            return float('inf'), []

        g_cost = {self.start: 0}
        h = self.manhattan_distance(self.start[0], self.start[1], self.end[0], self.end[1])
        f_cost = {self.start: h}

        pq = [(f_cost[self.start], self.start, [self.start])]
        visited = set()

        while pq:
            current_f, current, path = heapq.heappop(pq)

            if current == self.end:
                total_cost = g_cost[current]
                print(f"{total_cost} {', '.join(map(str, path))}")
                return total_cost, path

            if current in visited:
                continue
            visited.add(current)

            for dx, dy in self.directions:
                neighbor_x = current[0] + dx
                neighbor_y = current[1] + dy
                neighbor = (neighbor_x, neighbor_y)

                if self.is_valid(neighbor_x, neighbor_y):
                    terrain = self.map_matrix[neighbor_y][neighbor_x]
                    neighbor_cost = g_cost[current] + self.terrain_costs[terrain]

                    if neighbor not in g_cost or neighbor_cost < g_cost[neighbor]:
                        g_cost[neighbor] = neighbor_cost
                        h = self.manhattan_distance(neighbor_x, neighbor_y, self.end[0], self.end[1])
                        f_cost[neighbor] = neighbor_cost + h
                        new_path = path + [neighbor]
                        heapq.heappush(pq, (f_cost[neighbor], neighbor, new_path))

        print("No path found from start to goal.")
        return float('inf'), []
