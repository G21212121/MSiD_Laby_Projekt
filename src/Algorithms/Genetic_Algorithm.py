# + GeneticAlgorithm

# Atrybuty prywatne: - pop_size: int, - mutation_rate: float, - generations: int

# Operacje prywatne:

# - _selection(population: list, fitnesses: list) -> list[int] (np. selekcja turniejowa)
# - _crossover(parent1: list[int], parent2: list[int]) -> list[int] (np. Order Crossover - OX)
# - _mutate(route: list[int]) -> list[int]

# ======================================================================================================================

import random
from src.Optimization_Algorithm import OptimizationAlgorithm
from src.TSP_Problem import TSPProblem

# Implementacja algorytmu genetycznego dla problemu komiwojażera (TSP):

class GeneticAlgorithm(OptimizationAlgorithm):
    def __init__(self, problem: TSPProblem, pop_size: int=100, mutation_rate: float=0.1, generations: int=200, selection_size: int=2):
        super().__init__(problem)
        self._pop_size = pop_size
        self._mutation_rate = mutation_rate
        self._generations = generations
        self._selection_size = selection_size

    # Stworzenie losowego osobnika (permutację miast):
    def _create_individual(self) -> list[int]:
        route = list(range(self._problem.num_cities))
        random.shuffle(route)
        return route



    # Selekcja turniejowa dla losowych osobników o ilości: selection_size zwraca najlepszego:
    def _selection(self, population: list[list[int]], fitness: list[float]) -> list[int]:
        best_idx = -1
        best_fitness = float('inf')

        for _ in range(self._selection_size):
            idx = random.randint(0, self._pop_size - 1)

            if fitness[idx] < best_fitness:
                best_fitness = fitness[idx]
                best_idx = idx

        return population[best_idx]



    # Krzyżowanie:
    def _crossover(self, parent1: list[int], parent2: list[int]) -> list[int]:
        size = len(parent1)

        # Losowanie 2 pkt. przecięcia:
        start, end = sorted(random.sample(range(size), 2))


        # F. pom - stworzenie dziecka:
        def make_child(p1: list[int], p2: list[int]) -> list[int]:
            child = [-1]*size

            # Kopiowanie rdzenia z pierwszego rodzica:
            child[start:end+1] = p1[start:end+1]

            # Uzupełnienie z drugiego rodzica:
            p2_idx = 0
            for i in range(size):
                if child[i] == -1:
                    while p2[p2_idx] in child:
                        p2_idx += 1
                    child[i] = p2[p2_idx]

            return child


        # Stworzenie 2 dzieci (child1: p1-p2, child2: p2-p1):
        child1 = make_child(parent1, parent2)
        child2 = make_child(parent2, parent1)

        return child1, child2



    # Mutacja - dla mutation_rate zamieniamy miejsca 2 miastom:
    def _mutate(self, route: list[int]) -> None:
        if random.random() < self._mutation_rate:
            idx1, idx2 = random.sample(range(len(route)), 2)
            route[idx1], route[idx2] = route[idx2], route[idx1]



    # Pętla, która szuka osobnika z najlepszym fitnessem:
    def solve(self) -> tuple[list[int], float]:
        population = [self._create_individual() for _ in range(self._pop_size)]         # Inicjalizacja populacji początkowej:

        global_best_route = None
        global_best_fitness = float('inf')

        for generation in range(self._generations):
            # Ewaluacja przystosowania danego osobnika (im niższe tym lepsze):
            fitnesses = [self._problem.evaluate(individual) for individual in population ]

            # Aktualizacja globalnego najlepszego rozwiązania:
            current_best_fitness = min(fitnesses)
            if current_best_fitness < global_best_fitness:
                global_best_fitness = current_best_fitness
                best_idx = fitnesses.index(current_best_fitness)
                global_best_route = population[best_idx].copy()


            # Nowa populacja:
            new_population = []

            for _ in range(0, self._pop_size, 2):
                p1 = self._selection(population, fitnesses)
                p2 = self._selection(population, fitnesses)

                child1, child2 = self._crossover(p1, p2)

                self._mutate(child1)
                self._mutate(child2)

                new_population.append(child1)
                new_population.append(child2)

            # Zastąpienie starej populacji nową:
            population = new_population[:self._pop_size]        # Ucięcie na wypadek gdyby rozmiar populacji był nieparzysty


        return global_best_route, global_best_fitness