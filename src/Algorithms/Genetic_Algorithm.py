# + GeneticAlgorithm

# Atrybuty prywatne: - pop_size: int, - mutation_rate: float, - generations: int

# Operacje prywatne:

# - _selection(population: list, fitnesses: list) -> list[int] (np. selekcja turniejowa)
# - _crossover(parent1: list[int], parent2: list[int]) -> list[int] (np. Order Crossover - OX)
# - _mutate(route: list[int]) -> list[int]