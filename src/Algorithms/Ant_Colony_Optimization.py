# + AntColonyOptimization

# Atrybuty prywatne: - num_ants: int, - evaporation_rate: float, - alpha: float, - beta: float, - pheromone_matrix: list[list[float]]

# Operacje prywatne:

# - _construct_solution() -> list[int] (prawdopodobieństwo wyboru kolejnego miasta na podstawie feromonów i heurystyki)
# - _update_pheromones(all_routes: list, all_costs: list)