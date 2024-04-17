from math import log2  # Return the base-2 logarithm of x.
import pandas as pd  # Do ramki danych

# Wczytanie danych z pliku CSV
FILE_NAME = "klienci_banku.csv"  # Nazwa pliku
data = pd.read_csv(FILE_NAME)  # Wczytanie csv

# Funkcja do obliczania entropii zbioru


def calculate_entropy(data, target_column):
    # Prawdopodobieństwa wystąpienia każdej klasy w kolumnie docelowej
    probabilities = data[target_column].value_counts(normalize=True)
    # Obliczenie entropii
    entropy = -sum(
        probabilities * probabilities.apply(lambda x: log2(x) if x > 0 else 0)
    )
    return entropy


# Funkcja do obliczania entropii dla atrybutu


def entropy_of_attribute(data, attribute, target_column):
    # Unikalne wartości atrybutu
    values = data[attribute].unique()
    print(f"{values=}")
    # Waga dla każdej wartości atrybutu
    weights = data[attribute].value_counts(normalize=True)
    print(f"{weights=}")
    # Obliczanie entropii dla każdej wartości atrybutu i sumowanie ich
    attribute_entropy = sum(
        weights[val] *
        calculate_entropy(data[data[attribute] == val], target_column)
        for val in values
    )
    print(f"{attribute_entropy=}\n")
    return attribute_entropy


# Entropia całego zbioru S
total_entropy_S = calculate_entropy(data, "czy_dostal_kredyt")

# Obliczenie entropii dla każdego atrybutu
attributes = data.columns[:-1]  # Wszystkie kolumny poza czy_dostal_kredyt
entropy_values = {
    attr: entropy_of_attribute(data, attr, "czy_dostal_kredyt") for attr in attributes
}  # Zdobywamy entropie dla kazdego

# Zysk informacyjny dla każdego atrybutu
information_gain = {
    attr: total_entropy_S - entropy for attr, entropy in entropy_values.items()
}  # I potem obliczamy zysk informacyjny dla kazdego atrybutu

# Sortowanie weddlug najwyzszych wartosci
sorted_entropy_values = sorted(
    entropy_values.items(), key=lambda item: item[1], reverse=True)  # Entropie atrybutow
sorted_information_gain = sorted(
    information_gain.items(), key=lambda item: item[1], reverse=True)  # Zyski informacyjne atrybutow

print(f"Calkowita entropia zbioru S: {total_entropy_S}")

print("Posortowana entropia kazdego atrybutu:")
for i, (attribute, entropy_value) in enumerate(sorted_entropy_values, 1):
    print(f"{i}. {entropy_value:.3f} <- {attribute}")

print("Posortowany zysk informacyjny kazdego atrybutu:")
for i, (attribute, information_gain) in enumerate(sorted_information_gain, 1):
    print(f"{i}. {information_gain:.3f} <- {attribute}")

print("Wiec mozna wybrac korzen z 'dochody' lub 'wklad_wlasny'.")
