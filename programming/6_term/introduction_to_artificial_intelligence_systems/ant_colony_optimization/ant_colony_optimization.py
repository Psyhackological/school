from __future__ import annotations  # For linter satisfaction to annotations
import copy  # Allows for creating copies of objects
import random  # Provides functionalities for generating random numbers
from pprint import pprint as pp  # For pretty printing
import os  # For working with environement variables

# Main function to run the ant colony optimization


def main(
    # Dictionary of cities and their coordinates
    # Starting city for the ants
    cities: dict[str, tuple[int, int]],
    start_city: str,
    ants_num: int,  # Number of ants used in the simulation
    iterations_num: int,  # Number of iterations to perform
    pheromone_evaporation: float,  # Rate at which pheromone evaporates
    alpha: float,  # Influence of pheromone trails on the probability of selecting the next city
    beta: float,  # Influence of city distance on the probability of selecting the next city
    q: float,  # Constant used in pheromone update rule
) -> tuple[list[str], float]:  # Returns the best path found and its distance
    # Initialize pheromone levels between cities
    pheromone = {city: {other_city: 1.0 for other_city in cities}
                 for city in cities}

    best_path: list[str] = []  # Store the best path found
    best_distance = float("inf")  # Initialize the best distance with infinity

    # Perform the main loop of the algorithm
    for _ in range(iterations_num):
        ants_route = []  # List to store routes taken by all ants
        # Generate routes for each ant
        for _ in range(ants_num):
            # Copy of the cities to keep track of unvisited ones
            unvisited_cities = copy.copy(cities)
            # Determine the starting city for the ant
            current_city = (
                start_city
                if start_city in cities
                else random.choice(list(unvisited_cities.keys()))
            )
            # Remove the start city from the unvisited list
            del unvisited_cities[current_city]
            # Initialize the route with the starting city
            ant_route = [current_city]

            # Construct the route for the ant
            while unvisited_cities:
                current_city, unvisited_cities = city_select(
                    pheromone, current_city, unvisited_cities, alpha, beta
                )
                # Append the selected city to the route
                ant_route.append(current_city)
            # Complete the tour by returning to the start city
            ant_route.append(ant_route[0])
            ants_route.append(ant_route)  # Add the route to the list of routes

        # Update the pheromone levels based on the routes taken by the ants
        pheromone, best_path, best_distance = pheromone_update(
            pheromone,
            cities,
            pheromone_evaporation,
            ants_route,
            q,
            best_path,
            best_distance,
        )

    return best_path, best_distance  # Return the best path and its distance


# Function to calculate the Euclidean distance between two cities


def distance(city1: tuple[int, int], city2: tuple[int, int]) -> float:
    # Pythagorean theorem a^2 + b^2 = c^2
    return (((city1[0] - city2[0]) ** 2) + ((city1[1] - city2[1]) ** 2)) ** 0.5


# Function to update the pheromone levels after all ants have completed their routes


def pheromone_update(
    pheromone: dict[str, dict[str, float]],
    cities: dict[str, tuple[int, int]],
    pheromone_evaporation: float,
    ants_route: list[list[str]],
    q: float,  # Pheromone system parameters Q, constant
    best_path: list[str],
    best_distance: float,
) -> tuple[dict[str, dict[str, float]], list[str], float]:
    # Evaporate pheromone
    for city1 in cities:
        for city2 in cities:
            pheromone[city1][city2] *= pheromone_evaporation

    # Update pheromone based on routes taken by ants
    for ant_route in ants_route:
        total_distance = sum(
            distance(cities[ant_route[i]], cities[ant_route[i + 1]])
            for i in range(len(ant_route) - 1)
        )
        delta_pheromone = q / total_distance  # Calculate the pheromone to be added
        # Add pheromone to the paths taken by the ant
        for i in range(len(ant_route) - 1):
            pheromone[ant_route[i]][ant_route[i + 1]] += delta_pheromone
            pheromone[ant_route[i + 1]][ant_route[i]] += (
                delta_pheromone  # Symmetric update
            )

        # Update best path if a better one is found
        if total_distance < best_distance:
            best_path = ant_route
            best_distance = total_distance

    # Return updated pheromone, best path, and its distance
    return pheromone, best_path, best_distance


# Function to select the next city for an ant based on pheromone levels and distances


def city_select(
    pheromone: dict[str, dict[str, float]],
    current_city: str,
    unvisited_cities: dict[str, tuple[int, int]],
    alpha: float,
    beta: float,
) -> tuple[str, dict[str, tuple[int, int]]]:
    # Calculate the probabilities for moving to each unvisited city
    probabilities = []
    city_probabilities = {}
    for city in unvisited_cities:
        # Calculate probability based on pheromone and distance
        city_distance = (
            distance(unvisited_cities[current_city], unvisited_cities[city])
            if current_city in unvisited_cities
            else distance(cities[current_city], unvisited_cities[city])
        )
        probability = (pheromone[current_city][city] ** alpha) * (
            (1 / city_distance) ** beta
        )
        probabilities.append(probability)
        city_probabilities[city] = probability

    # Select the next city based on calculated probabilities
    chosen_city = random.choices(
        list(unvisited_cities.keys()), weights=probabilities)[0]
    # Remove the chosen city from unvisited cities
    del unvisited_cities[chosen_city]
    # Return the chosen city and the updated unvisited cities list
    return chosen_city, unvisited_cities


def generate_cities(ask_for_input: bool) -> tuple[str, dict[str, tuple[int, int]]]:
    # Default values from my mapa
    if not ask_for_input:
        # Predefined set of example cities with their coordinates
        return "A", {
            "A": (0, 0), "D": (1, 8), "F": (2, 10),
            "G": (3, 3), "B": (4, 7), "E": (6, 4), "C": (8, 13),
        }

    # Otherwise let's go
    # Empty dict for "appending" city with x, y values
    city_data: dict[str, tuple[int, int]] = {}
    # Use q to quit
    while True:
        user_input = input(
            "Podaj miasto w formacie 'CityName X Y' ('q' by wyjsc): ")
        # Ensuring lower so the condition can be easily checked
        if user_input.lower() == "q":
            break

        try:
            # Get 3 values
            city, x, y = user_input.split()
            # Create a pair
            pair = int(x), int(y)

            if pair in city_data.values():
                print("Te koordynaty juz istnieja. Daj cos innego.")
                continue

            city_data[city] = pair
        except (ValueError, TypeError):
            print("Zly format. Uzyj formatu 'CityName X Y'.")
        except Exception as e:
            print(f"Wystapil dziwny error, ktorego nie zlapalem: {e}")

    # Show city_data for choosing staring point
    pp(city_data)
    start_city = input("Poczatkowe miasto?: ")
    # I don't want to play, so I will choose it myself
    if start_city not in city_data:
        start_city = random.choice(list(city_data.keys()))

    return start_city, city_data


# Entry point of the script
if __name__ == "__main__":
    ASK_FOR_INPUT = os.environ.get('INPUT')
    ask_for_input = True if ASK_FOR_INPUT and ASK_FOR_INPUT.lower() == "yes" else False
    start_city, cities = generate_cities(ask_for_input)
    print("Twoje miasta:")
    pp(cities, indent=4)

    # Execute the main function to find the best path and its distance
    best_path, best_distance_value = main(
        cities=cities,  # Miasta - Nodes w Grafie
        start_city=start_city,  # Miasto poczatkowe - czyli start
        # Liczba mrowek - odkrywanie nowych tras ale srednio to dziala
        ants_num=len(cities) * 2,
        iterations_num=1200,  # Liczba iteracji - dlugosc znajdywania optymalnego rozwiazania
        # Wspolczynnik wyparowania feromonu - balansujacy czynnik przy wyborze sciezek
        pheromone_evaporation=0.7,
        alpha=1.0,  # Wplyw feromonu - rownowaga eksploracji i eksploatacji
        beta=5.0,  # Wplyw heurestyki - preferuje blizsze miasta
        q=10,  # Stala feromonu - ilosc pozostawianego feromonu
    )

    # Output the best path and its distance
    print(f"{best_distance_value} distance for {' -> '.join(best_path)}", end="")
