# Graphical Models

## Directed Graphical Models
- **PRML, Chap 8.1, 8.2**
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
- **Kevin Murphy, Chap 10**;
- Examples: Naive Bayes Classifier; HMM; QMR (quick medical reference); Gaussian Bayes Net;
- Inference;\
	<img src="/Bayes/images/gm/dgm-inf.png" alt="drawing" width="350"/>
- Learning;
	- With complete data:\
		<img src="/Bayes/images/gm/dgm-nbc.png" alt="drawing" width="400"/>\
		<img src="/Bayes/images/gm/dgm-inf-2.png" alt="drawing" width="400"/>
	- With missing data/latent, not convex;\
		<img src="/Bayes/images/gm/d-sep.png" alt="drawing" width="400"/>

## Undirected Graphical Models
- PRML, Chap 8.3
	- MRF:\
		<img src="/Bayes/images/gm/mrf-1.png" alt="drawing" width="400"/>
	- CRF
	- M. Schmidt. UGM: A Matlab toolbox for probabilistic undirected graphical models.
		- http://www.cs.ubc.ca/~schmidtm/Software/UGM.html. 
- Kevin Murphy, Chap 19
	- Hammersley-Clifford Theorem; Gibbs distribution; energy-based model;
	- Examples: Ising; Hopfield networks; Potts model (generalized Ising to multiple states);
		- Gaussian MRF;
			<img src="/Bayes/images/gm/gauss-mrf.png" alt="drawing" width="400"/>
	- Learning:
		- Exponential family:\
			<img src="/Bayes/images/gm/exp-1.png" alt="drawing" width="300"/>\
			<img src="/Bayes/images/gm/exp-2.png" alt="drawing" width="400"/>\
			<img src="/Bayes/images/gm/exp-3.png" alt="drawing" width="250"/>
		- Pseudo-likelihood:\
			<img src="/Bayes/images/gm/pseudo-likelihood.png" alt="drawing" width="400"/>
		- Stochastic maximum likelihood:\
			<img src="/Bayes/images/gm/batch-ml.png" alt="drawing" width="400"/>

## Inference in Graphical Models (PRML, Chap 8.4)
- Exact inference:
	- Variable elimination;
	- Factor graph;
		<img src="/Bayes/images/gm/factor-graph-1.png" alt="drawing" width="400"/>
		<img src="/Bayes/images/gm/factor-graph-2.png" alt="drawing" width="400"/>
		<img src="/Bayes/images/gm/factor-graph-3.png" alt="drawing" width="400"/>
		<img src="/Bayes/images/gm/factor-graph-4.png" alt="drawing" width="400"/>
	- **Sum-product** algorithm (same as **belief propagation**, variable elimination):
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

## CRF (Directed or Undirected)
- Inference Proposals
	- MAP inference:
		- alpha-expansion
		- TRW-S
	- M-Best-MAP:
		- D. Nilsson. An efficient algorithm for finding the m most probable configurations in probabilistic expert systems. Statistics and Computing, vol. 8, pp. 159–173, 1998.
		- C. Yanover and Y. Weiss, Finding the m most probable configurations using loopy belief propagation. NIPS'03
		- D. Batra. An Efficient Message-Passing Algorithm for the M-Best MAP Problem. UAI'12
	- Generate a diverse set of proposals:
		- D. Batra, P. Yadollahpour, A. Guzman-Rivera, and G. Shakhnarovich. Diverse M-Best Solutions in Markov Random Fields. ECCV'12
		- **PDivMAP**: F. Meier, A. Globerson, and F. Sha. The More the Merrier: Parameter Learning for Graphical Models with Multiple MAPs. in ICML Workshop on Inferning: Interactions between Inference and Learning, 2013
		- C. Chen, V. Kolmogorov, Y. Zhu, D. Metaxas, and C. H. Lampert. Computing the m most probable modes of a graphical model. AISTATS'13
- Dense CRF:
	- Philipp Krähenbühl, Vladlen Koltun. Efficient Inference in Fully Connected CRFs with Gaussian Edge Potentials. NIPS'12
	- DeepLab;
- Uncertainty measure:
	- G. Papandreou and A. L. Yuille, Perturb-and-map random fields: Using discrete optimization to learn and sample from energy models. ICCV'11
	- D. Tarlow, R. P. Adams, and R. S. Zemel. Randomized optimum models for structured prediction. AISTATS'12
	- **MAP-perturbation**: S. Maji, T. Hazan, and T. Jaakkola. Active boundary annotation using random map perturbations. AAAI'14

## Unclassified
- Boxin Zhao, Y. Samuel Wang, Mladen Kolar. Direct Estimation of Differential Functional Graphical Models. NIPS'19
- Shanshan Wu, Sujay Sanghavi, Alexandros G. Dimakis. Sparse Logistic Regression Learns All Discrete Pairwise Graphical Models. NIPS'19
- Lingrui Gan, Xinming Yang, Naveen Narisetty, Feng Liang. Bayesian Joint Estimation of Multiple Graphical Models. NIPS'19
- Radu Marinescu, Rina Dechter. Counting the Optimal Solutions in Graphical Models. NIPS'19
