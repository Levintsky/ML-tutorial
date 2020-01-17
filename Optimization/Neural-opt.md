# Optimization as a layer

## MIP
- A Ferber, B Wilder, B Dilkina, M Tambe. MIPaaL: Mixed Integer Program as a Layer. 2019
	- Take-away: We can handle "hard convex problems" using cutting planes
	- Forward Pass: solve MIP
	- Backward Pass: construct an LP to approximate the MIP exactly at the solution using cutting planes;

## Convex
- **cvxlayers**: A Agrawal, B Amos, S Barratt, S Boyd, S Diamond, and Z Kolter. Differentiable Convex Optimization Layers. NIPS'19
	- https://github.com/cvxgrp/cvxpylayers (support both pytorch and tf)