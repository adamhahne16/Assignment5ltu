"""
point cloud data is stored as a 2D matrix
each row has 3 values i.e. the x, y, z value for a point

Project has to be submitted to github in the private folder assigned to you
Readme file should have the numerical values as described in each task
Create a folder to store the images as described in the tasks.


"""

# %%
import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import KDTree
from sklearn.cluster import DBSCAN
from mpl_toolkits.mplot3d import Axes3D


# Utility functions
def show_cloud(points_plt):
    ax = plt.axes(projection="3d")
    ax.scatter(points_plt[:, 0], points_plt[:, 1], points_plt[:, 2], s=0.01)
    plt.show()


def show_scatter(x, y):
    plt.scatter(x, y)
    plt.show()


# Updated to return histogram data
def get_ground_level(pcd):
    z_values = pcd[:, 2]
    hist, bin_edges = np.histogram(z_values, bins=50)
    max_bin_index = np.argmax(hist)
    ground_level_estimate = (
        bin_edges[max_bin_index] + bin_edges[max_bin_index + 1]
    ) / 2
    return ground_level_estimate, hist, bin_edges


# New function to plot and save histogram
def plot_histogram_and_save(hist, bin_edges, dataset_name):
    plt.figure()
    plt.bar(
        bin_edges[:-1], hist, width=np.diff(bin_edges), edgecolor="black", align="edge"
    )
    plt.title(f"Histogram of Z-values for {dataset_name}")
    plt.xlabel("Z value")
    plt.ylabel("Frequency")
    plt.savefig(f"{dataset_name}_histogram.png")
    plt.close()


# Process and visualize each dataset
def process_dataset(dataset_path, dataset_name):
    # Read file with the point cloud data
    pcd = np.load(dataset_path)
    print(f"Processing {dataset_name}, shape: {pcd.shape}")

    # Estimate ground level and generate the hhistogram
    est_ground_level, hist, bin_edges = get_ground_level(pcd)
    print(f"Estimated ground level for {dataset_name}: {est_ground_level}")

    # Save the histogram "plot"
    plot_histogram_and_save(hist, bin_edges, dataset_name)

    # Remove ground plane
    pcd_above_ground = pcd[pcd[:, 2] > est_ground_level]

    return pcd_above_ground


# Main
if __name__ == "__main__":
    dataset_paths = ["dataset1.npy", "dataset2.npy"]
    for dataset_path in dataset_paths:
        dataset_name = dataset_path.split(".")[0]
        pcd_above_ground = process_dataset(dataset_path, dataset_name)

