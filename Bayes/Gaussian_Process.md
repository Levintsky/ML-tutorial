# Gaussian Process

## Good Summaries
- https://katbailey.github.io/post/gaussian-processes-for-dummies/
- http://www.gaussianprocess.org/
- https://distill.pub/2019/visual-exploration-gaussian-processes/

## Textbooks 
- Kevin Murphy's textbook
	- A GP defines a **prior over functions**, which can be converted into a posterior over functions once we have seen some data. Although it might seem difficult to represent a distrubtion over a function, it turns out that we only need to be able to define a distribution over the function’s values at a finite, but arbitrary, set of points, say (x1,...,xN). 
	- A GP assumes that p(f(x1),...,f(xN)) is jointly Gaussian, with some mean μ(x) and covariance ∑(x) given by ∑ij=k(xi,xj)
	, where k is a positive definite kernel function. The key idea is that if 
	xi and xj are deemed by the kernel to be similar, then we expect the output of the function at those points to be similar, too.
	- https://github.com/probml/pmtk3
- C Rasmussen, C Williams. Gaussian Processes for Machine Learning. 2006

## Theory
- D R. Burt, C E. Rasmussen, M van der Wilk. Rates of Convergence for Sparse Variational Gaussian Process Regression. ICML'19 best paper
	- Reduce O(NM^2+M^3) to  and O(NM+M^2)

## Deep GP
- Neil D Lawrence and Andrew J Moore. Hierarchical gaussian process latent variable models. ICML'07
- Andreas Damianou and Neil Lawrence. Deep gaussian processes. AISTATS'13
- David Duvenaud, Oren Rippel, Ryan Adams, and Zoubin Ghahramani. Avoiding pathologies in very deep networks. AISTATS'14
- Thang Bui, Daniel Herna ́ndez-Lobato, Jose Hernandez-Lobato, Yingzhen Li, and Richard Turner. Deep gaussian processes for regression using approximate expectation propagation. ICML'16

## Connection with Neural Network
- Radford M. Neal. Priors for infinite networks. 1994
	- Single hidden layer
- Radford M. Neal. Bayesian Learning for Neural Networks. 1994
- Christopher KI Williams. Computing with infinite networks. NIPS'97
- Jaehoon Lee, Yasaman Bahri, Roman Novak, Samuel S. Schoenholz, Jeffrey Pennington, Jascha Sohl-Dickstein. Deep Neural Networks as Gaussian Processes. ICLR'18
	- Exact equivalence between infinitely wide deep networks and GPs
	- Focus on exact Bayesian inference for regression tasks
	- https://github.com/brain-research/nngp

## Unclassified
- Orthogonally Decoupled Variational Gaussian Processes. NIPS'18
- Infinite-Horizon Gaussian Processes. NIPS'18
- Learning Gaussian Processes by Minimizing PAC-Bayesian Generalization Bounds. NIPS'18
