# Language Modeling

## Benchmark
- https://gluebenchmark.com/leaderboard/

## Semi-supervised (SOA)
- Legacy:
	- R Collobert and J Weston. A unified architecture for natural language processing: Deep neural networks with multitask learning. ICML'08
	- Mikolov, T.; Karafit, M.; Burget, L.; Cernock, J.; and Khudanpur, S. 2010. Recurrent neural network based language model. INTERSPEECH 2010
	- R Collobert, J Weston, L Bottou, M Karlen, K Kavukcuoglu, and P Kuksa. Natural language processing (almost) from scratch. JMLR'11
	- Mikolov, T.; Kombrink, S.; Burget, L.; ernock, J.; and Khudanpur, S. 2011. Extensions of recurrent neural network language model. ICASSP 2011
	- Sundermeyer, M.; Schluter, R.; and Ney, H. Lstm neural networks for language modeling. 2012
- G Lample and A Conneau. Cross-lingual language model pretraining. 2019
- C Wang, M Li, A J. Smola. Language Models with Transformers. 2019
	<img src="/NLP/images/candidate-sample.png" alt="drawing" width="500"/>
	<img src="/NLP/images/coordinate-as.png" alt="drawing" width="600"/>
- NVIDIA:
	- Megatron: https://github.com/NVIDIA/Megatron-LM

## Character Level
- **BPE**: 
	- Rico Sennrich, Barry Haddow, and Alexandra Birch. Neural machine translation of rare words with subword units. 2015
	- FastBPE: https://github.com/glample/fastBPE

## Generation
- Controlled Generation:
	- **CTRL**: N Keskar, B McCann, L Varshney, C Xiong, R Socher. CTRL: A Conditional Transformer Language Model for Controllable Generation. 2019
		- Insight: **conditional Transformer**; control code as first word without special treatment;
		- https://github.com/salesforce/ctrl
		- fastBPE for subword
		- No PAD, MASK, ...
		- Tied embeddings with vocabulary size 250k
		- 48-layer transformer; 1.63B parameters
		- Sampling with temperature;
		- Control codes: style by domain; more complex; specific task; zero-shot code-mixing;
		- Trained on 256 core of TPU v3; 800k iterations with AdaGrad; batch-size=1024;
	- Finetune with RL: Daniel M. Ziegler, Nisan Stiennon, Jeffrey Wu, Tom B. Brown, Alec Radford, Dario Amodei, Paul Christiano, and Geoffrey Irving. Fine-tuning language models from human preferences. arXiv'19
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
