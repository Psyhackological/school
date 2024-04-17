from math import log2  # Return the base-2 logarithm of x.
import pandas as pd  # Do ramki danych

# Wczytanie danych z pliku CSV
file_name = 'klienci_banku.csv'  # Nazwa pliku
data = pd.read_csv(file_name)  # Wczytanie csv

# Funkcja do obliczania entropii zbioru


def calculate_entropy(data, target_column):
    # Prawdopodobieństwa wystąpienia każdej klasy w kolumnie docelowej
    probabilities = data[target_column].value_counts(normalize=True)
    # Obliczenie entropii
    entropy = -sum(probabilities *
                   probabilities.apply(lambda x: log2(x) if x > 0 else 0))
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
    attribute_entropy = sum(weights[val] * calculate_entropy(
        data[data[attribute] == val], target_column) for val in values)
    print(f"{attribute_entropy=}")
    return attribute_entropy


# Entropia całego zbioru S
total_entropy_S = calculate_entropy(data, 'czy_dostal_kredyt')

# Obliczenie entropii dla każdego atrybutu
attributes = data.columns[:-1]  # Wszystkie kolumny poza czy_dostal_kredyt
entropy_values = {attr: entropy_of_attribute(
    data, attr, 'czy_dostal_kredyt') for attr in attributes}  # Zdobywamy entropie dla kazdego

# Zysk informacyjny dla każdego atrybutu
information_gain = {attr: total_entropy_S -
                    entropy for attr, entropy in entropy_values.items()}  # I potem obliczamy zysk informacyjny dla kazdego atrybutu

print(f"{total_entropy_S=}")
print(f"{entropy_values=}")
print(f"{information_gain=}")
