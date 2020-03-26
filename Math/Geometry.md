# Geometry

## Basics
- Distance:
	- d(x,y) >= 0; d(x,y) = d(y,x); d(x,z)+d(z,y) >= d(x,y);
- Norm:
	- ||x|| >= 0; ||alpha x|| = |alpha|\*||x||; ||x||+||y|| >= ||x+y||;
- Banach space: a complete normed vector space;
- Hilbert space: space with dot product
	- (x,y) = (y,x); ((ax1+bx2),y) = a(x1,y)+b(x2,y); (x, x) >= 0;
	- Could be infinite dimension (a function);
	- RKHS;

## Differential Manifold
- **Compact**:
	- A property that generalizes the notion of a subset of Euclidean space being closed (i.e., containing all its limit points) and bounded;
	- Any open cover has a finite subcover; (Heine-Borel)
- Topology structure:
	- n-dimensional Euclidean space: inner-product;
	- Continuous function on Euclidean;
	- Homeomorphism:
		- f is a bijection (one-to-one and onto);
		- f is continuous;
		- the inverse function f^{-1} is continuous (f is an open mapping).
	- Topology tau: a set of subsets of X;
		- The empty set and X itself belong to τ.
		- Any arbitrary (finite or infinite) union of members of τ still belongs to τ.
		- The intersection of any finite number of members of τ still belongs to τ.
	- Topology basis:
	- Open set; Closure; dense;
	- Continuous; Theorem: iff open set y, its pre-image is also open;
	- Hausdorff space: separated space or T2 space is a topological space where for any two distinct points there exist neighbourhoods of each which are disjoint from each other;
- Differential structure:
	- For a natural number n and some k which may be a non-negative integer or infinity, an n-dimensional **Ck differential structure** is defined using a **Ck-atlas**, which is a set of bijections called charts between a collection of subsets of M (whose union is the whole of M), and a set of open subsets of {\displaystyle \mathbb {R} ^{n}}\mathbb {R} ^{n}. **phi()** maps from U to m-dim Euclidean M;
	- Smooth function;
	- Smooth mapping f(.): M -> N; with M, N two smooth manifold;
		- Suppose phi, psi mapping to Euclid, then exist psi.f.phi^(-1) is a smooth function in Euclid, then f(.) is;
	- **Tangent vector**: v is a linear mapping from C to R satisfying Lebniz;
	- **Tangent space**:
		<img src="/Math/images/geometry/tangent-space.png" alt="drawing" width="400"/>
	- **Basis** of the tangent space at a point;
	- **Submanifold**;
	- **Poisson bracket**:
		- If we define product of two tangent vector as \[X, Y\], then Lebniz does not hold; so we define:
			<img src="/Math/images/geometry/poisson-bracket.png" alt="drawing" width="400"/>
	- Smooth tangent-vector field; coeffecient of differential operator smooth on manifold;
- Exterior derivative:
	- Good resources: https://zhuanlan.zhihu.com/p/43228423
	- Definition:\
		<img src="/Math/images/geometry/ext-derivative-1.png" alt="drawing" width="400"/>
	- Dual space V': all linear maps from V to R, where V: R^n; f: V -> R;
	- Dual basis;
	- For any u, v f(u, v)=-f(v,u)
	- Darboux Theorem;
	- Pullback of a smooth map
	- Orientability:
		- Definition: The most intuitive definitions require that M be a differentiable manifold. This means that the transition functions in the atlas of M are C1-functions. Such a function admits a **Jacobian determinant**. When the **Jacobian determinant is positive**, the transition function is said to be orientation preserving;
		- https://en.wikipedia.org/wiki/Orientability
		- Theorem: gamma(0)=gamma(1)=p, if the orientation is different for 0 and 1, it is non-orientable;
		- Example: Möbius strip, Klein bottle, sphere surface in R3;
	- Stokes Theorem:
		- General form:\
			<img src="/Math/images/geometry/stokes.png" alt="drawing" width="400"/>
		- 2D case: Green formula;
		- Ostrogradsky-Gauss formula;
		- Classical Stokes formula;
		- Proof: requires POU;
			- Case 1: cover U does not intersect boundary nabla-D. Integral = 0;
			- Case 2: cover U intersect boundary, 
- **Partition of unity**:
	- Partitions of unity are useful because they often allow one to **extend local constructions to the whole space**. They are also important in the interpolation of data, in signal processing, and the theory of spline functions.
		<img src="/Math/images/geometry/pou.png" alt="drawing" width="400"/>
- Riemann manifold:
	- Definition: (M, g) is a real, smooth manifold M equipped with an **inner product** gp on the tangent space TpM at each point p that varies smoothly from point to point in the sense that if X and Y are differentiable vector fields on M, then p ↦ gp(X|p, Y|p) is a smooth function;
	- Vector operator, differential operator;
	- Divergence and Laplace operator;
	- Hodge star operator;

## Differential Topology
- Differential Topology: http://www.jasoncantarella.com/wordpress/courses/math-4220/

## Differential Geometry
- Differential Geometry of Curves and Surfaces: http://www.jasoncantarella.com/wordpress/courses/math-4250/

## Manifold
- Grassman and Stiefel manifold: http://www.jasoncantarella.com/wordpress/courses/grassmannians/
