# Reasoning

## Tasks/Dataset
- VQA:
	- Clevr: J Johnson, J Hoffman, B Hariharan, L v d Maaten, Li Fei-Fei, L Zitnick, Ross Girshick. Inferring and Executing Programs for Visual Reasoning. ICCV'17
- Basics of causal inference:
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
- Causal inference:
	- B Scholkopf, D Janzing, J Peters, E Sgouritsa, K Zhang, J Mooij. On causal and anticausal learning. ICML'12
	- Test of time award, ICML'22
	- Schölkopf et al. Towards causal representation learning, Proceedings of the IEEE 2021
	- N Ke, S Bauer. Causality and Deep Learning: Synergies, Challenges and the Future. ICML'22 Tutorial 
		- https://sites.google.com/view/causalityandeeplearning


## Neural Reasoning
- As a program:
	- NMN. J Andreas, M Rohrbach, T Darrell, D Klein. Neural Module Networks. CVPR'16
- Program synthesis:
	- **Neural-Symbolic VQA**: K Yi, J Wu, C Gan, A Torralba, P Kohli, J Tenenbaum. Neural-Symbolic VQA: Disentangling Reasoning from Vision and Language Understanding. NeurIPS'18
	- Y Liu, Z Wu, D Ritchie, W Freeman, J Tenenbaum, and J Wu. Learning to describe scenes with programs. ICLR'19
- C Liang, J Berant, Q Le, K Forbus, N Lao. Neural Symbolic Machines: Learning Semantic Parsers on Freebase with Weak Supervision. ACL'17
- C Liang. Integrating Machine Learning and Symbolic Reasoning: Learning to Generate Symbolic Representations from Weak Supervision. Thesis 2018
- C Liang, M Norouzi, J Berant, Q Le, N Lao. Memory augmented policy optimization for program synthesis and semantic parsing. NeurIPS'18

## Backbone
- CNN-RNN: NMN; Neural-Symbolic VQA;

## Interpretability
- Neural Interaction Transparency (NIT): Disentangling Learned Interactions for Improved Interpretability

## Relation
- Relational recurrent neural networks (DeepMind)
- Learning to Reason with Third Order Tensor Products (Jürgen Schmidhuber)

## Physics
- Flexible neural representation for physics prediction (Fei-Fei Li)
- End-to-End Differentiable Physics for Learning and Control (Zico Kolter)

## Graph
- Dynamic Network Model from Partial Observations (Jure Leskovec)
- Graph Convolutional Policy Network for Goal-Directed Molecular Graph Generation (Jure Leskovec)
- **Discovery of Latent 3D Keypoints via End-to-end Geometric Reasoning (Google Brain)**

## Misc
- Trieu H Trinh and Quoc V Le. A simple method for commonsense reasoning. 2018
- Nazneen Fatema Rajani, Bryan McCann, Caiming Xiong, and Richard Socher. Explain yourself! leveraging language models for commonsense reasoning. 2019

## Tue Tutorial
- Embedding Logical Queries on Knowledge Graphs
- **GLoMo: Unsupervised Learning of Transferable Relational Graphs (FAIR)**
