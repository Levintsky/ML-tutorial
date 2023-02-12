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
		- DV or Donsker-Varadhan representation: dual form;\
			<img src="/Basic-ML/images/info-theory/dv.png" alt="drawing" width="350"/>
		- Proof by construction: when G=P, gap is zero;\
			<img src="/Basic-ML/images/info-theory/dv-dual.png" alt="drawing" width="450"/>
		- Data Processing Inequality (DPI): X->Y->Z, then I(X;Y)>=I(X;Z)
		- Reparametrization invariance: Two invertible functions f1, f2, then I(X;Y)=I(f1(X);f2(Y))
	- Information Plane Theorem:
		- X-axis: The sample complexity of Ti is determined by the encoder mutual information I(X;Ti). Sample complexity refers to how many samples you need to achieve certain accuracy and generalization.
		- Y-axis: The accuracy (generalization error) is determined by the decoder mutual information I(Ti;Y).\
			<img src="/Basic-ML/images/info-theory/info-plane.png" alt="drawing" width="450"/>

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
		- Key insight: use the upper bound by **dual representations of the KL-divergence**, a neural discriminator d(x;z);
		- Upper bound with neural approximation:\
			<img src="/Basic-ML/images/info-theory/mine-1.png" alt="drawing" width="450"/>
		- Algorithm:\
			<img src="/Basic-ML/images/info-theory/mine-2.png" alt="drawing" width="350"/>
		- Application: maximize MI to improve GAN on mode-collapse;\
			<img src="/Basic-ML/images/info-theory/mine-3.png" alt="drawing" width="350"/>
	- **DIM**: R Hjelm, A Fedorov, S Lavoie-Marchildon, K Grewal, P Bachman, A Trischler, Y Bengio. Learning deep representations by mutual information estimation and maximization. ICLR'19
		- https://github.com/rdevon/DIM
		- Problem setup: unsupervised learning;
		- Model:\
			<img src="/Basic-ML/images/info-theory/dim-1.png" alt="drawing" width="450"/>
		- Formulation:
			- **Mutual information maximization**: Find the set of parameters, phi, such that the mutual information, I(X;E(phi(X))), is maximized. Depending on the end-goal, this maximization can be done over the complete input, X, or some structured or "local" subset;
			- **Statistical constraints**: Depending on the end-goal for the representation, the marginal U(phi,P) should match a prior distribution, V. Roughly speaking, this can be used to encourage the output of the encoder to have desired characteristics (e.g., independence).
			- Put together: 1st/2nd terms for global/local MI with neural classifier parametrized by w1, w2; 3rd term discriminator with phi for statistical matching with prior;\
				<img src="/Basic-ML/images/info-theory/dim-5.png" alt="drawing" width="400"/>
		- Different ways to estimate MI:
			- MINE: based on DV (Donsker-Varadhan representation)\
				<img src="/Basic-ML/images/info-theory/dim-2.png" alt="drawing" width="400"/>
			- JS-MI:\
				<img src="/Basic-ML/images/info-theory/dim-3.png" alt="drawing" width="400"/>
			- InfoNCE:\
				<img src="/Basic-ML/images/info-theory/dim-4.png" alt="drawing" width="400"/>
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
	- Among early epochs, the mean values are three magnitudes larger than the standard deviations.
	- After a sufficient number of epochs, the error saturates and the standard deviations become much noisier afterward.
	- The further a layer is away from the output, the noisier it gets, because the noises can get amplified and accumulated through the back-prop process (not due to the width of the layer).
		<img src="/Basic-ML/images/info-theory/two-opt-phase.png" alt="drawing" width="450"/>
- R. Shwartz-Ziv and N. Tishby. Opening the black box of deep neural networks via information. arXiv preprint arXiv:1703.00810, 2017
	- Deep networks undergo two distinct phases consisting of an initial fitting phase and a subsequent compression phase;
	- the compression phase is causally related to the excellent generalization performance of deep networks; 
	- the compression phase occurs due to the diffusion-like behavior of stochastic gradient descen
- G Pereyra, G Tuckery, J Chorowski, and L Kaiser. Regularizing neural networks by penalizing confident output predictions. ICLRW'17

## DL Theory
- Learning Theory:
	- Old Generalization Bounds:
		- Read https://mostafa-samir.github.io/ml-theory-pt1/ and https://mostafa-samir.github.io/ml-theory-pt2/ for ML theory;
			<img src="/Basic-ML/images/info-theory/old-bound.png" alt="drawing" width="450"/>
	- New Input compression bound:\
			<img src="/Basic-ML/images/info-theory/new-bound.png" alt="drawing" width="450"/>
