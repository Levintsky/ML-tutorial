# Reinforcement Learning

## DeepMind
- https://deepmind.com/blog/unsupervised-learning/
- Re-imagining intelligence
	- https://deepmind.com/blog/agents-imagine-and-plan/
- https://deepmind.com/blog/reinforcement-learning-unsupervised-auxiliary-tasks/
- https://deepmind.com/research/publications/neural-predictive-belief-representations/
- **World Model**:
	- G Wayne, C Hung, D Amos, M Mirza, A Ahuja, A Grabska-Barwinska, J Rae, P Mirowski, J Z. Leibo, A Santoro, M Gemici, M Reynolds, T Harley, J Abramson, S Mohamed, D Rezende, D Saxton, A Cain, C Hillier, D Silver, K Kavukcuoglu, M Botvinick, D Hassabis, T Lillicrap. Unsupervised Predictive Memory in a Goal-Directed Agent
- **UNREAL**: M. Jaderberg et. al., Reinforcement Learning with Unsupervised Auxiliary Tasks. (2016)
	- Pixel control: maximizse change in pixel intensity
	- Reward prediction
- **ToMnet**: N C. Rabinowitz, F Perbet, H. Francis Song, C Zhang, S. M. A Eslami, M Botvinick. Machine Theory of Mind. ICML'18
	<img src = '/Weak-Unsupervised/images/tomnet.png' width = '500px'>

	- Predict 1. immediate action (policy); 2. consumed object (goal); 3. trajectory (successor representation).
	- VAE on character embedding: generate mean and variance;
	- DVIB for penalty
	<img src = '/Weak-Unsupervised/images/tomnet2.png' width = '500px'>

## Intrinsic Reward
- Curious Agent
	- Pathak et. al. Curiosity-driven Exploration by Self-supervised Prediction. ICML'17
		- https://pathak22.github.io/noreward-rl/index.html#sourceCode
		- **Prediction Error**: choose actions to maximise prediction error in observations.
	- Deepak Pathak, Dhiraj Gandhi, Abhinav Gupta. Self-Supervised Exploration via Disagreement. ICML'19
		- https://pathak22.github.io/exploration-by-disagreement/index.html#sourceCode
	- Ramanan Sekar, Oleh Rybkin, Kostas Daniilidis, Pieter Abbeel, Danijar Hafner, Deepak Pathak. Planning to Explore via Self-Supervised World Models. ICML'20
		- https://github.com/ramanans1/plan2explore
	- Wenlong Huang, Igor Mordatch, Deepak Pathak. One Policy to Control Them All: Shared Modular Policies for Agent-Agnostic Control. ICML'20
		- https://github.com/huangwl18/modular-rl/
- Baldi et. al., Bayesian Surprise Attracts Human Attention. (2005)
- Prediction Gain: Bellemare et. al. (Unifying Count-Based Exploration and Intrinsic Motivation. 2016)
- Complexity Gain: Graves et. al. Automated Curriculum learning For Neural Networks. (2017)
- Driven by Compression Progress: A Simple Principle Explains Essential Aspects of Subjective Beauty, Novelty, Surprise, Interestingness, Attention, Curiosity, Creativity, Art, Science, Music, Jokes, Schmidhuber, 2008
- Klyubin et. al. Empowerment: A Universal Agent-Centric Measure of Control (2005)
- Gregor et. al. Variational Intrinsic Control (2016)
- Wang, J.X. et al. Evolving intrinsic motivations for altruistic behavior. 2018
- Natasha Jaques, Angeliki Lazaridou, Edward Hughes, Caglar Gulcehre, Pedro A. Ortega, DJ Strouse, Joel Z. Leibo, Nando de Freitas. Social Influence as Intrinsic Motivation for Multi-Agent Deep Reinforcement Learning. ICML'19 best paper honorable mention
