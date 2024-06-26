# Word Embedding

## Basics
- Goal:
	- Meaningful embedding (semantically)
	- king - man + woman ~ queen
- Applications:
	- Always used as initialization in LM and other tasks;
- Evaluation:
	- Perplexity
- Count-Based Vector Space Model
- Context-Based: Skip-Gram Model
- Context-Based: Continuous Bag-of-Words (CBOW)
- Loss Functions
	- Full Softmax
	- Hierarchical Softmax
	- Cross Entropy
	- Noise Contrastive Estimation (NCE)
	- Negative Sampling (NEG)
- Other Tips for Learning Word Embedding
- GloVe: Global Vectors
- Resources
	- https://lilianweng.github.io/lil-log/2017/10/15/learning-word-embedding.html#context-based-continuous-bag-of-words-cbow
	- https://ruder.io/word-embeddings-softmax/
	- Cross-language: https://ruder.io/cross-lingual-embeddings/index.html
	- Latest: https://ruder.io/word-embeddings-2017/index.html

## Legacy
- Bengio et. al. A Neural Probabilistic Language Model. JMLR'03
	- word embeddings as distributed representations of words.
- Collobert and Weston. A unified architecture for natural language processing. ICML'08
	- Look-up table (pretrained?)
	- Embedding + downstream tasks;
- Traditional distributional semantics models (DSMs):
	- PPMI (Positive Pointwise Mutual Information):
		- PMI(w, c) = log[p(w,c)/p(w)p(c)]
	- SVD: factorize the word-context co-occurence matrix;

## Context
- **Word2Vec**:
	- T Mikolov. Efficient Estimation of Word Representations in Vector Space. ICLR'13
		- Low-rank predict
	- Mikolov, Distributed Representations of Words and Phrases and their Compositionality. NIPS'13
		- Improves on the previous
- **CBOW**: Continuous Bag-of-Words
	- Predict center using surroundings;
	- Average/sum of surrounding embeddings;
- **Skip-Gram**:
	- T. Mikolov et al. Efficient estimation of word representations in vector space. arXiv'13
	- T. Mikolov et al. Distributed Representations of Words and Phrases and their Compositionality. arxiv'13
	- Problem setup: given center, predict surrounding 5;
- **Glove**. J. Pennington, R. Socher, and C. Manning. Glove: Global vectors for word representation. EMNLP'14.
	- Explicitly word co-occurence;
	- J = ∑i,j f(Xij)(wi wj† + bi + bj - logXij)^2
- C Allen, T Hospedales. Analogies Explained: Towards Understanding Word Embeddings. ICML'19 best paper honorable mention
- Character-level:
	- Ling, et al. 2015, Finding Function in Form: Compositional Character Models for Open Vocabulary Word Representation.
		- biLSTM;
	- Char-CNN: Kim, Y., Jernite, Y., Sontag, D., & Rush, A. M. Character-Aware Neural Language Models. AAAI'16
		- char-CNN -> LSTM as word embedding
	- Brain. Exploring the Limits of Language Modeling (2016)
		- Char-CNN + LSTM
- Subword:
	- https://zhuanlan.zhihu.com/p/69414965
	- Insight: 每次从词表选出两个subword组成新的subword:
	- BPE: 每次选最高频pair组成新subword, 直到词表够大 或subword频率够低;
		- Build n-grams word **segment**: BPE;
		- BPE (Byte-Pair Encoding): R Sennrich, B Haddow, and A Birch. Neural machine translation of rare words with subword units. ACL'16
		- **BPE**: Radford '19
		- FastBPE: https://github.com/glample/fastBPE
	- WordPiece: BPE的变种; 基于概率而非最高词频生成下一subword;
		- Likelihood变化: log(P(tz)/P(tx)P(ty)) 选最大的;
		- M Schuster and K Nakajima. Japanese and korean voice search. ICASSP'12
		- Google's neural machine translation system: Bridging the gap between human and machine translation. 16
			- used by BERT;
	- ULM: 类似wordPiece,
		- T Kudo, J Richardson. **SentencePiece**: A simple and language independent subword tokenizer and detokenizer for Neural Text Processing. EMNLP'18
	- **fastText**: FAIR. Enriching Word Vectors with Subword Information. TACL'17
		- n-grams within words;
- Levy, O., Goldberg, Y., & Dagan, I. Improving Distributional Similarity with Lessons Learned from Word Embeddings. TACL'15
	- Compare Glove/word2vec with traditional;

## Loss Functions
- Softmax (skip-gram);
	- p(wo|wi) = exp(vo†vi) / ∑o exp（vo†vi)
	- Limitation: when V is very large, calculating denominator requires going through all the words for every single sample is impractical;
- Hierarchical Softmax: F Morin, Y Bengio. Hierarchical Probabilistic Neural Network Language Model. AISTATS'05
	- Encode in a tree structure;
- D-softmax: W Chen, D Grangier, M Auli. Strategies for Training Large Vocabulary Neural Language Models. 2015
	- Sparse embedding matrix;
- Cross Entropy;
	- L(θ) = -logp(wo|wi)
	- ∇L(θ) = -∇z_io + E_wj~Q(w)[∇zij], Q(w) as noise distribution;
- Noise Contrastive Estimation (NCE): Gutmann and Hyvärinen, 2010
	- Given wi, **discriminate real** wo with noise w1, w2, ... ~ Q(w)
	- L(θ) = -log[p(w|wi)/p(w|wi+Nq(w'))] + ∑log[Nq(w)/p(w|wi)+Nq(w')]; (Bayes)
		- Let p(w|wi) ~ exp(vo†vi)
	- Self-Normalization: Devlin. Fast and robust neural network joint models for statistical machine translation. ACL'14
		- Regularization s.t. Z(c) = 1 then we don't need normalizer;
	- Infrequent Normalisation: J Andreas, D Klein. When and why are log-linear models self-normalizing? NACCL'15
- Negative Sampling (NEG): simplified version of NCE
	- Used in Google's word2vec;
	- Binary sigmoid classifier:
		- p(d=1|w, wi) = σ(vo†vi)
		- p(d=0|w, wi) = 1 - σ(v†vi) = σ(-v†vi)

## Common Techniques
- Soft sliding window
- Subsampling frequent words
- Learning phrases first; (Treat "New York" as one word)
	- Could be based on unigram/bigram counts;

## Cross-Modality
- Unsupervised Cross-Modal Alignment of Speech and Text Embedding Spaces. NIPS'18

## Measure Distance
- Learning Deep Structured Semantic Models for Web Search using Clickthrough Data. CIKM'13

## Analysis, Theory
- Z Yin and Y Shen. On the Dimensionality of Word Embedding. NeurIPS'18
	- Bias-variance trade-off;