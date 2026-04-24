# + TSPProblem (Klasa definiująca dziedzinę problemu)

# Atrybuty:

# - distance_matrix: list[list[float]] (macierz odległości między miastami)
# - num_cities: int

# Operacje:

# + __init__(num_cities: int) (konstruktor generujący losowe punkty i macierz lub wczytujący z pliku)
# + evaluate(route: list[int]) -> float (funkcja celu: liczy całkowity dystans trasy)

# ======================================================================================================================

import math
import random

# Klasa reprezentująca problem komiwojażera (TSP):

class TSPProblem:

    # Konstruktor:
    def __init__(self, num_cities: int, min_x: float=0.0, max_x: float=100.0, min_y: float=0.0, max_y: float=100.0):
        self._num_cities = num_cities

        # Minimalne i maksymalne współrzędne dla miast:
        self._min_x = min_x
        self._max_x = max_x
        self._min_y = min_y
        self._max_y = max_y

        self._city_coords: list[tuple[float, float]] = [
            (random.uniform(min_x, max_x), random.uniform(min_y, max_y))
            for _ in range(num_cities)
        ]

        # Inicjalizacja macierzy odległości:
        self._dist_matrix: list[list[float]] = self._calculate_distance_matrix()



    @property
    def num_cities(self) -> int:                        # Zwraca liczbę miast
        return self._num_cities

    @property
    def dist_matrix(self) -> list[list[float]]:         # Zwraca macierz odległości
        return self._dist_matrix



    # Metoda, obliczająca odległości euklidesowe między wszystkimi parami współrzędnych:
    def _calculate_distance_matrix(self) -> list[list[float]]:
        matrix = [[0.0] * self._num_cities for _ in range(self._num_cities)]

        for i in range(self._num_cities):
            for j in range(self._num_cities):
                if i != j:
                    x1, y1 = self._city_coords[i]
                    x2, y2 = self._city_coords[j]

                    # math.hypot - obliczanie odległości euklidesowej
                    dist = math.hypot(x1 - x2, y1 - y2)
                    matrix[i][j] = dist

        return matrix



    # Funkcja celu: Oblicza całkowitą długość trasy:
    def evaluate(self, route: list[int]) -> float:
        if len(route) != self._num_cities:
            raise ValueError("Error: Invalid number of cities provided.")

        if len(set(route)) != self._num_cities:
            raise ValueError("Error: Invalid status of cities provided (duplicated or missing cities).")

        total_distance = 0.0
        for i in range(self._num_cities):
            current_city = route[i]
            next_city = route[(i + 1) % self._num_cities]           # % - zapewnia powrót do pkt. 0
            total_distance += self._dist_matrix[current_city][next_city]

        return total_distance


