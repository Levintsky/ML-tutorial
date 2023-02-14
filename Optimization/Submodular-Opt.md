# Submodular Optimization

## Basics
- Problem setup: marginal gains decreasing

## Legacy
- E.L.Lawler and D.E.Wood. Branch-and-bound methods: A survey. Operations Research, 14(4):699–719, 1966
- G. Nemhauser, L. Wolsey, and M. Fisher. An analysis of approximations for maximizing submodular set functions. Mathematical Programming. 1978
	- Cardinality constrained maximization of a monotone submodular F can be performed nearoptimally via a greedy algorithm.
- **Lazy-Greedy**: M. Minoux. Accelerated greedy algorithms for maximizing submodular set functions. Optimization Techniques. 1978

## Submodular Maximization and Diversity
- J. Carbonell and J. Goldstein. The use of mmr, diversity-based reranking for reordering documents and producing summaries. SIGIR'98
- D. Kempe, J. Kleinberg, and E. Tardos. Maximizing the spread of influence through a social network. SIGKDD'03
- A. Krause, A. Singh, and C. Guestrin. Near-optimal sensor placements in gaussian processes: Theory, efficient algorithms and empirical studies. JMLR'08
- M. Streeter and D. Golovin. An online algorithm for maximizing submodular functions. NIPS'08
- H. Lin and J. Bilmes. A class of submodular functions for document summarization. ACL'11
- D. Dey, T. Liu, M. Hebert, and J. A. Bagnell. Contextual sequence prediction with application to control library optimization. RSS'12
- S. Ross, J. Zhou, Y. Yue, D. Dey, and J. A. Bagnell. Learning policies for contextual submodular prediction. ICML'13
- A. Prasad, S. Jegelka, and D. Batra. Submodular meets structured: Finding diverse subsets in exponentially-large structured item sets. NIPS'14

## Applications
- **SubmodBoxes**: Q Sun, D Batra. SubmodBoxes: Near-Optimal Search for a Set of Diverse Object Proposals. NIPS'15
	- Problem setup: select a submodular subset greedily to achieve max gain and diversity:
		- argmax F(Y) = R(Y) + λD(Y) s.t. |Y|≤M
	- Relevance by EdgeBox score;
	- Diversity:
		- Sliding window + NMS heuristics: infinite penalty for overlapping, no reward for diversity (submodular but not monotone, gain can be negative);
		- ESS: one object at a time, then suppress it and redo; monotone and submodular if r(.) is positive; Equivalent to subtracts the score contribution coming from the intersection region;
		- Proposed:
	- Solution: lazy-greedy with branch-and-bound tree;