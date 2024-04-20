import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import ArrowStyle
from math import sqrt
import zipfile


class PlotConfig:
    def __init__(self):
        self.color_dots = "blue"
        self.color_arrows = "blue"
        self.color_distance = "black"
        self.color_letters = "black"
        # Using Fancy arrow style with custom parameters for a nicer look
        self.arrow_style = ArrowStyle(
            "Fancy", head_length=0.4, head_width=0.8, tail_width=0.4)
        self.marker = 'o'
        self.marker_start = 'o'
        self.marker_start_color = "red"  # Ensure the start marker is red
        self.marker_size = 14
        self.marker_edge_color = 'black'
        self.marker_edge_width = 1
        self.fontsize_distance = 8
        self.fontsize_city = 8


def plot_path_with_distances(path, cities_dict, ax, config):
    path_points = [cities_dict[city] for city in path]
    # Plot the first point separately to ensure it's red
    ax.plot(*zip(*path_points[:1]), marker=config.marker_start, color=config.marker_start_color,
            markersize=config.marker_size, markeredgecolor=config.marker_edge_color,
            markeredgewidth=config.marker_edge_width, zorder=3)
    # Plot the rest of the points
    ax.plot(*zip(*path_points[1:]), marker=config.marker, color=config.color_dots,
            linewidth=2, markersize=config.marker_size, markeredgecolor=config.marker_edge_color,
            markeredgewidth=config.marker_edge_width, zorder=3)

    for i in range(len(path_points) - 1):
        segment_dist = calculate_distance(path_points[i], path_points[i+1])
        mid_point = ((path_points[i][0] + path_points[i+1][0]) / 2,
                     (path_points[i][1] + path_points[i+1][1]) / 2)
        if segment_dist != 0:
            ax.text(mid_point[0], mid_point[1], f'{segment_dist:.2f}', ha='center',
                    fontsize=config.fontsize_distance, color=config.color_distance,
                    zorder=5, bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.2'))
        # Apply the new arrow style
        ax.annotate("", xy=path_points[i + 1], xytext=path_points[i],
                    arrowprops=dict(arrowstyle=config.arrow_style,
                                    color=config.color_arrows, linewidth=2),
                    zorder=2)

    for i, (city, point) in enumerate(zip(path, path_points)):
        ax.text(point[0], point[1], city, ha='center', color=config.color_letters,
                fontsize=config.fontsize_city, fontweight='bold',
                bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.2'), zorder=10)

    total_dist = total_distance(path, cities_dict)
    path_sequence = ' -> '.join(path)
    ax.set_title(f'{total_dist:.2f}: {path_sequence}')
    ax.set_xlim(-1, 10)
    ax.set_ylim(-1, 15)

# The rest of your code follows...


def calculate_distance(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


def total_distance(path, cities_dict):
    return sum(calculate_distance(cities_dict[path[i]], cities_dict[path[i+1]]) for i in range(len(path)-1))


def complete_path(paths):
    return [['A'] + path + ['A'] for path in paths]


def zip_graphs(paths, cities_dict, folder_path, config, dpi=300):
    os.makedirs(folder_path, exist_ok=True)
    zip_filename = "graphs.zip"
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for i, path in enumerate(paths):
            fig, ax = plt.subplots()
            plot_path_with_distances(path, cities_dict, ax, config)
            plt.grid(True)
            graph_filename = os.path.join(
                folder_path, f'path_{i+1:02d}_{total_distance(path, cities):.2f}.png')
            plt.savefig(graph_filename, dpi=dpi)
            plt.close()
            zipf.write(graph_filename, os.path.basename(graph_filename))
    return zip_filename


if __name__ == "__main__":
    csv_path = '../outcomes/paths.csv'
    full_paths_df = pd.read_csv(csv_path)
    cities = {"A": (0, 0),
              "D": (1, 8),
              "F": (2, 10),
              "G": (3, 3),
              "B": (4, 7),
              "E": (6, 4),
              "C": (8, 13)
              }
    full_completed_paths = complete_path(
        full_paths_df[full_paths_df.columns[3:]].values.tolist())
    config = PlotConfig()
    graphs_dir = 'graphs'
    zip_file = zip_graphs(full_completed_paths, cities, graphs_dir, config)
    print(f'All graphs have been saved in: {zip_file}')
