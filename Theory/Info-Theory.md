# Information Theory

## Basics
- Books
	- D MacKay. Information theory, inference and learning algorithms. Cambridge university press, 2003.

## Preliminary (K-Murphy-2.8)
- Entropy
	- H(X) = -Σp(x)logp(x)
- KL-divergence
	- KL(p|q) = Σp(x)log[p(x)/q(x)]
	- Cross entropy: -Σp(x)logq(x)
	- Theo-2.8.1: KL(p||q) ≥ 0 with equality iff p = q
- Mutual Info
	- I(X;Y) = ΣΣp(x,y)log[p(x,y)/p(x)p(y)]
	- I(X;Y) = H(X) - H(X|Y)
- F-divergence: more general:
	- Df(P|Q) = ∫f(dP/dQ)dQ = ∫f(dp(x)/dq(x))q(x)dx

## Information Bottleneck
- **IB**: N. Tishby, F Pereira, and W Biale. The information bottleneck method. Allerton'99
- W Bialek, I Nemenman, and N Tishby. Predictability, complexity, and learning. NC'01
- S Still and W Bialek. How many clusters? an information-theoretic perspective. NC'04
- D Barber and F Agakov. The IM algorithm: a variational approach to information maximization. NIPS'04
- N Slonim, G Atwal, G Tkacik, and W Bialek. Information-based clustering. PNAS'05
- O Shamir, S Sabato, and N Tishby. Learning and generalization with the information bottleneck. Theoretical Computer Science'10
- S Palmer, O Marre, M Berry, and W Bialek. Predictive information in a sensory population. PNAS'15
- DVIB:
	- Mutual Information: I(X; Y)
		- I(X;Z) = H(X) - H(X|Z);
		- DV (Donsker-Varadhan) representation: dual form;
			- KL(p,q) = sup.T:Ω→R E.p[T] - log(E.q[exp(e^T)])
		- Proof by construction: when G=P, gap is zero;
		- Data Processing Inequality (DPI): X->Y->Z, then I(X;Y)>=I(X;Z)
		- Reparametrization invariance: Two invertible functions f1, f2, then I(X;Y)=I(f1(X);f2(Y))
	- Information Plane Theorem:
		- X-axis: The sample-complexity of Ti depends on I(X;Ti). 
			- how many samples to achieve certain perf.
		- Y-axis: The perf (generalization accuracy) depends on I(Ti;Y).

## Deep Feature Learning
- Information Bottleneck
	- N. Tishby and N. Zaslavsky. Deep learning and the information bottleneck principle. In IEEE Information Theory Workshop, 2015
	- A Achille and S Soatto. Information dropout: Learning optimal representations through noisy computation. 2016.
	- A Alemi, B Poole, I Fischer, J Dillon, R Saurous, and K Murphy. An information-theoretic analysis of deep latent-variable models. 2017
	- **DVIB**: A Alemi, I. Fischer, J Dillon, K Murphy. Deep Variational Information Bottleneck. ICLR'17
		- Insight: x->z->y, z as info-bottleneck
			- Hopefully z has high MI with target y, but low MI with input x; (max-ent principle)
			- Essentially it forces Z to act like a minimal sufficient statistic of X for predicting Y;
		- Formulation:
			- Input X, enc Z, goal/target y
			- max_θ I(Z,Y;θ) s.t. I(X,Z;θ) <= Ic
			- Goal: maximize R = I(Z,Y;θ) − βI(Z, X; θ)
		- Assumption: Y ↔ X ↔ Z
			- p(Z|X,Y) = p(Z|X), makes unsupervised learning possible;
			- I(Z, Y) = E_yz[log[p(y,z)/p(y)p(z)]] = E_yz[log[p(y|z)/p(y)]]
				- where p(y|z) = E_x[p(y|x)p(z|x)/p(z)]
				- Approximate p(y|z) with q(y|z)
				- I(Z,Y) >= E_yz[log[q(y|z)/p(y)]] = E_yz[log(q(y|z))] + H(y), gap: KL(p(y|z),q(y|z))
			- I(Z, X) = E_xz[log[p(z|x)/p(z)]] = E_xz[logp(z|x)] + H(z)
				- Approximate p(z) with r(z)
				- I(Z,X) <= E_xz[logp(z|x)] + E_xz[logr(z)], gap KL(p(z)|r(z))
			- Loss: I(Z,Y;θ) − βI(Z, X; θ) with ELBO;
			- L ≈ 1/N Σn E_z|xn[logq(yn|z) - βlog[p(z|xn)/r(z)]]
				- encoder: p(z|x) = N(z|fµe(x), fΣe(x)),
			- p(z|x)dz = p(ε)dε
				- JIB = 1/N Σn Eε[−logq(yn|f(xn, ε))] + βKL[p(Z|xn), r(Z)].
		- Connection with VAE: no Y, just index i=1/N, each item a class, then:
			- max I(Z, X) − βI(Z, xi),
	- A Saxe, Y Bansal, J Dapello, M Advani, A Kolchinsky, B Tracey, D Cox. On the Information Bottleneck Theory of Deep Learning. ICLR'18
- Mutual information:
	- S Nowozin, Cseke, and R Tomioka. f-gan: Training generative neural samplers using variational divergence minimization. NIPS'16
	- MINE: I Belghazi, A Baratin, S Rajeswar, S Ozair, Y Bengio, A Courville, and R Hjelm. Mine: mutual information neural estimation. ICML'18
		- Problem setup: estimate MI;
		- Key insight: use the upper bound by dual of the KL, a neural discriminator d(x;z);
		- Upper bound with neural approx: I(X;Z) ≥ I(X,Z;Θ)
		- Application: maximize MI to improve GAN on mode-collapse;
	- DIM: R Hjelm, A Fedorov, S Lavoie-Marchildon, K Grewal, P Bachman, A Trischler, Y Bengio. Learning deep representations by mutual information estimation and maximization. ICLR'19
		- https://github.com/rdevon/DIM
		- Problem setup: unsupervised learning;
		- Model:
			- Im -> [conv] -> f-low -> [conv] -> f-high
			- Im1 -> f1-high+f1-low -> [D] -> real
			- Im2 -> f1-high+f2-low -> [D] -> fake
		- Formulation:
			- ψ = argmax I(X;E(ψ(X)));
			- Loss: global-MI + local-MI + prior-matching;
		- Different ways to estimate MI:
			- MINE: based on DV (Donsker-Varadhan representation)
			- JS-MI:
			- InfoNCE:
	- **AMDIM**: P Bachman, R Hjelm, W Buchwalter. Learning Representations by Maximizing Mutual Information Across Views. NIPS'19
		- https://github.com/Philip-Bachman/amdim-public
		- Problem setup: unsupervised learning;
		- Insight: maximizing mutual information between features extracted from multiple views of a shared context;
	- M Gabrié, A Manoel, C Luneau, J Barbier, N Macris, F Krzakala, L Zdeborová. Entropy and mutual information in models of deep neural networks. NIPS'18

## DL Training behavior
- Resources:
	- https://lilianweng.github.io/lil-log/2017/09/28/anatomize-deep-learning-with-information-theory.html
	- Information Theory in Deep Learning (Youtube): https://www.youtube.com/watch?v=bLqJHjXihK8&feature=youtu.be
- Two Optimization Phases:
	- Early: ∥μ∥ >> ∥σ∥
	- Later: std σ becomes much noiser;
	- σ noiser when a layer gets further away from output;
- R. Shwartz-Ziv and N. Tishby. Opening the black box of deep neural networks via information. arXiv preprint arXiv:1703.00810, 2017
	- Deep networks undergo two distinct phases consisting of an initial fitting phase and a subsequent compression phase;
	- the compression phase is causally related to the excellent generalization performance of deep networks; 
	- the compression phase occurs due to the diffusion-like behavior of stochastic gradient descen
- G Pereyra, G Tuckery, J Chorowski, and L Kaiser. Regularizing neural networks by penalizing confident output predictions. ICLRW'17

## DL Theory
- Learning Theory:
	- Old Generalization Bounds:
		- https://mostafa-samir.github.io/ml-theory-pt1/
		- https://mostafa-samir.github.io/ml-theory-pt2/
		- ε^2 < (log|Hε|+1/δ) / 2m
	- New Input compression bound;
