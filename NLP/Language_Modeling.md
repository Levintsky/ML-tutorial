# Language Modeling

## Benchmark
- https://gluebenchmark.com/leaderboard/

## Semi-supervised (SOA)
- Google NLP:
	- **GMNT**: Y. Wu, M. Schuster, Z. Chen, Q.V. Le, M. Norouzi, et al. Google’s Neural Machine Translation System: Bridging the Gap between Human and Machine Translation. 2016
		<img src="/NLP/images/gmnt.png" alt="drawing" width="500"/>

		- WordPiece for Korean, Japanese
		<img src="/NLP/images/gmnt2.png" alt="drawing" width="500"/>

	- **BERT**: Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova. BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding. ACL'19
		<img src = '/Weak-Unsupervised/images/bert.png' width = '600px'>

		- **Bidirectional Transformer** as model (L=12 for Base, L=24 for Large);
		- **Embedding**: sum of following three;
			- **WorldPiece** (Wu et al 2016): 30,000 tokens;
			- Learned positional embedding;
			- Segment embedding; (same sentence share same emb?)
		- Pretrain tasks:
			- Masked LM (15%): in the 15%, 10% replaced with other words, 10% unchanged, 80% [MASK]. So the model has to attend to every word.
			- Given two sentences concatenated together. Predict if B is next to A (50%). Achieve 97-98% accuracy;
		- Pretrain:
			- BooksCorpus (800M) + Wiki (2,500M), 1 Billion only sentence level;
			- BERT-BASE: 4 Cloud TPUs (16 chips), 4 days;
			- BERT-LARGE: 4 Cloud TPUs (64 chips), 4 days;
		- Fine-tunning:
			- First token [CLS], finally used as classifier after FC and softmax;
	- Parameter-Efficient Transfer Learning for NLP, 2019
		- Adapter module
	- Y You, J Li, J Hseu, X Song, J Demmel, C Hsieh. Reducing BERT Pre-Training Time from 3 Days to 76 Minutes. 2019
		- Batch-size: 64k - 32k
		- Optimizer: **LAMB** (Layer-wise Adaptive Moments optimizer for Batch training)
		- Iteration: 1m -> 8,599
	- **Transformer-XL**: Z Dai, Z Yang, Y Yang, J Carbonell, Q Le, R Salakhutdinov. Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context. 2019
		- https://github.com/kimiyoung/transformer-xl
		- Fixed-length segment;
		- Improved on Rami Al-Rfou et.al. 2018 [Character-level language modeling with deeper self-attention]
		- Cached previous hidden states;
- OpenAI:
	- **GPT**: Alec Radford, Karthik Narasimhan, Tim Salimans, Ilya Sutskever. Improving Language Understanding by Generative Pre-Training. 2018
		- https://github.com/openai/finetune-transformer-lm
		- Causal Transformer;
		- Semi-supervised fine-tuning;
		- Pretrain: BooksCorpus dataset;
		- 12 x self-attention (Transformer);
	- **GPT-2**: Alec Radford, Jeffrey Wu, Rewon Child, David Luan, Dario Amodei, Ilya Sutskever. Language Models are Unsupervised Multitask Learners. 2018
		- Input representation: Byte Pair Encoding (BPE) (Sennrich et al., 2015); A Character-Level Decoder without Explicit Segmentation for Neural Machine Translation (Yoshua Bengio)
		- Layer normalization: moved to the input of each sub-block
		- additional layer normalization: after the final self attention block
		- 48 layers of transformer
- Amazon:
	- C Wang, M Li, A J. Smola. Language Models with Transformers. 2019
	<img src="/NLP/images/candidate-sample.png" alt="drawing" width="500"/>
	<img src="/NLP/images/coordinate-as.png" alt="drawing" width="600"/>

## Character Level
- Mikolov, T.; Karafit, M.; Burget, L.; Cernock, J.; and Khudanpur, S. 2010. Recurrent neural network based language model. INTERSPEECH 2010
- Mikolov, T.; Kombrink, S.; Burget, L.; ernock, J.; and Khudanpur, S. 2011. Extensions of recurrent neural network language model. ICASSP 2011
- Sundermeyer, M.; Schluter, R.; and Ney, H. Lstm neural networks for language modeling. 2012