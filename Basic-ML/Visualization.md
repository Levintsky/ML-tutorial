# Embedding, Dimension Reduction

## t-SNE series
- **t-SNE**: Laurens van der Maaten, Geoffrey Hinton. Visualizing Data using t-SNE, JMLR 2008
	- Original space p: Gaussian (x)
	- New space q: Student-t (y)
	- KL(P||Q) = sum p log(p/q)
	- SGD on y points to minimize

## NIPS'18 Tue Tutorial
- https://media.neurips.cc/Conferences/NIPS2018/Slides/Visualization_for_ML.pdf
	- Attention
	- Interactive
	- Deep Visualization (Jason Yosinski, 2015)
	- Deep Dream (Google)
	- RNN (The Unreasonable Effectiveness of Recurrent Neural Networks, Andrej Karpathy, 2015)
	- Linear: PCA, 
	- Non-linear: Scaling, Sammon Mapping, Isomap, ...
		- t-SNE
		- **UMAP** (Uniform Manifold Approximation and Projection, 2018)
	- Tensorflow Playground
	- GAN lab: https://poloclub.github.io/ganlab/