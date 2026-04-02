# + SimulatedAnnealing

# Atrybuty prywatne: - initial_temp: float, - cooling_rate: float, - min_temp: float

# Operacje prywatne:

# - _generate_neighbor(current_route: list[int]) -> list[int] (np. zamiana dwóch miast miejscami - swap)
# - _acceptance_probability(current_cost: float, new_cost: float, temp: float) -> float