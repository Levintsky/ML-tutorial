# Algebra

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
