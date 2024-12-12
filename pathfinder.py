from bfs import BFS
from ids import IDS
from ucs import UCS
from astar import AStar
from greedy import Greedy

class PathFinder:
    def __init__(self, map_file, method, start_x, start_y, end_x, end_y):
        self.map_file = map_file
        self.method = method
        self.start = (start_x, start_y)
        self.end = (end_x, end_y)
        self.width = 0
        self.height = 0
        self.map_matrix = []
        self.terrain_costs = {
            '.': 1.0,
            ';': 1.5,
            '+': 2.5,
            'x': 6.0,
            '@': float('inf')
        }

    def load_map(self):
        try:
            with open(self.map_file, 'r') as file:
                self.width, self.height = map(int, file.readline().split())
                for _ in range(self.height):
                    row = file.readline().strip()
                    self.map_matrix.append(list(row))
        except FileNotFoundError:
            print(f"Erro: Arquivo '{self.map_file}' não encontrado.")
            exit(1)
        except Exception as e:
            print(f"Erro ao carregar o mapa: {e}")
            exit(1)

    def run_search(self):
        if self.method == "BFS":
            if not (0 <= self.start[0] < self.width and 0 <= self.start[1] < self.height):
                print(f"Erro: O ponto inicial {self.start} está fora do mapa.")
                return
            if not (0 <= self.end[0] < self.width and 0 <= self.end[1] < self.height):
                print(f"Erro: O ponto final {self.end} está fora do mapa.")
                return
            bfs = BFS(self.map_matrix, self.start, self.end, self.terrain_costs)
            cost, path = bfs.bfs_search()
            if cost == float('inf'):
                print("Nenhum caminho encontrado.")
        elif self.method == "UCS":
            if not (0 <= self.start[0] < self.width and 0 <= self.start[1] < self.height):
                print(f"Erro: O ponto inicial {self.start} está fora do mapa.")
                return
            if not (0 <= self.end[0] < self.width and 0 <= self.end[1] < self.height):
                print(f"Erro: O ponto final {self.end} está fora do mapa.")
                return
            ucs = UCS(self.map_matrix, self.start, self.end, self.terrain_costs)
            cost, path = ucs.ucs_search()
            if cost == float('inf'):
                print("Nenhum caminho encontrado.")
        elif self.method == "IDS":
            if not (0 <= self.start[0] < self.width and 0 <= self.start[1] < self.height):
                print(f"Erro: O ponto inicial {self.start} está fora do mapa.")
                return
            if not (0 <= self.end[0] < self.width and 0 <= self.end[1] < self.height):
                print(f"Erro: O ponto final {self.end} está fora do mapa.")
                return
            ids = IDS(self.map_matrix, self.start, self.end, self.terrain_costs)
            cost, path = ids.ids_search()
            if cost == float('inf'):
                print("Nenhum caminho encontrado.")
        elif self.method == "Astar":
            if not (0 <= self.start[0] < self.width and 0 <= self.start[1] < self.height):
                print(f"Erro: O ponto inicial {self.start} está fora do mapa.")
                return
            if not (0 <= self.end[0] < self.width and 0 <= self.end[1] < self.height):
                print(f"Erro: O ponto final {self.end} está fora do mapa.")
                return
            astar = AStar(self.map_matrix, self.start, self.end, self.terrain_costs)
            cost, path = astar.astar_search()
            if cost == float('inf'):
                print("Nenhum caminho encontrado.")
        elif self.method == "Greedy":
            if not (0 <= self.start[0] < self.width and 0 <= self.start[1] < self.height):
                print(f"Erro: O ponto inicial {self.start} está fora do mapa.")
                return
            if not (0 <= self.end[0] < self.width and 0 <= self.end[1] < self.height):
                print(f"Erro: O ponto final {self.end} está fora do mapa.")
                return
            greedy = Greedy(self.map_matrix, self.start, self.end, self.terrain_costs)
            cost, path = greedy.greedy_search()
            if cost == float('inf'):
                print("Nenhum caminho encontrado.")
        else:
            print(f"Método {self.method} não implementado ainda.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 7:
        print("Uso: python pathfinder.py [map_file] [method] [start_x] [start_y] [end_x] [end_y]")
        exit(1)
    map_file = sys.argv[1]
    method = sys.argv[2]
    start_x = int(sys.argv[3])
    start_y = int(sys.argv[4])
    end_x = int(sys.argv[5])
    end_y = int(sys.argv[6])
    pathfinder = PathFinder(map_file, method, start_x, start_y, end_x, end_y)
    pathfinder.load_map()
    pathfinder.run_search()
