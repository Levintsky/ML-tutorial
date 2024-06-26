# Learning Theory

## Resouces
- Princeton: https://youtu.be/PHcodnoOlgI
- MSR DL theory: https://www.youtube.com/live/3wbLr-NnIKI?feature=share
- MIT: https://www.mit.edu/~9.520/fall19/
- Duke:
	- https://users.cs.duke.edu/~cynthia/teaching.html
	- https://youtu.be/nACHK2CgyGg
- PAC-Bayes:
	- J Shawe-Taylor and R Williamson. A PAC analysis of a Bayesian estimator. COLT'97
	- P Alquier. PAC-Bayesian bounds for randomized empirical risk minimizers. 08

## Basics
- Goal:
	- Bound the gap of performance between population and empirical;
- Common techniques:
	- Symmetrization: z' an indepdent copy of z.
- Inequalities:
	- **Jensen**: f: R → R convex, then f(E[z]) ≤ E[f(z)]
	- **Markov Inequality**: X>0 random var,
		- P(X≥a) ≤ E[X]/a
	- **Chebyshev**: P(|Z-E[Z]|≥t) ≤ Var(Z)/t^2
	- **Chernoff bounds**: for ∀ t ≥ 0,
		- P(Z ≥ E[Z] + t) ≤ minλ≥0 E[exp(λ(Z−E[Z]))]exp(−λt) = minλ≥0 M(z-E[z],λ)exp(−λt)
	- **Hoeffding**: z1, z2, ... zn independent, zi ∈ [a, b] with a,b bounded. X̄ = 1/n ΣXi, let μ=E[x]
		- P(|X̄−μ|≤ε) ≥ 1 - 2exp(-2nε^2 / (b-a)^2)
	- **McDiarmid**: P(|f(X1..,Xn)-E[f]|≥t) ≤ 2exp(−2t^2/Σci^2)
	- Young's inequality, if 1/p + 1/q = 1, then
		- ab ≤ a^p/p + b^q/q, (= if a^p=b^q)
	- Holder: Let (S, Σ, μ) be a measure space and let p, q ∈ [1, ∞] with 1/p + 1/q = 1.
		- Then, |fg|1 ≤ |f|p |g|q	
- Asymptotic: for a given θˆ
	- L(θˆ) − infL(θ) ~ c/n + o(1/n)
	- θˆ − θ∗ ~ c/√n
- Uniform: ∀ θ, w.h.p. (with p≥1-δ)
	- Finite |H|: |L(h)-Lˆ(h)| ≤ √[(ln|H|+ln(2/δ))/2n]
	- Infinite (ε-cover+Lipschitz): |Lˆ(θ)−L(θ)| ≤ O(√(p max(ln(κBn), 1)/n))
- Rademacher complexity, bound expectation (weaker than uniform)
	- Goal bound excess risk expectation: E_z[sup_h∈H(L(h)-Lˆ(h))]
		- weaker than uniform, which doesn't have E_z;
	- Define: Rn(F) := E_z[E_σ[sup_f 1/n ∑σif(zi)]]
	- Let h()=f() i.e. loss function, we can bound excess risk:
		- E_z[sup_h(L(h)-Lˆ(h))] ≤ 2Rn(F); (strict)
	- Empirical Rs(F), with p≥1-δ
		- sup_f[1/n∑f(zi) - E_z[f(z)] ≤ 2Rs(F) + 3√[log(2/δ)/2n]; (McDiarmid)
	- VC-dim: a special case and Upper bound of Rademacher:
		- VC(f) := max(n) s.t. f(.) can shatter at most n points;
- Concrete models:
	- Margin theory: insight of why large margin works.
		- Hinge loss lγ(yh(x)) as surrogate for 0-1;
		- Talagrand's lemma: compose of Rad-complexity;
		- Generalization loss ≤ 2Rs(H)/γ_min + lower order; (Talagrand)
	- Linear model:
		- L2+L2 bound: |w2|2 ≤ B, E[|x|2^2] ≤ C, then
			- Rs(H) ≤ B/n √[∑|xi|^2]; (strict by Jensen)
			- Rn(H) ≤ BC/√n; (average Rs(H) over x sampling)
		- L1+L∞ bound: |w2|1 ≤ B, |x|∞ ≤ C, then
			- Rs(H) ≤ BC √[2log(2d)/n]; (strict by Holder)
	- 2-layer neural net: fθ(x) = ⟨w,φ(Ux)⟩ = wφ(Ux), x ∈ Rd and y ∈ R, w ∈ Rm and U ∈ Rm×d.
		- Theo 5.9 Rn(H) ≤ 2Bw Bu C √[m/n] (Rad-def + vec-norm-trick)
			- Not ideal, growing with m (not consistent with empirical results);
		- Theo 5.10 C(θ) = ∑|wj|∥uj∥2,  H = {fθ | C(θ) ≤ B}, ∥x∥2 ≤ C for all i ∈ {1,...,n}, then
			- Rs(H) ≤ 2BC/√n (improved bound)
		- Generalization bound decreases with m;
		- Equivalence with L1-svm;
	- Deep nets visa covering number;
		- Theo 5.16 covering number of linear model:
			- logN(ε, F, ρ) ≤ [B^2C^2/ε^2]log[2d+1];
		- Theo 5.20 Rs(F) ≤ c/√n (∏κi)(∑bi^(2/3)/κi^(2/3))^(3/2)
		- Remark 5.22 generalization bound ~ Rs(F)/γ_min
		- Lemma 5.23 log|C| ≤ ∑g(εi, ci−1)
- Data-dependent generalization bound
	- All-layer margin: robust in every layer implies good generalization;
- Tutorial:
	- Shai Shalev-Shwartz and Shai Ben-David. Understanding Machine Learning- From Theory to Algorithms. 2014
- Resources:
	- Stanford CS 229: https://cs229.stanford.edu/extra-notes/hoeffding.pdf
	- Stanford Stat 214;
	- https://zhuanlan.zhihu.com/p/337298338
	- https://docs.google.com/spreadsheets/d/1sLxEPagWrCiYBbkpLUcr5VOjgGjaZ-5mMsrKhTDhm40/edit#gid=0

## Preparation (Shai-Ben-David Textbook)
- Chap 3:
	- PAC learnability;
	- Sample complexity: m(ε, δ)
	- Agnostic PAC learning (realizability assumption removed)
	- Generalized loss;
- Chap 4: uniform convergence;
	- ∀h ∈ H, |LS(h) − LD(h)| ≤ ε.
	- Finite Classes Are Agnostic PAC Learnable
- Chap 5: The Bias-Complexity Tradeoff
	- No-Free-Lunch Theorem: every alg has its domain to work;
	- (in practice, we only face a very small set with free lunch)
- Chap 6: VC-Dimension
	- Restriction of H to C: Hc = {(h(c1),...,h(cm)) : h ∈ H}
	- Shattering: |Hc| = 2^|c|
	- VC-dim: maximal size of a set, able to shatter;
	- (In)finite VC-dim <-> PAC (un)learnable;
		- Growth function: τH(m) = max |HC|, m个样本可产生的最大set size;
		- Sauer Lemma: if VCdim(H) ≤ d < ∞, then (数学归纳法可证)
			- τH(m) ≤ ∑0..d C(m, i)
			- Especially, when m > d+1, τH(m) ≤ (em/d)^d
		- Theo 6.11 |LD(h)-Ls(h)| ≤ f(τH(m), m, δ)
			- Proof: 1. 对称性(z1',...,zm') + Jensen + 引入Rad σ, + Hoeffding -> 对某个h成立, 指数衰减成立;
			- 最多|Hc|个, 个数由VC决定(Sauer);
- Chap 7: Nonuniform learnability;
	- (ε, δ)-competitive: LD(h) ≤ LD(h′) + ε. (与uniform区别, 不同h)
	- nonuniformly learnable: LD(A(S)) ≤ LD(h) + ε.
	- Theo 7.2: NonUC iff H是可数个UC的并;
	- SRM (Structural Risk Minimization): 每个Hn一个weight w(n), ∑w(n)≤1.
		- Then NUC成立: ∀h∈H, LD(h) ≤ LS(h)+ min εn(m,w(n)·δ).
			- 证明: δn = w(n)δ
		- 算法: h ∈ argmin_h∈H [Ls(h) + εn(h)(m,w(n(h))·δ)]
	- Minimum Description Length and Occam’s Razor:
		- w(n)对更可能正确的赋更大w(n)
	- Kraft Inequality: S ⊆ {0, 1}∗ is a prefix-free set of strings, then
		- ∑σ∈s 1/2^|σ| ≤1
	- H中class: prefix-free set dsl for H, then ∀h∈H, LD(h) ≤ LS(h)+ √[|h|+ln(2/δ)/2m], 其中|h|=d(h)
	- Occam's Razor: 所有解释中prefer短的;
	- Consistency: LD(A(S)) ≤ LD(h) + ε.
- Chap 8: The Runtime of Learning
- Chap 9: Linear Predictors
	- Half space: HSd = sign ◦ Ld = {x → sign(h_w,b(x)) : h_w,b ∈ Ld}.
		- Homogenous: d
		- Nonhomogenous: VCdim(HSd) = d + 1.
		- Realizable: ERM;
		- Non-realizable: computationally hard, surrogate loss;
		- LP: max(u, w), s.t. Aw ≥ v
		- Perceptron: w(t+1) = w(t) + yixi for incorrect cases: yi(wt,xi) ≤ 0
			- Theo-9.1: B = min{∥w∥, yi(w,xi)≥1}, R = max_i∥xi∥, perceptron guarantee to converge within at most (RB)^2 steps.
			- Proof: Cosine angle between w⋆ and w(T+1) is at least √T/RB
				- Assume w1=0 zero-init,
				- Bound ⟨w⋆,w(T+1)⟩ ≥ T: (w⋆,wt+1) - (w⋆,wt) ≥ 1
				- Bound ∥w(t+1)∥ ≤ √TR: ∥w(t+1)∥^2 ≤ ∥wt∥^2 + R^2, 
				- Cosine angle: [w⋆, w(T+1)]/∥w⋆∥/∥wT+1∥
	- Linear regression
	- Logistic Regression: convex
		- Hsig = φsig ◦ Ld ={x → φsig(⟨w,x⟩) : w ∈ Rd}.
- Chap 10: Boosting
	- γ-Weak-Learnability: whp 1 − δ, L(D,f)(h) ≤ 1/2 − γ.
	- Decision stumps: HDS = {x → sign(θ−xi)·b: θ∈R, i∈[d], b∈{±1}}.
		- Find the best dimension and split, efficient by sorting;
	- Adaboost:
		- Init weight of each data D={1/m,1/m,...}
		- New learner ht = WL(D(t), S), compute weighted perf εt = ∑ D(t) 1[yi≠ht(x)]
		- Weight of new WL: wt = 1/2 log(1/ε −1)
		- Update weight of new data, Dt+1_i = normalize(Dt_i exp[-wt yi ht(xi)])
		- Theo-10.2: Ls(hs) ≤ exp(−2γ^2 T)
			- Proof: Zt+1/Zt =  2√[εt+1(1−εt+1)] ≤ exp(−2γ^2)
	- Linear Combinations of Base Hypotheses
		- VCdim(L(B, T )) ≤ T (VCdim(B) + 1) (3 log(T (VCdim(B) + 1)) + 2).
	- AdaBoost for Face Recognition
- Chap 11: Model Selection and Validation
	- Model Selection Using SRM
	- Validation, Hold Out Set, The Model-Selection Curve, k-Fold Cross Validation, LOO
- Chap 12: Convex Learning Problems
	- epigraph(f) = {(x,β) : f(x) ≤ β}.
		- a function f is convex if and only if its epigraph is a convex set
	- Smoothness: gradient is β-Lipschitz
		- v,w we have ∥∇f(v) − ∇f(w)∥ ≤ β∥v − w∥.
	- Surrogate Loss Functions: convex and upper bound the original loss;
- Chap 13: Regularization and Stability
	- Regularized Loss Minimization
		- argmin_w (LS(w) + R(w))
		- Ridge regression: λ∥w∥^2 + 1/m |wX-y|^2
			- w = (2λmI + A)−1 b.
			- Theo-13.1: if ∥x∥≤1, ∥w∥≤B holds, for any ε ∈ (0,1),let m ≥ 150B^2/ε^2
				- E[Ld(A(s))] ≤ min_w LD(w) + ε
	- Stable: S=(z1,...,zm), Si: replace zi with z';
		- l(A(S(i)), zi) − l(A(S), zi) should be small;
	- Tikhonov Regularization as a Stabilizer
		- Strongly convex: f(αw+(1−α)u) ≤ αf(w) + (1−α)f(u) − λ2α(1−α)∥w−u∥^2.
		- f(w) = λ∥w∥^2 is 2λ-strongly convex.
		- Lipschitz loss: l(A(S(i)), zi) − l(A(S), zi) ≤ ρ∥A(S(i)) − A(S)∥.
		- l(A(Si), zi) − l(A(S), zi) ≤ 2ρ2/λm
		- E[l(A(Si), zi) − l(A(S),zi)] ≤ 48β/λm E[LS(A(S))] ≤ 48βC/λm

## Prepration (Stanford CS-229)
- **Markov Inequality**: X>0 random var,
	- P(X≥a) ≤ E[X]/a
	- Proof: divide by X≥a and X≤a, bound each part;
- **Chebyshev**:
	- P(|Z-E[Z]|≥t) ≤ Var(Z)/t^2
	- Proof: Markov with |Z-E[Z]| as positive var;
- **Chernoff bounds**: for ∀ t ≥ 0,
	- P(Z ≥ E[Z] + t) ≤ minλ≥0 E[exp(λ(Z−E[Z]))]exp(−λt) = minλ≥0 M(z-E[z],λ)exp(−λt)
	- P(Z ≤ E[Z] - t) ≤ minλ≥0 E[exp(λ(E[Z]-Z))]exp(−λt) = minλ≥0 M(E[z]-z,λ)exp(−λt)
	- Proof: Markov with exp[λ(Z-E[Z])] as positive var;
		- P(Z−E[Z] ≥ t) = P(exp(λ(Z−E[Z])) ≥ exp(λt)) ≤ E[exp(λ(Z−E[Z]))]exp(-λt)
- **MGF**: moment generation function;
	- M(z, λ) := E[exp(λz)]
		- M(z, λ) ≤ exp(C^2λ^2/2), ∀ λ ∈ R, for some C ∈ R, depends on distribution of z. Always used with Chernoff bound;
	- Gaussian Z ∼ N (0, σ^2),
		- M(z, λ)=exp(σ^2λ^2/2)
	- Rademacher rv (±1 with p=1/2)
		- E[exp(λS)] ≤ exp(λ^2/2)
		- Combine with Chernoff to bound the sum of random sign Z=∑Si
		- P(Z≥t) ≤ E[exp(λZ)]exp(-λt) ≤ exp(nλ^2/2)exp(-λt)
			- Choose λ to minimize nλ^2/2-λt
			- P(Z≥t) ≤ exp(-t^2/2n)
- **Hoeffding's lemma**: required for Hoeffding's Inequality, zi∈[a, b] bounded
	- E[exp(λ(z−E[z]))] ≤ exp(λ^2(b-a)^2/8), ∀ λ ∈ R
	- Insight: symmetrization + Jensen + Rad-inequality, zi∈[a, b] required to bound (z-z')^2.
	- Proof:
		- Ez(exp(λ(z−E[z]))) = Ez(exp(λ(z−Ez'[z']))), (symmetrization)
		- ≤ Ez[Ez' exp(λ(z-z'))], (Jensen)
		- = Ez,z'[Es[exp(λs(z-z'))|z,z']], (Introduce S ∈ {−1, 1} is a random sign variable)
			- Es[exp(λs(z-z'))|z,z'] ≤ exp(λ^2(z-z')^2/2), (Rademacher rv, i.e. E[exp(λS)] ≤ exp(λ^2/2))
		- ≤ exp(λ^2(a-b)^2/2), (weaker version, with 2 not 8)
- **Hoeffding**: z1, z2, ... zn independent, zi ∈ [a, b] with a,b bounded. X̄ = 1/n ΣXi, let μ=E[x]
	- P(|X̄−μ|≤ε) ≥ 1 - 2exp(-2nε^2 / (b-a)^2)
	- Insight: Chernoff + Hoeffding Lemma;
	- Proof:
		- p(X̄−μ ≥ t) ≤ E[exp(λn(X̄−μ))]exp(-λnt); (Chernoff)
		- = ∏E[exp(λ(zi-μ))]exp(-λnt)
		- ≤ ∏exp(λ^2(b-a)^2/8) exp(-λnt); (Hoeffding's Lemma)
			- Minimize w.r.t. λ≥0, we have
		- p(X̄−μ ≥ t) ≤ exp(-2nt^2/(b-a)^2)
- Young's inequality, if 1/p + 1/q = 1, then
	- ab ≤ a^p/p + b^q/q, (= if a^p=b^q)
	- Proof: Jensen or area;
- Holder: Let (S, Σ, μ) be a measure space and let p, q ∈ [1, ∞] with 1/p + 1/q = 1.
	- Then, |fg|1 ≤ |f|p |g|q
	- Proof:
		- Let |f|p=|g|q=1, scale;
		- Young's inequality, if 1/p + 1/q = 1, then
			- ab ≤ a^p/p + b^q/q
		- Each point s, we have 
			- |f(s)g(s)| ≤ |f(s)|^p/p + |g(s)|^q/q
		- Integral on both sides, rhs=1 (1/p+1/q=1)
			- |fg|1 ≤ |f|p^p/p + |g(s)|q^q/q = 1

## Supervised Learning Formulations (Stanford CS-229/Stat-214)
- 1.1 Supervised learning
	- training set;
	- predictor, hypothesis, model;
	- expected loss, population loss, expected risk, population risk;
	- hypothesis class, hypothesis family, excess risk;
- 1.2 Empirical risk minimization
	- empirical risk: on training set;
		- equal to population risk in expectation;

## Asymptotic Analysis (Stanford CS-229/Stat-214)
- 2.1 Asymptotics of empirical risk minimization
	- Goal: show excess risk is bounded as:
		- L(θˆ) − infL(θ) ≤ c/n + o(1/n)
	- Theo 2.1 Suppose: (a) θˆ →p θ∗ as n → ∞ (consistency); (b) ∇^2 L(θ∗) full rank; (c) other appropriate regularity hold. Then:
		- √n(θˆ−θ∗) ~ Op(1) bounded in probability, i.e. given ε, exists M s.t. p(|√n(θˆ−θ∗)|>M) < ε.
		- √n(θˆ−θ∗) →d Gaussian
		- n(θˆ−θ∗) ~ Op(1)
		- n(L(θˆ)−L(θ∗)) →d Gaussian
		- Proof main idea: Taylor expansion at θ∗;
			- Part 1, 2: 0 = ∇Lˆ(θˆ) = ∇Lˆ(θ∗) + ∇^2 Lˆ(θ∗)(θˆ-θ∗) + O(|θˆ-θ∗|^2)
			- CLT with Xi = ∇l((xi, yi), θ∗), mean Xˆ = ∇L(θ∗)
			- Part 3, 4: L(θˆ) at θ∗ to 2nd order, then Lemma 2.3.
	- Theo 2.2 Central Limit Theorem. Xi i.i.d. Xˆ = 1/n ΣXi
		- 1. Xˆ → E[X];
		- 2. √n(Xˆ−E[X]) -> N(0, Σ)
	- Lemma 2.3 distribution compound
		- 1. If Z ∼ N(0, Σ) and A is a deterministic matrix, then AZ ∼ N(0, AΣA').
		- 2. If Z ∼ N(0, Σ^−1) and Z ∈ Rp, then Z'ΣZ ∼ χ2(p), where ∼ χ2(p) is the chi-squared distribution with p degrees of freedom.
	- Theo 2.4 (MLE paradigm) suppose P(y|x; θ), θ∈Θ; loss MLE, nll l(xi,yi,θ)=-logP(y|x; θ), then
		- θ converge;
		- E[∇l(θ∗)] = 0;
		- Cov(∇l) = ∇^2 L; (integral by part)
		- √n(θˆ−θ∗) →d N(0, ∇2L(θ∗)^−1).
- 2.2 Limitations of asymptotic analysis
	- Obscure dependencies on higher order terms

## Concentration Inequalities (Stanford CS-229/Stat-214)
- Insight:
	- 1. X1 +...+Xn concentrates around E[X1 +...+Xn].
	- 2. More generally, f(X1,...,Xn) concentrates around E[f(X1,...,Xn)].
- 3.1 The big-O notation
- 3.2 Chebyshev's inequality
	- Theo 3.1 (**Chebyshev**)
		- P(|Z-E[Z]|≥t) ≤ Var(Z)/t^2
	- Intuition: tail behavior, density decay at least at 1/t^2;
	- Proof: requires Markov Inequality:
		- Let X=(Z-μ)^2 and a=t^2, apply Markov;
- 3.3 Hoeffding's inequality
	- Theo 3.2 (**Hoeffding**) X1, X2, ... Xn independent real, ai ≤ Xi ≤ bi almost surely. X̄ = 1/n ΣXi, let μ=E[x]
		- P(|X̄−μ|≤ε) ≥ 1 - 2exp(-2n^2ε^2 / Σ(bi-ai)^2)
	- 1/n^2 Σ(bi-ai)^2: upper bound or proxy of Var(Xi)
	- Take ε=O(σ√logn)=σ√(clogn), P(|X̄−μ|≤ε) decays at n^(-2c)
	- Compact form when Xi are bounded;
- 3.4 Sub-Gaussian random variables
	- Def. E[exp λ(X-μ)] ≤ exp(σ^2λ^2/2). σ-sub-Gaussian and say it has variance proxy σ^2.
	- Theo 3.7 sub-Gaussian.
		- Pr[|X−μ|≥t] ≤ 2exp(−2t^2/σ2), ∀t∈R.
		- Proof: Markov with exp[λ()], with tightest λ. (similar to Hoeffding)
	- Theo 3.10 sum of sub-Gaussian.
	- 3.4.1 Examples of sub-Gaussian random variables
		- Rademacher random variables
		- Random variables with bounded distance to mean
		- Bounded random variables
- 3.5 Concentrations of functions of random variables
	- Theo 3.15 (**McDiarmid**'s inequality) f(X1,...,Xn) not overly sensitive to change of a single coord:
		- |f(.,xi,.)-f(,xiˆ,)| ≤ ci, then
		- P(|f(X1..,Xn)-E[f]|≥t) ≤ 2exp(−2t^2/Σci^2)
		- Proof: sub-Gaussian;
	- 3.5.1 Bounds for Gaussian random variables
		- Theo 3.18 (**Gaussian Poincare inequality**) X1, X2, ..., Xn i.i.d. N(0,1)
			- Var(f(X1,...,Xn)) ≤ E[|∇f(X1,...,Xn)|^2]
		- Theo 3.19 (**Wainwright**) f: L-Lipschitz w.r.t. Euclidean distance, Xi i.i.d. N(0,1)
			- P(|f(X)-E[f(X)]|≥t) ≤ 2exp(−t^2/2L^2)

## Generalization Bounds via Uniform Convergence
- Insight:
	- non-asymptotic analysis;
- 4.1 Basic concepts
	- Uniform convergence is a property of a parameter set Θ, which gives us bounds of the form:
		- Pr[|Lˆ(θ)−L(θ)|)≥ε] ≤ δ; ∀θ ∈ Θ.
	- 4.1.1 Motivation: Uniform convergence implies generalization
		- L(θˆ)−L(θ∗) = [L(θˆ)−Lˆ(θˆ)] + [Lˆ(θˆ)−Lˆ(θ∗)] + [Lˆ(θ∗)−L(θ∗)]
		- 1st: ?
		- 2nd: <0
		- 3rd: O(1/√n) via Hoeffding's inequality (l(.,.) bounded)
	- 4.1.2 Deriving uniform convergence bounds
		- 1. Suppose we have a bound of the form Pr[|Lˆ(θ) − L(θ)| ≥ ε′] ≤ δ′ for some single, fixed choice of θ.
		- 2. all possible values of θ.
	- 4.1.3 Intuitive interpretation of uniform convergence
		- Uniform convergence implies generalization, excess risk is small;
		- Asymptotic: L(θ) "close" to Lˆ(θ)
		- Uniform: shape L clsoe to Lˆ
- 4.2 Finite hypothesis class
	- Theo 4.1 H is finite, loss l() bounded in [0, 1], then with p≥1−δ
		- |L(h)-Lˆ(h)| ≤ √[(ln|H|+ln(2/δ))/2n]
	- Proof: union of sum
	- 4.2.1 Comparing Theorem 4.1 with standard concentration inequalities
		- ∀h ∈ H, w.h.p. |L^(h)−L(h)| ≤ O(1/√n), concentration inequality
		- w.h.p., ∀h ∈ H |L^(h)−L(h)| ≤ O(ln|H|/√n), uniform convergence
	- 4.2.2 Comparing Theorem 4.1 with asymptotic bounds
		- L(hˆ) − L(h∗) ≤ c/n + o(n^−1)
- 4.3 Bounds for infinite hypothesis class via discretization
	- Assume parameter within a L2-ball:
		- H={hθ: θ ∈ R, ∥θ∥ ≤ B}.
	- 4.3.1 Discretization of the parameter space by ε-covers
		- Def: ε-cover
		- Lemma 4.5 (ε-cover of l2 ball) B,ε > 0, and let S = {x ∈ Rp : ∥x∥ ≤ B}, then there exists an ε-cover with at most max((3B√p/ε)^p ,1) elements.
			- Proof: set C = {x ∈ S : xi =ki√p, ki ∈Z, |ki| ≤ B√p/ε} grid has at most max((3B√p/ε)^p ,1) balls.
	- 4.3.2 Uniform convergence bound for infinite H
		- Def. κ-Lipschitz functions: |L(θ) − L(θ′)| ≤ κ∥θ − θ′∥.
		- Theo 4.8 l((x, y), θ) ∈ [0, 1] and κ-Lipschitz in θ w.r.t. l2-norm. Then with p≥1−O(exp(−Ω(p))), we have:
			- ∀θ, |Lˆ(θ)−L(θ)| ≤ O(√(p max(ln(κBn), 1)/n))
		- Proof sketch: get finite ε-cover and bound with theo 4.1, and extend to all θ in each ball by Lipschitz.
		- Proof: Fix δ, ε > 0, let C be a ε-cover.
			- Event (within the ball) E={∀θ ∈ C, |Lˆ(θ)−L(θ)| ≤ δ). P(E) ≥ 1-2|C|exp(-2nδ^2); (Theo 4.1)
			- ∀θ ∈ S, we pick a ball containing it (θ0 ∈ C s.t. ∥θ−θ0∥ ≤ ε)
				- Within the ball, |Lˆ(θ)−L(θ)| ≤ |Lˆ(θ)−Lˆ(θ0)|+|Lˆ(θ0)−L(θ0)|+|L(θ0)−L(θ)| ≤ 2κε + δ;
				- Let ε = δ/(2κ), |Lˆ(θ) − L(θ)| ≤ 2δ
			- We set δ = √[c0p max(1,ln(κBn)))/n], with c0=36
				- Since ln |C| ≤ p ln(3B/(δ/2)), (Lemma 4.5)
				- ln|C|−2nδ^2 ≤ pln(6Bκ/δ) - 2nδ ≤ ... ≤ -p
			- Therefore, with
				- p ≥ 1 − 2|C|exp(−2nδ^2) = 1 − 2exp(ln|C|−2nδ^2) ≥ 1−O(exp(−p)),
				- |L(θ) − L(θ)| ≤ 2δ = O(√p/n max(1, ln(κBn))
- 4.4 Rademacher complexity
	- 4.4.1 Motivation for a new complexity measure
		- 1. If the hypothesis class H is finite,
			- L(hˆ) − Lˆ(hˆ) ≤ O(√(log|H|/n))
		- 2. p-dimensional
			- L(hˆ) − Lˆ(hˆ) ≤ O(√(p/n))
		- not precise enough: it depends solely on p and is not always optimal.
			- L(hˆ) − Lˆ(hˆ) ≤ O(√(Complexity(Θ)/n))
	- 4.4.2 Definitions
		- A weaker goal:
			- Uniform (supereme): sup_h∈H(L(h)−Lˆ(h))
			- Here (mean): E[sup(L(h)−Lˆ(h))] ≤ upper bound, expecation over training data {(xi, yi)}n;
		- Def 4.10 (**Rademacher complexity**) f: Z → R,
			- Rn(f) := Ez[Eσ[sup 1/n ∑σif(zi)]]
		- Theo 4.13 Ez[sup_f[1/n∑f(zi) - E_z[f(z)]]] ≤ 2Rn(f)
			- Proof: symmetrization.
				- sup_f[1/n∑f(zi) - E_z[f(z)]] = sup_f(1/n∑f(zi) - E_z'[1/n ∑f(zi')])
				- = sup_f(E_z'[1/n∑f(zi) - 1/n∑f(zi')])
				- ≤ E_z'[sup_f(1/n∑f(zi) - 1/n∑f(zi'))]; b/c sup_u(E_v[f(u,v)]) ≤ E_v[sup_u(g(u,v))]
			- Take E[] on both sides
				- Ez[.] ≤ E_z[E_z'[sup_f(1/n∑f(zi) - 1/n∑f(zi'))]]
				-       = E_z,z'[E_σ[sup_f(1/n ∑ σi(f(zi)-f(zi'))]], b/c σ(f(z)-f(z')) ->d f(z)-f(z')
				-       ≤ E_z,z',σ [sup_f(1/n∑σi(f(zi)) + sup_f(1/n∑-σi(f(zi'))]
				-       = 2Rn(F)
		- e.g. 15. Binary classification, y ∈ {±1}, l0-1((x,y),h)=(1-yh(x))/2, zero-one loss;
			- Rn(F) = Rn(H)/2
	- 4.4.3 Dependence of Rademacher complexity on P
		- Extreme example: z=z0 almost surely, Rn(f) = 1/√n
- 4.5 Empirical Rademacher complexity
	- Def 4.17 (**Empirical Rademacher complexity**) Rs(F), on dataset S={z1,z2,...,zn}
	- Theo 4.18 f∈F, 0≤f(z)≤1, Then with p≥1−δ
		- sup_f[1/n∑f(zi) - E_z[f(z)] ≤ 2Rs(F) + 3√[log(2/δ)/2n]
		- Proof:
			- Let g(z1,...,zn) = sup_f[1/n f(zi)−E[f(z)]]
			- 1. McDiarmid: change one z, diff ≤ 1/n
				- Then, p(g≥E[g]+ε) ≤ exp(-2nε^2); (McDiarmid)
			- 2. E[g] ≤ 2Rn(F); (Theo 4.13)
			- 3. empirical Rad-comp g'(z1,...,zn)=Rs(F)
				- g'(z1,...,zn)-g'(z1,..,zi',.,zn) ≤ 1/n, (similar to step-1, for emp)
				- p(g'-E[g']≥ε) ≤ exp(-2nε^2); (McDiarmid)
			- 4. set δ s.t. exp(−2nε^2) = δ/2, our goal (excess diff) satisfies with p≥1−δ:
				- g ≤ E[g] + ε
				-   ≤ 2Rn(F) + ε; (4.13)
				-   ≤ 2(Rs(F)+ε) + ε; (step-3)
				-   = 3Rs(F) + ε
	- Corollary 4.19. Let F be a family of loss functions F = {(x, y) 􏰀→ l((x, y), h) : h ∈ H} with l((x, y), h) ∈ [0, 1] for all l, (x, y) and h. Then, with probability 1 − δ, the generalization gap is
		- Lˆ(h) − L(h) ≤ 2RS(F) + 3√[log(2/δ)/2n]; for all h ∈ H. (4.92)
		- Insight: loss function for f(zi), LHS is excess risk;
	- 4.5.1 Rademacher complexity is translation invariant
		- Prop 4.5.1 Proposition 4.5.1. Let F be a family of functions mapping Z → R and define F′ = {f′(z) = f(z) + c0 | f ∈ F} for some c0 ∈ R. Then RS(F) = RS(F′) and Rn(F) = Rn(F′).
- 4.6 Covering number upper bounds Rademacher complexity
	- All potential output space:
		- Q := {(f(z1),...,f(zn)) : f ∈ F} ⊆ Rn,
	- Prop 4.6.1 (**Massart's finite lemma**) if 1/√n |v| ≤ M < ∞
		- Rs(F) ≤ √[2M^2log|Q|/n]
	- Corollary 4.21 f: z->R, if for all f, √[1/n Σf(zi)^2] ≤ M
		- Rs(F) ≤ √[2M^2log|F|/n]
	- Theorem 4.25. Let F be a family of functions Z → [−1, 1]. Then
		- Rs(F) ≤ inf_ε>0(ε+√[2logN(ε,F,L2(Pn))/n])
		- Insight: ε as discretization error;
	- 4.6.1 Chaining and Dudley's theorem
		- Theo 4.26 (**Dudley**) F: Z → R, then
			- Rs(F) ≤ 12 ∫0..∞ √[2logN(ε,F,L2(Pn))/n] dε
			- Insight: f bounded not required unlike Theo 4.25. Averaging over different scales;
		- Proof: chaining with progressively finer discretization;
	- 4.6.2 Translating Covering Number Bounds to Rademacher Complexity
		- Conditions that theo-4.26 finite (assume F bounded in [-1, 1])
			- N(ε,F,L2(Pn)) ~ (1/ε)^R
			- N(ε,F,L2(Pn)) ~ a^(R/ε)
		- Theo 4.28 (**Localized Dudley**) for any cutoff α ≥ 0
			- Rs(F) ≤ 4α + 12 ∫..∞ √[2logN(ε,F,L2(Pn))/n] dε
	- 4.6.3 Lipschitz composition
		- Lemma 4.29 Suppose φ is κ-Lipschitz, and ρ = L2(Pn). Then,
			- log N(ε, φ◦F, ρ) ≤ log N(ε/κ, F, ρ)
- 4.7 VC dimension and its limitations

## Rademacher Complexity Bounds for Concrete Models and Losses
- 5.1 Margin theory for classification problems
	- 5.1.1 Intuition
		- the larger this margin is, the smaller the bound on the generalization gap is.
	- 5.1.2 Formalizing margin theory
		- Def 5.1 (**(Unnormalized) Margin**). Fix the hypothesis hθ. The (unnormalized) margin for example (x,y) is defined as:
			- margin(x) = yhθ(x).
			- Margin is only defined on examples where sgn(hθ(x)) = y. (Note that margin(x) ≥ 0 because of our assumption of complete separability.)
		- Def 5.2 (Minimum margin). Given a dataset D = ((x(1), y(1)), . . . , (x(n), y(n))), the minimum margin over the dataset is defined as
			- γmin := min_i∈{1,...,|D|} y(i)hθ(x(i)).
		- **surrogate loss**: margin loss/ramp loss;
		- Lemma 5.3 (Talagrand’s lemma). Let φ : R → R be a κ-Lipschitz function. Then
			- RS (φ ◦ H) ≤ κRS (H),
		- Applying to margin loss: φ(t) = lγ (t), which is 1/γ-Lipschitz
			- Rs(F) ≤ 1/γ Rs(H′)
		- generalization loss ≤ 2Rs(H)/γ_min + low-order term,
- 5.2 Linear models
	- 5.2.1 Linear models with weights bounded in l2 norm
		- Theorem 5.5. Let H = {x → ⟨w,x⟩ | w ∈ Rd, ∥w∥2 ≤ B} for some constant B > 0. Moreover, assume E_x∼p[∥x∥2]≤C , where P is some distribution and C > 0 is a constant. Then
			- Rs(H) ≤ B/n √[∑|xi|^2]
			- Rn(H) ≤ BC/√n
	- 5.2.2 Linear models with weights bounded in l1 norm
		- Theorem 5.7. Let H = {x → ⟨w, x⟩|w ∈ Rd, ∥w∥1 ≤ B} for some constant B > 0. Moreover, assume |xi|∞ ≤ C for some constant C > 0 and all points in S = {xi} ⊂ Rd. Then
			- Rs(H) ≤ BC√[2log(2d)/n]
		- Lemma 5.8 (**Massart's lemma**). Suppose Q ⊂ Rn is finite and contained in the l2-norm ball of radius M√n for some constant M > 0, i.e.,
			- Q ⊂ {v ∈ Rn |∥v∥2 ≤ M√n}.
			- Then, for Rademacher variables σ = (σ1, σ2, . . . , σn) ∈ Rn,
			- E_σ[sup_v∈Q 1/n⟨σ,v⟩] ≤ M√[2log|Q|/n].
- 5.3 Two-layer neural networks
	- Assump: fθ(x) = ⟨w,φ(Ux)⟩ = wφ(Ux), with φ() as ReLU;
	- Theo 5.9. For some constants Bw > 0 and Bu > 0, let
		- H = {fθ | ∥w∥2 ≤ Bw, ∥ui∥2 ≤ Bu, ∀i ∈ {1,2,...,m}}, and E[∑x^2] ≤ C^2, then
		- **Then, Rn(H) ≤ 2Bw Bu C √[m/n]**
		- Proof: norm trick;
		- Insight: not an ideal bound, depends on m.
	- 5.3.1 Refined bounds
		- Theo 5.10 Let C(θ) = ∑|wj|∥uj∥2 , and for some constant B > 0 consider the hypothesis class
			- H = {fθ | C(θ) ≤ B}.
			- If ∥x∥2 ≤ C for all i ∈ {1,...,n}, then
			- **Rs(H) ≤ 2BC/√n**
		- Proof: positive homogeneity + vec-norm-trick (Cauchy-Schwarz)
		- Lemma 5.12 σ ∈ {±1}^n, sup_θ⟨σ,fθ(x)⟩ ≥ 0.
			- Eσ[sup_θ|⟨σ, fθ(x)⟩|] ≤ 2Eσ[sup_θ⟨σ, fθ(x)⟩].
- 5.4 More implications and discussions on two-layer neural nets
	- 5.4.1 Connection to l2 regularization
	- 5.4.2 Generalization bounds that are decreasing in m
		- L(θˆm) ≤ 4C/√n 1/γm∗ + (lower-order terms),
		- To show that this bound does not worsen as m grows, we just have to show that γm∗ is non-decreasing in m.
		- Theo 5.13. Let γm∗ be the minimum margin obtained by solving (II) with a two-layer neural network of width m. Then γ∗,m ≤ γ∗,m+j for all positive integers j.
	- 5.4.3 Equivalence to an l1-SVM in m → ∞ limit
- 5.5 Deep neural nets (via covering number)
	- 5.5.1 Preparation: covering number for linear models
		- Theo 5.16 ([Zhang, 2002]). Suppose x(1), ···, x(n) ∈ Rd are n data points, and p, q satisfies 1/p + 1/q = 1 and 2≤p≤∞. Assume that ||x(i)||p ≤C for all i. Let:
			- Fq ={x → w'x:| |w|q ≤ B};
		- Then **logN(ε,F ,ρ) ≤ [B^2C^2/ε^2] log[2d+1]**
		- Remark 5.17 **Rs(Fq) ≤ O(BC/√n)**
	- 5.5.2 Deep neural networks
		- fθ(x) = Wrσ(Wr−1σ(··· σ(W1x) ...))
		- Theo 5.20 Suppose that ∀i, ∥x(i)∥2 ≤ c and let
			- F = {fθ : ∥Wi∥op ≤ κi, ∥Wi'∥2,1 ≤ bi}, op as operator norm or spectral norm;
			- Then Rs(F) ≤ c/√n (∏κi)(∑bi^(2/3)/κi^(2/3))^(3/2)

## Data-dependent Generalization Bounds for Deep Nets
- Goal: derive a bound on the population loss at θ that is a polynomial function of the Lipschitz-ness of f on x(1),...,x(n) as well as the norm of θ.
	- Uniform convergence with a data-dependent hypothesis class.
		- ∀f ∈ F, L(f) ≤ comp(F)/√n
		- ∀f, L(f) ≤ comp(F)/√n
		- most results: type I, comp(F)/√n = Rn(F)
	- This chapter:
		- L(f) ≤ comp(f, {(x(i), y(i))}n)
		- Surrogate loss to obtain a data-dependent generalization bound;
- 6.1 All-layer margin
	- Generalized margin: gf(x,y) := f(x)y for correctly classification;
	- Lemma 6.4 Suppose gf is a generalized margin. Let G = {gf: f ∈ F}. Suppose that for some R, logN(ε,G) ≤ ⌊R^2/ε^2⌋ for all ε > 0. Then, with high probability over the randomness in the training data, for every f in F that correctly predicts all the training examples,
		- L01 ≤ O(1/√n R/min_i gf(xi, yi)) + O(1/√n)
	- Theo 6.5 w.h.p., for all f with training error 0, then
		- L01(f) ≤ O(1/√n · ∑|Wi|1,1/min_i∈[n]mf(x(i),y(i)) +O(r/√n),
		- Insight: robust in every layer -> good generalization;

## Theoretical Mysteries in Deep Learning
- 7.1 Framework for classical machine learning theory
	- 1. Approximation theory;
	- 2. Statistical generalization;
	- 3. Optimization;
- 7.2 Deep learning theory and its differences
	- 1. Approximation theory: over-parametrized -> 0 loss;
	- 2. Statistical generalization: l2 -> non-unique minimizer, some are good, some are bad;
	- 3. Optimization: implicit regularization effect of optimizers

## Nonconvex Optimization
- 8.1 Optimization landscape
	- 1. Identify a large set of functions that stochastic gradient descent/gradient descent can solve;
	- 2. Prove that some of the loss functions in machine learning problems belong to this set. (Most of the effort will be spent here.)
- 8.2 Efficient convergence to (approximate) local minima
	- Def-8.1 (Local minimum of a function)
	- ∇f(x) = 0 and ∇^2f(x) ≽ 0, with counter-examples;
	- Theo-8.3. It is NP-hard to check whether a point is a local minimum or not
	- 8.2.1 Strict-saddle condition
		- Theo-8.5 (Informally stated). If f is (α,β,γ)-strict-saddle for some positive α,β,γ, then many optimizers (e.g. gd, sgd, cubic regularization) can converge to a local minimum with ε-error in Euclidean distance in time poly(d, 1/α, 1/β, 1/γ, 1/ε).
- 8.3 All local minima are global minima: two examples
	- 8.3.1 Principal components analysis (PCA)
		- min g(x) = 1/2 ∥M−xx'∥^2.
		- Theo-8.7. All local minima of g are global minima (even though g is non-convex).
			- Proof: 1. all stationary points must be eigenvectors;
			- 2. Show that all local minima must be eigenvectors of the largest eigenvalue
	- 8.3.2 Matrix Completion
		- Def 8.9 PΩ(M)
		- Def 8.10 The matrix completion task is to recover M (with respect to some loss functions) given the observation PΩ(M).
		- Loss: f(x) = 1/2∥PΩ(M −xx')∥2F.
		- Def 8.12 (Incoherence) suppose L2-norm ∥z∥ = 1, ∥z∥∞ ≤ μ/√d.
		- Theo 8.14. Assume p = poly(μ, logd)/dε^2 for some sufficient small constant ε and assume z is incoherent. Then with high probability, all local minima of f are O(√ε)-close to +z or −z (the global minima of f).
		- Theo 8.23 (f has no bad local minimum). Assume p = poly(μ,logd)/dε^2. Then with high probability, all local minima of f are O(√ε)-close to +z or −z.
	- 8.3.3 Other problems where all local minima are global minima
- 8.4 The Neural Tangent Kernel (NTK) Approach
	- Insight: NTK kernel: Θ: Rin x Rin -> R
		- Feature map: x -> ∇f(x;Θ)
		- Θ(x, x′) := ⟨∇f(x;θ), ∇f(x′; θ)⟩
		- Physical meaning: influence of change val of f(x) on f(x′)
		- Learning:
			- For each x, we have label y;
			- Cost C := ∑c(f(xi), yi)
			- Full gradient flow of parameter Θ: ∂t Θ(t) = -∇C(f(.,Θ))
			- Prediction flow: ∂t f(x, Θ(t)) = -∑i Θ(x, xi) ∂c(yi′, yi)
		- Large width limit: NTK kernel Θ ~ constant;
	- fθ(x) = fθ0(x) + ⟨∇θfθ0(x), θ − θ0⟩ + higher order terms
		- Taylor expansion around θ0;
	- gθ(x) = ⟨∇θ fθ0(x), ∆θ⟩,
	- Def. 8.24 fθ0(x) = 0 so that y = y′
		- K(x, x′) = ⟨φ(x), φ(x′)⟩ = ⟨∇θfθ0 (x), ∇θfθ0(x′)⟩.
	- Benefits: l(fθ(x), y) ≈ l(gθ(x), y), RHS convex if l() convex;
	- 8.4.1 Two examples of the NTK regime
		- 1. Reparameterize with a scalar;
		- 2. Overparametrization (with specific initialization);

## Implicit/Algorithmic Regularization Effect
- 9.1 Implicit regularization effect of zero initialization in over-parametrized linear regression
	- Lˆ(β) = 1/2 ∥y − Xβ∥2.
	- Lemma 9.1. Let X+ denote the pseudoinverse1 of X. Then β is a global minimizer if and only if β = X+⃗y+ζ for some ζ such that ζ ⊥x1,...,xn.
	- Theo-9.3. Suppose gradient descent on Lˆ(β) with initialization β0 = 0 converges to a solution βˆ such that Lˆ(βˆ) = 0. Then βˆ = β⋆.
- 9.2 Implicit regularization of small initialization in nonlinear models
	- Lˆ(β) = 1/4n ∑(yi − fβ(xi))^2.
		- fβ(x) := ⟨β ⊙ β,x⟩
	- 9.2.1 Main results of algorithmic regularization
		- LASSO: Lˆ(β) = ∑(yi − θxi)^2 + |θ|1
		- Theo-9.4. Let c be a sufficiently large universal constant. Suppose n ≥ cr2 log^2(d) and α ≤ 1/d^c, then when log(d/α)/η <= T <= 1/η√dα, we have:
			- |β⊙β − β⋆⊙β⋆|2 ≤ O(α√d)
	- 9.2.2 Ground work for proof and the restricted isometry property
		- x ~ N(0,I)
		- Lemma 9.10. Assume n ≥ Ω(r2). w.h.p. over the randomness in x1, ... xn, ∀v such that ∥v∥0 ≤ r we have
			- (1−δ)∥v∥2 ≤ 1/n ∑⟨v, xi⟩2 ≤ (1+δ)∥v∥2
	- 9.2.3 Warm-up for analysis: Gradient descent on population loss
		- Theo-9.13. For sufficiently small η, gradient descent on L(β) converges to β in Θ( log(1/(εα))/η) in iteration with ε-error in l2-distance.
			- Proof:
				- βt+1 =βt − η(βt⊙βt − β⋆⊙β⋆)⊙βt.
				- Induction on sparse and zero index set;
	- 9.2.4 Proof of main result: gradient descent on empirical loss
		- Theo-9.14. Suppose η ≥ Ω(1). Then, gradient descent on Lˆ(β) with t = Θ(αlog(1/δ)/η) steps satisfies:
			- |β⊙β − β⋆⊙β⋆|2 ≤ O(1/√n).
- 9.3 From small to large initialization: a precise characterization
	- 9.3.1 Preparation: gradient flow
		- ∂w(t)/∂t = −∇L(w(t)
	- 9.3.2 Characterizing the implicit bias of initialization
		- f(x) = (w+⊙2 − w_⊙2)⊤ x
		- 

## PAC Basics
- Generalization error: E(h, D)
- Empirical error: E^(h,D)
- Inequalities:
	- Jensen: f() convex, then f(E(x)) <= E(f(x))
	- Hoeffding: m sample, P(|E^x-Ex|>=ε) <= exp(-2m ε^2)
	- McDiarmid: suppose sup|f(x1,..xi,..)-f(x1,..xi',..)|<=c, then p(|f(x)-f(xi')|>=ε)<=exp(-2ε^2/Σ(ci^2))
- Algorithm: L
- Concept: C: X to Y;
- Mapping: h: X to Y;
- Hypothesis space: H, containing all h;
- Separable/consistent: all correct
- Non-separable/consistent:
- PAC-identify: 0 < ε, δ < 1, P(E(h)<=ε)>=1-δ, then L can identify concept C from H;
- PAC-learnable: exist algorithm L, poly s.t. m>=poly(1/ε, 1/δ, |x|, |c|), L can PAC-identify C;
	- Insight: L can identify C, with error at most ε, with prob 1-δ;
- PAC-learning algirthm;
- Sample Compexity: minimum m, s.t. m>=poly();
- Case 1: separable:
	- m >= (ln|H| + ln(1/δ))/ε, O(1/m) convergence;
	- Intuition, a bad h() with generalization error > ε, but do well on training set is at most exp(-m ε);
- Case 2: non-separable:
	- p(E^(h)-E(h)>=ε)<= exp(-2m ε^2) (Hoeffding)
	- Agnostic PAC learnable: suppose h' best in hypothesis space, then L can learn P(E(h)-E(h')<=ε)>=1-δ;
- VC-dimension:
	- Growth function: all number of possibilities π(H,m)=max{|(h(x1),...,h(xm)|h in H}
	- Dichotomy:
	- Shattering: m samples, at most 2^m possibilites. Every assignment: dichotomy, pi(H,m)=2^m, then D is shattered;
	- VC-dim: max m s.t. π(H,m)=2^m;
	- Theorem: VC(H)=d, then P(E(h)-E^(h)) has a bound;
	- VC dimentionality is **distribution independent**;
- Rademacher complexity:
	- A tighter bound (distribution dependent);
	- Given z1, ..., zm, E_σ (sup_h (σ1 h(x1)+σ2 h(x2)+...)/m), where {σ} is a random variable half +1, half -1;
- Stability:
	- Three costs: l(L,D) generalization; l^(L,D) empirical; l(L,D-i) leave-one-out;
	- β-uniform stability: |l(L,D)-l(L,D-i)| <= β;
	- ERM (empirical-risk-minimization)
	- Theorem: algorithm L ERM and β-stable, then hypothesis H learnable;

## PAC-Bayes
- Currently the best theory to explain NN generalization;
- Legacy:
	- Shawe-Taylor J, Williamson R C. A PAC analysis of a Bayesian estimator. COLT'97
	- D McAllester. Some PAC-Bayesian theorems. COLT'98
		- Concept space observes any distribution D;
		- Prior in hypothesis space H;
		- Measure of C and H space;
		- U: a subspace of H;
		- P(E(U)<=...)>=1-δ; E(U) is generalization error;
	- D McAllester. Some PAC-Bayesian theorems. Machine Learning'99
		- First paper on PAC-Bayes;
	- D McAllester. PAC-Bayesian model averaging. COLT'99
	- J Langford and J Shawe-Taylor. Pac-bayes & margins. NIPS'02
	- D McAllester. PAC-Bayesian stochastic model selection. Machine Learning'03
	- David McAllester. Simplified pac-bayesian margin bounds. 2003
	- Seeger M. Pac-bayesian generalisation error bounds for gaussian process classification. JMLR'03
	- Shawe-Taylor J, Langford J. PAC-Bayes & margins. NIPS'03
	- Langford J. Tutorial on practical prediction theory for classification. JMLR'05
	- Germain P, Lacasse A, Laviolette F, et al. PAC-Bayesian learning of linear classifiers. ICML'09
	- Catoni O. PAC-Bayesian supervised classification: the thermodynamics of statistical learning. arxiv'07	
- M Holland. PAC-Bayes under potentially heavy tails. NIPS'18

## Misc
- M Loog, T Viering, A Mey. Minimizers of the Empirical Risk and Risk Monotonicity. NIPS'18
	- Insight: introduce Risk Monotonicity
- D Foster, S Greenberg, S Kale, H Luo, M Mohri, K Sridharan. Hypothesis Set Stability and Generalization. NIPS'18
