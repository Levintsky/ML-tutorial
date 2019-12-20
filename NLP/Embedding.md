# Word Embedding

## Resources
- https://lilianweng.github.io/lil-log/2017/10/15/learning-word-embedding.html#context-based-continuous-bag-of-words-cbow
- https://ruder.io/word-embeddings-softmax/

## Benchmarks
- **Skip-Gram**: T. Mikolov et al. Efficient estimation of word representations in vector space. arXiv 2013
	- Suppose that you have a sliding window of a fixed size moving along a sentence: the word in the middle is the “target” and those on its left and right within the sliding window are the context words
- Context-Based: Continuous Bag-of-Words (CBOW)
- **Glove**. J. Pennington, R. Socher, and C. Manning. Glove: Global vectors for word representation. EMNLP 2014.
- C Allen, T Hospedales. Analogies Explained: Towards Understanding Word Embeddings. ICML'19 best paper honorable mention

## Loss Functions
- Softmax (skip-gram);
- Hierarchical Softmax: Frederic Morin, Yoshua Bengio. Hierarchical Probabilistic Neural Network Language Model. AISTATS'05
- Cross Entropy;
- Noise Contrastive Estimation (NCE)
- Negative Sampling (NEG)

## Word + Character
- R. Jozefowicz et. al. Exploring the Limits of Language Modeling (2016)
	<img src = '/Weak-Unsupervised/images/limit-lm.png' width = '500px'>
- P Bojanowski and E Grave and A Joulin and T Mikolov. Enriching Word Vectors with Subword Information. TACL'17
	<img src = '/Weak-Unsupervised/images/fastText.png' width = '500px'>

## Unclassifed
- Diffusion Maps for Textual Network Embedding. NIPS'18
- Unsupervised Cross-Modal Alignment of Speech and Text Embedding Spaces. NIPS'18

## FAIR
- Matthew E Peters, Mark Neumann, Mohit Iyyer, Matt Gardner, Christopher Clark, Kenton Lee, and Luke Zettlemoyer. Deep contextualized word representations. 2018
- FastText

## Measure Distance
- Learning Deep Structured Semantic Models for Web Search using Clickthrough Data. CIKM 2013