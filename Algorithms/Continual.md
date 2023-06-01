# Continual/Lifelong Learning

## Problem Definition
- Non-stationary data (x1, y1, t1), (x2, y2, t2), ...
- Supervised:
	- X: input vector
 	- Y: class label
	- T: task (context) defines P(X,Y|T)
	- Task ID observed at training
		- observed at test: task-incremental CL
		- not observed at test: class/domain-incremental CL
	- Task ID not known at training: task-agnostic CL
	- Approaches:
		- Memory-based/replay: maintain a subset of samples;
			- Replay memory: also rehearsal
				- Papers: iCaRL, ER, SER, TEM;
			- Pseudo rehearsal: random input to previous models, use output as pseudo-sample, generative model could also be used;
				- Papers: DGR, PR, CCLUGM, LGM;
			- Contrained Optimization: constrain the gradient determined by previous task gradient;
				- GEM, A-GEM, GSS;
		- No (explicit) memory: by regularization, better privacy;
		- Architecture-based: each task uses different parameters;
- Unsupervised CL:
- CL in practice:
	- T Diethe et al. Continual Learning in Practise. Continual Learning Workshop at NeurIPS 2018.
	- V Lomonaco. Continual Learning for Production Systems: The new "Agile" in the Machine Learning Era. ContinualAI Publication, 2019.
	- D. Baylor et al. FX: A TensorFlow-Based Production-Scale Machine Learning Platform. KDD, 2017.
	- A Karpathy. Building the Software 2.0 Stack. Spark+AI Summit, 2018.
	- www.neurala.com
	- https://gantry.io
	- www.cogitai.com
- CL Tools:
	- V. Lomonaco et al. Avalanche: an End-to-End Library for Continual Learning. CLVision Workshop at CVPR 2021.
	- A. Douillard et al. Continuum: Simple management of complex continual learning scenarios. CLVision Workshop at CVPR 2021.
	- S.I. Mirzadeh et al. CL-Gym: Full-Featured PyTorch Library for Continual Learning. CLVision Workshop at CVPR 2021.
	- F. Normandin et al. Sequoia: A Software Framework to Unify Continual Learning Research. CLVision Workshop at CVPR 2021
- Impact on sustainable AI:
	- Accuracy & Robustness
	- Explainability, Transparency & Accountability
	- Bias
	- Fairness
	- Privacy & Security
	- Human, Social and Environmental Wellbeing

## Tutorials, Surveys and Summaries
- Soltoggio et al. Born to learn: the inspiration, progress, and future of evolved plastic artificial neural networks. 2017
- Z. Chen and B. Liu. Lifelong machine learning. Synthesis Lectures on Artificial Intelligence and Machine Learning, 2018
- de Lange et al. Continual learning: A comparative study on how to defy forgetting in classification tasks, 2019
- Parisi et al. Continual lifelong learning with neural networks: A review. 2019
- Hadsell et al. Embracing Change: Continual Learning in Deep Neural Networks. 2020
- Khetarpal et al. Towards Continual Reinforcement Learning: A Review and Perspectives. 2020
- Mundt et al. A wholistic view of continual learning with deep neural networks: Forgotten lessons and the bridge to active and open world learning. 2020
- Tutorial: ICML'21
	- https://sites.google.com/view/cltutorial-icml2021

## Continual Learning
- Challenge: Forgetting
	- Catastrophic Forgetting (McCloskey and Cohen, 1989)
	- R French. Catastrophic forgetting in connectionist networks. Trends in cognitive sciences, 3 (4):128–135, 1999.
	- R French and N Chater. Using noise to compute error surfaces in connectionist networks: a novel means of reducing catastrophic forgetting. NC'02
- Neural:
	- **hippocampus**: fast (one-shot) learning of episodic information, consolidated to the neocortex in sleep (or resting periods) via replay of neural activity patterns associated with the episode
	- **neocortex**: slow learning of structured knowledge; efficient representation for generalization.
- Task:
	- I Goodfellow, M Mirza, D Xiao, A Courville, and Y Bengio. An empirical investigation of catastrophic forgeting in gradient-based neural networks. ICLR'14
	- NELL: Mitchell et al. Never-Ending Language Learner. AAAI'15
		- http://rtw.ml.cmu.edu/rtw/
		- T. Mitchell et al. Never-Ending Learning. Communications of the ACM, 2018.
		- X. Chen et al. NEIL: Extracting Visual Knowledge from Web Data. ICCV, 2013.
		- Z. Chen et al. Topic modeling using topics from many domains, lifelong learning and big data. ICML, 2014.
		- P. Gupta et al. Neural topic modeling with continual lifelong learning. ICML'20
- DeepMind. The forget me not process. NIPS'16
- **VCL**: C Nguyen, Y Li, T Bui, R Turner. Variational Continual Learning. ICLR'18
- Continual Unsupervised Learning

## 1. Data Focused/Replay/...
- **Constrained Optimization**:
	- GEM: Lopez-Paz and Ranzato (2017). Gradient episodic memory for Continual Learning. NeurIPS'17
- Episodic (exact) vs Generative Replay: van de Ven et al (2020). Brain-inspired replay for continual learning with artificial neural networks
- F Zenke, B Poole, S Ganguli. Continual Learning Through Synaptic Intelligence. ICML'17
	- Synaptic Intelligence (SI)
- Meta-learning:
	- Continual Meta-Learning
		- He et al. Task agnostic continual learning via meta learning. 2019
	- Meta CL:
		- K. Javed and M. White. Meta-learning representations for continual learning. 2019.
	- Hadsell et al. Embracing Change: Continual Learning in Deep Neural Networks, 2020.
	- **MER**/Meta-experience replay: Riemer et al (2019) Learning to Learn without Forgetting By Maximizing Transfer and Minimizing Interference.
		- Transfer: gradient agrees with each other (positive inner product)
		- Interference: gradient disagrees with each other (negative inner product)
		- Learn to learn s.t. it generalizes well to other examples

## 2. Model Focused
- Assumes model parameter distribution over a prior;
- **EWC**: DeepMind. Overcoming catastrophic forgetting in neural networks. PNAS'17
	- Elastic-weight consolidation: based on a diagonal Laplace approximation;
- H Ritter, A Botev, D Barber. Online Structured Laplace Approximations For Overcoming Catastrophic Forgetting. NIPS'18
	- Extend EWC to structured Laplace;
- Hsu et al (2018). Re-evaluating continual learning scenarios: A categorization and case for strong baselines.
	- Multi-head
	- Multi-task learning with a set or subset of shared parameters
- Parameter Isolation methods:
	- Fixed Network: PackNet, PathNet, Piggyback, HAT;
	- Dynamic Architecture: PNN, Expert Gate, RCL, DAN;

## 3. Architecture based
- Lee at al (2020) A Neural Dirichlet Process Mixture Model for Task-Free Continual Learning. ICLR2020

## Continual RL
- J Mendez, S Shivkumar, E Eaton. Lifelong Inverse Reinforcement Learning. NIPS'18
- K Khetarpal, M Riemer, I Rish, D Precup. Towards Continual Reinforcement Learning: A Review and Perspectives. 2020

## Unsupervised CL
- CURL: D. Rao et al. Continual Unsupervised Representation Learning. NeurIPS 2019
	- Learn a latent graphical generative model (does not scale)
- SSL:
	- S. Zhang et Al. Self-Supervised Learning Aided Class-Incremental Lifelong Learning. CLVision Workshop Findings at CVPR, 2021.
	- J. Gallardo et Al. Self-Supervised Training Enhances Online Continual Learning. arXiv, 2021. 
- Sequential Learning:
	- Y. Cui et al. Continuous online sequence learning with an unsupervised neural network model. Neural Computation, 2016.
	- A. Cossu et Al. Continual Learning for Recurrent Neural Networks: an Empirical Evaluation. Elsevier Neural Networks, 2021.
	- B. Ehret et Al. Continual learning in Recurrent Neural Networks. ICLR 2021.
- Contrastive Learning:
	- M. Zheda et al. Supervised Contrastive Replay: Revisiting the Nearest Class Mean Classifier in Online Class-Incremental Continual Learning. CLVision Workshop at CVPR 2021.
	- C. Hyuntak et al. CO2L: Contrastive Continual Learning. arXiv, 2021.
- Hebbian-like Learning:
	- G. Parisi et al. Lifelong learning of spatiotemporal representations with dual-memory recurrent self-organization. Frontiers in neurorobotics, 2018.
	- P. Bashivan et al. Continual learning with self-organizing maps. CL Workshop at NeurIPS 2018
- Active Learning:
	- L. Pellegrini et al. Continual Learning at the Edge: Real-Time Training on Smartphone Devices. ESANN, 2021.
	- R. Camoriano et al. Incremental robot learning of new objects with fixed update time. ICRA, 2017.
- Weakly/semi-supervised learning:
	- Lomonaco V. and Maltoni D. Semi-Supervised Tuning from Temporal Coherence. ICPR 2016.
	- L. Wang et al. Ordisco: Effective and efficient usage of incremental unlabeled data for semi-supervised continual learning. CVPR 2021. 
- Randomized Network:
	- A. Cossu et al. Continual Learning with Echo State Networks. ESANN 2021. 
	- M. Wortsman et al. Supermasks in superposition. NeurIPS 2020.
