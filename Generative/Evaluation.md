# Evaluation of Generative Modeling

## Evaluation
- **IS (Inception Score)**: proposed in Improved Techniques for Training GANs. NIPS'16
	- Quality: the Inception-v3 to every generated image to get the conditional label distribution p(y|x), should be low-entropy
	- Diversity: KL()
- **FID (Fréchet Inception Distance)**: proposed in M Heusel, H Ramsauer, T Unterthiner, B Nessler, G Klambauer, and S Hochreiter. GANs trained by a two time-scale update rule converge to a local nash equilibrium.
	- FID: Wasserstein metric between two multidimensional Gaussian distributions (μ1, Σ1) and (μ2, Σ2)
		- Inception V3 used to get real image (μ1, Σ1) and generated (μ2, Σ2)
	- FID := |μ1-μ2|^2 + tr(Σ1+Σ2-2(Σ1^(.5)Σ2 Σ1^(.5))^.5)

## Unclassified
- Alexander A. Alemi, Ian Fischer. GILBO: One Metric to Measure Them All. NIPS'18
- Mehdi S. M. Sajjadi, Olivier Bachem, Mario Lucic, Olivier Bousquet, Sylvain Gelly. Assessing Generative Models via Precision and Recall. NIPS'18
- L Theis, A van den Oord, and M Bethge. A note on the evaluation of generative models. In arXiv preprint arXiv:1511.01844, 2015.
- Y Wu, Y Burda, R Salakhutdinov, and R Grosse. On the quantitative analysis of decoder-based generative models. 2017.
- S Arora and Y Zhang. Do gans actually learn the distribution? an empirical study. 2017
- A Bakhtin, A Szlam, M Ranzato. GenEval: A benchmark suite for evaluating generative models, in submission to ICLR 2019
	- GenEval dataset
- David Bau, Jun-Yan Zhu, Jonas Wulff, William Peebles, Hendrik Strobelt, Bolei Zhou, Antonio Torralba. Seeing What a GAN Cannot Generate. ICCV'19
	- http://ganseeing.csail.mit.edu/
	- https://github.com/davidbau/ganseeing