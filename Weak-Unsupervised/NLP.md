# Semi/Un Supervised Learning

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

- **Work**:
	- Unsup on several applications
	- Word embeddings
	- Text gen of short sentences
- **Sort-of-Work**:
	- Sentence embedding
	- Unsup MT under some conditions
- **Does-not-Work-yet**:
	- Modeling long documents
- **FAIR**:
	- Yann. Adversarially-Trained Normalized Noisy-Feature Auto-Encoder for Text Generation, 2018
	- Yann. Byte-Level Recursive Convolutional Auto-Encoder for Text, 2018