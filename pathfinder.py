from bfs import BFS
from ids import IDS
from ucs import UCS
from astar import AStar

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
            '.': 1.0,   # Grama
            ';': 1.5,   # Grama Alta
            '+': 2.5,   # Água
            'x': 6.0,   # Fogo
            '@': float('inf')  # Parede
        }

    def load_map(self):
        """Carrega o mapa do arquivo especificado."""
        try:
            with open(self.map_file, 'r') as file:
                # Lê dimensões do mapa
                self.width, self.height = map(int, file.readline().split())
                
                # Lê a matriz do mapa
                for _ in range(self.height):
                    row = file.readline().strip()
                    self.map_matrix.append(list(row))
                
        except FileNotFoundError:
            print(f"Erro: Arquivo '{self.map_file}' não encontrado.")
            exit(1)
        except Exception as e:
            print(f"Erro ao carregar o mapa: {e}")
            exit(1)

    def log_state(self):
        """Exibe os dados carregados para verificação."""
        print(f"Mapa: {self.map_file}")
        print(f"Método: {self.method}")
        print(f"Ponto inicial: {self.start}")
        print(f"Ponto final: {self.end}")
        print(f"Dimensões: {self.width}x{self.height}")
        print("Mapa carregado:")
        for row in self.map_matrix:
            print("".join(row))

    def run_search(self):
        """Executa o método de busca selecionado."""
        if self.method == "BFS":
            print("Executando BFS...")
            # Verifica se os pontos inicial e final estão dentro do mapa
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
            else:
                print(f"Custo total: {cost}")
                print(f"Caminho: {path}")

        elif self.method == "UCS":
            print("Executando UCS...")
            # Verifica se os pontos inicial e final estão dentro do mapa
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
            else:
                print(f"Custo total: {cost}")
                print(f"Caminho: {path}")
        elif self.method == "IDS":
            print("Executando IDS...")
            # Verifica se os pontos inicial e final estão dentro do mapa
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
            else:
                print(f"Custo total: {cost}")
                print(f"Caminho: {path}")
        else:
            print(f"Método {self.method} não implementado ainda.")



# Lê os argumentos de entrada
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) != 7:
        print("Uso: python pathfinder.py [map_file] [method] [start_x] [start_y] [end_x] [end_y]")
        exit(1)
    
    # Argumentos da linha de comando
    map_file = sys.argv[1]
    method = sys.argv[2]
    start_x = int(sys.argv[3])
    start_y = int(sys.argv[4])
    end_x = int(sys.argv[5])
    end_y = int(sys.argv[6])

    # Criação da instância e carregamento do mapa
    pathfinder = PathFinder(map_file, method, start_x, start_y, end_x, end_y)
    pathfinder.load_map()

    # Log dos dados carregados
    pathfinder.log_state()

    # Executa o método de busca selecionado
    pathfinder.run_search()
