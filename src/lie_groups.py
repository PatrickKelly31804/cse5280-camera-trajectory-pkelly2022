import numpy as np
from scipy.linalg import expm, logm


def hat(w):
    return np.array([
        [0, -w[2], w[1]],
        [w[2], 0, -w[0]],
        [-w[1], w[0], 0]
    ])


def se3_hat(xi):
    v = xi[:3]
    w = xi[3:]

    m = np.zeros((4, 4))
    m[:3, :3] = hat(w)
    m[:3, 3] = v
    return m


def se3_exp(xi):
    return expm(se3_hat(xi))


def make_pose(position, target):
    position = np.array(position, dtype=float)
    target = np.array(target, dtype=float)

    forward = target - position
    forward = forward / np.linalg.norm(forward)

    up = np.array([0, 1, 0], dtype=float)

    right = np.cross(forward, up)
    right = right / np.linalg.norm(right)

    true_up = np.cross(right, forward)

    R = np.eye(3)
    R[:, 0] = right
    R[:, 1] = true_up
    R[:, 2] = -forward

    T = np.eye(4)
    T[:3, :3] = R
    T[:3, 3] = position

    return T


def interpolate_se3(T1, T2, a):
    relative = np.linalg.inv(T1) @ T2
    move = expm(a * logm(relative).real)
    return T1 @ move


def interpolate_euclidean(T1, T2, a):
    T = np.eye(4)
    T[:3, 3] = (1 - a) * T1[:3, 3] + a * T2[:3, 3]

    R = (1 - a) * T1[:3, :3] + a * T2[:3, :3]
    u, _, vh = np.linalg.svd(R)
    T[:3, :3] = u @ vh

    return T


def right_perturb(T, xi):
    return T @ se3_exp(xi)


def left_perturb(T, xi):
    return se3_exp(xi) @ T