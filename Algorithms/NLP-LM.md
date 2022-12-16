# Language Modeling

## Basics
- Goal:
	- Statistical/probabilistic model for a sequence of words in a sentence;
	- Could be character-level;
- Approach:
	- Traditional: n-grams, p-LSI, LDA;
	- RNN;
	- Transformer: GPT, Bert, ...
	- (Self)-Supervision/loss:
		- Causal (predict next word/token/character): GPT-1,2,3;
		- Masked language modeling: BERT, ...
		- Next sentence prediction;
- Applications:
	- (Conditional) generation, completion;
	- Downstream tasks;
- Evaluation:
	- Perplexity: J(t)(θ) = − ∑yt,j × log(yˆt,j)
		- Perplexity = 2^J
	- Downstream tasks;
- Benchmark
	- https://gluebenchmark.com/leaderboard/
	- PennTreeBank
	- WikiText-2, WikiText-3

## Legacy
- Unigram: p(w1,...,wn) = ∏P(wi)
- Bigram: p(w1,...,wn) = ∏P(wi|wi-1)
- N-grams:
	- p(wt|wt-1,...,wt-n+1) = count(wt-n+1..t) / count(wt-n+1..t-1)
- Sparsity problem:
	- Smoothing;
	- Fall back;

## Backbone
- CNN (1d): 
	- R Collobert and J Weston. A unified architecture for natural language processing: Deep neural networks with multitask learning. ICML'08
	- R Collobert, J Weston, L Bottou, M Karlen, K Kavukcuoglu, and P Kuksa. Natural language processing (almost) from scratch. JMLR'11
- RNN:
	- Mikolov, T.; Karafit, M.; Burget, L.; Cernock, J.; and Khudanpur, S. 2010. Recurrent neural network based language model. INTERSPEECH'10
	- Mikolov, T.; Kombrink, S.; Burget, L.; ernock, J.; and Khudanpur, S. 2011. Extensions of recurrent neural network language model. ICASSP'11
	- Sundermeyer, M.; Schluter, R.; and Ney, H. Lstm neural networks for language modeling. 2012
	- ELMo
	- Matthew E Peters, Mark Neumann, Mohit Iyyer, Matt Gardner, Christopher Clark, Kenton Lee, and Luke Zettlemoyer. Deep contextualized word representations. NAACL'18
		- Deep ELMO;
- Transformer:
	- BERT: J. Devlin, et.al. ACL'19
		- Embedding: WorldPiece;
		- 12/24 layer (base/large)
	- Y. You. Accelerate BerT to 76 minutes. '19
	- NVIDIA: Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism. 19
		- Megatron: https://github.com/NVIDIA/Megatron-LM
	- RoBerTa: FB reproducing BERT;
	- C Wang, M Li, A J. Smola. Language Models with Transformers. 2019
		- AutoML, add LSTM in;
	- GPT: 12-layers; '18
	- GPT-2: 48-layers; '18
	- GPT-3: 12/24/32/40/96-layers from small to B;

## Supervision Design
- Masked:
	- ELMo, BERT, Roberta;
	- (Joshi & Chen et al., 2020): SpanBERT: Improving Pre-training by Representing and Predicting Spans
		- contiguous spans of words instead of 15% random;
		- Two end points of span to predict all the masked in between;
- Causal:
	- GPT-series;
- Together with other tasks:
	- R Collobert and J Weston. A unified architecture for natural language processing: Deep neural networks with multitask learning. ICML'08
	- R Collobert, J Weston, L Bottou, M Karlen, K Kavukcuoglu, and P Kuksa. Natural language processing (almost) from scratch. JMLR'11

## Inference Time Techniques
- Beam Search;
- Learning to bridge the gap of "teacher-forcing";
	- Scheduled sampling: Bengio'15
	- GOLD: offline RL with Importance-Sampling; ICLR'21
- Yun Chen, Victor OK Li, Kyunghyun Cho, and Samuel R Bowman. A stable and effective learning strategy for trainable greedy decoding. arxiv'18

## Cross-Lingual
- G Lample and A Conneau. Cross-lingual language model pretraining. NeurIPS'19
	- Embedding: all languages shared vocabulary through BPE;
	- sentence #1 (En) - sentence #2 (Fr) with masked loss;
- Nishant Subramani, Sam Bowman, and Kyunghyun Cho. Can unconditional language models recover arbitrary sentences? arxiv'19
- Ari Holtzman, Jan Buys, Maxwell Forbes, Antoine Bosselut, David Golub, and Yejin Choi. Learning to write with cooperative discriminators. CoRR'18
