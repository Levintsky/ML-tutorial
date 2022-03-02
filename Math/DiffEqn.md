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