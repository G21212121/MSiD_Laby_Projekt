# + SimulationRunner (Klasa zarządzająca eksperymentami)

# Atrybuty:

# - algorithms: list[OptimizationAlgorithm]
# - num_runs: int

# Operacje:

# + run_all() -> dict (wykonuje pętlę po algorytmach i liczbie uruchomień, mierzy czas, zbiera wyniki)
# + display_results_table(results: dict) (generuje tabelę wymaganą w specyfikacji)

# ======================================================================================================================

import time
from TSP_Problem import TSPProblem
from Algorithms.Genetic_Algorithm import GeneticAlgorithm


# Funkcja do uruchamiania i testowania algorytmów dla problemu komiwojażęra (TSP):

def main():
    # 1. Inicjalizacja problemu:
    problem = TSPProblem(
        num_cities=20,                      # Liczba miast
        min_x=0.0,                          # Zakres współrzędnych:
        max_x=100.0,
        min_y=0.0,
        max_y=100.0,
    )


    # 2. Tworzenie instacji algorytmów metaheurystycznych:

    # a) Simulated Annealing:


    # b) Genetic Algorithm:
    ga_solver = GeneticAlgorithm(
        problem=problem,
        pop_size=100,
        mutation_rate=0.2,
        generations=200,
        selection_size=2
    )

    # c) Ant Colony Optimization:


    # d) Bees Algorithm:



    # 3. Przygotowanie statystyk:

    # a) Simulated Annealing:


    # b) Genetic Algorithm:
    start_time_ga = time.perf_counter()
    best_route_ga, best_cost_ga = ga_solver.solve()
    end_time_ga = time.perf_counter()

    execution_time_ga = end_time_ga - start_time_ga

    # c) Ant Colony Optimization:


    # d) Bees Algorithm:



    # 4. Wyświetlenie statystyk:

    # a) Simulated Annealing:


    # b) Genetic Algorithm:
    print("-" * 40)
    print("WYNIKI Algorytmu Genetycznego:")
    print("-" * 40)
    print(f"Najlepszy wynik (dystans): {best_cost_ga:.2f}")
    print(f"Najlepsza trasa: {best_route_ga}")
    print(f"Czas wykonywania: {execution_time_ga:.4f}")
    print("-" * 40 + "\n")

    # c) Ant Colony Optimization:


    # d) Bees Algorithm:



if __name__ == "__main__":
    main()
