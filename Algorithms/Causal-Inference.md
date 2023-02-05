# Causal Inference

## Basics
- Problem setup:
	- If A -> B? (e.g. rain -> umbrella, but umbrella -/-> rain);
		- Causal or correlation;
	- Common approach: A/B test or meta-learning;
		- Effect: E[f(B)|A] - E[f(B)|not A]
- Representation:
	- Find correct DAG;
	- Approach 1: constraint-based;
		- Test conditional independence;
		- Iteratively delete edges;
	- Approach 2: score-based;
		- G = argmax s(D|G)
- Courses:
	- Stanford: https://www.youtube.com/playlist?list=PLxq_lXOUlvQAoWZEqhRqHNezS30lI49G-

## Tutorials
- B Scholkopf, D Janzing, J Peters, E Sgouritsa, K Zhang, J Mooij. On causal and anticausal learning. ICML'12
	- Test of time award, ICML'22
- Schölkopf et al. Towards causal representation learning, Proceedings of the IEEE 2021
- N Ke, S Bauer. Causality and Deep Learning: Synergies, Challenges and the Future. ICML'22 Tutorial 
	- https://sites.google.com/view/causalityandeeplearning
