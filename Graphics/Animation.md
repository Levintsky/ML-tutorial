# Animation

## Physics Based
- ODE, PDE: http://graphics.pixar.com/pbm2001/
- W Reeves: Particle systems— a technique for modeling a class of fuzzy objects, Proc. SIGGRAPH 1983
- Runge-Kutta:
	- Witkin, Baraff, Kass: Physically-based Modeling Course Notes, SIGGRAPH 2001
- Fluid:
	- **SPH** (Smoothed Particle Hydrodynamics)
		- Losasso, F., Talton, J., Kwatra, N. and Fedkiw, R., Two-way Coupled SPH and Particle Level Set Fluid Simulation, IEEE TVCG 14, 797-804 (2008).
	- R. Bridson, J. Hourihan, and M. Nordenstam. Curl noise for procedural fluid flow. SIGGRAPH'07
		- Lennard-Jones force: Repulsive + attractive force;
- Gravity: n-Body problem;
	- **Fast Multipole Method**, Greengard and Rokhlin, J Comput Phys 73, p. 325 (1987)
- http://processing.org/learning/topics/smokeparticlesystem.html

## Unclassified
- **MANN**: H Zhang, S Starke, T Komura, J Saito. Mode-Adaptive Neural Networks for Quadruped Motion Control. SIGGRAPH'18
	- Could be used in pedestrian simulation;

## Modeling the skilled movement of articulated figures
- Kinematics:
	- A Safonova and J Hodgins. Construction and optimal search of interpolated motion graphs. TOG'07
	- Y Lee, K Wampler, G Bernstein, J Popović, and Z Popović. Motion Fields for Interactive Character Locomotion. SIGGRAPH Asia'10
	- Y Ye and C Liu. 2010b. Synthesis of Responsive Motion Using a Dynamic Model. CGF'10
	- S Levine, J Wang, A Haraux, Z Popović, and V Koltun. Continuous Character Control with Low-Dimensional Embeddings. TOG'12
	- S Agrawal and M Panne. Task-based Locomotion. TOG'16
	- D Holden, J Saito, and T Komura. A Deep Learning Framework for Character Motion Synthesis and Editing. TOG'16
	- D Holden, T Komura, and J Saito. Phase-functioned Neural Networks for Character Control. TOG'17
- Physics based: products of an underlying simplified model and an optimization process
	- S Coros, P Beaudoin, and M v d Panne. Generalized Biped Walking Control. TOG'10
	- Y Ye and K Liu. Optimal feedback control for character animation using an abstract model. TOG'10
	- J Wang, S Hamner, S Delp, V Koltun, and More Specifically. Optimizing locomotion controllers using biologically-based actuators and objectives. TOG'12
	- I Mordatch, E Todorov, and Z Popović. Discovery of Complex Behaviors Through Contact-invariant Optimization. TOG'12
	- Y Tassa, T Erez, and E Todorov. Synthesis and stabilization of complex behaviors through online trajectory optimization. IROS'12
	- S Agrawal, S Shen, and M v d Panne. Diverse Motion Variations for Physics-based Character Animation. 2013
	- K Wampler, Z Popović, and J Popović. Generalizing Locomotion Style to New Animals with Inverse Optimal Regression. TOG'14
	- S Ha and C K Liu. Iterative training of dynamic skills inspired by human coaching techniques. TOG'14
	- **MPC**: P Hämäläinen, J Rajamäki, and C K Liu. Online control of simulated humanoids using particle belief propagation. TOG'15
- RL:
	- X B Peng, G Berseth, and M v d Panne. Dynamic Terrain Traversal Skills Using Reinforcement Learning. TOG'15
	- L Liu and J Hodgins. Learning to Schedule Control Fragments for Physics-Based Characters Using Deep Q-Learning. TOG'17