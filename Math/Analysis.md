# Calculus

## Gradient, Diffentiation
- Function composition
- Fermat Theorem: x0 is a stationary point of f(x), if f'(x)=0;
- Mean value theorem: closed interval [a, b], exists a c s.t. f'(c)=(f(b)-f(a))/(b-a)
- L'Hopital's Rule

## Integral
- Antiderivative: Also: primitive function, primitive integral or indefinite integral
- Integration by parts: int u(dv) = int (duv) - int v(du)
- Definite integral;
- Fundamental theorem of calculus (Newton-Lebniz): int_(a,b)f(t)dt=F(b)-F(a)
- Integration by substitution

## Multivariable calculus
- Partial derivative;
- Implicit Function Theorem;
- Application in geometry:
	- Frenet–Serret formulas;
		- T is the unit vector tangent to the curve, pointing in the direction of motion.
		- N is the **normal** unit vector, the derivative of T with respect to the arclength parameter of the curve, divided by its length.
		- Osculating plane: plane extended by T and N
		- B is the **binormal** unit vector, the cross product of T and N. B=TxN
		- Then we have **Frenet-Serret Equation**:\
			<img src="/Math/images/analysis/frenet–serret.png" alt="drawing" width="350"/>
	- Arc length; s=int(a_b) sqrt(1+(dy/dx)^2)dx
	- Curvature: (1) The change of angle (deviation from a straight line) w.r.t. arc-length; (2) The curvature is the reciprocal of radius of curvature: k=1/R. k=|r'xr''| / |r'|^3;
	- Torsion of a curve: deviation from osculating plane; change of B (angle) w.r.t. arc-length;
	- A good summary: https://zhuanlan.zhihu.com/p/74380868
- Local maximum/minium:
	- Minimum: Gradient zero, Hessian positive-definite;
- Multiple integral;
	- Polar coordinate system: r dr dtheta;
	- Sphere coordinate system: r^2 sin(phi) dr dphi dtheta;
- Curve integral;
	- Scalar function scalar arc-length (Type I): int f(x,y)ds
	- Vector function, inner product (Type II): int f(x,y,z)(dx,dy,dz) = int X x'(t) + Y y'(t) dt
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
	- **Lebesgue**: if f(x) monotonically increasing on [a,b], then the set of non-differentiable point set has 0-measure, and int f'(x)dx <= f(b) - f(a).
	- **Bounded Variation**, or BV;
	- **Absolute Continuity** implies BV;
	- **Fundamental theorem of calculus**: for absolute continous function f(x), int f'(x)dx=f(x)-f(a)
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
