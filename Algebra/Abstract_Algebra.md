# Abstract Algebra

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

## Skew-symmetric Matrices
- A^T = -A
	<img src="/Algebra/images/Skew-symmetric.png" alt="drawing" width="500"/>

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
