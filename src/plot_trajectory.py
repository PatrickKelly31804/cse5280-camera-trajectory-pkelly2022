import numpy as np
import matplotlib.pyplot as plt
from camera_path import make_path, make_euclidean_path, make_perturbed_path


def get_centers(path):
    return np.array([T[:3, 3] for T in path])


def plot_path(path, name):
    centers = get_centers(path)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    ax.plot(centers[:, 0], centers[:, 1], centers[:, 2])
    ax.scatter(centers[:, 0], centers[:, 1], centers[:, 2])

    ax.scatter([0], [0], [0])

    ax.set_title(name)

    plt.savefig(f"output/plots/{name}.png")
    plt.close()


def main():
    plot_path(make_path(), "se3_trajectory")
    plot_path(make_euclidean_path(), "euclidean_trajectory")
    plot_path(make_perturbed_path(mode="right"), "right_perturbed")
    plot_path(make_perturbed_path(mode="left"), "left_perturbed")


if __name__ == "__main__":
    main()