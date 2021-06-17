# Explain NN

## Tutorial
- NeurIPS'20: https://explainml-tutorial.github.io/
	- Explain pre-built models in a **post-hoc** manner
		- Marco Tulio Ribeiro, Sameer Singh, Carlos Guestrin. Why Should I Trust You?: Explaining the Predictions of Any Classifier. KDD'16
		- Marco Tulio Ribeiro, Sameer Singh, Carlos Guestrin. Anchors: High-Precision Model-Agnostic Explanations. AAAI'18
		- Himabindu Lakkaraju, Ece Kamar, Rich Caruana, Jure Leskovec. Faithful and Customizable Explanations of Black Box Models. AEIS'19
	- **Local** versus **Global** Explanations
	- Approaches for Post hoc Explainability:
		- Local:
			- Feature Importance:
				- LIME: Sparse, Linear Explanations;
				- SHAP: Shapley Values as Importance;
			- Rule based:
			- Saliency Maps: visualize the gradient w.r.t. the input data;
				- Learning Important Features Through Propagating Activation Differences. 2019
				- Noise-adding Methods of Saliency Map as Series of Higher Order Partial Derivative. 2018
				- Path integral;
				- Modified Backprop: Jost Tobias Springenberg, Alexey Dosovitskiy, Thomas Brox, Martin Riedmiller. Striving for Simplicity: The All Convolutional Net. 2015
			- Prototypes/Example Based;
				- Influence Functions: Which training data points have the most influence on the test loss?
				- Cook's distance: Robust statistics for assessing the effect of a sample on regression parameters;
				- Pang Wei Koh, Percy Liang. Understanding Black-box Predictions via Influence Functions. ICML'17
			- Counterfactuals: What features need to be changed and by how much to flip a model's prediction
		- Global:
			- Collection of Local Explanations;
				- Network Dissection: Quantifying Interpretability of Deep Visual Representations;
			- Representation Based;
			- Model Distillation;
			- Summaries of Counterfactuals;

## Interpretability
- David Alvarez-Melis, Tommi S. Jaakkola. Towards Robust Interpretability with Self-Explaining Neural Networks. NIPS'18
- Wenbo Guo, Sui Huang, Yunzhe Tao, Xinyu Xing, Lin Lin. Explaining Deep Learning Models -- A Bayesian Non-parametric Approach. NIPS'18
- Liwei Wang, Lunjia Hu, Jiayuan Gu, Yue Wu, Zhiqiang Hu, Kun He, John Hopcroft. Towards Understanding Learning Representations: To What Extent Do Different Neural Networks Learn the Same Representation. NIPS'18
- Sara Hooker, Dumitru Erhan, Pieter-Jan Kindermans, Been Kim. A Benchmark for Interpretability Methods in Deep Neural Networks. NIPS'19
- Patrick Schwab, Walter Karlen. CXPlain: Causal Explanations for Model Interpretation under Uncertainty. NIPS'19

## Analysis
- Matthew Olson, Abraham Wyner, Richard Berk. Modern Neural Networks Generalize on Small Data Sets. NIPS'18
- Ann-Kathrin Dombrowski, Maximillian Alber, Christopher Anders, Marcel Ackermann, Klaus-Robert Müller, Pan Kessel. Explanations can be manipulated and geometry is to blame. NIPS'19
- Randall Balestriero, Romain Cosentino, Behnaam Aazhang, Richard Baraniuk. The Geometry of Deep Networks: Power Diagram Subdivision. NIPS'19

## Visualization
- Pei Wang, Nuno Nvasconcelos. Deliberative Explanations: visualizing network insecurities. NIPS'19
- Suraj Srinivas, François Fleuret. Full-Gradient Representation for Neural Network Visualization. NIPS'19
- Emily Reif, Ann Yuan, Martin Wattenberg, Fernanda B Viegas, Andy Coenen, Adam Pearce, Been Kim. Visualizing and Measuring the Geometry of BERT. NIPS'19

## NIPS'19
- Sara Hooker, Dumitru Erhan, Pieter-Jan Kindermans, Been Kim. A Benchmark for Interpretability Methods in Deep Neural Networks
- Wieland Brendel, Jonas Rauber, Matthias Kümmerer, Ivan Ustyuzhaninov, Matthias Bethge. Accurate, reliable and fast robustness evaluation
- Ke Li, Tianhao Zhang, Jitendra Malik. Approximate Feature Collisions in Neural Nets
- Matthew Sotoudeh, Aditya V Thakur. Computing Linear Restrictions of Neural Networks
- Patrick Schwab, Walter Karlen. CXPlain: Causal Explanations for Model Interpretation under Uncertainty
- Ann-Kathrin Dombrowski, Maximillian Alber, Christopher Anders, Marcel Ackermann, Klaus-Robert Müller, Pan Kessel. Explanations can be manipulated and geometry is to blame
- Juyeon Heo, Sunghwan Joo, Taesup Moon. Fooling Neural Network Interpretations via Adversarial Model Manipulation
- Lukas Hoyer, Mauricio Munoz, Prateek Katiyar, Anna Khoreva, Volker Fischer. Grid Saliency for Context Explanations of Semantic Segmentation
- Alessio Ansuini, Alessandro Laio, Jakob H Macke, Davide Zoccolan. Intrinsic dimension of data representations in deep neural networks
- Ari Morcos, Haonan Yu, Michela Paganini, Yuandong Tian. One ticket to win them all: generalizing lottery ticket initializations across datasets and optimizers
- Randall Balestriero, Romain Cosentino, Behnaam Aazhang, Richard Baraniuk. The Geometry of Deep Networks: Power Diagram Subdivision
- Scott Gigante, Adam S Charles, Smita Krishnaswamy, Gal Mishne. Visualizing the PHATE of Neural Networks
