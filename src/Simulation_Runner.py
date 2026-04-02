# + SimulationRunner (Klasa zarządzająca eksperymentami)

# Atrybuty:

# - algorithms: list[OptimizationAlgorithm]
# - num_runs: int

# Operacje:

# + run_all() -> dict (wykonuje pętlę po algorytmach i liczbie uruchomień, mierzy czas, zbiera wyniki)
# + display_results_table(results: dict) (generuje tabelę wymaganą w specyfikacji)