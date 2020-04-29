# Geometry

## Resources
- Courses:
	- Differential Manifold: https://www.youtube.com/watch?v=maxAFbPM-JA&list=PLTXfpSaASMberGS1wkbfUxZzhDkjC9K_S&index=1
	- Differential geometry coureses: https://www.youtube.com/watch?v=NS1EhHZGPZ0&list=PLUjcZXQwHFGZjLC4FlubdFCPaOO-ywWql
- Nice intuition:
	- Su, Jianlin: https://spaces.ac.cn/archives/3963

## Basics
- Distance:
	- d(x,y) >= 0; d(x,y) = d(y,x); d(x,z)+d(z,y) >= d(x,y);
- Norm:
	- ||x|| >= 0; ||alpha x|| = |alpha|\*||x||; ||x||+||y|| >= ||x+y||;
- Banach space: a **complete** normed vector space;
- Hilbert space: a **complete** space with dot product;
	- Could be infinite dimensional;
	- (x,y) = (y,x); ((ax1+bx2),y) = a(x1,y)+b(x2,y); (x, x) >= 0;
	- Could be infinite dimension (a function);
	- RKHS;
- Classical:
	- Fundamental I, II:\
		<img src="/Math/images/geometry/classic-1.png" alt="drawing" width="350"/>
	- Curvature:\
		<img src="/Math/images/geometry/classic-2.png" alt="drawing" width="350"/>
	- Rayleigh quotient:\
		<img src="/Math/images/geometry/classic-3.png" alt="drawing" width="350"/>
	- Gaussian Curvature:\
		<img src="/Math/images/geometry/classic-4.png" alt="drawing" width="350"/>
- Modern:
	- Fundamental I, II:\
		<img src="/Math/images/geometry/modern-1.png" alt="drawing" width="350"/>
	- **Compatability** conditions: change differential order, separate tangent and normal;\
		<img src="/Math/images/geometry/modern-2.png" alt="drawing" width="350"/>
	- Riemann curvature from compatability condition I:\
		<img src="/Math/images/geometry/modern-3.png" alt="drawing" width="350"/>
	- Dof, Gaussian curvature is intrinsic:\
		<img src="/Math/images/geometry/modern-4.png" alt="drawing" width="350"/>
- Geodisic from shortest path:
	- Definition:\
		<img src="/Math/images/geometry/geo-1-1.png" alt="drawing" width="350"/>
	- Calculus of variation:\
		<img src="/Math/images/geometry/geo-1-2.png" alt="drawing" width="350"/>\
		<img src="/Math/images/geometry/geo-1-3.png" alt="drawing" width="350"/>
	- Riemann connection:\
		<img src="/Math/images/geometry/geo-1-4.png" alt="drawing" width="350"/>
	- Same result as Christoffel Symbol:\
		<img src="/Math/images/geometry/geo-1-5.png" alt="drawing" width="350"/>
- Geodisic from curvature:\
	<img src="/Math/images/geometry/geo-2-1.png" alt="drawing" width="350"/>
- Curvature and moving frame:
	- Local coordinate (u, v) with orthogonal basis (e1, e2):\
		<img src="/Math/images/geometry/moving-frame-1.png" alt="drawing" width="350"/>\
		<img src="/Math/images/geometry/moving-frame-2.png" alt="drawing" width="350"/>\
		<img src="/Math/images/geometry/moving-frame-3.png" alt="drawing" width="350"/>
	- Geodesic curvature: if it is zero, the curve is geodesic;

## Classical
- https://zhuanlan.zhihu.com/p/41583624
- https://www.zhihu.com/question/41683915

## Differential Manifold
- Topology structure:
	- n-dimensional Euclidean space: inner-product;
		- Continuous function on Euclidean;
		- **Homeomorphism**:
			- f is a bijection (one-to-one and onto);
			- f is continuous;
			- the inverse function f^{-1} is continuous (f is an open mapping).
	- Topology space:
		- **Topology**: tau: a set of subsets of X;
			- The empty set and X itself belong to τ.
			- Any arbitrary (finite or infinite) union of members of τ still belongs to τ.
			- The intersection of any finite number of members of τ still belongs to τ.
		- Topology basis:
	- Open set; Closure; dense;
	- Continuous; Theorem: iff open set y, its pre-image is also open;
	- **Quotient space**;
		- Equivalence class: a~a (reflexivity), (symmetry), (transitivity);
	- Important property:
		- Separable:
			- **Hausdorff space**: separated space or T2 space is a topological space where for any two distinct points there exist neighbourhoods of each which are disjoint from each other;
		- **Compact**:
			- A property that generalizes the notion of a subset of Euclidean space being closed (i.e., containing all its limit points) and bounded;
			- Any open cover has a finite subcover; (Heine-Borel)
		- **Connected** space;
			- Path connectedness;
- Differential structure:
	- Differential structure;\
		<img src="/Math/images/geometry/diff-structure.png" alt="drawing" width="500"/>
	- Smooth function: Hausdauff space to R;
	- **Chart**: allowable coordinate transformation; compatibility of two charts;
	- **Atlas**: set of chart;
	- **Trivial Manifold**: could be covered with one coordinate system;
	- **Partition of unity**: very useful to extend local to global;
		- Partitions of unity are useful because they often allow one to **extend local constructions to the whole space**. They are also important in the interpolation of data, in signal processing, and the theory of spline functions.\
			<img src="/Math/images/geometry/pou.png" alt="drawing" width="500"/>
	- Smooth mapping f(.): M -> N; with M, N two smooth manifolds;
		- Suppose phi, psi mapping to Euclid, then exist psi.f.phi^(-1) is a smooth function in Euclid, then f(.) is;
	- Tangent:
		- **Tangent vector**: v is a linear mapping from C to R satisfying Lebniz;
		- **Tangent space**:\
			<img src="/Math/images/geometry/tangent-space.png" alt="drawing" width="400"/>
		- **Basis** of the tangent space at a point;
		- **Pushforward**: Tangent mapping: mapping of tangent vector from M to N;
			- Tangent vector v in Tp(M), f() is a function on N, smooth mapping phi() from M to N defines pushforword phi(v) as phi(v)(f)=v(f(phi(.)));
	- **Submanifold**;
		- Immersed submanifolds: from M to N, m <= n,  full rank (rk=m);
	- Smooth tangent field:
		- Definition: define a tangent vector everywhere, the coefficient under the basis are smooth function;
		- **Poisson bracket**: also commutator;
			- If we define product of two tangent vector as \[X, Y\], then Lebniz does not hold; so we define:
				<img src="/Math/images/geometry/poisson-bracket.png" alt="drawing" width="400"/>
		- Smooth tangent-vector field; coeffecient of differential operator smooth on manifold;
	- **Integral Curve**: C(t) is called integral curve of f, if its tangent vector equals v;
		- Uniqueness;
	- **One-parameter group of diffeomorphisms**: definition;
		- 1. phi(t): M to M is diffeomorphism for any t;
		- 2. phi(t).phi(s)=phi(t+s);
	- **Tensor of type (k,l)**: a mapping from dual1 x dual2 x ... x dk x v1 x .. x vl to R;
	- type(1, 1) as a linear transformation: from dual to dual, or from v to v;
	- **Contraction**: (k,l) tensor to (k-1,l-1);
		- T(d, v), is a matrix, same trace with different basis;
	- **Metric tensor field**: Symmetric, non-degenerate type (0,2) tensor field;
		- ds^2=g(u,v)du x dv (tensor product)
	- **Contravariant**: tangent;
	- **Covariant**: dual
- Exterior derivative:
	- Good resources:
		- https://zhuanlan.zhihu.com/p/43228423
		- https://www.doubilee.com/cotspace/
	- Exterior forms:
		- Dual space V': all linear maps from V to R, where V: R^n; f: V -> R;
		- Dual basis;
		- Tensor product; multilinear map;
		- Antisymmetric: For any u, v, f(u, v)=-f(v,u)
		- Anti-symmetric operator; \[h\](x1,...,xr)=sum perm(u1,..,ur)(h(u1,..,ur)) / r!;
		- Outer product of **exterior form** definition **^**: if f r-form, g s-form, then 
			- Definition: **f ^ g** = (r+s)!/r!/s! [f, g]
			- Reflective: **f ^ g** = (-1)rs g^f
			- Associative, disruptive;
		- Basis of exterior form;
		- **Darboux Theorem**: f is a 2-form, then exists basis {e1, e2, ...}, s.t. f=e1^e2+e3^e4+...
		- **Cartan Corollary**:
		- **Pullback**: 
	- Exterior differential forms:
		- A good summary: https://www.doubilee.com/cotspace/
		- Cotangent space; cotangent vector: linear function of tangent vector\
			<img src="/Math/images/geometry/cotangent.png" alt="drawing" width="400"/>
		- Exterior derivative:\
			<img src="/Math/images/geometry/ext-derivative-1.png" alt="drawing" width="400"/>
		- **Invariant** to local coordinate choice: Jacobian as the bridge;
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
			- Case 2: cover U intersect boundary, maps to Rm+
- Riemann manifold:
	- Good summary: https://en.wikipedia.org/wiki/List_of_formulas_in_Riemannian_geometry
	- **Riemann manifold**: (M, g) is a real, smooth manifold M equipped with an **inner product** gp on the tangent space TpM at each point p that varies smoothly from point to point in the sense that if X and Y are differentiable vector fields on M, then p ↦ gp(X|p, Y|p) is a smooth function;
		- Euclid space: vector space is equivalent to tangent space;
		- Theorem: (N, h) n-dim Riemann manifold, f: M -> N immersed of dimension m, for any point p in M, let g(p)(u,v)=h(f(p))(f(u), f(v)), then g=f\*h();
		- First fundamental form:\
			<img src="/Math/images/geometry/1st-fundamental.png" alt="drawing" width="400"/>
		- **Homeomorphism** of tangent and cotangent space: for any u in T, alpha(u)(v)=< u, v >, then u to alpha(u) is a linear mapping; 
	- Vector operator, differential operator;
		- grad f = sum (i,j) g(i,j) df/dui duj
		- Gradient field is the normal of Isosurface;
		- **Covariant derivative**: a way of specifying a derivative along tangent vectors of a manifold. Alternatively, the covariant derivative is a way of introducing and working with a connection on a manifold by means of a differential operator;
			- https://zhuanlan.zhihu.com/p/116507127
		- **Christoffel symbols**;
			- Good resources: https://zhuanlan.zhihu.com/p/71568731
			- Definition:\
				<img src="/Math/images/geometry/christoffel.png" alt="drawing" width="400"/>
	- Divergence and Laplace operator;
		- Laplace == 0, harmonic function;
	- Hodge star operator;
		- In n-dim, k-form and (n-k)-form both have C(n,k) dimension;
		- In a space V with inner-product, Hodge-star operator is a linear operator of Exterior algebra (^(V)).
		- Divergence with Hodge star operator;
		- Laplace with Hodge star operator;

## Differential Geometry (General Relativity, Liang)
- Chap 3, Intrinsic geometry:
	- Differential Operator:
		- Definition: a mapping from (k,l) to (k,l+1)\
			<img src="/Math/images/geometry/diff-operator.png" alt="drawing" width="400"/>
		- Difference between two gradient: a (2, 1) type\
			<img src="/Math/images/geometry/diff-grad.png" alt="drawing" width="300"/>
			<img src="/Math/images/geometry/grad-3-1-4.png" alt="drawing" width="150"/>
			<img src="/Math/images/geometry/grad-3-1-5.png" alt="drawing" width="150"/>
		- Relation between normal differential operator:\
			<img src="/Math/images/geometry/grad-3-1-6.png" alt="drawing" width="300"/>
			<img src="/Math/images/geometry/grad-3-1-7.png" alt="drawing" width="200"/>
		- Define [u,v] without f:\
			<img src="/Math/images/geometry/grad-3-1-9.png" alt="drawing" width="150"/>
		- Covariant derivative:
	- Parallel transport:
		- Definition: gradient of the vector along the gamma(t) curve is 0\
			<img src="/Math/images/geometry/parallel-transport.png" alt="drawing" width="350"/>
		- Grad a is called **Connection**;\
			<img src="/Math/images/geometry/transport-2.png" alt="drawing" width="300"/>
		- Connection with metric, condition **inner-product preserving**:\
			<img src="/Math/images/geometry/transport-3.png" alt="drawing" width="300"/>
		- Christoffel symbol:\
			<img src="/Math/images/geometry/transport-4.png" alt="drawing" width="300"/>
		- Parallel transport makes vector differentiable:\
			<img src="/Math/images/geometry/transport-5.png" alt="drawing" width="300"/>
	- Geodisic:
		- Definition:\
			<img src="/Math/images/geometry/geodisic-1.png" alt="drawing" width="350"/>
		- Parametrization makes curve geodesic: **affine parameter**;\
			<img src="/Math/images/geometry/geodisic-2.png" alt="drawing" width="350"/>
		- Theorem: **Arc-length is an affine parameter**;
	- Riemann Curvature:
		- Torsion-free Gradient: commutative for type (0, 0), not for other type;\
			<img src="/Math/images/geometry/curv-1.png" alt="drawing" width="350"/>
		- Definition: maps from type-(0, 1) to type-(0, 2):\
			<img src="/Math/images/geometry/curv-2.png" alt="drawing" width="350"/>
			<img src="/Math/images/geometry/curv-3.png" alt="drawing" width="350"/>
			<img src="/Math/images/geometry/curv-4.png" alt="drawing" width="350"/>
		- Theorem: Riemann curvature is 0 for Euclid and Minkowski space (pseudo-Euclidean);
		- For 6 numbers, only 1 dof: **Ricci Tensor**:\
			<img src="/Math/images/geometry/curv-5.png" alt="drawing" width="350"/>
		- **Weyl Tensor**:\
			<img src="/Math/images/geometry/curv-6.png" alt="drawing" width="350"/>
		- Curvature from metric;\
			<img src="/Math/images/geometry/curv-7.png" alt="drawing" width="350"/>
	- Intrinsic v.s. extrinsic curvature;
		- Parallel transport for vector is **path-dependent** for space with curvature;

## Differential Topology
- Differential Topology: http://www.jasoncantarella.com/wordpress/courses/math-4220/

## Differential Geometry
- Differential Geometry of Curves and Surfaces: http://www.jasoncantarella.com/wordpress/courses/math-4250/

## Manifold
- Grassman and Stiefel manifold: http://www.jasoncantarella.com/wordpress/courses/grassmannians/
