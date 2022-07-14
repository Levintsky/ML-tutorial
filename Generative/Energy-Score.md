# Energy/Score-based Model

## Energy-based
- Erik Nijkamp, Mitch Hill, Song-Chun Zhu, Ying Nian Wu. Learning Non-Convergent Non-Persistent Short-Run MCMC Toward Energy-Based Model. NIPS'19

## Score-based
- Basics: denote p_data(x) as p'
	- Score function ∇xlog(p'(x))
- A. Hyvärinen. Estimation of non-normalized statistical models by score matching. JMLR'05
	- Insight: learn parameters for a **unnormalized** p.d.f.
	- Let p(x;θ)= q(x;θ)/Z(θ), x data; θ parameter; data x n-dimension;
	- Z(θ) = ∫q(x; θ)dx normalizing factor;
	- Score function: ψ(x; θ)=∇x logp(x; θ)
	- Loss: J(θ) = 1/2 ∫p(x)|ψ(x;θ)−∇x logp(x)|^2dx
		- Score matching: θ=argmin J(θ)
	- Theo-1: Assume that the model score function ψ(x; θ) is differentiable, as well as some weak regularity conditions. Then loss can be formulated as:
		- J(θ) = ∫p(x)Σi=1..n(∂iψi(x; θ)+ψi(x; θ)^2/2)dx + const
		- constant does not depends on θ;
		- ψi(x; θ) = ∂logq(x; θ)/∂xi; 1st-order gradient w.r.t. data
		- ∂ψi(x; θ)/∂xi = ∂^2logq(x; θ)/∂xi^2; 2nd-order gradient w.r.t. data
	- Proof: integral by part;
- **Denoising score matching**: Pascal Vincent. A Connection Between Score Matching and Denoising Autoencoders. NC'11
	- Insight: circumvents tr(∇x sθ(x))
	- Denote: q(x) data distribution, p(x;θ)= exp(-E(x;θ))/Z(θ)
	- ESM (explicit): J(θ) = Eq(x) (1/2 |∂ψ(x; θ)-∂logq(x)/∂x|)
	- ISM (implicit): J(θ) = Eq(x) (1/2 |ψ(x;θ)^2+Σi ∂ψi(x;θ)/∂xi|)
	- DSM: qσ(x',x) = qσ(x'|x)q0(x), ∂logqσ(x')/∂x=1/σ^2(x-x')
	- Add noise to the data qσ(x'|x) = N(x'|x, σ^2I), ∇x'logqσ(x'|x)=−(x'−x)/σ
- **Stein-Score**: Q. Liu, J. Lee, and M. Jordan. A kernelized stein discrepancy for goodness-of-fit tests. ICML'16
	- Insight: a discrepancy measure of two p.d.f. by score function sq=∇x logq(x);
	- Problem setup: sample {xi} ∼ p(x) from q(x)? H0: p = q;
	- **Stein's method**: p(x) and q(x) are identical iff Ep\[sq(x)f(x)+∇xf(x)\] = 0
		- (Stein) score function of q(x): sq(x) = ∇x log q(x) = ∇xq(x)/q(x)
	- RKHS: k(x, x') = Σj λj ej(x)ej(x'), {ej}, {λj} are the orthonormal eigenfunctions and positive eigenvalues of k(x,x');
		- If k(x,x') positive definite, its RKHS space H:
		- f(x) = Σj fjej(x), with Σj fj^2/λj < ∞
		- Then (f, g)=Σj fj.gj/λj, equip the space with norm ||f||=(f, f)=Σj fj^2/λj.
		- Every kernel defines a RHKS s.t. k(x,.) ∈ H, f(x)=(f, k(.,x)), k(x, x')=(k(.,x), k(.,x')), k is the reproducing kernel;
	- Stein-class: f(x) s.t. ∫ ∇x(f(x)p(x))dx = 0.
	- Stein operator Ap: Apf(x) = sp(x)f(x) + ∇xf(x)
	- **KSD**: The kernelized Stein discrepancy (KSD) between two distribution p, q;
		- S(p, q) = Ex,x'∼p\[δq,p(x)k(x, x')δq,p(x')\],
		- where δq,p(x) = sq(x) − sp(x) is the score difference;
	- Theorem: Let uq(x,x') = Σjλj (Aqej(x))'(Aqej(x')), where Apf(x) = sp(x)f(x) + ∇xf(x), then KSD:
		- S(p,q) = Σj λj||Ex∼p(Aqej(x))||2.
	- Goodness of fitting given {xi} from p and score function sq():
		- Su(p,q) = 1/n(n-1) Σij uq(xi,xj)
- Y. Song, S. Garg, J. Shi, and S. Ermon. Sliced score matching: A scalable approach to density and score estimation. UAI'19
	- Insight: efficient with a random vector v, p(v)
		- Ep(v) Ep(data) v∇xsθ(x)v + 1/2|sθ(x)|^2 
- **SMLD**: Yang Song, Stefano Ermon. Generative Modeling by Estimating Gradients of the Data Distribution. NIPS'19
	- Insight: a neural network sθ(x) to approximate ∇xlog(pdata(x))
		- 1) perturbing the data using various levels of noise;
		- 2) simultaneously estimating scores corresponding to all noise levels by training a single conditional score network
	- Equivalent to: Ep'(x)\[tr(∇xsθ(x)) + 2|sθ(x)|^2\]
	- Noise Conditional Score Network (NCSN): sθ(x, σ)
		- θ=argmin_θ σi^2 Ep'(x)Epσi(x'|x) ||sθ(x',σi)-∇x logpσi(x'|x)||^2.
- Yang Song, Jascha Sohl-Dickstein, Diederik P. Kingma, Abhishek Kumar, Stefano Ermon, Ben Poole. Score-Based Generative Modeling through Stochastic Differential Equations. ICLR'21
	- Insight: unify SMLD and DDPM in a SDE framework, propose a stochastic solver (PC) and a deterministic (ODE);
	- SMLD:
		- Probability: pσ(x'|x):=Np(x';x,σ^2I) perturbation kernel, pσ(x')=∫pdata(x)pσ(x'|x)dx, NCSN
		- Loss: θ = argmin  Σi=1..N σi^2 E pdata(x)Epσi(x'|x) |sθ(x',σi) - ∇x' logpσi(x'|x)|^2
		- Langevin MCMC: x^i_m = x^i_m-1 + εi sθ(x^i_m-1, σi) + sqrt(2ε)z^i_m, m=1,2,...,M
	- DDPM:
		- Probability: p(xi|xi-1) ~ N(xi; sqrt(1-βi)xi-1, βiI)
		- Loss (ELBO): θ = argmin Σi=1..N (1-αi) E pdata(x)Epαi(x'|x) |sθ(x',i) - ∇x' logpαi(x'|x)^2
		- Reverse MCMC: xi-1 = 1/sqrt(1-β) (xi + βi sθ(xi, i)) + sqrt(β)zi, i=N, N-1, ..., 1
	- DDPM and SMLD as SDE:
		- Forward: dx = f(x,t)dt + g(t) dw
		- Reverse: dx = (f(x, t) - g(t)^2 ∇xlogpt(x))dt + g(t)dw
		- SMLD as SDE: dx = sqrt(d(σ(t)^2)/dt)dw; VE (variance-exploding SDE)
		- DDPM as SDE: dx = -1/2 β(t)xdt + sqrt(β(t))dw
		- Proposed new VP-SDE (variance-preserving): dx = -1/2 β(t)xdt + sqrt(β(t)(1-exp(-2∫0..t β(s)ds))dw
	- Solver
		- PC (stochastic):
			- Predictor: xi = (2-sqrt(1-β))xi+1 + βi+1 sθ(xi+1, i+1)) + sqrt(βi+1)z
			- Corrector: xi = xi + εi sθ(xi, i) + sqrt(εi)z