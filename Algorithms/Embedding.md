# Embedding, Hashing, 

## Unclassified
- Fully Understanding The Hashing Trick. NIPS'18

## Graph Embedding
- Maximilian Nickel, Douwe Kiela. Poincaré Embeddings for Learning Hierarchical Representations. NeurIPS'17
- Benjamin Paul Chamberlain, James Clough, Marc Peter Deisenroth. Neural Embeddings of Graphs in Hyperbolic Space. 2017
- https://dawn.cs.stanford.edu/2018/03/19/hyperbolics/
- Octavian-Eugen Ganea, Gary Bécigneul, Thomas Hofmann. Hyperbolic Neural Networks. NIPS'18
- https://youtu.be/MdPk3qD4Wig

## t-SNE series
- **t-SNE**: Laurens van der Maaten, Geoffrey Hinton. Visualizing Data using t-SNE, JMLR 2008
	- Original space p: Gaussian (x)
	- New space q: Student-t (y)
	- KL(P||Q) = sum p log(p/q)
	- SGD on y points to minimize