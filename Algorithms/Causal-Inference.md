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

## Tutorials
- Bernhard Scholkopf, Dominik Janzing, Jonas Peters, Eleni Sgouritsa, Kun Zhang, Joris Mooij. On causal and anticausal learning. ICML'12
	- Test of time award, ICML'22
- Schölkopf et al. Towards causal representation learning, Proceedings of the IEEE 2021
- Nan Rosemary Ke, Stefan Bauer. Causality and Deep Learning: Synergies, Challenges and the Future. ICML'22 Tutorial 
	- https://sites.google.com/view/causalityandeeplearning

## Misc
- Causal Inference via Kernel Deviance Measures. NIPS'18
- Experimental Design for Cost-Aware Learning of Causal Graphs. NIPS'18
- Causal Inference with Noisy and Missing Covariates via Matrix Factorization. NIPS'18
- Fast Estimation of Causal Interactions using Wold Processes. NIPS'18
- Direct Estimation of Differences in Causal Graphs. NIPS'18
- Causal Inference and Mechanism Clustering of A Mixture of Additive Noise Models. NIPS'18

## NIPS'19
- Claudia Shi, David Blei, Victor Veitch. Adapting Neural Networks for the Estimation of Treatment Effects
- Dominik Janzing. Causal Regularization.
- Murat Kocaoglu, Amin Jaber, Karthikeyan Shanmugam, Elias Bareinboim. Characterization and Learning of Causal Graphs with Latent Variables from Soft Interventions.
- Kolyan Ray, Botond Szabo. Debiased Bayesian inference for average treatment effects.
- Andrew Bennett, Nathan Kallus, Tobias Schnabel. Deep Generalized Method of Moments for Instrumental Variable Analysis.
- Daniel Kumor, Bryant Chen, Elias Bareinboim. Efficient Identification in Linear Structural Causal Models with Instrumental Cutsets.
- Vasilis Syrgkanis, Victor Lei, Miruna Oprescu, Maggie Hei, Keith Battocchi, Greg Lewis. Machine Learning Estimation of Heterogeneous Treatment Effects with Instruments.
- Amin Jaber, Jiji Zhang, Elias Bareinboim. Identification of Conditional Causal Effects under Markov Equivalence.
- Jean Pouget-Abadie, Kevin Aydin, Warren Schudy, Kay Brodersen, Vahab Mirrokni. Variance Reduction in Bipartite Experiments through Correlation Clustering.
- Santtu Tikka, Antti Hyttinen, Juha Karvanen. Identifying Causal Effects via Context-specific Independence Relations.
- Robert Ness, Kaushal Paneri, Olga Vitek. Integrating Markov processes with structural causal modeling enables counterfactual inference in complex systems.
- Junzhe Zhang, Elias Bareinboim. Near-Optimal Reinforcement Learning in Dynamic Treatment Regimes.
- Andrew Bennett, Nathan Kallus. Policy Evaluation with Latent Confounders via Optimal Balance.
- Kristjan Greenewald, Dmitriy Katz, Karthikeyan Shanmugam, Sara Magliacane, Murat Kocaoglu, Enric Boix Adsera, Guy Bresler. Sample Efficient Active Learning of Causal Trees
- Atalanti Mastakouri, Bernhard Schölkopf, Dominik Janzing. Selecting causal brain features with a single conditional independence test per feature
- Biwei Huang, Kun Zhang, Pengtao Xie, Mingming Gong, Eric Xing, Clark Glymour. Specific and Shared Causal Relation Modeling and Mechanism-Based Clustering
- Amanda Gentzel, Dan Garant, David Jensen. The Case for Evaluating Causal Models Using Interventional Measures and Empirical Data
- Ruichu Cai, Feng Xie, Clark Glymour, Zhifeng Hao, Kun Zhang. Triad Constraints for Learning Causal Structure of Latent Variables
- Victor Veitch, Yixin Wang, David Blei. Using Embeddings to Correct for Unobserved Confounding in Networks
