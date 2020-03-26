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
			<img src="/Math/images/calculus/frenet-serret.png" alt="drawing" width="350"/>
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
		<img src="/Math/images/calculus/green-formula.png" alt="drawing" width="350"/>
- Surface Integral:
	- Type I: surface area (x, y, z(x,y)):\
		<img src="/Math/images/calculus/surface-area.png" alt="drawing" width="400"/>
	- Type II: vector function v=Xi+Yj+Zk, inner product with surface normal;\
		<img src="/Math/images/calculus/surface-int-1.png" alt="drawing" width="400"/>\
		<img src="/Math/images/calculus/surface-int-2.png" alt="drawing" width="400"/>
	- Divergence (strength of flux), curl (strength of circulation);
	- Gauss-divergence theorem;\
		<img src="/Math/images/calculus/gauss-divergence.png" alt="drawing" width="400"/>
	- Stokes' Theorem: (Green formula is a special 2D-case)\
		<img src="/Math/images/calculus/stokes-theorem.png" alt="drawing" width="400"/>

## Field
- Vector field;
- Conservative vector field:
	- Integral result does not depend on path;
	- Equivalent to Circular integral equals zero;
	- Has potential function;
	- Conservative vector field: **curl == 0 always**; curl == 0 does not imply conservative; (sufficient only)
- Harmonic function: Divergence == 0 and curl == 0;
	- Laplace operator == 0;