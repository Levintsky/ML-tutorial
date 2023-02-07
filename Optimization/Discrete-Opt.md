# Discrete/Combinatorial Optimization

## Basics
- Books:
	- C Papadimitriou and K Steiglitz. Combinatorial Optimization: Algorithms and Complexity. '82
	- G Nemhauser and L Wolsey. Integer and Combinatorial Optimization. '88
	- W Cook. Combinatorial Optimization. '97
	- Wolsey. Integer Programming. '98

## Mix-Integer Programming
- Classic
	- Cutting plane method;
- MIP + DL
	- Take-aways:
		- These types of trained networks can be modeled as a MIP and embedded into another optimization problem.
		- there are ways to accelerate the solution process of these MIPs by understanding the polyhedral geometry
	- MIP commercial solver: gurobi
	- M Fischetti and J Jo. Deep Neural Networks as 0-1 Mixed Integer Linear Programs: A Feasibility Study. 2017
		- x = RELU(wy+b)
		- option 1: wy+b=x-s, s.t., x >= 0, s >= 0;
		- option 2: z = 0,1 for +/-, 
	- R Anderson, J Huchette, W Ma, C Tjandraatmadja, J Vielma. Strong mixed-integer programming formulations for trained neural networks. 2019
		- Contained in tf.opt, will be open source;
		- Experiments: Faster MNIST;
	- M Ryu, Y Chow, R Anderson, C Tjandraatmadja, C Boutilier. CAQL: Continuous Action Q-Learning. ICLR'20
	- A Ferber, B Wilder, B Dilkina, M Tambe. MIPaaL: Mixed Integer Program as a Layer. 2019
		- Take-away: We can handle "hard convex problems" using cutting planes
		- Forward Pass: solve MIP
		- Backward Pass: construct an LP to approximate the MIP exactly at the solution using cutting planes;

## Neural Combinatorial Solver
- A Graves, G Wayne, I Danihelka. Neural Turing Machines. 2014
- J Weston, S Chopra, A Bordes. Memory Networks. 2014
- K Kurach, M Andrychowicz, I Sutskever. Neural Random-Access Machines. 2015
- A Joulin, T Mikolov. Inferring Algorithmic Patterns with Stack-Augmented Recurrent Nets. NIPS'15
- S Sukhbaatar, A Szlam, J Weston, R Fergus. End-To-End Memory Networks. 2015
- A Neelakantan, Q Le, I Sutskever. Inducing latent programs with gradient descent. ICLR'16
- Ł Kaiser, I Sutskever. Neural gpus learn algorithms. ICLR'16
- S Reed, N Freitas. Neural programmer interpreters. ICLR'16
- W Zaremba, T Mikolov, A Joulin, R Fergus. Learning simple algorithms from examples. ICLR'16
- DNC: A Graves, et. al. Hybrid computing using a neural network with dynamic external memory. Nature'16
	- https://github.com/deepmind/dnc
- P Wang, P Donti, Bryan Wilder, Zico Kolter. SATNet: Bridging deep learning and logical reasoning using a differentiable satisfiability solver. ICML'19