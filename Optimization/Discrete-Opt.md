# Discrete/Combinatorial Optimization

## Basics
- Books:
	- C Papadimitriou and K Steiglitz. Combinatorial Optimization: Algorithms and Complexity. '82
	- G Nemhauser and L Wolsey. Integer and Combinatorial Optimization. '88
	- W Cook. Combinatorial Optimization. '97
	- Wolsey. Integer Programming. '98

## DL
- Po-Wei Wang, Priya L. Donti, Bryan Wilder, Zico Kolter. SATNet: Bridging deep learning and logical reasoning using a differentiable satisfiability solver. ICML'19

## NIPS'19
- Nathaniel Lahn, Deepika Mulchandani, Sharath Raghvendra. A Graph Theoretic Additive Approximation of Optimal Transport
- Changyong Oh, Jakub Tomczak, Efstratios Gavves, Max Welling. Combinatorial Bayesian Optimization using the Graph Cartesian Product
- Maxime Gasse, Didier Chetelat, Nicola Ferroni, Laurent Charlin, Andrea Lodi. Exact Combinatorial Optimization with Graph Convolutional Neural Networks
- Emre Yolcu, Barnabas Poczos. Learning Local Search Heuristics for Boolean Satisfiability
- Xinyun Chen, Yuandong Tian. Learning to Perform Local Rewriting for Combinatorial Optimization
- Hao Yu. A Communication Efficient Stochastic Multi-Block Alternating Direction Method of Multipliers
- Jiajin Li, SEN HUANG, Anthony Man-Cho So. A First-Order Algorithmic Framework for Wasserstein Distributionally Robust Logistic Regression
- Bin Shi, Simon Du, Weijie Su, Michael Jordan. Acceleration via Symplectic Discretization of High-Resolution Differential Equations
- Hadrien Hendrikx, Francis Bach, Laurent Massoulié. An Accelerated Decentralized Stochastic Proximal Algorithm for Finite Sums
- Kimon Antonakopoulos, Veronica Belmega, Panayotis Mertikopoulos. An adaptive Mirror-Prox method for variational inequalities with singular operators
- Cyrille Combettes, Sebastian Pokutta. Blended Matching Pursuit
- Jun Sun, Tianyi Chen, Georgios Giannakis, Zaiyue Yang. Communication-Efficient Distributed Learning via Lazily Aggregated Quantized Gradients
- Sebastien Bubeck, Qijia Jiang, Yin-Tat Lee, Yuanzhi Li, Aaron Sidford. Complexity of Highly Parallel Non-Smooth Convex Optimization
- Zhao Song, Ruosong Wang, Lin Yang, Hongyang Zhang, Peilin Zhong. Efficient Symmetric Norm Regression via Linear Sketching
- Tao Sun, Yuejiao Sun, Dongsheng Li, Qing Liao. General Proximal Incremental Aggregated Gradient Algorithms: Better and Novel Results under General Scheme
- DongDong Ge, Haoyue Wang, Zikai Xiong, Yinyu Ye. Interior-Point Methods Strike Back: Solving the Wasserstein Barycenter Problem
- Daniel Levy, John Duchi. Necessary and Sufficient Geometries for Gradient Methods
- Aaron Defazio. On the Curved Geometry of Accelerated Optimization
- Giulia Luise, Saverio Salzo, Massimiliano Pontil, Carlo Ciliberto. Sinkhorn Barycenters with Free Support via Frank-Wolfe Algorithm
- PHUONG_HA NGUYEN, Lam Nguyen, Marten van Dijk. Tight Dimension Independent Lower Bound on the Expected Convergence Rate for Diminishing Step Sizes in SGD
- Clarice Poon, Jingwei Liang. Trajectory of Alternating Direction Method of Multipliers and Adaptive Acceleration

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