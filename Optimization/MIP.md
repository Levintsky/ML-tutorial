# Mix-Integer Programming

## Classic
- Cutting plane method;

## MIP + DL
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