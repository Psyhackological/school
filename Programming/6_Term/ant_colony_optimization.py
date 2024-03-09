"""
Use an ant colony optimization algorithm to solve the travelling salesman problem (TSP)
which asks the following question:
"Given a list of cities and the distances between each pair of cities, what is the
 shortest possible route that visits each city exactly once and returns to the origin
 city?"

https://en.wikipedia.org/wiki/Ant_colony_optimization_algorithms
https://en.wikipedia.org/wiki/Travelling_salesman_problem
"""

import copy
import random


def main(
    cities: dict[str, tuple[int, int]],
    start_city: str,
    ants_num: int,
    iterations_num: int,
    pheromone_evaporation: float,
    alpha: float,
    beta: float,
    q: float,  # Pheromone system parameters Q，which is a constant
) -> tuple[list[str], float]:
    """
    Ant colony algorithm main function
    >>> main(cities=cities, ants_num=10, iterations_num=20,
    ...      pheromone_evaporation=0.7, alpha=1.0, beta=5.0, q=10)
    ([0, 1, 2, 3, 4, 5, 6, 7, 0], 37.909778143828696)
    >>> main(cities={0: [0, 0], 1: [2, 2]}, ants_num=5, iterations_num=5,
    ...      pheromone_evaporation=0.7, alpha=1.0, beta=5.0, q=10)
    ([0, 1, 0], 5.656854249492381)
    >>> main(cities={0: [0, 0], 1: [2, 2], 4: [4, 4]}, ants_num=5, iterations_num=5,
    ...      pheromone_evaporation=0.7, alpha=1.0, beta=5.0, q=10)
    Traceback (most recent call last):
      ...
    IndexError: list index out of range
    >>> main(cities={}, ants_num=5, iterations_num=5,
    ...      pheromone_evaporation=0.7, alpha=1.0, beta=5.0, q=10)
    Traceback (most recent call last):
      ...
    StopIteration
    >>> main(cities={0: [0, 0], 1: [2, 2]}, ants_num=0, iterations_num=5,
    ...      pheromone_evaporation=0.7, alpha=1.0, beta=5.0, q=10)
    ([], inf)
    >>> main(cities={0: [0, 0], 1: [2, 2]}, ants_num=5, iterations_num=0,
    ...      pheromone_evaporation=0.7, alpha=1.0, beta=5.0, q=10)
    ([], inf)
    >>> main(cities={0: [0, 0], 1: [2, 2]}, ants_num=5, iterations_num=5,
    ...      pheromone_evaporation=1, alpha=1.0, beta=5.0, q=10)
    ([0, 1, 0], 5.656854249492381)
    >>> main(cities={0: [0, 0], 1: [2, 2]}, ants_num=5, iterations_num=5,
    ...      pheromone_evaporation=0, alpha=1.0, beta=5.0, q=10)
    ([0, 1, 0], 5.656854249492381)
    """
    # Initialize the pheromone matrix
    # Initialize the pheromone matrix as a dictionary of dictionaries
    pheromone = {city: {other_city: 1.0 for other_city in cities}
                 for city in cities}

    best_path: list[str] = []
    best_distance = float("inf")

    for _ in range(iterations_num):
        ants_route = []
        for _ in range(ants_num):
            unvisited_cities = copy.copy(cities)
            current_city = start_city if start_city in cities else random.choice(
                list(unvisited_cities.keys()))
            del unvisited_cities[current_city]
            ant_route = [current_city]

            while unvisited_cities:
                current_city, unvisited_cities = city_select(
                    pheromone,
                    current_city,
                    unvisited_cities,
                    alpha,
                    beta,
                )
                ant_route.append(current_city)
            ant_route.append(ant_route[0])
            ants_route.append(ant_route)

        pheromone, best_path, best_distance = pheromone_update(
            pheromone,
            cities,
            pheromone_evaporation,
            ants_route,
            q,
            best_path,
            best_distance,
        )

    return best_path, best_distance


def distance(city1: tuple[int, int], city2: tuple[int, int]) -> float:
    """
    Calculate the distance between two coordinate points
    >>> distance( (0, 0), (3, 4) )
    5.0
    >>> distance( (0, 0), (-3, 4) )
    5.0
    >>> distance( (0, 0), (-3, -4) )
    5.0
    """
    return (((city1[0] - city2[0]) ** 2) + ((city1[1] - city2[1]) ** 2)) ** 0.5


def pheromone_update(
    pheromone: dict[str, dict[str, float]],
    cities: dict[str, tuple[int, int]],
    pheromone_evaporation: float,
    ants_route: list[list[str]],
    q: float,  # Pheromone system parameters Q，which is a constant
    best_path: list[str],
    best_distance: float,
) -> tuple[dict[str, dict[str, float]], list[str], float]:
    """
    Update pheromones on the route and update the best route
    >>>
    >>> pheromone_update(pheromone=[[1.0, 1.0], [1.0, 1.0]],
    ...                  cities={0: [0,0], 1: [2,2]}, pheromone_evaporation=0.7,
    ...                  ants_route=[[0, 1, 0]], q=10, best_path=[],
    ...                  best_distance=float("inf"))
    ([[0.7, 4.235533905932737], [4.235533905932737, 0.7]], [0, 1, 0], 5.656854249492381)
    >>> pheromone_update(pheromone=[],
    ...                  cities={0: [0,0], 1: [2,2]}, pheromone_evaporation=0.7,
    ...                  ants_route=[[0, 1, 0]], q=10, best_path=[],
    ...                  best_distance=float("inf"))
    Traceback (most recent call last):
      ...
    IndexError: list index out of range
    >>> pheromone_update(pheromone=[[1.0, 1.0], [1.0, 1.0]],
    ...                  cities={}, pheromone_evaporation=0.7,
    ...                  ants_route=[[0, 1, 0]], q=10, best_path=[],
    ...                  best_distance=float("inf"))
    Traceback (most recent call last):
      ...
    KeyError: 0
    """
    for city1 in cities:
        for city2 in cities:
            pheromone[city1][city2] *= pheromone_evaporation

    for ant_route in ants_route:
        total_distance = 0.0
        for i in range(len(ant_route) - 1):  # Calculate total distance
            total_distance += distance(cities[ant_route[i]],
                                       cities[ant_route[i + 1]])

        delta_pheromone = q / total_distance

        for i in range(len(ant_route) - 1):  # Update pheromones
            pheromone[ant_route[i]][ant_route[i + 1]] += delta_pheromone
            pheromone[ant_route[i + 1]][ant_route[i]] = pheromone[ant_route[i]][
                ant_route[i + 1]
            ]

        if total_distance < best_distance:
            best_path = ant_route
            best_distance = total_distance

    return pheromone, best_path, best_distance


def city_select(
    pheromone: dict[str, dict[str, float]],
    current_city: str,
    unvisited_cities: dict[str, tuple[int, int]],
    alpha: float,
    beta: float,
) -> tuple[str, dict[str, tuple[int, int]]]:
    """
    Choose the next city for ants
    >>> city_select(pheromone=[[1.0, 1.0], [1.0, 1.0]], current_city={0: [0, 0]},
    ...             unvisited_cities={1: [2, 2]}, alpha=1.0, beta=5.0)
    ({1: [2, 2]}, {})
    >>> city_select(pheromone=[], current_city={0: [0,0]},
    ...             unvisited_cities={1: [2, 2]}, alpha=1.0, beta=5.0)
    Traceback (most recent call last):
      ...
    IndexError: list index out of range
    >>> city_select(pheromone=[[1.0, 1.0], [1.0, 1.0]], current_city={},
    ...             unvisited_cities={1: [2, 2]}, alpha=1.0, beta=5.0)
    Traceback (most recent call last):
      ...
    StopIteration
    >>> city_select(pheromone=[[1.0, 1.0], [1.0, 1.0]], current_city={0: [0, 0]},
    ...             unvisited_cities={}, alpha=1.0, beta=5.0)
    Traceback (most recent call last):
      ...
    IndexError: list index out of range
    """
    probabilities = []
    city_probabilities = {}
    for city in unvisited_cities:
        city_distance = distance(
            unvisited_cities[city],
            unvisited_cities[current_city]
            if current_city in unvisited_cities
            else cities[current_city],
        )
        probability = (pheromone[current_city][city] ** alpha) * (
            (1 / city_distance) ** beta
        )
        probabilities.append(probability)
        city_probabilities[city] = probability

    chosen_city = random.choices(
        list(unvisited_cities.keys()),
        weights=probabilities,
    )[0]
    del unvisited_cities[chosen_city]
    return chosen_city, unvisited_cities


if __name__ == "__main__":
    cities = {
        "A": (0, 0),
        "D": (1, 8),
        "F": (2, 10),
        "G": (3, 3),
        "B": (4, 7),
        "E": (6, 4),
        "C": (8, 13),
    }

    start_city = 'A'

    best_path, best_distance = main(
        cities=cities,  # Miasta - Nodes w Grafie
        start_city=start_city,  # Miasto poczatkowe - czyli start
        ants_num=len(cities),  # Liczba mrowek - proporcjonalnie do miast
        iterations_num=1000,  # Liczba iteracji - dlugosc znajdywania optymalnego rozwiazania
        # Wspolczynnik wyparowania feromonu - balansujacy czynnik przy wyborze sciezek
        pheromone_evaporation=0.7,
        alpha=1.0,  # Wplyw feromonu - rownowaga eksploracji i eksploatacji
        beta=5.0,  # Wplyw heurestyki - preferuje blizsze miasta
        q=10,  # Stala feromonu - ilosc pozostawianego feromonu
    )

    print(f"Best path starting from '{best_path[0]}': {best_path}")
    print(f"Best distance: {best_distance}")
