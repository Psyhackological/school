"""
This module implements a decision tree generator for classification based on the entropy and information gain metrics. It uses a dataset from a CSV file to build a decision tree that predicts whether a bank's clients will receive credit based on several attributes.

The tree is built recursively, selecting the attribute that maximizes information gain at each node. The resulting decision tree is then visualized in JSON format and can be saved to a JSON file named after the root attribute of the tree if it doesn't exist already. This implementation also includes functions to calculate entropy and information gain for given attributes within the dataset.

Functions:
- calculate_entropy: Computes the entropy of a specified target column in a dataset.
- entropy_of_attribute: Calculates the entropy for different values of a given attribute, considering the target column for classification.
- choose_best_attribute: Identifies the attribute that provides the maximum information gain and should be used for the next split in the tree building process.
- build_tree: Recursively constructs the decision tree from the provided dataset.
- main: Controls the flow of building and saving the decision tree, also handles command line integration.

Usage:
Run this script directly from the command line to build and save the decision tree using data from 'klienci_banku.csv'.

Example:
    python decision_tree.py

This will generate and save the decision tree, handling file existence checks to avoid overwriting existing data.
"""

import os  # Checking for existance of file
import json  # Visualizaing and saving decision tree in json format
import random  # For fun due to same value of the tree's root
from math import log2  # Return the base-2 logarithm of x.
import pandas as pd  # For .csv file


# Loading CSV into dataframe
data = pd.read_csv("klienci_banku.csv")


def calculate_entropy(dataset, target_column):
    """
    Calculates the weighted entropy for different values of a given attribute in the dataset.

    This function helps in understanding how much a specific attribute contributes to the disorder or randomness in the target column.

    Args:
    data (DataFrame): The Pandas DataFrame containing the dataset.
    attribute (str): The attribute for which the entropy is to be calculated.
    target_column (str): The target column against which the entropy needs to be measured.

    Returns:
    float: The total weighted entropy of the attribute.
    """
    # Probabilities of each class in the target column
    probabilities = dataset[target_column].value_counts(normalize=True)
    # Entropy calculation
    entropy = -sum(
        probabilities * probabilities.apply(lambda x: log2(x) if x > 0 else 0)
    )

    return entropy


def entropy_of_attribute(clients_data, attribute, target_column):
    """
    Calculates the weighted entropy for different values of a given attribute in the dataset.

    This function helps in understanding how much a specific attribute contributes to the disorder or randomness in the target column.

    Args:
    data (DataFrame): The Pandas DataFrame containing the dataset.
    attribute (str): The attribute for which the entropy is to be calculated.
    target_column (str): The target column against which the entropy needs to be measured.

    Returns:
    float: The total weighted entropy of the attribute.
    """
    # Unique attribute values
    values = clients_data[attribute].unique()
    # Weight for each attribute value
    weights = clients_data[attribute].value_counts(normalize=True)
    # Calculating the entropy for each attribute value and adding them up
    attribute_entropy = sum(
        weights[val]
        * calculate_entropy(clients_data[clients_data[attribute] == val], target_column)
        for val in values
    )

    return attribute_entropy


def choose_best_attribute(clients_data, attributes, target_column):
    """
    Determines the best attribute for splitting the data at the current node by calculating the information gain for each attribute.

    Args:
    data (DataFrame): The dataset being used.
    attributes (list): List of column names considered for the next split.
    target_column (str): The name of the target column.

    Returns:
    str: The attribute name with the highest information gain. If multiple attributes have the same information gain, one is randomly selected.
    """
    # Calculate the total entropy of the current dataset subset
    total_entropy = calculate_entropy(clients_data, target_column)
    information_gain = {}

    # Calculate the information gain for each attribute by subtracting the attribute's entropy from the total entropy
    for attr in attributes:
        attr_entropy = entropy_of_attribute(clients_data, attr, target_column)
        information_gain[attr] = total_entropy - attr_entropy
        print(f"Atrybut: {attr}, Zysk informacyjny: {information_gain[attr]:.2f}")

    # Find the maximum information gain across all attributes
    max_gain = max(information_gain.values())
    # Collect all attributes that have the maximum information gain
    best_attrs = [attr for attr, gain in information_gain.items() if gain == max_gain]
    # Randomly select one if multiple attributes have the same maximum gain
    best_attr = random.choice(best_attrs)
    print(f"=== Najlepszy atrybut: {best_attr} ===")
    return best_attr


def build_tree(clients_data, target_column, attributes):
    """
    Recursively builds a decision tree using the information gain metric to choose the best attribute for splitting the data at each node.

    Args:
    data (DataFrame): The dataset being used.
    target_column (str): The name of the target column.
    attributes (list): List of column names to consider for splits.

    Returns:
    dict: A nested dictionary representing the decision tree.
    """
    # If all values in the target column are the same, return a leaf node with that value
    if len(clients_data[target_column].unique()) == 1:
        decision = clients_data[target_column].iloc[0]
        print(f"Tworze lisc: {decision}")
        return decision

    # If there are no more attributes to split on, return a leaf node with the majority class
    if not attributes:
        majority = clients_data[target_column].mode()[0]
        print(f"Tworze lisc (dominujaca klasa): {majority}")
        return majority

    # Choose the best attribute to split on based on information gain
    best_attr = choose_best_attribute(clients_data, attributes, target_column)
    tree = {best_attr: {}}

    # For each value of the best attribute, recursively build the tree
    for value in clients_data[best_attr].unique():
        print(f"Tworze wezel dla {best_attr} = {value}")
        subset = clients_data[clients_data[best_attr] == value]
        # Recursive call excluding the current best attribute from the list of attributes
        subtree = build_tree(
            subset, target_column, [attr for attr in attributes if attr != best_attr]
        )
        tree[best_attr][value] = subtree

    return tree


def main():
    """
    Main execution function for building and saving a decision tree.

    This function orchestrates the process of building a decision tree based on the attribute "czy_dostal_kredyt", displaying it in JSON format, and saving it to a file named after the root attribute of the decision tree if it doesn't already exist.
    The function defines which column to use as the decision attribute, prepares other attributes for building the tree, and manages file output.
    """
    # Column by which we will divide
    decision_attribute = "czy_dostal_kredyt"
    # Preparing attributes without a decision column
    attributes = [col for col in data.columns if col != decision_attribute]

    # Building the tree
    decision_tree = build_tree(data, "czy_dostal_kredyt", attributes)

    # Display tree in JSON format
    print("Wygenerowane drzewo decyzyjne:")
    print(json.dumps(decision_tree, indent=4))

    # Generating root attribute
    root_attribute = next(iter(decision_tree))
    # Using it as filename subfix
    filename = f"decision_tree_{root_attribute}.json"

    # Saving the tree to a JSON file only if it doesn't already exist
    if not os.path.exists(filename):  # Checks if the file does not exist
        # Saving the tree to a JSON file
        with open(filename, "w", encoding="utf-8") as json_file:
            # Saves the decision tree to the file
            json.dump(decision_tree, json_file, indent=4)


if __name__ == "__main__":
    main()
