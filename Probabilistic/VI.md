# EM, Variational Inference

## Basics
- VI, ELBO:
	- KL(q(z) | p(z|x)) = E(log q(z)) - E(log p(z,x)) + log p(x)
	- logp(x) <= ELBO(q) = E_q(z)[log p(z, x)] - H(q)
		- logp(x) = log[∫p(x,z)dz]
		- = log[∫p(x,z)q(z)/q(z)dz]
		- = log[E_q(z)[logp(x,z)/q(z)]]
		- >= E_q(z)[log[p(x,z)/q(z)]] (Jensen, swap E[.] and log)
	- Special case: mean field;
		- qj(xj) ~ exp(E_-qj[logp(x)]); marginalize out other var xi with qi(.);
- VBEM: infer z and learn θ; p(θ,z1..N|D) ~ q(θ)Πqi(zi)
- MCMC:
	- Hard to do m-step, sample some z and average
- Black-box VI: used in VAE;
	- MC sample instead of integral to compute gradient;

## Summaries and Tutorials
- M. J. Wainwright and M. I. Jordan, Graphical models, exponential families, and variational inference, Foundations and Trends in Machine Learning. 2008
- Blei, D. M., Jordan, M. I., and Paisley, J. W. Variational Bayesian inference with Stochastic Search. ICML'12
- Hoffman, M. D., Blei, D. M., Wang, C., and Paisley, J. Stochastic variational inference. JMLR'13
- David Blei. Variational Inference: A Review for Statisticians, 2018
	- ELBO (Evidence Lower-Bound)

## Mixture Models/EM, (PRML-Chap-9, Kevin Murphy Chap-11)
- {X, Z}, posterior of z (E-step);
	- Q(θ,θ-old) = Σ_z p(z|X,θ-old)p(X,Z|θ)
	- θ-new = argmax_θ Q(θ,θ-old)
	- Similar to ELBO, q = p(z|X,θ-old) to approx p(z|X,θ)
- EM for Bayesian linear regression: converge to the same result with direct method:
	- logp(t,w|α,β) = logp(t|w,β) + logp(w|α)
	- p(α) ~ Gam(α|a0, b0)
	- p(t,w,α) = p(t|w)p(w|α)p(α)
- General EM:
	- p(X|θ) = Σ_z p(X,Z|θ); intractable;
	- logp(X|θ) = L(q,θ) + KL(q||p)
	- L(q,θ) = Σ_z q(z)log[p(x,z|θ)/q(z)]
	- KL(q||p) = Σ_z q(z)log[p(z|x,θ)/q(z)]
- The generalized EM, or GEM, algorithm addresses the problem of an intractable M step. Instead of aiming to maximize L(q, θ) with respect to θ, it seeks instead to change the parameters in such a way as to increase its value;
- 11.1 Latent variable
- 11.2 Mixture models
	- p(x|θ) = Σk πk pk(xi|θ)
	- 11.2.1 Mixture of Gaussian
		- p(x|θ) = Σk πk N(xi|μk,Σk)
	- 11.2.2 Mixture of multinomial
		- p(xi|zi=k,θ) = Π_k Ber(xij|μjk)
	- 11.2.3 Mixture for clustering
		- To infer p(zi=k|xi,θ)
		- Posterior: p(zi)p(x|zi,θ) / Σp(zi)p(x|zi,θ); soft
		- MAP: maxp(zi)p(x|zi,θ); hard clustering
	- 11.2.4 Mixture for experts
		- Graphical model: xi->zi->yi (zi controls different experts); generative
		- p(yi|xi,zi=k,θ) = N(yi|wkxi,σk^2)
		- p(zi|xi,θ) = Cat(zi|S(Vxi)), zi posterior by generative likelihood
- 11.3 Parameter estimation for mixture models
	- 11.3.1 Unidentifiability
	- 11.3.2 Computing a MAP estimate is **non-convex**
		- log p(D|θ) = Σ_x log[Σ_z p(xi,zi|θ)]
- 11.4 The EM algorithm
	- 11.4.1 Basic idea
		- Complete likelihood: lc=Σlogp(xi,zi|θ)
		- Q(θ, θ-old) = E[lc(θ)|D, θ-old]
		- M-step: θ-new = argmax_θ Q(θ, θ-old)+logp(θ)
	- 11.4.2 EM for GMM
	- 11.4.3 EM for mixture of experts
	- 11.4.4 EM for DGM
	- 11.4.5 EM for the Student distribution
	- 11.4.6 EM for probit regression
	- 11.4.7 Theoretical basis for EM
		- Lower bound: Jensen's inequality
		- ΣlogΣ > ΣΣlog, b/c log(.) concave;
		- ELBO: L(θ, qi) = -KL(qi(zi)||p(zi|xi,θ)) + logp(xi|θ)
	- 11.4.8 Online EM
		- Batch-EM: sgd-style parameter update;
		- Incremental EM: optimize q1, then q2, ...;
		- Stepwise-EM: paramter Polyak averaging;
	- 11.4.9 Other EM variants
		- Annealed EM: smooth the posterior by raising temperature, then gradually cooling;
		- Variational EM: q(zi) could be approximate;
		- Monte Carlo EM: draw samples, then sufficient statistics;
		- Generalized EM: partial M-step, increase ELBO rahter than maximization;
		- ECEM: conditional;
		- Over-relaxed EM: θt+1 = θt + η(M(θt)−θt), with aggressive η;
- 11.5 Model selection for latent variable models
	- K∗ = argmaxk p(D|K).
- 11.6 Fitting models with missing data
- Important property:
	- **log-sum-exp is Convex**, so Z(w) is always convex for mixture models
- Modern:
	- Ji Xu, Daniel Hsu, Arian Maleki. Benefits of over-parameterization with EM. NIPS'18
	- Wu Lin, Mohammad Emtiyaz Khan, Mark Schmid. Fast and Simple Natural-Gradient Variational Inference with Mixture of Exponential-family Approximations. ICML'19
	- Belhal Karimi, Hoi-To Wai, Eric Moulines, Marc Lavielle. On the Global Convergence of (Fast) Incremental Expectation Maximization Methods. NIPS'19

## VI (Kevin Murphy, Chap-21, 22)
- 21.1 Intro
- 21.2 VI
	- KL(p|q) = Σ_x p(x)log(p/q); (intractable, b/c Expectation over p(x))
	- KL(q|p) = Σ_x q(x)log(q/p);
	- Main goal: J(q) = KL(q||p)
	- Generally unnormalized p^(x)=p(x,D)=p(x)Z is tractable, in practice:
		- KL(q|p^) = KL(q|p) - logZ
	- 21.2.1 Alternative interpretation
		- J(q) = -H(q) + Eq[E(x)], E(x)=-logp^(x) energy
	- 21.2.2 Forward or reverse KL
		- KL(q|p): I-projection, zero avoiding
		- KL(p|q): mode-covering
- 21.3 Mean field
	- q(x) = Πqi(xi)
	- Goal: min_q1,... KL(q||p)
	- logqj(xj) = E_-qj[logp(x)] = Σ_x-jΠ_i≠j qi(xi)logp(x)
	- 21.3.1 Derivation
		- L(q) = -J(q) = Σq(x)log(p^(x)/q(x))
		- qj(xj) ~ exp(E_-qj[logp(x)])
	- 21.3.2 Example: Ising model
		- x: hidden clean image; y: obs;
		- p(x) = 1/Z0 exp(-E0(x)), with energy E0(x)=-ΣΣWijxixj defined on neighbor;
		- Likelihood: p(y|x) = Πp(yi|xi) = Σexp(-Li(xi))
		- Posterior: p(x|y) = 1/Z exp(-E0(x)+Li(x))
		- Approx: q(x) = Πqi(xi, μi), assuming μi as mean of xi;
		- Logp^(x) = xiΣWijxj + Li(xi)
- 21.4 Structured Mean field
	- Exploit tractable substructure (no need to fully factorize)
	- 21.4.1 Example: factorial HMM
- 21.5 Variational Bayes
	- So far, we assume we know θ and infer z;
	- Both θ and z, VB;
	- VBEM: p(θ,z1..N|D) ~ q(θ)Πqi(zi)
	- 21.5.1 Example: VB for a univariate Gaussian
		- p(μ,λ) = N(μ|μ0,(κ0λ)−1)Ga(λ|a0,b0)
		- Approx with: q(μ, λ) = qμ(μ)qλ(λ)
	- 21.5.2 Example: VBEM for linear regression
- 21.6 Variational Bayes EM
	- Latent model: zi → xi ← θ.
	- p(θ, z1:N|D) ≈ q(θ)q(z) = q(θ)Πq(zi)
	- 21.6.1 Example: VBEM for mixtures of Gaussians
		- Variational E-step: logq(z) by integral q(θ)
		- Variational M-step: logq(θ) by integral q(z)
- 21.7 Variational message passing and VIBES
	- One can then sweep over the graph, updating nodes one at a time, in a manner similar to Gibbs sampling. This is known as variational message passing or VMP (Winn and Bishop 2005)
- 21.8 Local variational bounds
	- Variational logistic regression
		- p(y|X,w) = Πexp(yiηi-lse(ηi)), with ηi=Xiwi
			- log-sum-exp or lse(ηi)=log(1+Σexp(Σηim))
		- Not conjugate to Gaussian prior;
- 22.1 Introduction
- 22.2 Loopy belief propagation: algorithmic issues
	- 22.2.1 A brief history
	- 22.2.2 LBP on pairwise models
		- Initialize message ms→t=1, beliefs bel(xs)=1;
		- ms→t(xt) = Σs[ψs(xs)ψst(xs, xt) ∏u mu→s(xs)]
		- bel(xs) ∝ ψs(xs) ∏t mt→s(xs)
	- 22.2.3 LBP on a factor graph
	- 22.2.4 Convergence
		- Damping: 
		- TRP, TRW
	- 22.2.5 Accuracy of LBP
- 22.3 Loopy belief propagation: theoretical issues
	- 22.3.1 UGMs represented in exponential family form
	- 22.3.2 The marginal polytope
		- The space of allowable μ vectors is called the marginal polytope, and is denoted M(G), where G is the structure of the graph defining the UGM.
	- 22.3.3 Exact inference as a variational optimization problem
		- L(q) = −KL(q||p)+logZ = Eq[logp'(x)]+H(q) ≤ logZ
		- maxμ∈M θ'μ + H(μ)
	- 22.3.4 Mean field as a variational optimization problem
		- inner approximation: MF(G) ⊆ M(G), some edges (sufficient stat) are set as zero;
	- 22.3.5 LBP as a variational optimization problem
		- Σx τs(xs) = 1; normalization constraint;
		- Σt τs(xs, xt) = τs(xs); marginalization constraint.
		- L(G) := {τ ≥ 0 : (1) holds ∀s ∈ V and (2) holds ∀(s, t) ∈ E}
	- 22.3.6 Loopy BP vs mean field
- 22.4 Extensions of belief propagation
	- 22.4.1 Generalized belief propagation
	- 22.4.2 Convex belief propagation
- 22.5 Expectation propagation
	- 22.5.1 EP as a variational inference problem
	- 22.5.2 Optimizing the EP objective using moment matching
	- 22.5.3 EP for the clutter problem
- 22.6 MAP state estimation
	- 22.6.1 Linear programming relaxation
		- argmax_x∈X m θφ(x) = argmax_μ∈M(G) θ'μ
	- 22.6.2 Max-product belief propagation
	- 22.6.3 Graphcuts
		- Submodular: Euv(1, 1) + Euv(0, 0) ≤ Euv(1, 0) + Euv(0, 1)
	- 22.6.4 Experimental comparison of graphcuts and BP
	- 22.6.5 Dual decomposition

## Approximate Inference (PRML-Chap-10, Kevin-Murphy-Chap-21)
- Basics: Many problems can be expressed in terms of an optimization problem in which the quantity being optimized is a functional. This is done by restricting the range of functions over which the optimization is performed. Our goal is to find an approximation for the posterior distribution p(Z|X) as well as for the model evidence p(X).
- E.g.1: factorized Gaussian to approximate 2-dimension Gaussian:\
	<img src="/Bayes/images/VI/em-gauss-1.png" alt="drawing" width="400"/>\
	- Iteratively optimize:\
		<img src="/Bayes/images/VI/em-gauss-2.png" alt="drawing" width="400"/>
- E.g.2: Gaussian, factorized prior (mean, precision) for conjugate prior:
	- Assume q(μ,τ)=q(μ)q(τ), we have
- E.g.3: EM of GMM with Dirichlet prior on π (PRML 10.2), Gaussian-Wishart prior on mean, precision;
- E.g.4: EM of linear regression: a gamma prior α ~ gamma(a0, b0) for weight precision; assume q(w, α) ~ q(w)q(α)
	<img src="/Bayes/images/VI/em-lr-1.png" alt="drawing" width="400"/>\
	<img src="/Bayes/images/VI/em-lr-2.png" alt="drawing" width="400"/>\
	<img src="/Bayes/images/VI/em-lr-3.png" alt="drawing" width="300"/>
	- Assume variational factorized posterior: q(w, α) = q(w) q(α)
	- Prior alpha:\
		<img src="/Bayes/images/VI/em-lr-4.png" alt="drawing" width="400"/>
	- Weight w:\
		<img src="/Bayes/images/VI/em-lr-5.png" alt="drawing" width="400"/>\
		<img src="/Bayes/images/VI/em-lr-6.png" alt="drawing" width="400"/>
	- Predict:\
		<img src="/Bayes/images/VI/em-lr-7.png" alt="drawing" width="400"/>\
		<img src="/Bayes/images/VI/em-lr-8.png" alt="drawing" width="400"/>
- E.g.5: exponential family;
	- Model: (x, z) with latent z, conjagate prior on nita;\
		<img src="/Bayes/images/VI/em-exp-family-1.png" alt="drawing" width="400"/>
	- Variational factorized posterior: q(z,η)=q(z)q(η)
	- q(z)\
		<img src="/Bayes/images/VI/em-exp-family-2.png" alt="drawing" width="400"/>
	- q(η)\
		<img src="/Bayes/images/VI/em-exp-family-3.png" alt="drawing" width="400"/>
- Local variational method, **conjugate function**:\
	<img src="/Bayes/images/VI/local-vi-1.png" alt="drawing" width="400"/>
	- For convex function f(x) and g(λ), we define its **lower bound**:\
		<img src="/Bayes/images/VI/local-vi-2.png" alt="drawing" width="400"/>
	- For concave funtions, we could get **upper bound**:\
		<img src="/Bayes/images/VI/local-vi-3.png" alt="drawing" width="400"/>
	- Log(logistic) is concave, with upper bound:\
		<img src="/Bayes/images/VI/local-vi-4.png" alt="drawing" width="400"/>
	- Log(logistic) lower bound:\
		<img src="/Bayes/images/VI/local-vi-5.png" alt="drawing" width="400"/>
		<img src="/Bayes/images/VI/local-vi-6.png" alt="drawing" width="400"/>
		<img src="/Bayes/images/VI/local-vi-7.png" alt="drawing" width="400"/>
- E.g.6: variational logistic regression:
- Expectation propagation: the **reverse form KL(p, q)**:
	- We use an exponential family q(z) to approx p(z):\
		<img src="/Bayes/images/VI/ep-1.png" alt="drawing" width="400"/>
	- E.g. Moment matching; the cost:\
		<img src="/Bayes/images/VI/ep-2.png" alt="drawing" width="400"/>

## Black-box VI
- Rajesh Ranganath Sean Gerrish David M. Blei. Black Box Variational Inference. AISTATS'14
	- Basics behind VAE;
	- Assume q(z|λ) with λ as parameter;
	- ELBO: L(λ) = E_q(λ)[logp(x,z)-logq(z)]
	- ∇λL = Eq[∇λ logq(z|λ)(logp(x,z) − logq(z|λ))].
	- Noisy unbiased gradient of ELBO by MC:
		- Sample some z[s] ~ q(z|λ)
		- ∇λL ≈ 1/S Σ_s ∇λ logq(zs|λ)(logp(x, zs) − logq(zs|λ)),

## Conjugate Prior
- Mohammad Emtiyaz Khan, Wu Lin. Conjugate-Computation Variational Inference: Converting Variational Inference in Non-Conjugate Models to Inferences in Conjugate Models. AISTATS'17

## Minibatch
- MD Hoffman, DM Blei, C Wang, J Paisley. Stochastic variational inference. JMLR'13
	- Insight: case of mini-batch, a global variable β to guarantee correctness; otherwise, x1, x2 is not independent of x3; minibatch won't work;
		<img src="/Bayes/images/VI/svi.png" alt="drawing" width="400"/>

## Latent Models
- Binary latent factors:
	- Z Ghahramani and T Griffiths. Infinite latent feature models and the indian buffet process. NIPS'06
- Matrix Factorization:
	- A Mnih and R Salakhutdinov. Probabilistic matrix factorization. NIPS'08
- Clustering, co-clustering:
	- C Kemp, J Tenenbaum, T Griffiths, T Yamada, and N Ueda. Learning systems of concepts with an infinite relational model. AAAI'06
- Sparse coding:
- Dependent GSM:
	- Y Karklin and M Lewicki. Emergence of complex cell properties by learning to generalize in natural scenes. Nature'09
- Structure discovery (recursive search-based):
	- C Kemp and J Tenenbaum. The discovery of structural form. PNAS'08
	- R Grosse, R Salakhutdinov, W Freeman, and J Tenenbaum. Exploiting compositionality to explore a large space of model structures. UAI'12
