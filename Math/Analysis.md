# Calculus

## Gradient, Diffentiation
- Function composition
- Fermat Theorem: x0 is a stationary point of f(x), if f'(x)=0;
- Mean value theorem: closed interval a, b, exists a c s.t. f'(c)=(f(b)-f(a))/(b-a)
- L'Hopital's Rule

## Integral
- Antiderivative: Also: primitive function, primitive integral or indefinite integral
- Integration by parts: ∫u(dv) = ∫(duv) - ∫v(du)
- Definite integral;
- Fundamental theorem of calculus (Newton-Lebniz): int_(a,b)f(t)dt=F(b)-F(a)
- Integration by substitution

## Multivariable calculus
- https://ocw.mit.edu/courses/mathematics/18-02sc-multivariable-calculus-fall-2010/index.htm
- 1. Vectors and Matrices
	- Vectors, dot product, lengths and angles, areas/volumes and determinants
	- Equation of planes: (P1, P2, P3) a plane, a new point P, det(P1P2,P1P3, P1P)=0
	- Curves: Q(t)=(x(t), y(t), z(t))
		- e.g. cycloid: (a theta-a sin(theta), a-a cos(theta))
	- Kepler's second law: constant rate of swept area; cross(r, v)=C
		- d(cross(r,v))/dt=0, a||r, acceleration or force parallel to radius;
- 2. Partial derivative;
	- Level curves, contour plots;
	- Critical point: fx=0, fy=0, (local min, max or saddle)
	- Chain rule, gradient and directional derivative;
	- Lagrange multiplier: nabla(f)=nabla(g)
		- nabla(f)=lambda nabla(g)
- 3. Double Integral:
	- Change of variable: dudv=|ux uy;vx vy|dxdy
	- Vector field, work and line integral;
	- Fundamental theory of line integral: F=nabla(f), potential, F: gradient field of f;
		- ∫F dr= f(p1)-f(p2), path independent
		- Conservative field, energy preserving;
		- F=(M, N), My=Nx iff conservative, proof: fxy=fyx
		- curl(F)=0 conservative;
		- curl(M,N)=Nx-My, measures 2x angular velocity of rotational component;
			- F=(-y, x), curl(F)=2
	- Green Theorem:
		- C: closed curve, clockwise;
		- ∮ Fdr = ∫∫ curl(F)dA
		- Proof ∮ Mdx = -∫∫My dA, cut into vertical simple regions, then sum;
			- Each small region satisfy the eqn, and addible;
		- Special case: ∮ xdy = Area(R)
		- Flux: ∮(F, n) ds = ∮ -Ndx + Mdy = ∫∫ div(F) dA
- 4. Triplet integrals and surface integrals in 3-d space;
	- Triplet integral;
	- Polar coord: x=rsin(phi)cos(theta), y=rsin(phi)sin(theta), z=rcos(phi)
		- dV = r^2 sin(phi) dr dphi dtheta
	- Flux and divergence theorem:
		- Divergence Theorem (Gauss-Green): ∯F dS = ∫∫∫ div(F) dV
		- div(F): source rate, amount of flux generated
		- Heat eqn: u_t = k Lap(u)
	- Line integral:
		- Curl in 3d: F = (X,Y,Z)
		- curl(F)=(Zy-Yz)i+(Xz-Zx)j+(Yx-Xy)k
		- F conservative, curl(F)=0
		- Stokes' Theorem: ∮ F dr= ∫∫ curl(F) n dS (C closed curve, S any surface bounded by C)
- Implicit Function Theorem;
- Application in geometry:
	- Frenet–Serret formulas;
		- T is the unit vector tangent to the curve, pointing in the direction of motion.
		- N is the **normal** unit vector, the derivative of T with respect to the arclength parameter of the curve, divided by its length.
		- Osculating plane: plane extended by T and N
		- B is the **binormal** unit vector, the cross product of T and N. B=TxN
		- Then we have **Frenet-Serret Equation**:\
			<img src="/Math/images/analysis/frenet–serret.png" alt="drawing" width="350"/>
	- Arc length; s=∫(a_b) sqrt(1+(dy/dx)^2)dx
	- Curvature: (1) The change of angle (deviation from a straight line) w.r.t. arc-length; (2) The curvature is the reciprocal of radius of curvature: k=1/R. k=|r'xr''| / |r'|^3;
	- Torsion of a curve: deviation from osculating plane; change of B (angle) w.r.t. arc-length;
	- A good summary: https://zhuanlan.zhihu.com/p/74380868
- Local maximum/minium:
	- Minimum: Gradient zero, Hessian positive-definite;
- Multiple integral;
	- Polar coordinate system: r dr dtheta;
	- Sphere coordinate system: r^2 sin(phi) dr dphi dtheta;
- Curve integral;
	- Scalar function scalar arc-length (Type I): ∫ f(x,y)ds
	- Vector function, inner product (Type II): ∫ f(x,y,z)(dx,dy,dz) = ∫ X x'(t) + Y y'(t) dt
	- Green formula: integral in a ring\
		<img src="/Math/images/analysis/green-formula.png" alt="drawing" width="350"/>
- Surface Integral:
	- Type I: surface area (x, y, z(x,y)):\
		<img src="/Math/images/analysis/surface-area.png" alt="drawing" width="400"/>
	- Type II: vector function v=Xi+Yj+Zk, inner product with surface normal;\
		<img src="/Math/images/analysis/surface-int-1.png" alt="drawing" width="400"/>\
		<img src="/Math/images/analysis/surface-int-2.png" alt="drawing" width="400"/>
	- Divergence (strength of flux), curl (strength of circulation);
	- Gauss-divergence theorem;\
		<img src="/Math/images/analysis/gauss-divergence.png" alt="drawing" width="400"/>
	- Stokes' Theorem: (Green formula is a special 2D-case)\
		<img src="/Math/images/analysis/stokes-theorem.png" alt="drawing" width="400"/>

## Field
- Vector field;
- Conservative vector field:
	- Integral result does not depend on path;
	- Equivalent to Circular integral equals zero;
	- Has potential function;
	- Conservative vector field: **curl == 0 always**; curl == 0 does not imply conservative; (sufficient only)
- Harmonic function: Divergence == 0 and curl == 0;
	- Laplace operator == 0;

## Real Analysis
- Set:
	- Cantor-Bernstein Theorem;
	- Countable, uncountable;
	- Limit point;
	- Bolzano-Weierstrass Theorem;
	- Derived set;
	- **Heine-Borel**: any open cover has a finite sub cover;
- Lebesgue Measure;
	- **Cantor set**;
	- Outer measure;
	- Cantor set has outer measure = 0;
	- **Measurable**: E in Euclidean Rn, a set T in Rn, m(T)=m(T and E)+E(T and comp(E));
	- Non-empty closure is measurable;
	- **Borel set**: formed from open sets (or, equivalently, from closed sets) through the operations of countable union, countable intersection, and relative complement.
		- Borel set is measurable; 
	- Unmeasurable;
	- Transformation: for T: Rn to Rn not-irregular linear transformation, then m(T(E))=|detT|.m(E)
- Measurable function;
	- Measurable function: measure E, for any t, set of {x, s.t.f(x)>t} is measurable, then f() is measurable function;
	- **Convergence of measures**;
	- Measurable function v.s. continuous;
- Lebesgue Integral;
	- Theorem: f(x) finite defined on [a,b], f(x) Riemann integralable iff discontinuous point on f(x) is a zero-measure set.
	- Fubini's Theorem: Relation between Multiple integral with iterated integral;
		<img src="/Math/images/analysis/fubini.png" alt="drawing" width="400"/>
- Derivative and Antiderivative;
	- Vitali cover;
	- **Lebesgue**: if f(x) monotonically increasing on [a,b], then the set of non-differentiable point set has 0-measure, and ∫f'(x)dx <= f(b) - f(a).
	- **Bounded Variation**, or BV;
	- **Absolute Continuity** implies BV;
	- **Fundamental theorem of calculus**: for absolute continous function f(x), ∫f'(x)dx=f(x)-f(a)
	- Integral by part;
	- u-substitution;
- Lp space;
	- Lp norm with p >= 1;
	- **Conjugate index**; 1/p + 1/q=1;
	- **Holder inequality**;\
		<img src="/Math/images/analysis/holder-inequality.png" alt="drawing" width="400"/>
	- Minkowski inequality;
	- L2 space;
		- Fourier series;
		- Bessel inequality;
		- Riesz-Fischer theorem;
	- Convolution:
		- Young inequality;

## Functional Analysis
- https://www.zhihu.com/question/27024743
- Metric space:
	- Contraction mapping;
	- Banach fixed point theorem;
	- Hausdauff Theorem;
	- Normed vector space;
	- Linear functional: Hom(V), a scalar, v vector;
		- f(v+w) = f(v) + f(w)
		- f(av) = a f(v)
	- Minkowski functional;
	- Brower fixed-point;
	- **Banach fixed point theorem**: uniqueness!\
		<img src="/Math/images/analysis/banach-fixed-point.png" alt="drawing" width="400"/>
	- Related to Picard theorem (Lipschitz < 1 has unique solution);
- Linear functional
	- Definition: T(ax+by)=aT(x)+bT(y);
	- Riesz–Fréchet Theorem:\
		<img src="/Math/images/analysis/reisz-frechet.png" alt="drawing" width="400"/>
	- Zorn Corollary;
	- Hahn-Banach Theorem;\
		<img src="/Math/images/analysis/hahn-banach.png" alt="drawing" width="400"/>
- Generalized function and Sobolev Space:
	- B0 space;
	- **Sobolev space**: a vector space of functions equipped with a norm that is a combination of Lp-norms of the function together with its derivatives up to a given order;
- Compact operator, Fredholm operator;
	- Fredholm theorem: used to handle eigen-functions of differential operators:\
		<img src="/Math/images/analysis/fredholm-1.png" alt="drawing" width="400"/>
		<img src="/Math/images/analysis/fredholm-2.png" alt="drawing" width="400"/>
- **Uniform boundedness principle** or **Banach–Steinhaus theorem**;
- **Open mapping theorem** or **Banach–Schauder theorem**: if a continuous linear operator between Banach spaces is surjective then it is an open map. 
- **Closed graph theorem**: If X and Y are Banach spaces, and T : X -> Y is a linear operator, then T is continuous if and only if its graph is closed in X × Y
