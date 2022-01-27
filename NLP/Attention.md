# Attention Model

## Good Summaries
- https://lilianweng.github.io/lil-log/2018/06/24/attention-attention.html
- https://lilianweng.github.io/lil-log/2019/01/31/generalized-language-models.html
- https://lilianweng.github.io/lil-log/2020/04/07/the-transformer-family.html
- https://zhuanlan.zhihu.com/p/109992475

## Classic
- **Attention**: D Bahdanau, K Cho, and Y Bengio. Neural machine translation by jointly learning to align and translate. arxiv'14
- **ELMO**: Matthew E. Peters, Mark Neumann, Mohit Iyyer, Matt Gardner, Christopher Clark, Kenton Lee, Luke Zettlemoyer. Deep contextualized word representations. NAACL'18
	- https://allennlp.org/elmo
	- ELMo (Embeddings from Language Models)
	- bidirectional LSTM, predict next/last word

## Transformer/BERT series
- **Transformer**: Attention is all you need. NIPS 2017
	- A very good intro: http://jalammar.github.io/illustrated-transformer/
	- Explanation with Pytorch: http://nlp.seas.harvard.edu/2018/04/03/attention.html
	- https://github.com/Kyubyong/transformer
	- Pytorch: https://github.com/jadore801120/attention-is-all-you-need-pytorch
		<img src="/NLP/images/transformer1.png" alt="drawing" width="500"/>
		<img src="/NLP/images/transformer2.png" alt="drawing" width="600"/>
- Rami Al-Rfou, Dokook Choe, Noah Constant, Mandy Guo, Llion Jones. Character-Level Language Modeling with Deeper Self-Attention. AAAI'19
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
- Neil Houlsby, Andrei Giurgiu, Stanislaw Jastrzebski, Bruna Morrone, Quentin de Laroussilhe, Andrea Gesmundo, Mona Attariyan, Sylvain Gelly. Parameter-Efficient Transfer Learning for NLP. ICML'19
	- Adapter module
- Y You, J Li, J Hseu, X Song, J Demmel, C Hsieh. Reducing BERT Pre-Training Time from 3 Days to 76 Minutes. 2019
	- Batch-size: 64k - 32k
	- Optimizer: **LAMB** (Layer-wise Adaptive Moments optimizer for Batch training)
	- Iteration: 1m -> 8,599
- **Transformer-XL**: Z Dai, Z Yang, Y Yang, J Carbonell, Q Le, R Salakhutdinov. Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context. 2019
	- https://github.com/kimiyoung/transformer-xl
	- Insight: improved attention span; (Improved on Rami Al-Rfou et.al. 2018 [Character-level language modeling with deeper self-attention])
	- Dynamic masking;
	- Fixed-length segment; hidden state reuse\
		<img src = '/NLP/images/transformer-xl.png' width = '600px'>
	- Relative position encoding:\
		<img src = '/NLP/images/transformer-xl-2.png' width = '600px'>
- **XLNet**: Zhilin Yang, Zihang Dai, Yiming Yang, Jaime Carbonell, Ruslan Salakhutdinov, Quoc V. Le. XLNet: Generalized Autoregressive Pretraining for Language Understanding. 2019
	- https://github.com/zihangdai/xlnet
- Sainbayar Sukhbaatar, Edouard Grave, Piotr Bojanowski, Armand Joulin. Adaptive Attention Span in Transformers. 2019
- **RoBERTa**: Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike Lewis, Luke Zettlemoyer, Veselin Stoyanov. RoBERTa: A Robustly Optimized BERT Pretraining Approach. 2019
	- Difference from BERT:
		- More data (160G v.s. Bert 16G): Books Corpus + English Wikipedia 16GB; CC-New (76G); OpenWebText (38G); Stories (31GB);
	- More Steps; (500k steps)
	- Large Batch; (8000 v.s. BERT 256)
	- ADAM (0.98 v.s. BERT 0.999)
- **Universal Transformers**: Mostafa Dehghani, Stephan Gouws, Oriol Vinyals, Jakob Uszkoreit, Łukasz Kaiser. Universal Transformer. ICLR'19
	- Transformer + RNN;
- Zhenzhong Lan, Mingda Chen, Sebastian Goodman, Kevin Gimpel, Piyush Sharma, Radu Soricut. ALBERT: A Lite BERT for Self-supervised Learning of Language Representations.
- **Google-T5**: https://ai.googleblog.com/2020/02/exploring-transfer-learning-with-t5.html
	- Transfer learning;
- **Reformer**: Nikita Kitaev, Łukasz Kaiser, Anselm Levskaya. Reformer: The Efficient Transformer. ICLR'20
	- LSH instead of fc for speed;

## GPT
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

## Position Encoding
- Original in transformer:\
	<img src="/NLP/images/pos-enc.png" alt="drawing" width="500"/>	
- Learned Position Encoding: Jonas Gehring, Michael Auli, David Grangier, Denis Yarats, Yann N. Dauphin. Convolutional Sequence to Sequence Learning. 2017

## BERT for RL
- **GTrXL**: Emilio Parisotto, H. Francis Song, Jack W. Rae, Razvan Pascanu, Caglar Gulcehre, Siddhant M. Jayakumar, Max Jaderberg, Raphael Lopez Kaufman, Aidan Clark, Seb Noury, Matthew M. Botvinick, Nicolas Heess, Raia Hadsell. Stabilizing Transformers for Reinforcement Learning.
