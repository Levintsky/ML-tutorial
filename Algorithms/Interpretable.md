# Explain/Interpretable

## Basics
- Types of explanations:
	- Feature-based:
		- M. Ribeiro et al., "Why Should I Trust You?": Explaining the Predictions of Any Classifier, KDD, 2016.
		- S. Lundberg and S. Lee, A Unified Approach to Interpreting Model Predictions, NeurIPS, 2017.
		- M. Sundararajan, Axiomatic Attribution for Deep Networks, ICML, 2017.
	- Training-based:
		- P. Koh and P. Liang, Understanding Black-box Predictions via Influence Functions, ICML'17
	- Concept-based: (attributes?)
		- B. Kim et al., Interpretability Beyond Feature Attribution: Quantitative Testing with Concept Activation Vectors (TCAV), ICML'18
	- Surrogate models:
		- A. Alaa and M. van der Shaar, Demystifying Black-box Models with Symbolic Metamodels, NeurIPS, 2019
	- Natural language (In ICML'21 tutorial)
		- SNLI: S. Bowman et al., A large annotated corpus for learning natural language inference, EMNLP, 2015.
			- 550k train, 10k test;
		- M. Marelli et al., A SICK cure for the evaluation of compositional distributional semantic models, LREC, 2014.
		- A. Williams et al., A Broad-Coverage Challenge Corpus for Sentence Understanding through Inference, NAACL, 2018.
		- S. Gururangan et al., Annotation Artifacts in Natural Language Inference Data, NAACL, 2019.
		- A. Bosselut et al., COMET: Commonsense transformers for automatic knowledge graph construction. ACL, 2019.
		- Oana-Maria Camburu, Brendan Shillingford, Pasquale Minervini, Thomas Lukasiewicz, Phil Blunsom. Make Up Your Mind! Adversarial Generation of Inconsistent Natural Language Explanations. ACL'20
		- M. Lewis et al., BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension. ACL, 2020.
		- NILE: Kumar and Talukdar. NILE: Natural Language Inference with Faithful Natural Language Explanations. ACL'20
		- Majumder et al., Rationale-Inspired Natural Language Explanations with Commonsense. 2021
	- With vision:
		- Y. Chen et al., UNITER: Universal image-text representation learning, ECCV, 2020.
		- J. Park et al., VisualCOMET: Reasoning about the dynamic context of a still image. ECCV, 2020.
		- A. Radford et al., Language Models are Unsupervised Multitask Learners, 2019.
		- Attibutes based:
			- Attribute Prototype Network for Zero-Shot Learning; Xu, Xian, Wang, Schiele, Akata at NeurIPS 2020
		- Textual Explanations for Self-Driving Vehicles; Kim, Rohrbach, Darrell, Canny, Akata at ECCV 2018
		- Transformer: Natural Language Rationales with Full-Stack Visual Reasoning: From Pixels to Semantic Frames to Commonsense Graphs; Marasovic, Bhagavatula, Park, Bras, Smith, Choi at EMNLP 2020
		- Learning Decision Trees Recurrently Through Communication; Alaniz, Marcos, Schiele, Akata at CVPR 2021

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
- ICML'21: Natural-XAI: Explainable AI with Natural Language Explanations.
	- Audience friendly:
		- H. Kaur et al., Interpreting Interpretability: Understanding Data Scientists' Use of Interpretability Tools for Machine Learning, Proceedings of the 2020 CHI Conference on Human Factors in Computing Systems, 2020.
		- T. Miller, Explanation in Artificial Intelligence:Insights from the Social Sciences, Elsevier, 2019.
		- M. Druzdzel, Qualitative Verbal Explanations in Bayesian Belief Networks, Artificial Intelligence and Simulation of Behaviour Quarterly, Special issue on Bayesian belief networks, 1996.
	- 4 Challenges: faithfulness, zero/few-shot learning, automatic evaluation, NLE for any task;
	- Faithfulness:
		- S. Kumar and P. Talukdar, NILE: Natural Language Inference with Faithful Natural Language Explanations, ACL, 2020.
		- P. Hase et al., Leakage-Adjusted Simulatability: Can Models Generate Non-Trivial Explanations of Their Behavior in Natural Language?, ACL, 2020.
		- O. Camburu et al., Make Up Your Mind! Adversarial Generation of Inconsistent Natural Language Explanations, ACL, 2020.
	- Few shot: S. Narang et al., WT5?! Training Text-to-Text Models to Explain their Predictions, 2020
	- Automatic Eval:
		- O. Camburu et al., e-SNLI: Natural Language Inference with Natural Language Explanations, NeurIPS, 2018.
		- M. Kayser et al., e-ViL: A Dataset and Benchmark for Natural Language Explanations inVision-Language Tasks, 2021.

## Interpretability
- Why Is My Classifier Discriminatory? NIPS'18
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
