# + BeesAlgorithm

# Atrybuty prywatne: - num_scouts: int, - num_best_sites: int, - num_elite_sites: int, - iterations: int

# Operacje prywatne:

# - _neighborhood_search(site: list[int], patch_size: int) -> list[int]

import random
from src.TSP_Problem import TSPProblem
from src.Optimization_Algorithm import OptimizationAlgorithm

class BeesAlgorithm(OptimizationAlgorithm):
    def __init__(self, problem: TSPProblem, num_scouts: int = 30, num_best_sites: int = 10,
                 num_elite_sites: int = 3, elite_foragers: int = 10, best_foragers: int = 5,
                 iterations: int = 100, patch_size: int = 1):
        super().__init__(problem)
        self._num_scouts = num_scouts
        self._num_best_sites = num_best_sites
        self._num_elite_sites = num_elite_sites
        self._elite_foragers = elite_foragers
        self._best_foragers = best_foragers
        self._iterations = iterations
        self._patch_size = patch_size

    def _generate_random_site(self) -> list[int]:
        route = list(range(self._problem.num_cities))
        random.shuffle(route)
        return route

    def _neighborhood_search(self, site: list[int], patch_size: int) -> list[int]:
        neighbor = site.copy()
        for _ in range(patch_size):
            i, j = random.sample(range(len(neighbor)), 2)
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
        return neighbor

    def _search_site(self, site: list[int], cost: float, num_foragers: int) -> list[int]:
        best_site, best_cost = site, cost
        for _ in range(num_foragers):
            neighbor = self._neighborhood_search(site, self._patch_size)
            neighbor_cost = self._problem.evaluate(neighbor)
            if neighbor_cost < best_cost:
                best_site, best_cost = neighbor, neighbor_cost
        return best_site

    def solve(self) -> tuple[list[int], float]:
        population = [self._generate_random_site() for _ in range(self._num_scouts)]
        best_route, best_cost = None, float('inf')

        for _ in range(self._iterations):
            fitnesses = sorted([(s, self._problem.evaluate(s)) for s in population], key=lambda x: x[1])

            if fitnesses[0][1] < best_cost:
                best_route, best_cost = fitnesses[0][0].copy(), fitnesses[0][1]

            next_generation = (
                [self._search_site(s, c, self._elite_foragers) for s, c in fitnesses[:self._num_elite_sites]] +
                [self._search_site(s, c, self._best_foragers) for s, c in fitnesses[self._num_elite_sites:self._num_best_sites]] +
                [self._generate_random_site() for _ in range(self._num_scouts - self._num_best_sites)]
            )

            population = next_generation

        return best_route, best_cost