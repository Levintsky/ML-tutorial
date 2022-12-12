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
	- Perplexity;
	- Downstream tasks;
- Benchmark
	- https://gluebenchmark.com/leaderboard/

## Legacy
- N-grams:
	- p(wt|wt-1,...,wt-n+1) = count(wt-n+1..t) / count(wt-n+1..t-1)

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
	- GPT: 12-layers; '18
	- GPT-2: 48-layers; '18
	- GPT-3: 12/24/32/40/96-layers from small to B;

## Supervision Design
- Masked:
	- ELMo, BERT, Roberta;
- Causal:
	- GPT-series;
- Together with other tasks:
	- R Collobert and J Weston. A unified architecture for natural language processing: Deep neural networks with multitask learning. ICML'08
	- R Collobert, J Weston, L Bottou, M Karlen, K Kavukcuoglu, and P Kuksa. Natural language processing (almost) from scratch. JMLR'11

## Cross-Lingual
- G Lample and A Conneau. Cross-lingual language model pretraining. 2019

## Generation
- Controlled Generation:
	- Training with conditions:
		- Yuta Kikuchi, Graham Neubig, Ryohei Sasano, Hiroya Takamura, and Manabu Okumura. Controlling output length in neural encoder-decoders. EMNLP'16
		- Jessica Ficler and Yoav Goldberg. Controlling linguistic style aspects in neural language generation. 2017
	- **SeqGAN**: L Yu, W Zhang, J Wang, and Y Yu. SeqGAN: Sequence generative adversarial nets with policy gradient. AAAI'17
	- **PPLM**: Sumanth Dathathri, Andrea Madotto, Janice Lan, Jane Hung, Eric Frank, Piero Molino, Jason Yosinski, Rosanne Liu. Plug and Play Language Models: a Simple Approach to Controlled Text Generation. ICLR'20
		- https://github.com/uber-research/pplm
		- Insight: modify history in the direction to maximize both p(x) and p(a|x), then we get p(x|a);
			<img src="/NLP/images/pplm.png" alt="drawing" width="400"/>
- Steer (with a small NN?):
	- Jiatao Gu, Graham Neubig, Kyunghyun Cho, and Victor OK Li. Learning to translate in real-time with neural machine translation. arxiv'16
	- Jiatao Gu, Kyunghyun Cho, and Victor OK Li. Trainable greedy decoding for neural machine translation. arxiv'17
	- Yun Chen, Victor OK Li, Kyunghyun Cho, and Samuel R Bowman. A stable and effective learning strategy for trainable greedy decoding. arxiv'18
	- Nishant Subramani, Sam Bowman, and Kyunghyun Cho. Can unconditional language models recover arbitrary sentences? arxiv'19
- Ari Holtzman, Jan Buys, Maxwell Forbes, Antoine Bosselut, David Golub, and Yejin Choi. Learning to write with cooperative discriminators. CoRR'18
