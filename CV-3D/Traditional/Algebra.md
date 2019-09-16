# Algebra

## Linear Algebra
- SVD:
	- A Geometric Interpretation of SVD: maps unit-sphere to ellipsoid

## Skew-symmetric Matrices
<img src="/CV-3D/images/trad/skew-symmetric.png" alt="drawing" width="500"/>

- Cross Product with skew-symmetric matrix
<img src="/CV-3D/images/trad/cross-product.png" alt="drawing" width="500"/>

- Rigid body motion:
	- g: R3 to R3
	- Preserve norm and cross product
	- gt(x) = Rx + T

- Lie group: SO(3), Lie algebra so(3), infinitesimal rotation;
<img src="/CV-3D/images/trad/exp-family.png" alt="drawing" width="500"/>

- Lie algebra to Lie group: exponential
	- R = exp(w), where w is skew-symmetric
- Lie group to Lie algebra: logarithm of SO(3)
<img src="/CV-3D/images/trad/log-lie.png" alt="drawing" width="500"/>

## Group
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

## Ring
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

## Field
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
