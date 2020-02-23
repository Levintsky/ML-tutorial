# Evaluation of Generative Modeling

## Evaluation
- **IS (Inception Score)**: proposed in Improved Techniques for Training GANs. NIPS'16
	- Quality: the Inception-v3 to every generated image to get the conditional label distribution p(y|x), should be low-entropy
	- Diversity: KL()
- **FID (Fréchet Inception Distance)**: proposed in M Heusel, H Ramsauer, T Unterthiner, B Nessler, G Klambauer, and S Hochreiter. GANs trained by a two time-scale update rule converge to a local nash equilibrium.
	- FID: compare the statistics of two Gaussian;
	```python
	m1, s1 = compute_statistics(path, model, bsize)
	m2, s2 = compute_statistics(path, model, bsize)
	frechet_dist(m1, s1, m2, s2)
	```
	<img src = '/Generative/images/fid.png' width = '400'>

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