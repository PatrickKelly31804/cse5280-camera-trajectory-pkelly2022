import os
import imageio.v2 as imageio
from camera_path import make_path
from raytrace import render


def main():
    os.makedirs("output/frames", exist_ok=True)

    path = make_path(frames_per_segment=6)

    frame_files = []

    for i, pose in enumerate(path):
        filename = f"output/frames/frame_{i:04d}.png"
        print("Rendering", i)
        render(pose, filename)
        frame_files.append(filename)

    images = [imageio.imread(f) for f in frame_files]
    imageio.mimsave("output/animation.mp4", images, fps=24)

    print("DONE → output/animation.mp4")


if __name__ == "__main__":
    main()