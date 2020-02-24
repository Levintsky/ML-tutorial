# Game Theory

## Courses
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

## Books
- Noam Nisan, Tim Roughgarden, Eva Tardos and Vijay V. Vazirani (Editors), Algorithmic Game Theory, Cambridge University Press, 2007. The closest to a textbook this course has.
- Tim Roughgarden, An Algorithmic Game Theory Primer (survey), TCS 2008.

## Stochastic Games
- Yoav Freund, Robert E. Schapire. Game Theory, On-line Prediction and Boosting. COLT'97
	- Von Neumann's well-known minmax theorem states that the outcome is the same in either case so that

## Imperfect information Game
- **CFR** (Counterfactual Regret Minimization)
	- A great summary (Ricson): http://modelai.gettysburg.edu/2013/cfr/
	- https://zhuanlan.zhihu.com/p/30438383
	- Zinkevich, M., Johanson, M., Bowling, M., & Piccione, C. Regret minimization in games with incomplete information, NIPS 2008
	- Lanctot, M., Waugh, K., Zinkevich, M., & Bowling, M, Monte Carlo sampling for regret minimization in extensive games, NIPS 2009
	- Johanson, M., Bard, N., Lanctot, M., Gibson, R., & Bowling, M, Efficient Nash equilibrium approximation through Monte Carlo counterfactual regret minimization, 2012
	- Johanson, M., Waugh, K., Bowling, M., & Zinkevich, M. Accelerating best response calculation in large extensive games, AAAI 2011
	- Codes: https://github.com/tansey/pycfr
	- A simple (Rock-Paper-Scissors) codes: https://hackernoon.com/artificial-intelligence-poker-and-regret-part-1-36c78d955720
	- Todd W. Neller, Marc Lanctot. An Introduction to Counterfactual Regret Minimization. 2013
- Noam Brown, Tuomas Sandholm. (CMU)
	- Safe and Nested Subgame Solving for Imperfect-Information Games, NIPS'17 best paper award
	- Libratus: The Superhuman AI for No-Limit Poker, IJCAI 2017
	- Reduced Space and Faster Convergence in Imperfect-Information Games via Pruning, ICML'17
	- N Brown, T Sandholm, and B Amos. Depth-Limited Solving for Imperfect-Information Games. NIPS'18
	- Tuomas Sandholm. Practical exact algorithm for trembling-hand equilibrium refinements in games. NIPS'18
	- N Brown, A Lerer, S Gross, T Sandholm. Deep Counterfactual Regret Minimization. AAAI'19
	- G Farina, C Kroer, N Brown, T Sandholm. Stable-Predictive Optimistic Counterfactual Regret Minimization. ICML'19
	- Superhuman AI for multiplayer poker. Science'19

## Resources
- Equlibiria Notions:
	- John Nash, Non-Cooperative Games (JSTOR), Annals of Mathematics 1951.  John Nash's Homepage
		- Math reviews on Nash's papers: An anemic review of the announcement in PNAS
		- An enthusiastic one on the full paper by David Gale.
	- R. J. Aumann, Subjectivity and correlation in randomized strategies. Journal of Mathematical Economics, 1:67-96, 1974  
- The Complexity of Computing Equilibria:
	- X. Chen, X. Deng, Settling the Complexity of 2-Player Nash-Equilibrium, Proc. of FOCS 2006
	- C. Daskalakis, P. W. Goldberg and C. H. Papadimitriou, The Complexity of Computing a Nash Equilibrium, Proc. of STOC 2006.
	- I. Gilboa and E. Zemel, Nash and Correlated Equilibria: Some Complexity Considerations, Games and Economic Behavior, 1 pp. 80-93 (1989)
	- P. W. Goldberg and C. H. Papadimitriou, Reducibility Among Equilibrium Problems, Proc. of STOC 2006.
	- Mihalis Yannakakis: Equilibria, Fixed Points, and Complexity Classes (Survey), STACS 2008.
- Graphical Games
	- M. Kearns, M. Littman, and S. Singh, Graphical Models for Game Theory, Proceedings of UAI 2001.
	- Michael Kearns, Graphical Games, in Algorithmic Game Theory.
- The price of anarchy and stability:
	- Worst-case Equilibria, by Elias Koutsoupias and Christos Papadimitriou
	- How Bad is Selfish Routing?, by Tim Roughgarden and Eva Tardos, Journal of the ACM, 49(2):236--259, 2002.
	- Tim Roughgarden, Selfish Routing and the Price of Anarchy, MIT Press. First chapter available here.
- The Braess paradox:
	- On a Paradox of Traffic Planning, English translation of the original 1968 article on the "paradox".
	- What if They Closed 42d Street and Nobody Noticed?, by Gina Kolata, December 25, 1990, New York Times.
	- The Braess paradox in mechanical, traffic, and other networks, by C. M. Penchina and L. J. Penchina, American Journal of Physics, Volume 71(5), May 2003, pp. 479--482.
	- Paradoxical behaviour of mechanical and electrical networks, by J. E. Cohen and P. Horowitz, Nature, Vol 352, pp. 699-701, 1991.
	- Braess's paradox in Wikipedia.
- Regret Minimization:
	- Avirm Blum and Yishai Mansour, Learning, Regret Minimization, and Equilibria, in Algorithmic Game Theory.
	- Dean Foster and Rakesh Vohra, Regret in the On-Line Decision Problem, Games and Economic Behavior 1999. A survey with the history of the development of the idea in different fields.
	- Robert Kleinberg, A Course on Learning, Games, and Electronic Markets, Cornell
- Social Choice- Arrow's Impossibility Theorem:
	- Kenneth Arrow, A Difficulty in the Concept of Social Welfare, The Journal of Political Economy, 1950, Pages 328-346.
	- John Geanakoplos, Three Brief Proofs of Arrow's  impossibility Theorem
	- Philip J. Reny, Arrow’s Theorem and the Gibbard-Satterthwaite Theorem: A Unified Approach, Economics Letters Volume 70, Issue 1, January 2001, Pages 99-105
	- Alan D. Taylor, The Manipulability of Voting Systems, American Mathematical Monthly, 2002.
	- Ehud Friedgut, Gil Kalai and Noam Nisan, Elections Can be Manipulated Often
- Stable Matching:
	- Gale and Shapely, College admissions and the stability of marriage, American Mathematical Monthly, 1962. (JSTOR)
	- Alvin Roth, A history of the application to matching residents and hospitals
	- Alvin Roth and Marilda Sotomayor, Two-Sided Matching: A Study in Game-Theoretic Modeling and Analysis, Cambridge University Press, 1990.
	- Dan Gusfield and Robert Irving, The Stable Marriage Problem: Structure and Algorithms, MIT Press, 1989
- Mechanism Design:
	- Introduction to Mechanism Design (for Computer Scientists), by Noam Nisan, in Algorithmic Game Theory.
	- Algorithmic Mechanism Design (or here), by Noam Nisan and Amir Ronen, in Games and Economic Behavior, Volume 35(1-2), April 2001, Pages 166--196.
	- Designing the Perfect Auction, by Hal Varian, Communications of the ACM, 51 (2008), pp. 9-11.
	- Tutorial on Optimal Mechanism Design without Prior, by Jason Hartline
- Auctions:
	- Combinatorial Auctions by Liad Blumrosen and Noam Nisan, in Algorithmic Game Theory.
	- A Course on Auction Theory, taught by Ron Lavi, Technion.
	- William Vickrey's 1961 paper on auctions: Counterspeculation, auctions, and competitive sealed tenders.
	- Noam Nisan and Ilya Segal, The communication requirements of efficient allocations and supporting pricesstar, Journal of Economic Theory Volume 129(1), July 2006, Pages 192-224.
	- D. Lehman, L. I. Oćallaghan Y. Shoham, Truth revelation in approximately efficient combinatorial auctions, J. ACM, 49(5) Pages: 577 - 602,  2002.
	- Article in Haaretz about the Bezeq Auction and interview with Moti Perry (Hebrew)
- Game Theory and Cryptography:
	- Jonathan Katz, Bridging Cryptography and Game Theory: Recent Results and Future Directions, 5th Theory of Cryptography Conference (TCC 2008).
	- Rational Cryptographic Protocols, Ecrypt Report, Revision 1.0, March 2007.
	- Yevgeniy Dodis and Tal Rabin, Cryptography and Game Theory, in Algorithmic Game Theory.
	- Joe Halpern and Rafael Pass, Game Theory with Costly Computation
- Resources
	- Game Theory Net, Many Resources on Game Theory (Lecture notes, pointers to literature).
