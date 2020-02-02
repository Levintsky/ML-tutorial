# Graphical Models

## Directed Graphical Models (PRML, Chap 8.1, 8.2)
- Concepts
	- Markov blanket
- Bayesian network:
	- LR:\
		<img src="/Bayes/images/gm/gm-lr.png" alt="drawing" width="400"/>
	- Linear Gaussian Models:\
		<img src="/Bayes/images/gm/gm-lgm-1.png" alt="drawing" width="400"/>
		<img src="/Bayes/images/gm/gm-lgm-2.png" alt="drawing" width="400"/>
- Conditional Independence
	- Explain away;
		<img src="/Bayes/images/gm/gm-ind.png" alt="drawing" width="400"/>
	- d-separation: all paths are blocked; A ind B \| C;
		- blocked definition ((a) the arrows on the path meet either head-to-tail or tail-to-tail at the node, and the node is in the set C, or (b) the arrows meet head-to-head at the node, and neither the node, nor any of its descendants, is in the set C.)

## Undirected Graphical Models (PRML, Chap 8.3)
- MRF:\
	<img src="/Bayes/images/gm/gm-mrf-1.png" alt="drawing" width="400"/>
- CRF

## Inference in Graphical Models (PRML, Chap 8.4)
- Exact inference:
	- Variable elimination;
	- Factor graph;
		<img src="/Bayes/images/gm/factor-graph-1.png" alt="drawing" width="400"/>
		<img src="/Bayes/images/gm/factor-graph-2.png" alt="drawing" width="400"/>
		<img src="/Bayes/images/gm/factor-graph-3.png" alt="drawing" width="400"/>
		<img src="/Bayes/images/gm/factor-graph-4.png" alt="drawing" width="400"/>
	- Sum-product algorithm:
		- Used to find marginal of a node p(x):
		- Belief propagation (Pearl, 1988) is a special case; sum-product for a node x first does sum of neighbor xb, then x takes all sum and do product;\
			<img src="/Bayes/images/gm/sum-product.png" alt="drawing" width="400"/>
	- Max-product: 
		- Used to find x maximize the joint distribution;
			<img src="/Bayes/images/gm/max-product-1.png" alt="drawing" width="400"/>
			<img src="/Bayes/images/gm/max-product-2.png" alt="drawing" width="400"/>
- Exact inference:
	- Trunction tree: sum-product, max-product produces efficient, exact inference on tree, so make graph a tree;
- Loopy BP;
- Learning grah structure;
