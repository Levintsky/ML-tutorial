# Information Theory

## Books
- David JC MacKay. Information theory, inference and learning algorithms. Cambridge university press, 2003.

## Basics (Kevin Murphy Chap 2.8)
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

## DVIB
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