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
from src.Optimization_Algorithm import OptimizationAlgorithm


# Klasa zarządzająca eksperymentami i uruchamianiem algorytmów:

class SimulationRunner:
    def __init__(self, algorithms: list[OptimizationAlgorithm], num_runs: int):
        self._algorithms = algorithms
        self._num_runs = num_runs


    # Wykonuje pętle po algorytmach i mierzy wyniki i czas i zbiera dane w słownik:
    def run_all(self) -> dict:
        results = {}

        for algo in self._algorithms:
            algo_name = algo.__class__.__name__         # Pobiera nazwę klasy algorytmu:

            best_cost = float('inf')
            total_cost = 0.0
            total_time = 0.0

            for i in range(self._num_runs):
                # Mierzenie czasu:
                start_time = time.perf_counter()
                _, current_cost = algo.solve()
                end_time = time.perf_counter()

                run_time = end_time - start_time

                # Zbieranie statystyk
                total_time += run_time
                total_cost += current_cost
                if current_cost < best_cost:
                    best_cost = current_cost

            # Obliczanie średnich
            avg_cost = total_cost / self._num_runs
            avg_time = total_time / self._num_runs

            # Zapisuje do słownika wyników
            results[algo_name] = {
                "best_cost": best_cost,
                "avg_cost": avg_cost,
                "avg_time": avg_time,
                "total_time": total_time
            }

        return results



    # Generuję sformatowaną tabelę z wynikami:
    def display_results_table(self, results: dict):
        print("\n" + "=" * 115)
        print(" PODSUMOWANIE ")
        print("=" * 115 + "\n")

        # Nagłówek tabeli
        header = f"| {'Nazwa algorytmu':<25} | {'NAJLEPSZY WYNIK':<17} | {'ŚREDNI WYNIK':<15} | {'ŚREDNI CZAS (s)':<15} | {'CAŁKOWITY CZAS (s)':<18} |"
        print(header)
        print("-" * 115)

        # Wypisywanie wierszy z danymi
        for name, stats in results.items():
            row = (f"| {name:<25} | "
                   f"{stats['best_cost']:<17.2f} | "
                   f"{stats['avg_cost']:<15.2f} | "
                   f"{stats['avg_time']:<15.4f} | "
                   f"{stats['total_time']:<18.4f} |")
            print(row)

        print("-" * 115 + "\n")





# Funkcja główna - uruchamia powyższe funkcję i wyświetla:
def main():
    # 1. Inicjalizacja problemu:
    num_cities = 20

    problem = TSPProblem(
        num_cities=num_cities,                      # Liczba miast
        min_x=0.0,                          # Zakres współrzędnych:
        max_x=100.0,
        min_y=0.0,
        max_y=100.0,
    )

    print(f"Problem komiwojazera (TSP) dla {num_cities} miast.\n\n")



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


    # Lista algorytmów:
    algorithms_list = [ga_solver]



    # 3. Konfiguracją i uruchomienie Runner'a:
    n = 10          # Liczbia uruchomień algorytmów

    runner = SimulationRunner(algorithms=algorithms_list, num_runs=n)

    results = runner.run_all()



    # 4. Wyświetlenie wyników:
    runner.display_results_table(results)



if __name__ == "__main__":
    main()
