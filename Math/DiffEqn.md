# Differential Equation

## Basics
- ODE:
	- F(x, y1, y2, ...), each yi=yi(x) is only function of x
	- F(x, y, y', y''), high-order;
		- n-th order, n general solution? (for linear homogeneous)
	- Total differential equation (also exact differential equation, perfect differential equation)
		- Integral factor;
	- Variable separation: P(x, y) = X(x) Y(y)
	- Reparametrize;
	- Homogeneous: P(x,y)dx + Q(x,y)dy = 0
		- Bernoulli Eqn;
		- Riccati;
	- Existence and Uniqueness;
		- Picard: exist & unique;
		- Osgood condition;
		- Peano existnce;
		- Extension of solution;
	- Singular solution;
- PDE:
	- Always (mathematical methods for physics);
	- Linear 2nd-order PDE;
		- D'Ambert, Laplacian, Wave-eqn, Heat-eqn, Hermholtz Eqn, Poisson Eqn, Schrondinger, Klein-Gordon;
	- Variable separation;
	- Sphere coords: Legendre;
	- Cylinder coords: Bessel;
	- Green function: impulse response of inhomegeneous PDE;
	- Resources:
		- MIT:
			- https://youtu.be/UZiEFO3J8mE
			- https://ocw.mit.edu/courses/chemical-engineering/10-34-numerical-methods-applied-to-chemical-engineering-fall-2015/
		- Khan https://youtu.be/O3ahEHAX-KU
- SDE:
	- Basics: dx(t) = - nabla U(x(t)) dt + sigma dBt
	- First term: force (conservative from potential); second: Brownian motion;
	- Fokker-Planck equation (also Kolmogorov forward eqn, statistical mechanics):
		- Describe probability p(x, t);
		- dXt = mu(Xt, t)dt + sigma(Xt, t) dWt
		- mu() drift; D(Xt, t) = sigma()^2 / 2, diffusion coefficient;
		- partial p(x, t)/partial t = - partial mu(x,t)p(x,t) / partial x + partial^2 D(x,t)p(x,t) / partial x^2
	- Ito's Lemma, dXt = mu_t dt + sigma_t dBt; f(x, t) 2nd-order differentiable;
		- df = ()dt + ()dBt
	- Geometric Brownian motion:
		- dSt = mu St dt + sigma St dBt
		- Black-Scholes Model; pricing model for options;

## ODE
- Series Solution to ODE:
	- e.g. y'' + p(x)y' + q(x)y=r(x)
	- Let y(x)=sum an(x-x0)^n;
	- Make p(x), q(x), r(x) power series of (x-x0)^n too;
	- Take derivative, and make coefficient every order to zero;
	- Typical eg **Legendre Eqn**: (1-x2)y''-2xy'+l(l+1)y=0
- Frobenius Method:
	- Regular singular point: x0,
	- Typical eg **Bessel Eqn**:
	- Gamma Function and Properties:
- Strum-Liouville Theory: **completeness** and **orthogonal**
	- (p(x)y')' + q(x)y = - lambda w(x) y
	- Any linear 2nd-order ODE can be converted to this form, e.g. Legendre, Bessel, ...
	- Lambda: to be determined (eigen value) l1, l2, ...
	- Corresponding eigenvector: g1(x), g2(x), ...
	- Theory int_(a, b) yn ym w(x) = delta(m-n)
- Green function:
	- Solution to inhomogenous: (p(x)y')' + (q(x)+lambda w(x))y = f(x), with boundary condition;
		- Get func satisfying the same boundary condition for delta func (source);
		- Then we can add them together for multiple source;
	- y(x) = int_(a, b) (sum_n yn(z)yn(x) / (lambda-lambda_n)) f(z)dz
	- Definition: G(x, z)=sum_n yn(z)yn(x) / (lambda-lambda_n)
	- G(x)=G(x,x), solution to f(x)=delta(x)
- Perturbation theory;
	- D1(x) + eps D2(x) = 0, with small eps
	- Get solution to D1(x)=0 as y0(x);
	- Let y(x)=y0(x)+ y1(x)eps ... (Taylor series)
	- Back to eqn, solve
- Hermite Eqn:
	- y''-2x y'+ lambda y=0
	- Hermite polynomial:
		- Orthonal to each other int from -inf to +inf, with weight func exp(-x2)
	- Related Roderigus formula: H(x, n) = (-1)^n exp(x2) dn/dxn exp(-x^2)

## PDE
- Classic:
	- Laplacian: Lap(u) = 0
	- Heat-eqn, diffusion: Lap(u) = c u_t
	- Wave-eqn (vibrating string, D'alembert equation?): Lap(u) = c u_tt
	- Poisson Eqn: Lap(u) = f(x)
	- Hermholtz Eqn, Schrondinger, Klein-Gordon;
- Categories:
	- A u_xixj + B u_xi + cu + f = 0
	- A, b, c, f only function of (x1, x2,...), linear;
	- f=0: homogenious;
	- Superposition principle: addible;
	- A y'' + B y' + C = 0
		- B^2 > 4AC: Hyperbolic (Wave-eqn)
		- B^2 = 4AC: Parabolic (heat, diffusion)
		- B^2 < 4AC: Elliptic (steady temperature, field, ...)
- Variable separation:
	- u_tt - c u_xx = 0 (wave eqn)
		- u(x,t)=X(x)T(t)
		- X(x) = c sin(n pi x/l)
		- T(t) = a cos(n pi a t/l) + b sin(n pi a t/l)
		- Solve a,b,c to satisfy boundary condition;
	- Electric potential: Cylinder cone
		- u_xx + u_yy = 0
		- u(x2+y2=a2) = 0 (on cylinder)
		- Polar coord: u_r2 + 1/r u_r + 1/r2 u_phi2 = 0
		- u(r, rho) = R(r) Phi(phi)
	- Inhomegenious eqn:
		- e.g. u_tt - c u_xx = f
		- Fourier series;
	- Inhomegenious boundary condition:
	- Poisson Eqn: Lap(u) = f(x), f() is independent of x;
		- Find a specific solution, ignoring boundary condition;
		- General fo homogenious;
- Common 2nd order PDE:
	- Sphere Laplacian:
		- u = R(r)Phi(phi)Theta(theta)
		- 1/R d/dr(r2 R') = lambda
		- Phi'' = -m^2 Phi, m integer
		- lambda sin(theta)^2 + sin(theta)/Theta d/dtheta(sin(theta)Theta')=m^2
			- set x = cos(theta),
			- ((1-x^2)d2/dx2 - 2x d/dx + l(l+1)) Theta(x)=0 (Legendre)

## Theory of Differential Equations: Classical and Qualitative
- First-order:
	- Basic results;
	- First-order linear system:\
		<img src="/Math/images/ode-pde/vcf.png" alt="drawing" width="500"/>
	- Autonomous system: dx/dt=f(x)\
		<img src="/Math/images/ode-pde/potential.png" alt="drawing" width="500"/>
	- Generalized Logitstic Equation: dy/dt=(p(t)-q(t)y)y\
		<img src="/Math/images/ode-pde/logistic-1.png" alt="drawing" width="400"/>\
		<img src="/Math/images/ode-pde/logistic-2.png" alt="drawing" width="400"/>
	- Bifurcation;
- Linear system:
	- Introduction: x'=A(t)x+b(t)\
		<img src="/Math/images/ode-pde/linear-1.png" alt="drawing" width="400"/>\
		<img src="/Math/images/ode-pde/linear-2.png" alt="drawing" width="400"/>
	- Vector Equation: x'=A(t)x\
		<img src="/Math/images/ode-pde/linear-eigen-1.png" alt="drawing" width="400"/>\
		<img src="/Math/images/ode-pde/linear-eigen-2.png" alt="drawing" width="400"/>\
		<img src="/Math/images/ode-pde/linear-eigen-3.png" alt="drawing" width="400"/>\
		<img src="/Math/images/ode-pde/linear-eigen-4.png" alt="drawing" width="400"/>\
		<img src="/Math/images/ode-pde/linear-eigen-5.png" alt="drawing" width="400"/>\
		<img src="/Math/images/ode-pde/linear-eigen-6.png" alt="drawing" width="400"/>
	- Matrix Exponential:
		- Definition: Let A be an n × n constant matrix. Then we define the matrix exponential function by eAt is the solution of the IVP X'=AX, X(0)=I, where I is the n × n identity matrix.
		- **Cayley-Hamilton Theorem**: Every n × n constant matrix satisfies its characteristic equation.

## Laplace Transform
- Applicable for linear forms;