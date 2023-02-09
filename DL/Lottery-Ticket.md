# Lottery Ticket

## Pruning in Training
- J Frankle, M Carbin. The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks. ICLR'19
	- **First lottery paper**;
	- Randomly initialize a neural network.
	- Train the network for j iterations, reaching parameters.
	- Prune s% of the parameters, creating a mask m where Pm = (100 − s)%.
	- To extract the winning ticket, **reset the remaining parameters to their initial values** in θ0, creating the untrained network.
- Z Liu, M Sun, T Zhou, G Huang, T Darrell. Rethinking the Value of Network Pruning. ICLR'19
- A Morcos, H Yu, M Paganini, Y Tian. One ticket to win them all: generalizing lottery ticket initializations across datasets and optimizers. NIPS'19
- E Malach, G Yehudai, S Shalev-Shwartz, and O Shamir. Proving the Lottery Ticket Hypothesis: Pruning is All You Need. 2020
	- First, we show that a ReLU network of arbitrary depth l can be approximated by finding a weight-subnetwork of a random network of depth 2l and sufficient width;
	- Second, we show that depth-two (one hidden-layer) networks have neuron-subnetworks that are competitive with the best random-features classifier (i.e. the best classifier achieved when training only the second layer of the network);

## Sub-Network Finding
- H. Zhou, J. Lan, R. Liu, and J. Yosinski. Deconstructing lottery tickets: Zeros, signs, and the supermask. NIPS'19
	- The existence of Supermasks, masks that can be applied to an untrained, randomly initialized network to produce a model with performance far better than chance
- V. Ramanujan, M. Wortsman, A. Kembhavi, A. Farhadi, and M. Rastegari. What’s hidden in a randomly weighted neural network? arxiv'19
	- Conjecture: a sufficiently over-parameterized neural network with random initialization contains a subnetwork that achieves competitive accuracy