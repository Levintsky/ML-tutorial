# Linear Model

## Basics
- Fisher
- Linear regression:
	- MLE (L2)
	- Bias/Variance trade-off;
	- Bayesian (prior, posterior, predictive);
- Linear classifier (Logistic Regression):
	- MLE, IRLS, Newton/BFGS;
	- Bayesian (Laplacian Approx), BIC, probit-approx for predictive;
	- Online learning: perceptron;
	- Fisher
	- Probit regression:
		- Approx sigmoid with Gaussian erf (probit function);
- GLM, exponential family;
	- learning: ∇θlogp(D|θ) = φ(D) − NE[φ(X)]; moment matching;
	- Max-entropy -> exp family;
- Latent linear
	- FA: obs x=Wz, infer W, z
	- PCA: obs x=Wz, z Gaussian, minimize reconstruction error;
		- y = L^(-1/2)U'(x-E[x])
	- ICA: obs x=Wz, z-Non-Gaussian;
		- fast-ICA (Newton's method, assuming all distribution known and same)
- Sparse linear model
	- L1-norm;
	- Optimization: Lasso; Coord-descent; proximal methods;

## Linear Regression (Kevin Murphy, Chap 7; Bishop, Chap 3)
- 7.1 Introduction;
	- y(x,w) = Σwjφj(x) = wφ(x)
	- (Bishop) Multiple output target t, with Moore-Penrose pseudo-inverse:
		- p(t|x,w,β) = N(t|y(x,w), β^-1)
		- lnp(t|x,w,β) = Nlnβ/2 - Nln(2π)/2 - βE(w) with E(w) as MSE fitting error;
		- Pseudo-inverse: (Φ'Φ)^(-1)Φ'
- 7.2 Model specification:
	- p(y|x,θ) = N(y|wx, σ^2)
	- p(y|x,θ) = N(y|wφ(x), σ^2), basis function;
- 7.3 MLE:
	- l(θ) = Σlogp(yi|xi,θ)
	- OLS (ordinary least squares):
		- NLL(w) = 1/2 (y-Xw)'(y-Xw) = 1/2 w'(X'X)w - w'(X'y)
		- w = (X'X)^(-1)X'y
	- Geometric interpretation: residual y-y^ orthogonal to span of X;
		- y' = X w^ = X (X'X)^(-1) X'y
- 7.4 Robust linear regression:
	- L1-norm
	- Huber-loss
- 7.5 Ridge-regression:
	- J(w) = 1/N Σ(yi-(w0+wxi))^2 + λ|w|^2
	- w = (λI+X'X)^(-1) X'y
	- 7.5.2 Numerical stability:
		- Avoid inverting matrix
		- Cholesky decomposition
		- QR decomposition
	- 7.5.3 Connection with PCA
		- Let X = USV (SVD)
		- y^ = Σ_j uj Sjj uj' y
		- dof(λ) = Σ_j σj^2/(σj^2+λ)
- 7.6 Bayesian linear regression
	- 7.6.1 Posterior (known σ^2):
		- p(y|X,w,μ,σ^2) ~ N(y|μ+Xw,σ^2I) for all observed y;
		- Conjugate prior (Gaussian): p(w) ~ p(w|w0,V0);
		- w0 = 0, V ~ τI: Ridge regression;
	- 7.6.2 Posterior predictive: (test x)
		- p(y|x,D,σ^2) = ∫N(y|xw,σ^2)N(w|w,Vn)dw
		- ~ N(y|wx,σ(x)^2)
		- σ(x)^2 = σ^2 + x Vn x; var of obs and weight w;
	- 7.6.3 Bayesian inf with unknown σ^2:
		- Conjugate prior: p(w,σ^2) = N(w0,σ^2V0)IG(σ^2|a0,b0)
		- Posterior:
			- p(σ^2|D) ~ IG(aN, bN)
			- p(w|D) ~ T(wN, bN/aNVN, 2aN), student-t;
		- Predictive of new test y: p(y|x,D) ~ T(xw, bN/aN(Im+XVnX'), 2aN); student-t;
	- Bishop 3.3: non-diagonal Var
		- Prior: p(w) ~ N(m0, S0)
		- Posterior: p(w) ~ N(mN, SN)
		- m = SN(S^(−1)m0 + βΦ't), β: precision;
		- SN^(-1) = S0^(-1) + βΦ'Φ
		- Predictive: p(t|D,α,β) = ∫p(t|w,β)p(w|D,α,β)dw
		- p(t|D,α,β) ~ N(mNφ(x), σN^2(x))
			- with σN^2(x) = 1/β + φ'(x)SN φ(x)
		- 3.3.3 Equivalent kernel;
			- Express weight by training D={x};
			- y(x,m) = mφ(x) = Σβφ'(x)Sφ(x)t = Σk(x,xn)tn
			- Kernel maxtrix: k(x1,x2) = βφ'(x1)Sφ(x2)
- Bishop 3.2: Bias and Variance trade-off,
	- let h(x) = E[t|x], the true mean of t(x); bias measures diff y(x;D) from h; variance of a solution measures its vary around its own average;
	- E[{y(x;D)-h(x)}^2] = (bias)^2 + Evar
		- (bias)^2 = {E_D[y(x;D)]-h(x)}^2; diff y(x;D) from h
		- Variance: Ev = E_D[{y(x;D)-E[y(x;D)]}^2]
	- Loss: E[L] = ∫{y(x)-h(x)}^2p(x)dx + ∫{h(x)-t}^2p(x,t)dxdt = (Eb)^2 + Ev + noise
		- Noise = ∫{h(x)-t}^2 p(x,t)dxdt
	- In practice, train L different models yi(x);
		- y^(x) = 1/L Σyi(x)
		- (bias)^2 = 1/N Σ{y^(xn)-h(xn)}^2; over all x
		- Variance = 1/NL ΣΣ{yi(x)-y^(x)}^2; over all i, x;
- Bishop 3.4 Bayesian Model comparison:
	- L models {Mi}, i = 1, ..., L.
	- **Bayes factor**: p(D|Mi)/p(D|Mj)
- Bishop 3.5 Evidence approximation:
	- Empirical Bayes:
		- Hyperparameters α, β(w ~ N(0, α^-1), y ~ N(xw, β^-1))
		- Marginalized LE p(t|α, β)
		- Marginalize over w, implicit optimization for α, β respetively;

## Logistic Regression (Kevin Murphy, Chap 8; PRML-Chap-4)
- 8.1 Intro
- 8.2 Model: p(y|x, w) ~ Ber(y, σ(wx))
- 8.3 Fitting
	- 8.3.1 MLE: loss, gradient and Hessian
		- NLL(w) = Σlog(1+exp(-yi w'xi))
		- g = df(w)/dw = X'(μ-y), with μ=σ(wx)
		- H = X'SX, with diag(μi(1−μi))
	- 8.3.2 SGD
		- Avoid zigzag: momentum
	- 8.3.3 Newton's method
	- 8.3.4 IRLS (Iterated reweighted Least Square)
		- Apply Newton's method for logistic regression;
		- w -= H^(-1)g
	- 8.3.5 Quasi-Newton: BFGS;
		- Assumption: Hessian as Diagonal + low-rank approx;
		- Approximate Bk ~ Hk;
			- Bk+1 = Bk + ykyk/yksk - (Bksk)(Bksk)'/skBksk
			- sk = θk - θk-1
			- yk = gk - gk-1
		- Ck ~ Hk^(-1):
			- Ck+1 = (I-skyk'/yksk')Ck(I-skyk'/yksk') _ sksk'/yk'sk
	- 8.3.6 l2 regularization
	- 8.3.7 Multiclass: softmax
- 8.4 Bayesian logistic:
	- **Lapalace approx**: Find a Gaussian approximation q(z) which is centred on a **mode** of the distribution p(z);
		- p(θ|D) = 1/Z exp(-E(θ)), with E(θ) as energy function;
		- E(θ) = -logp(θ,D) ≈ E(θ∗) + (θ-θ∗)g + 1/2 (θ-θ∗)H(θ-θ∗), Taylor expansion around mode θ∗;
		- H = ∇^2 E(θ)|θ∗
		- Approximate p^(θ|D) ≈ exp(-E(θ∗)) exp[-1/2(θ-θ∗)H(θ-θ∗)] ~ N(θ|θ∗, H^(-1));
	- 8.4.2 BIC:
		- log p(D) ≈ log p(D|θ∗) + log p(θ∗) − 1/2log|H|
	- 8.4.3 Gaussian
		- p(w|D) ≈ N(w|w^, H^-1)
		- w^ = argminE(w)
	- 8.4.4 Approx posterior predictive
		- p(y|x, D) = ∫p(y|x, w)p(w|D)dw
		- p(y = 1|x, D) ≈ p(y = 1|x, E[w]), Bayesian point with E[w];
		- MC: p(y=1|x,D) ≈ Σσ(wx) with w sampled from posterior;
		- Probit approx, moderated output
			- Gaussian approx posterior:
				- p(w|D) ≈ N (w|mN, VN)
				- p(y=1|x, D) ≈ ∫σ(wx)p(w|D)dw = ∫σ(a)N (a|μ_a, σa^2)da
				- a = wx, μ_a=E[a], σa^2 = var[a] = xVNx
			- Probit function (Gaussian cdf) erf(a):
				- Φ(a) = ∫N(x|0,1)dx
				- Probit really similar to Sigmoid σ(.); Approx with it!
			- Rescale s.t. σ(.) and Φ(.) has the same slope at origin;
			- Advantage: we can convolve with Gaussian analytically;
- 8.5 Online learning, regret minimization;
	- Regret: 1/k Σf(θ,zt) - min1/kΣf(θ∗,zt)
	- SGD:
		- Running mean: θ^ = 1/k Σθt
		- Polyak averaging: θk = θk-1 - 1/k(θk-1-θk)
	- Sufficient converge condition (Robbins-Monroe):
		- Ση = ∞, Ση^2 < ∞ (e.g. η ~ 1/k)
	- Per-parameter: adagrad with moving variance s;
		- θ = θ - ηg/(τ+sqrt(s))
	- Perceptron: iterate each item, 
		- w = w - η∇E(w) = w + ηφt
		- if y ≠ y^, θ += yixi
		- The perceptron convergence theorem: 
			- if there exists an exact solution (training set linearly separable),
			- Perceptron algorithm is guaranteed to find an exact solution in a finite number of steps
- 8.6 Generative v.s. discriminative models
	- D: p(y|x, w)
	- G: p(x, y|w)
- Bishop 4.1: Fisher
	- m1, m2 as class mean, get direction w (mapping to 1-dim) such that the between class have high variance and within class has low variance:
		- J(w) = wSBw / wSWw
		- Between class: SB = (m2-m1)(m2-m1)'
		- Within class: SW = ΣΣ(xi-mci)(xi-mci)'
		- w ∝ SW^(-1)(m2-m1)

## Generalized Linear Models, Exponential Family (Kevin Murphy, Chap 9)
- 9.1 Introduction
- 9.2 Exponential Family:
	- p(x|θ) = 1/Z(θ) h(x) exp[θφ(x)] = h(x)exp[θφ(x)-A(θ)]
	- A(θ) = logZ(θ); Log-Partition function
	- 9.2.2 Examples
		- Bernoulli, Multinoulli, Univariate Gaussian
	- 9.2.3 Log partition function
		- dA/dθ = E[φ(x)]
		- ∇^2 A(θ) = cov[φ(x)]
	- 9.2.4 MLE
		- **Pitman-Koopman-Darmois theorem**: under certain regularity conditions, the exponential family is the only family of distributions with finite sufficient statistics.
		- ∇θlogp(D|θ) = φ(D) − NE[φ(X)]; moment matching;
	- 9.2.5 Bayes for the exponential family
		- Likelihood: p(D|η) ∝ exp(NηTs − NA(η))
		- Prior: p(θ|ν0, τ0) ∝ g(θ)^ν0 exp(η(θ)τ0)
		- Posterior: p(θ|ν0+N, τ0+SN)
	- 9.2.6 Maximum entropy derivation
		- The principle of maximum entropy or maxent says we should pick the distribution with maximum entropy (closest to uniform),
		- s.t. the constraints that the moments of the distribution match the empirical:
			- Σ_x fk(x)p(x) = Fk
		- Maximize entropy s.t. prob and moment matching constraint:
			- J(p, λ) = -Σp(x)log(x) + λ0(1-Σp(x)) + Σ_k λk(Fk-Σp(x)fk(x))
			- ∂J/∂p(x) = -1 - logp(x) - λ0 - Σ_k λkfk(x) = 0
			- p(x) ∝ exp(- Σλkfk(x)): Gibbs distribution;
- 9.3 Generalized linear models (GLMs)
	- 9.3.2 ML and MAP estimation
	- 9.3.3 Bayesian inference
		- MCMC
- 9.4 Probit regression
	- Logistic: p(y=1|xi, w) = σ(wxi)
	- General: p(y=1|xi, w) = g^−1(wT xi), with g^(-1) maps [−∞, ∞] to [0,1]. Φ(η): standard cdf: probit regression;
	- 9.4.1 ML/MAP estimation using gradient-based optimization
		- μi = wxi, yi^={-1,+1}
		- gradient gi = dlogp(y^|wx)/dw = x yφ(wx)/Φ(yiwxi)
			- φ(.) normal pdf, Φ(.) cdf;
		- Hessian Hi = d^2logp(y^|wx)/dw^2
	- 9.4.2 Latent variable interpretation
		- RUM
	- 9.4.3 Ordinal probit regression
	- 9.4.4 Multinomial probit models
- 9.5 Multi-task learning
	- Different tasks with own parameters share a same prior. Model trained on fewer data could borrow from group with more data;
	- logp(D|β) + logp(β) = Σ[logp(Dj|βj) + |βj−β∗|2] - ||β∗||^2 / 2σ∗^2

## Latent Linear Models (Kevin Murphy, Chap 12)
- 12.1 Factor Analysis (FA)
	- p(zi) = N(zi|μ0, Σ0)
	- p(xi|zi, θ) = N(Wzi+μ, Ψ)
	- 12.1.1 FA is a low rank parameterization of an MVN
		- Marginal: p(xi|θ) = N(xi|Wμ0+μ, Ψ+WΣ0W')
	- 12.1.2 Inference
		- p(zi|xi, θ) = N(zi|mi, Σi)
		- Σi ~ [Σ0^−1 + W'Ψ^(−1)W]^−1
		- mi ~ Σi(W'Ψ^(−1)(xi−μ) + Σ0^(−1)μ0)
	- 12.1.3 Unidentifiability
	- 12.1.4 Mixtures of factor analysers
		- p(xi|zi,qi=k,θ) = N(xi|μk +Wkzi,Ψ), extra: qi
		- p(zi|θ) = N(zi|0, I)
		- p(qi|θ) = Cat(qi|π)
	- 12.1.5 EM for factor analysis models
	- 12.1.6 Fitting FA models with missing data
- 12.2 PCA (Also PRML, Chap-12)
	- 12.2.1 Classical PCA: statement of the theorem
		- J(W, Z) = 1/N Σ|xi-xi^|^2, where xi = Wzi
	- 12.2.2 Proof
	- 12.2.3 Singular value decomposition (SVD)
		- X = USV'
	- 12.2.4 Probabilistic PCA
		- logp(X|W,σ^2) = -N/2log|C| - 1/2Σ xiC^(-1)xi = -N/2log|C| + tr(C^-1Σ^)
	- 12.2.5 EM algorithm for PCA
		- E step: Z^ = (W'W)^(−1)W'X
		- M step: W^ = X^Z'(ZZ')^(-1), σ
- 12.3 Choosing the number of latent dimensions
	- 12.3.1 Model selection for FA/PPCA
- 12.4 PCA for categorical data
- 12.5 PCA for paired and multi-view data
	- 12.5.1 Supervised PCA (latent factor regression)
		- p(zi) ~ N(0, IL)
		- p(yi|zi) ~ N(wy'zi +μy, σy^2)
		- p(xi|zi) ~ N(Wx'zi +μx, σx2^ID)
	- 12.5.2 Partial least squares
- 12.6 ICA (Independent Component Analysis)
	- xt = Wzt + εt, W: mixing matrix;
	- Prior: p(zt)=∏pj(ztj), any form; PCA: i.i.d. Gaussian;
	- 12.6.1 Maximum likelihood estimation
		- Assume observed x is centered and whitened, obs x noise-free;
		- i.e. E[xx']=I, let V=W^(-1)
		- px(Wzt) = pz(Vxt)|det(V)|
		- Assume T i.i.d. samples with same W(V):
			- 1/Tlogp(D|V) = log|det(V)| + 1/T ΣΣlogpj(vjxt)
		- NLL(V) = ΣE[Gj(zj)]
	- 12.6.2 The FastICA algorithm (Hyvarinen and Oja 2000)
		- Fast ICA = Approximate Newton
		- G(z) = −logp(z), g(z) = dG(z)/dz
		- f(v) = E[G(vx)] + λ(1−v'v)
		- ∇f(v) = E[xg(vx)] - βv
		- H(v) = E[xx'g'(vx)] - βI
		- v∗ := E[xg(v'x)] − E[g'(v'x)]v
	- 12.6.3 Using EM
	- 12.6.4 Other estimation principles
		- Maximizing non-Gaussianity
		- Minimizing mutual information
		- Maximizing mutual information (infomax)

## Sparse Linear Models (Kevin Murphy, Chap 13)
- 13.1 Intro
- 13.2 Bayesian variable selection
	- γj = 1 if feature j is "relevant", and let γj = 0 otherwise.
	- f(γ) := −[logp(D|γ) + logp(γ)]
	- 13.2.1 Spike and Slab model
		- Posterior p(γ|D) ∝ p(γ)p(D|γ)
	- 13.2.2 From the Bernoulli-Gaussian model to l0 regularization
		- p(γ, w) ∝ N(w|0, σ2I)π^|γ|0 (1− π)^(D−|γ|0)
		- f(w) = |y−Xw|^2 + λ|w|0
	- 13.2.3 Algorithms
		- Greedy search: matching pursuit, ...
		- Stochastic search: MCMC
		- EM and VI
- 13.3 l1 regularization: basics
	- f(w) = RSS(w) + λ|w|1
	- 13.3.1 Why does l1 regularization yield sparse solutions?
	- 13.3.2 Optimality conditions for lasso
	- 13.3.3 Comparison of least squares, lasso, ridge and subset selection
		- MLE: w^ols = wy
		- Ridge w = w^ols/(1+λ)
		- Lasso w = sign(w^ols)(|w^ols|-λ/2)+
		- Subset selection: w = w^ols if rank(w^ols)<=K else 0
	- 13.3.4 Regularization path
	- 13.3.5 Model selection
	- 13.3.6 Bayesian inference for linear models with Laplace priors
- 13.4 l1 regularization: algorithms
	- 13.4.1 Coordinate descent
		- wj∗ =argminf(w+zej)−f(w); one-coord at a time;
	- 13.4.2 LARS and other homotopy methods
		- Active set of coords rather than just one coord;
	- 13.4.3 Proximal and gradient projection methods
		- f(x) = L(x) + R(x);
			- L: convex, differentiable;
			- R: convex, non-differentiable; e.g. L1-norm
		- prox_R(xt) = argmin_z R(z)+ 1/2|z−xt|^2
		- Proximal operators
			- proxR(x) = soft(x, λ) soft thresholding for L1;
			- hard thresholding for L0;
		- Proximal gradient method
			- Key idea: approx L(.) with quadratic near xt;
			- xt+1 = argmin_z R(z)+L(xt)+gk'(z−xt)+ 1/2tk |z−xt|^2, with gk=∇L(θk)
			- xt+1 = argmin[tkR(z)+1/2|z−ut|^2] = proxτtR(ut)
			- with ut = −τtgt, gt = ∇L(xt)
		- Nesterov
	- 13.4.4 EM for lasso
- 13.5 l1 regularization: extensions
	- 13.5.1 Group Lasso
	- 13.5.2 Fused lasso
	- 13.5.3 Elastic net (ridge + lasso)
- 13.6 Non-convex regularizers
	- 13.6.1 Bridge regression
	- 13.6.2 Hierarchical adaptive lasso
	- 13.6.3 Other hierarchical priors
- 13.7 Automatic relevance determination (ARD)/sparse Bayesian learning (SBL)
- 13.8 Sparse coding
	- non-negative matrix factorization, NMF
	- min_W,z Σ|xi-Wzi|+λ|z|
	- 13.8.3 Compressed sensing
	- 13.8.4 Image inpainting and denoising

## Unclassified
- Alexander Munteanu, Chris Schwiegelshohn, Christian Sohler, David P. Woodruff. On Coresets for Logistic Regression. NIPS'18