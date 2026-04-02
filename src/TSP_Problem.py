# + TSPProblem (Klasa definiująca dziedzinę problemu)

# Atrybuty:

# - distance_matrix: list[list[float]] (macierz odległości między miastami)
# - num_cities: int

# Operacje:

# + __init__(num_cities: int) (konstruktor generujący losowe punkty i macierz lub wczytujący z pliku)
# + evaluate(route: list[int]) -> float (funkcja celu: liczy całkowity dystans trasy)