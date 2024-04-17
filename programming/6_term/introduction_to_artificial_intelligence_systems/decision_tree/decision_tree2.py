import pandas as pd
from math import log2
import random
import json

# Wczytanie danych z pliku CSV
data = pd.read_csv("klienci_banku.csv")


def calculate_entropy(data, target_column):
    probabilities = data[target_column].value_counts(normalize=True)
    entropy = -sum(
        probabilities * probabilities.apply(lambda x: log2(x) if x > 0 else 0)
    )

    return entropy


def entropy_of_attribute(data, attribute, target_column):
    values = data[attribute].unique()
    weights = data[attribute].value_counts(normalize=True)
    attribute_entropy = sum(
        weights[val] *
        calculate_entropy(data[data[attribute] == val], target_column)
        for val in values
    )
    return attribute_entropy


def choose_best_attribute(data, attributes, target_column):
    total_entropy = calculate_entropy(data, target_column)
    information_gain = {}
    for attr in attributes:
        attr_entropy = entropy_of_attribute(data, attr, target_column)
        information_gain[attr] = total_entropy - attr_entropy
        print(
            f"Atrybut: {attr}, Zysk informacyjny: {information_gain[attr]:.2f}")

    max_gain = max(information_gain.values())
    best_attrs = [attr for attr, gain in information_gain.items()
                  if gain == max_gain]
    best_attr = random.choice(best_attrs)
    print(f"=== Najlepszy atrybut: {best_attr} ===")
    return best_attr


def build_tree(data, target_column, attributes):
    if len(data[target_column].unique()) == 1:
        decision = data[target_column].iloc[0]
        print(f"Tworzę liść: {decision}")
        return decision

    if not attributes:
        majority = data[target_column].mode()[0]
        print(f"Tworzę liść (dominująca klasa): {majority}")
        return majority

    best_attr = choose_best_attribute(data, attributes, target_column)
    tree = {best_attr: {}}

    for value in data[best_attr].unique():
        print(f"Tworzę węzeł dla {best_attr} = {value}")
        subset = data[data[best_attr] == value]
        subtree = build_tree(
            subset, target_column, [
                attr for attr in attributes if attr != best_attr]
        )
        tree[best_attr][value] = subtree

    return tree


# Przygotowanie atrybutów bez kolumny decyzyjnej
attributes = [col for col in data.columns if col != "czy_dostal_kredyt"]

# Budowanie i wyświetlanie drzewa
decision_tree = build_tree(data, "czy_dostal_kredyt", attributes)

# Wyświetlenie drzewa w formacie JSON
print("Wygenerowane drzewo decyzyjne:")
print(json.dumps(decision_tree, indent=4))

# Zapisanie drzewa do pliku JSON
with open("decision_tree.json", "w") as json_file:
    json.dump(decision_tree, json_file, indent=4)
