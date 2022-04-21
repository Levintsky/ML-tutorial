# Geometry

## Resources
- Recommended books:
	- Kuhnel, Wolfgang. Differential Geometry: Curves – Surfaces – Manifolds.
	- Spivak, Michael. A Comprehensive Introduction to Differential Geometry. Vol. 2.
	- Spivak, Michael. A Comprehensive Introduction to Differential Geometry. Vol. 4.
	- do Carmo, Manfredo Perdigañ. Differential Geometry of Curves and Surfaces.
	- Pressley, Andrew. Elementary Differential Geometry. Springer undergraduate mathematics series.
- Courses:
	- Differential Manifold: https://www.youtube.com/watch?v=maxAFbPM-JA&list=PLTXfpSaASMberGS1wkbfUxZzhDkjC9K_S&index=1
	- Differential geometry coureses: https://www.youtube.com/watch?v=NS1EhHZGPZ0&list=PLUjcZXQwHFGZjLC4FlubdFCPaOO-ywWql
- Nice intuition:
	- Su, Jianlin: https://spaces.ac.cn/archives/3963

## MIT 18.900
- Chap-1: 多边形 polygon
	- 1. Cutting and pasting polygons
	- 2. Integer polygons
		- Theo 2.1 (Pick's theorem) 整多边形面积=内点数 + 边界点数/2 -1
		- Def. integer affine transform. det(M2x2)=1
		- Def. integer affine equivalent. 
		- Def. minimal integer triangles. Area=1/2
		- Fact 2.7. Any two minimal integer triangles are integer affine equivalent.
	- 3. The shoelace formula and the winding number
		- (3b) **The shoelace formula**. Take a polygon P with n vertices, having coordinates
			- v0 = (x0,y0), v1 = (x1,y1), ...,vn−1 = (xn−1,yn−1), vn = (xn,yn) = (x0,y0) = v0.
			- area(P)= 1/2|v0×v1 +v1×v2 +···+vn−1×vn|.
			- Proof: (0, 0)连线, 所有三角形面积之和.
	- 4. The winding number (continued)
		- Def. winding numbers: number of counterclockwise rounds;
			- 从点往外发射线 跨过边顺时针-1 逆时针+1
	- 5. The free homotopy class
		- Def. Homotopy class
		- Fact 5.2. 所有文字可由自由同伦类的某曲线表示.
		- Theo 5.3. 自由同伦类与射线选择无关 移动ab点也无关(不能越过path p).
		- Prop 5.4. p的自由同伦类不形如\[\], \[B···B\], \[B'...B'\] (可去掉A), 则无法把a移动到infty而不穿过p.
		- Prop 5.5. p的自由同伦类不形如\[\], \[BA...BA\], \[A'B'...A'B'\]. 从a走到b必穿过p.
		- Prop 5.6. 多边形的自由同伦类形如: \[\], \[A\], \[A'\], \[B\], \[B'\], \[AB\]=\[BA\], \[A'B'\]=\[B'A'\].
- Chap-II: Billiards
	- 6. Introduction to billiards
		- Proposition 6.2. 多边形所有角度为180/n的整数倍, 则billiard轨迹最多有2n个不同方向.
		- Prop 6.7. 锐角三角形的内接三角形中 垂心三角形周长最短.
	- 7. phase space
		- Theorem 7.1. Inside any polygon, choose a point and a direction, in any way you want. Then, there is a billiards trajectory whose starting position and direction are arbitrarily close to the ones we picked, and which after some amount of bounces, returns to a position and direction arbitrarily close to the ones we picked.
		- def. Phase space: Jacobi of partial(s, t)/(s', t')
		- Theorem 7.5. (Liouville's theorem) In (s,t) coordinates on the phase space, the billiards map is area-preserving.
	- 8. Billiards in curved domains
		- Fact 8.3. Suppose that our billiards region is strictly convex (this means that any diameter, meaning a line segment connecting two different boundary points, goes through the interior of the region; so, no part of the boundary can be a straight line segment). Take the diameter (straight line connecting two boundary points) which is the longest possible. Then, that hits the boundary perpendicularly at both ends, and therefore gives a 2-bounce periodic trajectory.
		- (8c) Billiards in ellipses. (For the following discussion, a circle is not considered an ellipse.) Any ellipse has two focal points v1,v2. The ellipse itself can be defined as the set of points at a fixed sum of distances from the foci, (8.10) {v∈R2 : ∥v−v1∥+∥v−v2∥=S}.
- Chap-III: Loops
	- 9. Closed curves
- CHAPTER VI: Triangulations
	- 24. Delaunay triangulations
		- Def. 给定点和凸包, P三角剖分成不相交三角形T1,...,TN, s.t. 所有vi无其他点为三角形顶点.
		- Def. Delaunay. 对任何一个三角形做外接圆, 不包含其他三角形顶点. (尽量锐角?)
		- Theo 24.4. For any finite set of points as in (24.3), there is a Delaunay triangulation.
		- Def. 线性插值 f(x)p剖分, 分段线性f', 每个三角形内线性, 共享顶点取等值f'(v)=f(v).
		- Prop 24.6. 函数f(x,y) = x^2 + y^2三角剖分后线性插值f'. 剖分Delaunay iff f' convex.
	- 25. Betti number
		- Def. Planar complex. 可以有离散的点和边, 但是不能相交穿过.
		- Def. Suppose that a planar complex K consists of n0 points, n1 edges, and n2 triangles. Its **Euler characteristic** χ = χ(K) is χ=n0 −n1 +n2.
		- Def. boundary operator:
			- D1. (n0, n1), 一列对应一条边, -1, +1.
			- D2. (n1, n2), 一列队迎一个三角形, (p, q, r), pq, qr: +1; pr: -1;
		- Fact 25.4. The boundary operators satisfy D1D2 = 0 (the zero matrix).
		- Betti number: The Betti numbers b0 = b0(K), b1 = b1(K), b2 = b2(K), aredefined by
			- b0 = n0 − rank(D1),
			- b1 = n1 − rank(D1) − rank(D2),
			- b2 = n2 − rank(D2).
		- Note that the alternating sum of the Betti numbers is the Euler characteristic: b0 −b1 +b2 =n0 −n1 +n2 =χ.
		- b0, b1, b2: non-negative integers.
	- 26. Betti numbers (continued)
		- Proposition 26.2. For any planar complex K, b2(K) = 0.
		- Theorem 26.3. For a planar complex K, b1(K) is the number of bounded components of the complement R2 \ K (meaning, the total number of components of the complement minus 1, to exclude the unbounded compoment).
		- Corollary 26.4. For any planar complex,
			- χ(K) = #(components of K) − #(bounded components of R2 \ K).
		- Def. Orientable surfaces. One reason why orientability is important is that it has significant implications for the Betti numbers.
		- Proposition 27.8. The Euler characteristic of an orientable surface is always even.
		- Corollary 27.9. For an orientable surface, b1 is even.

## de Carmo, Chap-1 Curves
- 1-1 Introduction
	- 1-2 to 1-4: 参数化曲线 弧长 内积
	- 1-5: **Frenet**标架
	- 1-6: conanical form (Bouquet公式)
- 1-2 Parametrized Curves
	- Def. 参数可微曲线. 1-d到3-d可微map. α: I=(a, b) -> R^3
	- Def. norm/length, inner product.
	- If s **arc-length**, then t: **unit vector**.
- 1-3 Regular Curves; Arc length
	- Def. 正则曲线. regular. α'(t) ≠ 0 for all t.
- 1-4 Vector product;
	- Def. same orientation: matrix to change basis has positive determinant;
	- Def. (u^v)w = det(u, v, w)
	- (u^v) or uxv, cross product;
	- (u^v).(x^y)= \[(u.x v.x); (u.y v.y)\]
- 1-5 Local theory of curves
	- def. 曲率 **curvature**. α: I=(a, b) -> R^3. |α''(s)|
	- def. **tangent** t(s), 主法向量 **normal** n(s), 次法向量 **binormal** b(s)=t(s)^n(s), t(s), n(s): 密切平面 **osculating plane**.
	- Intuition: b'(s) how fast the curve pulls away from osculating plane. b'(s)=t'(s)^n(s)+t(s)^n'(s)=t(s)^n'(s)
		- b'(s)平行于n(s), b'(s)=τ(s)n(s)
	- Def. 挠率 **torsion** of α at s. τ(s)
		- τ(s) remains invariant under a change of orientation.
	- Def. **Frenet trihedron**: (t(s), n(s), b(s)), t'(s)=kn
		- t' =     κn
		- n' = -κt    - τb
		- b' =     τn
	- Prop:
		- κ = |α'^α''|/|α'|^3
		- τ = (α',α'',α''')/|α',α''|^2
	- fundamental theorem of local theory of curves: 可微k(s)>0, τ(s), 存在regular曲线α(s); 其他满足条件的曲线之间差一个刚体运动.
- 1-6 The Local Canonical Form (Bouquet公式)
	- α: I=(a, b) -> R^3, parametrized by arc length;
	- Local at s0, let s0=0, α'(0)=t, α''(0)=kn
	- α'''(0)=(κn)'=κ'n+κn'=κ'n-κ^2t-κτb (Frenet)
	- α(s) = α(0) + sα'(0) + s^2/2 α''(0) + s^3/6 α'''(0) + R (R为s的高阶无穷小)
	- α(s) = (s-k^2s^3/6)t + (s^2k/2 + s^3k'/6)n - s^3/6 kτb + R
	- 取方向 t=(1,0,0), n=(0, 1, 0), b=(0,0,1), **Local canonical form**
	- x(s) = s - κ^2 s^3/6 + Rx
	- y(s) = κs^2/2 + κ's^3/6 + Ry
	- z(s) = - κτ/6 s^3 + Rz
- 1-7 Global Properties of Plane Curves
	- Def. 闭曲线. Closed plane curve. α: I=(a, b) -> R^3, α(a)=α(b), α'(a)=α'(b), α''(a)=α''(b)
	- Def. simple: no intersection.
	- Def. interior of a simple closed curve.
	- The Isoperimetric Inequality:
		- 给定周长l, 最大面积?
		- A=-int_a_b y(t)x'(t)dt=int x(t)y'(t)dt=1/2 int(xy'-yx')dt
		- Theo 1. l^2 - 4πA ≥ 0
	- Theo of turning tangents: simple闭曲线rotation index为+/-1, 决定于方向.
	- Theo (4-vertex) 闭曲线必有至少4个极值点 k'(t)=0
	- Theo (Cauchy-Crofton)

## de Carmo, Chap-2 Regular Surfaces
- 2-1 Introduction
	- 2-2: 正则曲面;
	- 2-3: 正则曲面上可微函数;
	- 2-4: 第一基本形式, 测度(面积 弧长)
	- 2-6: 定向;
- 2-2 Regular Surfaces; Inverse Images of Regular Values;
	- Def. 每个p临域可以找到map x: U ⊂ R2 -> V ∈ R3 onto mapping. s.t.
	 	- x differentiable: x(u, v) = (x(u, v), y(u, v), z(u, v));
	 	- Def. x is a homeomorphism同胚(映射 逆映射都连续);
	 	- R2 -> R3 is one-to-one;
	 - x_u^x_v ≠ 0
	 - Prop 1. f: U -> R 可微, 则(x, y, f(x,y))是regular surface.
	 - Def. 映射F: U ⊂ Rn -> Rm, p点不是满射, critical point; image F(p)∈Rm, critical value, 其他点 regular value.
	 	- f_x=f_y=f_z=0 critical point.
	 - Prop 2. R3->R. p是regular value的原像f^-1(a)是regular surface.
- 2-3 Change of Parameters; Differential Functions on Surfaces;
	- Prop 换参数. 微分同胚. **diffeomorphic**
	- def. f: V->R可微, 若f.x复合x先从R2到V的映射在x^-1(p)可微.
	- def. x: U ⊂ R2 -> R3. **x(U)**: trace of x.
	- def. **tangent surface**. α(t) a curve in R3, then
		- x(t,v) = α(t) + vα'(t)
- 2-4 The Tangent Plane; the Differential of a Map
	- Def. Tangent plane. T_p(S) of a point p ∈ S.
	- Prop: x: U ⊂ R2 -> R3. 则dx与切向量重合.
	- Unit normal vector: N(q)=x_u^x_v / |x_u^x_v|
- 2-5 The First Fundamental Form; Area
	- def. 第一基本形式: quadratic form I_p. 定义在Tp(S). 若
		- 对称\<w1, w2\>=\<w2, w1\>
		- 正定\<w, w\> >=0
	- 令E(u0, v0)=(X_u, X_u), F=(X_u, X_v), G=(X_v, X_v)
		- Quadratic form: I_p = E(u')^2 + 2Fu'v' + G(v')^2
	- 弧长: ds^2 = E(du)^2 + 2Fdudv + G(dv)^2
	- 面积: A(R) = int |x_u ^ x_v| dudv
	- Insight: 本质上变动(du, dv)的Taylor一阶展开 α = X_udu + X_vdv, 在切平面. E F G描述展开系数.
- 2-6 Orientation of Surfaces;
	- Def. orientable. 可以被同一定向的面铺满.
	- e.g. 可定向: 球面, 
	- e.g. 不可定向: Mobius strip,
	- Prop. regular surface f(x,y,z)=a可定向. (Proof: 法向量是连续函数)
	- 可定向是整体性质 不是local
- 2-7 A Characterization of Compact Orientable Surfaces;
	- R3中可定向平面都是某可微函数在某regular value的inverse image;
- 2-8 A Geometric Definition of Area;

## de Carmo, Chap-3 The Geometry of the Gauss Map
- 3-1 Introduction
	- 3-2: 高斯映射 主曲率 主方向
	- 3-3: 高斯映射局部坐标
	- 3-4: 正则曲面存在正交参数化坐标系;
	- 3-5: 直纹曲面, 极小曲面
- 3-2 Gauss Map, Fundamental Properties;
	- x: U ⊂ R2 -> R3.
	- differentiable field of unit normal: N(q)=x_u^x_v/|x_u^x_v| q ∈ x(U)
	- def. 高斯映射 **Gauss map**. 可定向曲面到单位球面S2的映射.
	- S ⊂ R3上的curve α(t)在单位球面S2上曲线 N(t). N'(0)对应法线变化速度. dNp: how N pulls away from N(p) in the neighborhood of p.
	- Prop 1: dNp: Tp(S) -> Tp(S) of the Gauss map is a self-adjoint linear map.
		- Proof: self-adjoint, (dNp(w1),w2)=(w1,dNp(w2)) for basis {w1, w2}.
	- def. **Second fundamental form**: quadratic form IIp, defined in Tp(S) by IIp(v)=-(dNp(v),v).
		- (N(s), α'(s))=0 切向量法向量垂直
		- (N, α'')=-(N', α') 第二基本形式, 切向量二阶导在法线投影.
	- def. 法曲率. 正则曲面S上取曲线C. k为C在p点的curvature, 令cosθ=(n, N)曲线法向量和曲面法向量夹角. kn=kcosθ为**normal curvature**.
		- 法曲率取值与定向无关,随定向变号.
		- IIp(α'(0))=kn(p) 曲面切向量的第二基本形式等于曲线的法曲率.
	- Prop2 (Meusnier) 所有过p有相同切线的曲线有相同的法曲率.
	- def. **maximum normal curvature** k1, **minimum normal** curvature k2. The corresponding directions of min, max e1, e2: **principal directions**.
	- def. regular connected curve: 所有点的切线都是principal direction.
	- Prop3 (Olinde Roderigues) regular connected curve充要条件: N'(t)=λ(t)α(t) 法线变化与切线同向.
	- Def. dNp: Tp(S) -> Tp(S)可微高斯映射. dNp的行列式: **Gaussian curvature** K; negative of half of the trace of dNp: **mean curvature**.
		- K=k1k2, H=(k1+k2)/2
	- Def.
		- Elliptic: det(dNp) > 0
		- Hyperbolic: det(dNp) < 0
		- Parabolic: det(dNp) = 0, dNp≠0
		- Planar: dNp=0
	- Def. 脐点. umbilical point: k1=k2的点.
	- Prop. 所有点umbilical, 是sphere or plane.
	- Prop. 渐近方向 Asymptotic direction: a normal direction where 法曲率为零.
		- Elliptic: no such point;
	- Def. Dupin indicatrix at p: set of vectors s.t. IIp(w)=±1
		- Insight: 主方向正交basis{e1, e2}坐标x1, x2, 法向量n, 坐标x3
			- Tp(S): x3 = 0
			- 密切抛物面mp(S): x3=1/2(k1x1^2 + k2x2^2),
			- 取距离Tp(S)为1/2的平面截取S得:
			- k1 x^2 + k2 y^2 = ±1, where .
	- Def. Two non-zero vectors w1, w2 ∈ Tp(S)共轭 if
		- (dNp(w1), w2) = (w1, dNp(w2)) = 0
		- 充要条件: 若两正交basis (e1, e2), 满足dNp(e1)=-k1e1, dNp(e2)=-k2e2, θ, φ为r1 r2与e1交角, 共轭 iff k1 cosθ cosφ = -k2 sinθ sinφ
	- Insight:
		- 第二基本形式: 本质上变动(du, dv)Taylor二阶展开 α = X_udu + X_vdv + 1/2 (X_uu du^2 + 2X_uv dudv + X_vv dv^2, n)n, 二阶项在法向n上投影. e, f, g描述X_uu, X_uv, X_vv在n方向投影系数.
		- 法曲率: Tp(S)上取切向量v=x1 dX/du1 + x2 dX/du2, κ(v)=II(v, v)/I(v, v)
- 3-3 The Gauss Map in Local Coordinates
	- 曲面法向量N=x_u^x_v/|x_u^x_v|, 记p点曲线α(t)切线α'=x_u u' + x_v v'
	- Weingarten映射: 找到矩阵W=(a11, a12, a21, a22), s.t. X, Y ∈ Tp(S), I(X, WY)=II(X,Y)成立, i.e.
		- N_u = a11 x_u + a21 x_v
		- N_v = a12 x_u + a22 x_v
	- IIp(α') = -(N', α') = e(u')^2 + 2f u'v' + g(v')^2
		- e = (N, x_uu)
		- f = (N, x_uv)
		- g = (N, x_vv)
	- 第一基本形式带入 E=(x_u, x_u), F=(x_u, x_v), G=(x_v, x_v)
	- Equation of Weingarten: 第-二基本形式系数表达N_u, N_v在x_u x_v下的投影
		- a11, a21 = - (e f) (E F)^-1
		- a12, a22     (f g) (F G)
	- Weingarten映射矩阵W=(a11, a12, a21, a22)性质:
		- Gaussian curvature: K=det(aij) = det(II)/det(I) = (eg-f^2)/(EG-F^2)
		- dN(v) = -kv = -kIv for v ∈ Tp(S), then k^2 - 2Hk + K = 0
		- W的eigenvalue, eigenvector: 主方向和对应的主曲率λ=κ(X)
		- 渐近线: e(u')^2 + 2fu'v' + g(v')^2 = 0. 渐近线存在iff eg-f^2 <= 0. 椭圆曲线没有.
		- 若f=F=0, 主曲率e/E, g/G, K=eg/EG, H=1/2 (eG-gE)/EG
	- Prop. Elliptic point: 存在临域所有点在切平面同侧; hyperbolic: 异侧.
- 3-4 Vector Fields
	- Theo 1. 向量场w在开集U ⊂ R2, 存在唯一曲线α: I->U, s.t. α'(t)=w(α(t))
	- Theo 2. 同theo1. α(q, 0)=q, α_t(q,t)=w(α(q,t)), α()可微.
	- Theo (main). w1, w2两向量场在开集U上某点p线性独立, 则可建立坐标系	 坐标轴与w1(q), w2(q)平行
- 3-5 Ruled Surfaces and Minimal Surfaces
	- Def. 直纹曲面/ruled surface. 单参数曲线{α(t), w(t)}, x(t, v) = α(t) + vw(t).
	- Def. 极小曲面/Minimal surface. mean curvature H=(k1+k2)/2处处为0.

## de Carmo, Chap-4 The Intrinsic Geometry of Surfaces
- 4-1 Introduction
	- chap-2: 第一基本形式: 内蕴(intrinsic)
	- 4-2: 同构, 相同第一基本形式;
	- 4-3: Gauss formula: 高斯曲率K是可以由第一基本形式系数完全决定的函数, 内蕴;
	- 4-4: 内蕴 协变导数;
	- 4-5 Gauss-Bonnet定理;
	- 4-6: 指数映射, normal coordinates, geodesic polar coordinates;
	- 4-7: 测地线;
- 4-2 Isometries; Conformal Maps;
	- def. 微分同胚. diffeomorphism φ: S -> S'. s.t. (w1, w2)p = (dφ_p(w1), dφ_p(w2))φ(p). S, S'同构.
	- def. local isometry. 临域内同构.
	- e.g. cylinder, plane. local isometry. 局部保内积.
	- Prop. 假设存在 x: U->S, x':U->S', s.t. E=E', F=F',G=G'.则φ: x'.x^-1: x(U)->S' local isometry.
	- def. 共形映射. conformal map. diffeomorphism φ: S -> S', s.t ∀ p ∈ S, v1, v2 ∈ Tp(S), we have
		- (dφp(v1), dφp(v2)) = λ^2(p) (v1, v2)p
	- Local conformal map. 保角不保长度.
	- Theo. 任何两正则曲面都局部共形.
		- Proof: 都可以正交化(chap-3)
- 4-3 The Gauss Theorem and the Equations of Compatibility;
	- x: U ⊂ R2 -> S. each point x(U) we assign a natural trihedron (x_u, x_v, N), we study the derivatives of trihedron:
		- x_uu = Γ^1_11 x_u + Γ^2_11 x_v + L1 N
		- x_uv = Γ^1_12 x_u + Γ^2_12 x_v + L2 N
		- x_vu = Γ^1_21 x_u + Γ^2_21 x_v + L2'N
		- x_vv = Γ^1_22 x_u + Γ^2_22 x_v + L3 N
		- N_u = a11 x_u + a21 x_v
		- N_v = a12 x_u + a22 x_v
	- (a11, a12, a21, a22) Weingarten.
	- 第一基本形式系数. L1=e, L2=L2'=f, L3=g
	- Christoffel symbols;
		- Γ^1_12=Γ^1_21, Γ^2_12=Γ^2_21 (x_uv=x_vu), symmetric relative to lower indices;
		- 前4式分别与x_u, x_v内积. 带入第一基本形式EFG及其导数, 得到6等式,
		- 另x_uuv-x_uvu=0, x_vvu-x_vuv=0, N_uv-N_vu=0, 可得3等式
			- Ai x_u + B_i x_v + C_i N=0, i=1,2,3;
			- Ai, Bi, Ci是E,F,G,e,f,g及其导数的函数, 令Ai=0, Bi=0, Ci=0;
		- d(Γ^1_12)/du - d(Γ^1_12)/dv + Γ^1_12 Γ^2_11 + Γ^2_12 Γ^2_12 - Γ^2_11 Γ^2_22 - Γ^1_11Γ^2_12 = -E (eg-f^2)/(EG-F^2)=-EK
	- Theo (Theorema Egregium, Gauss) Gaussian curvature K在local isometry下不变.
	- Theo (Bonnet) E,F,G,e,f,g可微函数, s.t. E>0, G>0, Gauss-Codazzi equations, EG-F^2>0. 
		- 存在临域微分同胚x:U->x(U) ⊂ R3, I和II满足E,F,G,e,f,g.
		- U连通if x':U->x'(U) ⊂ R3是另一微分同胚, 与x差一个平移和正交旋转.
- 4-4 Parallel Transport; Geodesics;
	- def. covariant derivative.
- 4-5 Gauss-Bonnet Theorem and its Applications;
- 4-6 The Exponential Map. Geodesic Polar Coordinates;
- 4-7 Further properties of geodesics; convex neighborhoods

## de Carmo, Chap-5 Global Differential Geometry
- 5-1 Introduction
- 5-2 The Rigidity of the Sphere
- 5-3 Complete Surfaces. Theorem of Hopf-Rinow
- 5-4 First and Second Variations of Arc Length; Bonnet's Theorem;
- 5-5 Jacobi Fields and Conjugate Points
- 5-6 Covering Spaces: The Theorems of Hadamard
- 5-7 Global Theorems for Curves; The Fary-Milnor Theorem
- 5-8 Surfaces of Zero Gaussian Curvature
- 5-9 Jacobi's Theorems
- 5-10 abstract Surfaces: Further Generalizations;
- 5-11 Hilbert's Theorem

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
