# Bundle Adjustment

## Optimality in Noisy Real World Conditions
- 8-points: closed form, elegant; not robust to noise;

## Bundle Adjustment
- Minimize reprojection error from 3D to each camera
<img src="/CV-3D/images/trad/ba.png" alt="drawing" width="600"/>

- Jointly estimate camera parameters and 3D coordinates

## Nonlinear Optimization
- Gradient Descent
- Least Squares Estimation
- Newton Methods
- The Gauss-Newton Algorithm
- The Levenberg-Marquardt Algorithm
<img src="/CV-3D/images/trad/jm-optimizer.png" alt="drawing" width="600"/>

## Summary
- Snavely, Seitz, Szeliski, Modeling the world from Internet photo collections, IJCV 2008.
- **PTAM**: Klein, Murray, Parallel Tracking and Mapping (PTAM) for Small AR Workspaces, ISMAR 2007

## Example Applications