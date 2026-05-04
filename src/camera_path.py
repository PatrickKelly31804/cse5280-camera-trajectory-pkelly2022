import numpy as np
from lie_groups import make_pose, interpolate_se3, interpolate_euclidean, right_perturb, left_perturb


def keyframes():
    target = np.array([0.0, 0.0, -600.0])

    poses = [
        make_pose([0.0, 0.0, 0.0], target),
        make_pose([180.0, 70.0, -120.0], target),
        make_pose([220.0, 100.0, -500.0], target),
        make_pose([120.0, 70.0, -850.0], target),
        make_pose([-120.0, 70.0, -850.0], target),
        make_pose([-220.0, 100.0, -500.0], target),
        make_pose([-180.0, 70.0, -120.0], target),
        make_pose([0.0, 0.0, 0.0], target)
    ]

    return poses


def make_path(frames_per_segment=8):
    poses = keyframes()
    path = []

    for i in range(len(poses) - 1):
        T1 = poses[i]
        T2 = poses[i + 1]

        for j in range(frames_per_segment):
            a = j / frames_per_segment
            path.append(interpolate_se3(T1, T2, a))

    path.append(poses[-1])
    return path


def make_euclidean_path(frames_per_segment=8):
    poses = keyframes()
    path = []

    for i in range(len(poses) - 1):
        T1 = poses[i]
        T2 = poses[i + 1]

        for j in range(frames_per_segment):
            a = j / frames_per_segment
            path.append(interpolate_euclidean(T1, T2, a))

    path.append(poses[-1])
    return path


def make_perturbed_path(frames_per_segment=8, mode="right"):
    base_path = make_path(frames_per_segment)
    path = []

    for i, T in enumerate(base_path):
        t = i / max(1, len(base_path) - 1)

        xi = np.array([
            20.0 * np.sin(2 * np.pi * t),
            8.0 * np.cos(2 * np.pi * t),
            0.0,
            0.0,
            0.15 * np.sin(4 * np.pi * t),
            0.0
        ])

        if mode == "right":
            path.append(right_perturb(T, xi))
        else:
            path.append(left_perturb(T, xi))

    return path