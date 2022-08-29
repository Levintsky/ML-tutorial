# SSL

## Cloze Test, Future Prediction
- Bidirectional:
	- **BERT**: Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova. BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding. ACL'19
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
		<img src = '/Weak-Unsupervised/images/bert.png' width = '600px'>
	- Y You, J Li, J Hseu, X Song, J Demmel, C Hsieh. Reducing BERT Pre-Training Time from 3 Days to 76 Minutes. 2019
		- Batch-size: 64k - 32k
		- Optimizer: **LAMB** (Layer-wise Adaptive Moments optimizer for Batch training)
		- Iteration: 1m -> 8,599
	- **RoBERTa**: Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike Lewis, Luke Zettlemoyer, Veselin Stoyanov. RoBERTa: A Robustly Optimized BERT Pretraining Approach. 2019
		- Difference from BERT:
			- More data (160G v.s. Bert 16G): Books Corpus + English Wikipedia 16GB; CC-New (76G); OpenWebText (38G); Stories (31GB);
		- More Steps; (500k steps)
		- Large Batch; (8000 v.s. BERT 256)
		- ADAM (0.98 v.s. BERT 0.999)
- Causal:
	- **GPT**: A Radford, K Narasimhan, T Salimans, I Sutskever. Improving Language Understanding by Generative Pre-Training. 2018
		- https://github.com/openai/finetune-transformer-lm
		- Causal Transformer;
		- Semi-supervised fine-tuning;
		- Pretrain: BooksCorpus dataset;
		- 12 x self-attention (Transformer);
	- R Al-Rfou, D Choe, N Constant, M Guo, L Jones. Character-Level Language Modeling with Deeper Self-Attention. 2018
		- 64 transformer layers (deep, multi-head self-attention + fc x 2);
		- Mask for causal attention;
		- Auxiliary loss:
			- Multiple prediction (predict every character in the sequence)
			- Intermediate layer losses (deep supervision)
			- Multiple targets
		- 235 million parameters, dropout (0.55)
	- **GPT-2**: A Radford, J Wu, R Child, D Luan, D Amodei, I Sutskever. Language Models are Unsupervised Multitask Learners. 2018
		- Input representation: Byte Pair Encoding (BPE) (Sennrich et al., 2015); A Character-Level Decoder without Explicit Segmentation for Neural Machine Translation (Yoshua Bengio)
		- Layer normalization: moved to the input of each sub-block
		- additional layer normalization: after the final self attention block
		- 48 layers of transformer
	- R Child, S Gray, A Radford, and I Sutskever. Generating long sequences with sparse transformers. 2019
	- **GPT-3**: Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel M. Ziegler, Jeffrey Wu, Clemens Winter, Christopher Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever, Dario Amodei. Language Models are Few-Shot Learners. 2020
		- https://github.com/openai/gpt-3
		- 175B parameters, 45T training data;

## Embedding
- Discrete token, carries a lot of meaning (not like pixels in vision)
- P Bojanowski and E Grave and A Joulin and T Mikolov. Enriching Word Vectors with Subword Information. TACL'17
<img src = '/Weak-Unsupervised/images/fastText.png' width = '500px'>

- Joulin et al. Bag of tricks for efficient text classification, ACL 2016
	- https://fasttext.cc/
- Sentences:
	- A. Vaswani et al. Attention is all you need, NIPS'17
	<img src="/NLP/images/transformer1.png" alt="drawing" width="500"/>
	<img src="/NLP/images/transformer2.png" alt="drawing" width="600"/>

	- **BERT**: J. Devlin et al. BERT: Pre-training of deep bidirectional transformers for language understanding. ACL'19
	<img src = '/Weak-Unsupervised/images/bert.png' width = '500px'>

- Generative models:
	- Auto-regressive (RNN/CNN/Transformers) are good at generating short sentences.
		- I. Serban et al. Building end-to-end dialogue systems using generative hierarchical neural network models. AAAI 2016
	- Retrieval-based
		- A. Bordes et al. Question answering with subgraph embeddings, EMNLP 2014
		- R. Yan et al. Learning to Respond with Deep Neural Networks for Retrieval-Based Human-Computer Conversation System, SIGIR 2016
		- M. Henderson et al. Efficient natural language suggestion for smart reply, arXiv 2017
	- Combining Two:
		- J. Gu et al. Search Engine Guided Non-Parametric Neural Machine Translation, arXiv 2017
		- K. Guu et al. Generating Sentences by Editing Prototypes, ACL 2018
- Generate documents (open challenges):
	- are coherent,
	- how to keep track of state,
	- how to model uncertainty,
		- M. Ott et al. Analyzing uncertainty in NMT, ICML 2018
	- how to ground,
		- starting with D. Roy / J. Siskind’s work from early 2000’s
	- meaningful metrics & standardized tasks!
- Unsupervised Translation:
	- A. Conneau et al. Word translation without parallel data, ICLR 2018
		- https://github.com/facebookresearch/MUSE
		- https://github.com/facebookresearch/fastText
		- W = argmin||Wx-y||^2
		- No pair data, so fool discrimitor for Wx and y
		- Nearest neighbor for refinements
		- Orthogonality
	- G. Lample et al. Phrase-based and neural unsupervised machine translation, EMNLP 2018
- van den Oord, A., et al. WaveNet: A Generative Model for Raw Audio. NIPS'16
	- Dilated Conv
	<img src = '/NLP/images/wavenet1.png' width = '500px'>

	- ResNet
	<img src = '/NLP/images/wavenet2.png' width = '500px'>
