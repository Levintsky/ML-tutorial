# Algebra

## Good Resources
- http://www.cmth.ph.ic.ac.uk/people/d.vvedensky/courses.html

## Algebra and Geometry
- Set, relation, operator, structure;
	- Power set, binary relation;
		- Reflective, symmetric, transitive, Antisymmetric;
	- Order;
		- **Poset**: Partially ordered set (reflexivity, antisymmetric, transitive)
		- Equivalence relation (reflexivity, symmetric, transitive)
		- well-ordered set: Poset with minimum;
		- Mathematical induction;
	- Mapping:
		- Injection; (x1!=x2, y1!=y2)
		- Surjection; (for any y, there is a x, s.t. f(x)=y)
		- Bijection; (injection + surjection)
		- Inverse mapping;
	- Inner product, outer product;
	- Gaussian Elimination 
- Linear Space;
	- Linear subspace; linearly dependent;
	- Basis, dimension, rank;
	- Coordinate;
	- Dim(W1) + Dim(W2) = dim(W1+W2) + dim(W1 intersect W2)
	- Inner-product space:
		- Euclid space; Cauchy-Schwarz inequality;
	- Orthogonal basis
- Linear mapping;
	- Image: for all x, image is the set of y=f(x) 
	- Kernel: all pre-image of 0
	- Isomorphism of linear space;
- Matrix;
	- Identity, zero;
	- Matrix product: associative, linear, distributive;
	- Invertible, inverse;
	- Transpose;
	- Normal matrix; (equivalence) Exist PAQ=B, iif rank(A)=rank(B);
	- Coordinate transform:
		- if (b1, b2, ...)=(a1, a2, ...) A, then Y=inv(A) \* X;
- Polynomial ring:

- Determinant:
	- Linear dependent: det == 0;
	- Vandermonde
	- Cramer's rule;
		<img src="/Math/images/algebra/cramer.png" alt="drawing" width="400"/>
	- Binet-Cauchy formula;\
		<img src="/Math/images/algebra/binet-cauchy.png" alt="drawing" width="400"/>
- Linear equations and linear algebra;
	- Homogeneous systems; Ax=0;
	- nonhomogeneous systems: Ax=b;
- Eigen-value, Eigen-vector, normal form;
	- Orthogonal Matrix;
	- Same linear transformation under different basis: B=inv(P)AP
	- **Similar matrix**: B=inv(P)AP, iff A, B have the same eigen polynomial;
	- **Diagonalizable matrix**;
		- Rotation matrix is not diagonizable;
	- **Minimal polynomial**: according to Hamilton-Cayley, a nxn matrix's order is at most n;
		- If A has minimum polynomial (lambda-a)^n, then it is aI+B, where B satisfy B^n=0;
		- **Jordan normal form**;
		- Cyclic subspace; I, f, ff, ...
		- If A's minimum polynomial can be factorized to 1st order products, then it has Jordan norm form; (not working for complex eigen cases)
		- If both matrices have the same Jordan form, then they are similar;
	- **Hamilton-Cayley**:
		<img src="/Math/images/algebra/hamilton-cayley.png" alt="drawing" width="400"/>
	- Real symmetric matrix:
		- All eigenvalues are real;
		- All eigenvectors are orthogonal to each other;
	- **Quadratic form**: real symmetric A, x^TAx
	- Principal axis theorem; X^TAx = Y(Q^TAQ)Y in diagonal form;
	- Positive-definite;
		- Digonal items > 0; det > 0;
- Bilinear-function:
	- f under basis alpha is A, (alpha1,...,alpha_n)=(beta,...)P, then f under basis beta is B=P'AP
	- Matrix **congruence**: P'AP=B
	- All symmetric f can be diagonalized;
	- All antisymmetric f can be divided to [0, 1;-1, 0];
	- Witt's theorem;
- Metric linear space:
	- Unitary spaces (for complex numbers); (alpha, beta)=alpha beta\*
	- Unitary transform: A inner-product preserving, (Aa,Ab)=(a,b)
	- Hermite transform, or Hermite matrix; (Aa,b)=(a,Ab), i.e. A=A\*
	- A positive definite; x\*Ax>0;
	- **Normal matrix**: AA\*=A\*A;
	- if A is normal matrix, then A is diagonizable by inv(P)AP
	- Orthogonal space; isometric, anisometric;
		- Orthogonal transform: transform J, f(a,b)=f(Ja,Jb);
		- **Symplectic space**: antisymmetric bilinear function, e.g., f(a,b)=x1y2-x2y1
- Curve and Surface;
	- Frenet Frame:
	- First fundamental form: I;
	- Second fundamental form: II;

## Abstract Algebra
- Group;
	- **Group**:
		- A set with binary operation (G, .)
		- Closure: for a, b in G, a.b in G.
		- Associativity: (a.b).c=a.(b.c)
		- Identity: e.a=a.e
		- Inverse: for a in G, exist b, s.t. a.b=b.a=e
		- Group homomorphism:
			- G -> H: injective (G, .), (H, \*)
			- a(g.k) = a(g) \* a(k)
		- Orthogonal group: O(n)
			- (Ax, Ay) = (a, b), det(R) = +/- 1
			- Special orthognal group SO(n): det(R) = +1
			- Special Euclidean group SE(n)
	- Semigroup;
		- Associative: (a.b).c=a.(b.c)
- Ring and Field;
	- **Ring**:
		- A set R with two binary operation: +, .
		- R is abelian group under +:
			- Associative: (a+b)+c=a+(b+c)
			- Commutative: a+b=b+a
			- Additive identity: Exist 0, s.t., 0+a=a
			- Additive inverse: -a, s.t. a+(-a)=0
		- R is monoid under multiplication
			- Associative: (a.b).c=a.(b.c)
			- Identity: exist 1, s.t., a.1=1.a=a
		- Multiplication is distributive with respect to addition:
			- a ⋅ (b + c) = (a · b) + (a · c)
			- (b + c) · a = (b · a) + (c · a)
	- **Field**:
		- Associativity of addition and multiplication:
			- a + (b + c) = (a + b) + c
			- a · (b · c) = (a · b) · c.
		- Commutativity of addition and multiplication:
			- a + b = b + a
			- a · b = b · a
		- Additive and multiplicative identity:
			- there exist two different elements 0 and 1 in F such that a + 0 = a and a · 1 = a
		- Additive inverses: for every a in F, there exists an element in F, denoted −a, called the additive inverse of a, such that a + (−a) = 0.
		- Multiplicative inverses: for every a ≠ 0 in F, there exists an element in F, denoted by a−1 or 1/a, called the multiplicative inverse of a, such that a · a^(−1) = 1.
		- Distributivity of multiplication over addition:
			- a · (b + c) = (a · b) + (a · c).


## Quaternion
- https://krasjet.github.io/quaternion/quaternion.pdf
- https://github.com/Krasjet/quaternion
- Complex operation as matrix;\
	<img src="/Math/images/algebra/complex.png" alt="drawing" width="350"/>
- 3D rotation, Rodrigues' Rotation Formula:\
	<img src="/Math/images/algebra/3d-rotate-1.png" alt="drawing" width="350"/>\
	<img src="/Math/images/algebra/3d-rotate-2.png" alt="drawing" width="350"/>
- Quaternion:
	- Alyssa's notes: https://docs.google.com/document/d/1b9nHkjUYuhrQH21vDuim2odW1rHP25io-dkowuz2fHM/edit
	- ii = jj = kk = ijk = -1
	- Left product of q1:\
		<img src="/Math/images/algebra/left-prod-1.png" alt="drawing" width="350"/>\
		<img src="/Math/images/algebra/left-prod-2.png" alt="drawing" width="350"/>
	- Right product of q1:\
		<img src="/Math/images/algebra/right-prod.png" alt="drawing" width="350"/>
	- Graßmann Product:\
		<img src="/Math/images/algebra/grasmann-prod.png" alt="drawing" width="350"/>
	- Pure Quaternion:\
		<img src="/Math/images/algebra/pure-qua-1.png" alt="drawing" width="350"/>
	- Inverse: conjugate;
	- 3D rotation:\
		<img src="/Math/images/algebra/qua-prod-1.png" alt="drawing" width="400"/>\
		<img src="/Math/images/algebra/qua-prod-2.png" alt="drawing" width="400"/>\
		<img src="/Math/images/algebra/qua-prod-3.png" alt="drawing" width="400"/>\
		<img src="/Math/images/algebra/qua-prod-4.png" alt="drawing" width="400"/>
	- From Quaternion to axis, angle:\
		<img src="/Math/images/algebra/qua-prod-5.png" alt="drawing" width="400"/>\
		<img src="/Math/images/algebra/qua-prod-6.png" alt="drawing" width="400"/>
	- Bijective? No, q and -q is the same rotation; 2-1 Surjective Homomorphism;
		<img src="/Math/images/algebra/qua-exp-1.png" alt="drawing" width="400"/>\
		<img src="/Math/images/algebra/qua-exp-2.png" alt="drawing" width="400"/>
	- Interpolation: t=0, q0; t=1, q1. derive a smooth transition?
		<img src="/Math/images/algebra/slerp.png" alt="drawing" width="400"/>\




