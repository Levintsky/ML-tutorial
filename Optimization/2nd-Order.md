# 2nd-Order Optimizer

## Natural Gradient (check RL section)
- Key idea:
	- Left multiplying inverse of Fisher Information matrix
- Exact natural gradient in deep linear networks and application to the nonlinear case. NIPS'18
- Fast Approximate Natural Gradient Descent in a Kronecker Factored Eigenbasis. NIPS'18
- **KFAC**: J. Martens and R. Grosse. Optimizing neural networks with kronecker-factored approximate curvature. 2015
	- Kronecker approximation to Fisher
- **FANG**: R. Grosse and R. Salakhudinov. Scaling up natural gradient by sparsely factorizing the inverse fisher matrix.
	- Cholesky decomposition.
- **PRONG**: G. Desjardins, K. Simonyan, R. Pascanu, et.al. Natural neural networks. NIPS 2015
	- Whitening each layer.
