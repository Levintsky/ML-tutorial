# Optimal Transport

## Resources
- Matthew Thorpe. Introduction to Optimal Transport. 2018
	- Def 1.1. We say that T : X → Y transports μ ∈ P(X) to ν ∈ P(Y), and we call T a transport map, if
		- ν(B) = μ(T−1(B)) for all ν-measurable sets B 搬运后测度相等;
	- Def 1.3. Monge's Optimal Transport Problem: given μ ∈ P(X) and ν ∈ P(Y), 
		- minimize M(T)= ∫X c(x, T(x)) dμ(x)
		- over μ-measurable maps T : X → Y subject to ν = T#μ.
	- A measure π ∈ P(X × Y) and think of dπ(x, y) as the amount of mass transferred from x to y
	- Def 1.4. Kantorovich's Optimal Transport Problem: given μ ∈ P(X) and ν ∈ P(Y),
		- minimize K(π)= ∫XxY c(x,y) dπ(x, y)
		- over π ∈ Π(μ, ν).
	- inf K(π) ≤ inf M(T). 可拆分搬运?
	- Existence:
		- Prop 1.5. Let μ ∈ P(X), ν ∈ P(Y) where X, Y are Polish spaces, and assume c : X × Y → [0, ∞) is lower semi-continuous. Then there exists π ∈ Π(μ, ν) that minimises K (defined in Definition 1.4) over all π ∈ Π(μ, ν).
	- Special case 1d:
		- Theorem 2.1. Let μ,ν ∈ P(R) with cumulative distributions F and G respectively. Assume c(x, y) = d(x−y) where d is convex and continuous. Let π† be the measure on R2 with cumulative distribution function H(x, y) = min{F (x), G(y)}. Then π† ∈ Π(μ, ν) and furthermore π† is optimal for Kantorovich’s optimal transport problem with cost function c. Moreover the optimal transport cost is
			- minπ K(π)= ∫0..1 d(F^−1(t)−G^−1(t)) dt.
			- Insight: 依cdf greedy搬到最近的;
	- Theorem 3.1. Kantorovich Duality. Let μ ∈ P(X), ν ∈ P(Y) where X, Y are Polish spaces. Let c: X×Y → [0,+∞)be a lower semi-continuous cost function. Define K as in Def 1.4 and J by
		- J: L1(μ) × L1(ν) → R, J(φ, ψ) = ∫X φdμ + ∫Y ψ dν.
		- Let Φc ={(φ,ψ) ∈ L1(μ)×L1(ν) : φ(x)+ψ(y) ≤ c(x,y)}
	- min K(π) = sup J(φ, ψ).