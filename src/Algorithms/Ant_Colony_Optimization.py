# + AntColonyOptimization

# Atrybuty prywatne: - num_ants: int, - evaporation_rate: float, - alpha: float, - beta: float, - pheromone_matrix: list[list[float]]

# Operacje prywatne:

# - _construct_solution() -> list[int] (prawdopodobieństwo wyboru kolejnego miasta na podstawie feromonów i heurystyki)
# - _update_pheromones(all_routes: list, all_costs: list)

import random
from src.TSP_Problem import TSPProblem
from src.Optimization_Algorithm import OptimizationAlgorithm


class AntColonyOptimization(OptimizationAlgorithm):
    def __init__(self, problem: TSPProblem, num_ants: int = 20, evaporation_rate: float = 0.1,
                 alpha: float = 1.0, beta: float = 2.0, iterations: int = 100):
        super().__init__(problem)
        self._num_ants = num_ants
        self._evaporation_rate = evaporation_rate
        self._alpha = alpha
        self._beta = beta
        self._iterations = iterations
        n = self._problem.num_cities
        self._pheromone_matrix = [[1.0] * n for _ in range(n)]

    def _construct_solution(self) -> list[int]:
        unvisited = list(range(self._problem.num_cities))
        route = [random.choice(unvisited)]
        unvisited.remove(route[0])

        while unvisited:
            current = route[-1]
            probs = []
            for city in unvisited:
                d = self._problem.dist_matrix[current][city]
                p = (self._pheromone_matrix[current][city] ** self._alpha) * ((1.0 / d) ** self._beta if d > 0 else 0)
                probs.append((city, p))

            total = sum(p for _, p in probs)
            if total == 0:
                route.append(random.choice(unvisited))
            else:
                rand_val, cumulative = random.uniform(0, total), 0.0
                for city, p in probs:
                    cumulative += p
                    if cumulative >= rand_val:
                        route.append(city)
                        break

            unvisited.remove(route[-1])

        return route

    def _update_pheromones(self, all_routes: list[list[int]], all_costs: list[float]) -> None:
        n = self._problem.num_cities
        for i in range(n):
            for j in range(n):
                self._pheromone_matrix[i][j] *= (1.0 - self._evaporation_rate)

        for route, cost in zip(all_routes, all_costs):
            deposit = 100.0 / cost
            for i in range(n):
                a, b = route[i], route[(i + 1) % n]
                self._pheromone_matrix[a][b] += deposit
                self._pheromone_matrix[b][a] += deposit

    def solve(self) -> tuple[list[int], float]:
        best_route, best_cost = None, float('inf')

        for _ in range(self._iterations):
            all_routes, all_costs = [], []
            for _ in range(self._num_ants):
                route = self._construct_solution()
                cost = self._problem.evaluate(route)
                all_routes.append(route)
                all_costs.append(cost)
                if cost < best_cost:
                    best_route, best_cost = route.copy(), cost

            self._update_pheromones(all_routes, all_costs)

        return best_route, best_cost