# Game Theory

## Resources
- Basics:
	- Nash Equilibrium: no player can perform better by changing strategy;
- Poker Agents:
	- Knowledge-based; (if-else/manual/formula/...)
	- Simulation-based; (mcts)
	- Game theoretical;
- Courses
	- http://www.cs.umd.edu/~hajiagha/474GT15/GT15.html
	- https://www.cis.upenn.edu/~mkearns/teaching/cgt/
	- **Columbia CS364A**: Algorithmic Game Theory (Fall 2013)
		- http://timroughgarden.org/f13/f13.html
		- Nash's Theorem ('51): Every bimatrix game has a Nash equilibrium.
		- With Youtube link: https://www.youtube.com/channel/UCcH4Ga14Y4ELFKrEYM1vXCg
	- **Cornell CS-6840**
		- https://www.cs.cornell.edu/courses/cs6840/2017sp/schedule.htm
	- **Weizmann**:
		- http://www.wisdom.weizmann.ac.il/~naor/COURSE/agt-fkn.html
	- https://online.stanford.edu/courses/soe-ycs0004-game-theory-ii-advanced-applications
	- https://oyc.yale.edu/economics/econ-159
- Books
	- N Nisan, T Roughgarden, E Tardos and V Vazirani, Algorithmic Game Theory, Cambridge University Press, 2007. The closest to a textbook this course has.
	- T Roughgarden, An Algorithmic Game Theory Primer (survey), TCS 2008.

## Stochastic Games
- Y Freund, R Schapire. Game Theory, On-line Prediction and Boosting. COLT'97
	- Von Neumann's well-known minmax theorem states that the outcome is the same in either case so that

## Imperfect information Game
- CFR basics:
	- ⟨H, Z, P, p, u, I, σc⟩; σc: chance-player/dealer;
	- Strategy:
		- σp(I, a): probability of taking action a at infoset I;
		- σ(I): strategy (prob);
		- π.σ(h): prob of reaching h if every player follow σ;
		- π.pσ(h): prob of reaching h if player p follow σ;
		- π.-pσ(h): prob of reaching h if other player follow σ;
		- π.pσ(z|h)
	- Equations of prob:
		- π.σ(h) = π.pσ(h)π.-pσ(h)
		- π.σp(I,a) = π.σp(I) σ(I,a)
		- π.σ(z) = π.σ(h) π.σ(z,h)
	- Best response;
		- br.p(σ): best utility if other follow σ, p don't;
		- vbr.p(σ): the best utility;
	- ε-Nash Equilibrium;
		- ∀ p⊆P, ∃(vbr.p(σ)-v.pσ < ε) 
	- Counterfactual value:
		- vi(σ,h) = ∑.z,h⊏z π.σ,-i(h) π.σ(z,h) ui(z)
		- vi(σ,I) = ∑.z π.σ,-i(z[I]) π.σ(z[I],z) ui(z)
		- r(h, a) = vi(σ.I→a,h) - vi(σ,h)
	- Final strategy: normalized regret (regret matching);
- MCCFR: sampling instead of traversing the tree;
- **CFR** (Counterfactual Regret Minimization)
	- A great summary (Ricson): http://modelai.gettysburg.edu/2013/cfr/
	- https://zhuanlan.zhihu.com/p/30438383
	- CFR: M Zinkevich, M Johanson, M Bowling, C Piccione. Regret minimization in games with incomplete information, NIPS'08
	- MCCFR: M Lanctot, K Waugh, M Zinkevich, M Bowling. Monte Carlo sampling for regret minimization in extensive games, NIPS'09
	- Johanson, M., Waugh, K., Bowling, M., & Zinkevich, M. Accelerating best response calculation in large extensive games, AAAI'11
	- Johanson, M., Bard, N., Lanctot, M., Gibson, R., & Bowling, M, Efficient Nash equilibrium approximation through Monte Carlo counterfactual regret minimization, 2012
	- Codes: https://github.com/tansey/pycfr
	- A simple (Rock-Paper-Scissors) codes: https://hackernoon.com/artificial-intelligence-poker-and-regret-part-1-36c78d955720
	- T Neller, M Lanctot. An Introduction to Counterfactual Regret Minimization. 2013
		- Basic CFR (one round):\
			<img src="/RL/images/game-theory/cfr-1.png" alt="drawing" width="400"/>
		- Multiple round: probability of reaching infoset + self-play\
			<img src="/RL/images/game-theory/cfr-2.png" alt="drawing" width="400"/>
- Poker AIs:
	- Cepheus: O Tammelin, N Burch, M Johanson, M Bowling. 2-15
	- DeepStack;
- S Hart and A Mas-Colell. A simple adaptive procedure leading to correlated equilibrium. Econometrica'00
- Unsafe subgame solving:
	- D Billings, N Burch, A Davidson, R Holte, J Schaeffer, T Schauenberg, and D Szafron. Approximating game-theoretic optimal strategies for full-scale poker. IJCAI'03
	- A Gilpin and T Sandholm. A competitive Texas Hold'em poker player via automated abstraction and real-time equilibrium computation. AAAI'06
	- A Gilpin and T Sandholm. Better automated abstraction techniques for imperfect information games, with application to Texas Hold'em poker. AAMAS'07
	- S Ganzfried and T Sandholm. Endgame solving in large imperfect-information games. AAMAS'15
- Texas Hod'em
	- N Burch, M Johanson, and M Bowling. Solving imperfect information games using decomposition. AAAI'14
	- **CBR**: M Moravcik, M Schmid, K Ha, M Hladik, and S Gaukrodger. Refining subgames in large imperfect information games. AAAI'16
	- N Brown, T Sandholm. Safe and Nested Subgame Solving for Imperfect-Information Games, NIPS'17 best paper award
	- Libratus: The Superhuman AI for No-Limit Poker, IJCAI 2017
	- Reduced Space and Faster Convergence in Imperfect-Information Games via Pruning, ICML'17
	- N Brown, T Sandholm, and B Amos. Depth-Limited Solving for Imperfect-Information Games. NIPS'18
	- T Sandholm. Practical exact algorithm for trembling-hand equilibrium refinements in games. NIPS'18
	- N Brown, A Lerer, S Gross, T Sandholm. Deep Counterfactual Regret Minimization. AAAI'19
	- G Farina, C Kroer, N Brown, T Sandholm. Stable-Predictive Optimistic Counterfactual Regret Minimization. ICML'19
	- Pluribus: Superhuman AI for multiplayer poker. Science'19

## Regret Minimization
- A Blum and Y Mansour, Learning, Regret Minimization, and Equilibria, in Algorithmic Game Theory.
-  Foster and R Vohra, Regret in the On-Line Decision Problem, Games and Economic Behavior 1999. A survey with the history of the development of the idea in different fields.
- R Kleinberg, A Course on Learning, Games, and Electronic Markets, Cornell