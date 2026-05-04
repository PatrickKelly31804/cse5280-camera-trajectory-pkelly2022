# Camera Trajectory Animation Using Lie-Group Interpolation

Patrick Kelly  
CSE5280

## Overview

This project extends my original ray tracing assignment by adding a moving camera animation. Instead of moving the camera using simple linear interpolation, I represented camera poses using SE(3), which models rigid body transformations. I then interpolated between poses using Lie-group methods to create a smooth and consistent camera trajectory.

## Features

- Ray-traced animation with a moving camera
- Multiple camera keyframes forming a closed loop
- SE(3) Lie-group interpolation using exponential and logarithm maps
- Euclidean interpolation for comparison
- Camera trajectory visualization (3D plots)
- Tangent-space perturbations (twists)
- Comparison between left and right perturbations

## How It Works

Each camera pose is represented as a 4x4 transformation matrix (rotation + translation).

To interpolate between two poses T1 and T2, I compute:

T(a) = T1 * exp(a * log(T1⁻¹ * T2))

This keeps the interpolation on the SE(3) manifold, which ensures smooth and physically correct motion.

For comparison, I also implemented a Euclidean interpolation method that linearly blends position and rotation. While this works visually, it is less accurate for rotations.

## Results

- SE(3) interpolation produced smoother and more natural camera motion
- Euclidean interpolation was slightly less consistent
- Left and right perturbations created noticeably different motion behaviors:
  - Left perturbation affects motion in the world frame
  - Right perturbation affects motion in the camera frame

## Animation

https://drive.google.com/file/d/1csMuccHlNMpt9xm7fXAYsotJ6Eiagz4S/view?usp=sharing

## Project Structure

cse5280-camera-trajectory-pkelly2022/
│
├── src/
│   ├── raytrace.py
│   ├── lie_groups.py
│   ├── camera_path.py
│   ├── render_animation.py
│   └── plot_trajectory.py
│
├── output/
│   ├── frames/
│   ├── plots/
│   └── animation.mp4
│
├── report/
│   └── report.md
│
├── requirements.txt
└── README.md

## How to Run

Install dependencies:

pip install -r requirements.txt

Generate trajectory plots:

python3 src/plot_trajectory.py

Render animation:

python3 src/render_animation.py

## Output

- Animation: output/animation.mp4
- Frames: output/frames/
- Plots: output/plots/

## Notes

The animation resolution was slightly reduced to improve rendering speed. This does not affect the correctness of the interpolation or trajectory.

## Conclusion

Using Lie-group interpolation on SE(3) provides a much more accurate and consistent way to animate camera motion compared to standard Euclidean methods. The results show smoother transitions and better handling of rotations, especially when combining translation and orientation changes.
