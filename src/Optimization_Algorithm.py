# + OptimizationAlgorithm (Klasa abstrakcyjna / Interfejs)

# Atrybuty:

# # problem: TSPProblem (asocjacja do problemu)

# Operacje:

# + solve() -> tuple[list[int], float] (metoda abstrakcyjna zwracająca najlepszą trasę i jej koszt)

# ======================================================================================================================

from abc import ABC, abstractmethod
from TSP_Problem import TSPProblem

# Abstrakcyjna klasa bazowa dla wszystkich algorytmów metaheurystycznych:

class OptimizationAlgorithm(ABC):
    def __init__(self, problem: TSPProblem):
        self._problem: TSPProblem = problem

    # Metoda abstrakcyjną, którą musi zaimplementować każdy algorytm
    @abstractmethod
    def solve(self) -> tuple[list[int], float]:     # Zwraca krotkę (najlepsza trasa, całkowity koszt)
        pass