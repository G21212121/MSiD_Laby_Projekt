# + SimulatedAnnealing

# Atrybuty prywatne: - initial_temp: float, - cooling_rate: float, - min_temp: float

# Operacje prywatne:

# - _generate_neighbor(current_route: list[int]) -> list[int] (np. zamiana dwóch miast miejscami - swap)
# - _acceptance_probability(current_cost: float, new_cost: float, temp: float) -> float

import math
import random
from src.TSP_Problem import TSPProblem
from src.Optimization_Algorithm import OptimizationAlgorithm

class SimulatedAnnealing(OptimizationAlgorithm):
    def __init__(self, problem: TSPProblem, initial_temp: float = 1000.0, cooling_rate: float = 0.99, min_temp: float = 0.01):
        super().__init__(problem)
        self._initial_temp = initial_temp
        self._cooling_rate = cooling_rate
        self._min_temp = min_temp

    def _generate_neighbor(self, route: list[int]) -> list[int]:
        neighbor = route.copy()
        i, j = random.sample(range(len(neighbor)), 2)
        neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
        return neighbor

    def solve(self) -> tuple[list[int], float]:
        current_route = list(range(self._problem.num_cities))
        random.shuffle(current_route)
        current_cost = self._problem.evaluate(current_route)
        best_route, best_cost = current_route.copy(), current_cost
        temp = self._initial_temp

        while temp > self._min_temp:
            neighbor = self._generate_neighbor(current_route)
            neighbor_cost = self._problem.evaluate(neighbor)

            accept = neighbor_cost < current_cost or math.exp((current_cost - neighbor_cost) / temp) > random.random()
            if accept:
                current_route, current_cost = neighbor, neighbor_cost
                if current_cost < best_cost:
                    best_route, best_cost = current_route.copy(), current_cost

            temp *= self._cooling_rate

        return best_route, best_cost