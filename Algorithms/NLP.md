# Basics of NLP

## Basics
- Word Embedding;
- Language model & representation;
- Downstream tasks;
- Courses:
	- Oxford: https://github.com/oxford-cs-deepnlp-2017/lectures
	- Stanford: cs224
- Resources:
	- torch-text: https://github.com/pytorch/text

## Benchmarks
- https://machinelearningmastery.com/datasets-natural-language-processing/
- https://github.com/niderhoff/nlp-datasets
- **GLUE**: A. Wang, A. Singh, J. Michael, F. Hill, O. Levy, and S. R. Bowman. Glue: A multi-task benchmark and analysis platform for natural language understanding. 2018
- Large corpse for LM:
	- **text8**: Mahoney, M. 2009. Large text compression benchmark. http://www.mattmahoney.net/text/text.html.
	- **enwik8**
	- **lm1b**: Chelba, C.; Mikolov, T.; Schuster, M.; Ge, Q.; Brants, T.; Koehn, P.; and Robinson, T. 2013. One billion word benchmark for measuring progress in statistical language modeling. 2013
	- **Newsroom**: Max Grusky, Mor Naaman, and Yoav Artzi. Newsroom: A dataset of 1.3 million summaries with diverse extractive strategies. NAACL'18
- Natural Language Inference
	- entailment, contradiction or neutral.
- Sentiment analysis
	- SST-5. Stanford Sentiment Treebank Socher. et al., 2013
- NER (Named entity extraction)
	- CoNLL 2003: NER task (Sang and Meulder, 2003)
- Question Answering
	- SQuAD
	- Mandar Joshi, Eunsol Choi, Daniel S Weld, and Luke Zettlemoyer. **Triviaqa**: A large scale distantly supervised challenge dataset for reading comprehension. 2017
	- Adam Trischler, Tong Wang, Xingdi Yuan, Justin Harris, Alessandro Sordoni, Philip Bachman, and Kaheer Suleman. **Newsqa**: A machine comprehension dataset. 2016
- Advice:
	- Y Choi. Evaluating Machines by their Real-World Language Use. 2020
		- Benchmark: Giving helpful advice;
		- http://rowanzellers.com/advice/
- 中文:
	- LCCC: (Large-scale Cleaned Chinese Conversation): 对话;

## Evaluation Metrics
- Generation quality:
	- N-gram overlap: BLEU, ROUGE, METEOR, CIDEr
		- **BLEU**: Kishore Papineni, Salim Roukos, Todd Ward, and Wei-Jing Zhu. Bleu: a method for automatic evaluation of machine translation. ACL'02
	- Semantic overlap:
		- PYRAMID: Nenkova, et al., 2007
		- SPICE: abstract scene graph, Anderson et al., 2016.
		- SPIDEr: SPICE (semantic graph similarity) + CIDER (n-grams); Liu et al., 2017
	- Model-based
		- Vector similarity: Embedding average, vector extrema, meant, yisi;
		- World mover's distance
		- BERTSCORe;
		- Sentence Movers Similarity;
		- BLEURT;
	- Human evaluation;

## Backbones
- Bag of vectors
	- n-grams:
		- FastText: Joulin et al. Bag of tricks for efficient text classification, ACL'16
			- https://fasttext.cc/
- CNN
- RNN
- Transformer (SOTA)
- Recursive (Tree-structured)
	- TreeRNN: Socher, Manning, and Ng. ICML, 2011
	- Socher, Perelygin, Wu, Chuang, Manning, Ng, and Potts 2013
	- Tai, Socher, Manning [2015]: TreeLSTMs

## Parsing
- Syntactic Structure: Consistency and Dependency
- Problem:
	- Root and acyclic tree;
- Dependency Grammar and Treebanks
- Benchmark:
	- Brown corpus 1967 (PoS tagged 1979)
	- Lancaster-IBM Treebank (late 1980s)
	- Universal Dependencies: http://universaldependencies.org/
- Evaluation metric:
	- Acc = correct deps / deps
	- UAS
	- LAS
- Dynamic programming: Eisner'96, O(n^3)
- Graph algorithms
	- MST McDonald'05 O(n^2)
	- Neural graph-based: Dozat and Manning'17 (SOTA)
		- Slower than transition-based;
- Transition-based dependency parsing
	- Greedy transition-based Nivre'03
		- Shift-reduce
	- MaltParser [Nivre and Hall'05]
		- 3 untyped choices (|R|x2+1 at max)
		- Features: top of stack, POS; first in buffer, POS;
		- No search, but can add beam search;
		- Lower accuracy, but fast linear time parsing;
	- Nivre'08
	- Non-projectivity: add SWAP action
	- **Neural dependency parsing**
		- Chen and Manning 2014
			- Word embedding; POS and dependency also d-dim vectors;
			- MLP + softmax-classifier;
		- Weiss'15
		- Andor'16: SyntaxNet (SOTA), McParseFace

## Machine Translation
- Benchmarks:
	- WMT'14, '16, ...
- Evaluation:
	- Human;
	- BLEU; number of matched n-grams;
- So far the most succesful DL + NLP;
- Challenges: OOV, ...
	- Has AI surpassed humans at translation? Not even close! https://www.skynettoday.com/editorials/state_of_nmt
- Embedding:
	- Character-level: GMNT (WordPiece);
- Backbone:
	- LSTM:
		- **GMNT**: Y. Wu, et al. Google's Neural Machine Translation System: Bridging the Gap between Human and Machine Translation. 2016
			- WordPiece for Korean, Japanese
		- Massive Exploration of Neural Machine Translation Architecutres, Britz et al, 2017.
	- Attention:
		- More information: Deep Learning for NLP Best Practices, Ruder, 2017. http://ruder.io/deep-learning-nlp-best-practices/index.html#attention
- Loss design:
	- Efficient:
		- NCE: Zoph et al. 2016, Simple, Fast Noise- Contrastive Estimation for Large RNN Vocabularies. '16
		- Hierarchical Softmax, char-level;
- Tricks:
	- Token [UNK] for unknown words; Gulcehre et al. 2016, Pointing the Unknown Words. (Copy)
- M Johnson, et al. Googles multilingual neural machine translation system: Enabling zero-shot translation. TACL'17
- Generative Neural Machine Translation. NIPS'18
- Steer (with a small NN?):
	- J Gu, G Neubig, K Cho, and V Li. Learning to translate in real-time with neural machine translation. arxiv'16
	- J Gu, K Cho, and V Li. Trainable greedy decoding for neural machine translation. arxiv'17

## (Conditional) Generation
- Generally contains a lot of problems
	- Translation (multi-lingual generation)
	- Summarization
	- QA, Dialog
- Backbone:
	- Transformer:
		- Google-Brain. Generating Wikipedia by Summarizing Long Sequences. ICLR'18
- Decoding:
	- Top-k sampling:
		- Fan et al., ACL 2018; Holtzman et al., ACL 2018
	- re-balancing distributions: 
		- Khandelwal et. al., ICLR 2020
	- Encourage divesrity, unlikelihood training:
		- Welleck et al., 2020
	- Exposure bias: scheduled sampling, DAgger;
- Evaluation:
	- Likelihood (also training loss);
	- Quality;
		- Surrogate with BLEU (RL);
- Challenges:
	- A Holtzman, J Buys, L Du, M Forbes, Y Choi. The Curious Case of Neural Text Degeneration. ICLR'20
- Loss design:
	- MLE: Σlogp(yt|y0..t-1, x), x as context;
	- RL reward: J(θ) = Eθ[Σγ^t rt]
	- Learn from Human feedback:
		- ADEM Lowe'17, HUSE Hashimoto'19
- LLM SOTA:
	- **LaMDA**: Romal Thoppilan. LaMDA: Language Models for Dialog Applications. 2022
- Social impact:
	- Ethics: Sheng et al., EMNLP'19; Zellers et al., NeurIPS'19
	- Hidden biases: Wallace et al., EMNLP'19; Gehman et al., EMNLP Findings 2020
- Conditional:
	- S Bengio. Content preserving text generation with attribute controls. NIPS'18
- Deep State Space Models for Unconditional Word Generation. NIPS'18
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
- Finetune with RL:
	- **SeqGAN**: L Yu, W Zhang, J Wang, and Y Yu. SeqGAN: Sequence generative adversarial nets with policy gradient. AAAI'17
	- OpenAI. Fine-tuning language models from human preferences. arXiv'19
		- Learn a reward function;
		- Use reward model for policy training;
- Training with conditions:
	- Y Kikuchi, G Neubig, R Sasano, H Takamura, and M Okumura. Controlling output length in neural encoder-decoders. EMNLP'16
	- J Ficler and Y Goldberg. Controlling linguistic style aspects in neural language generation. 2017
- Inference time:
	- **PPLM**: Uber-AI. Plug and Play Language Models: a Simple Approach to Controlled Text Generation. ICLR'20
		- https://github.com/uber-research/pplm
		- Insight: modify history in the direction to maximize both p(x) and p(a|x), then we get p(x|a);
- **GOLD**: R Pang, H He. Text Generation by Learning from Demonstrations. ICLR'21
	- https://github.com/yzpang/gold-off-policy-text-gen-iclr21
	- Also used in AlphaCode;
	- Offline RL with reward rt = p_human(at|st)
	- Offline: reduce interaction with the environment and stay close to the demonstrated trajectories.
		- E[Σwt ∇θlogπ(at|st;θ) Q(st, at)]
		- wt: IS weight, wt = ∏t π(at;θ)/π(at;b); approx as wt = π(at;θ)/π(at;b) in GOLD;
	- Final gradient: ∇J(θ) = ΣΣ π(at|st;θ) ∇logπ(at|st;θ) Q(st,at)
		- R(s,a) := logp_MLE(a|s), with γ = 1
		- Q(s,a) := Σt p(at|st)
- Summarization:
	- A See, P Liu, and C Manning. Get to the point: Summarization with pointer-generator networks. ACL'17

## (External)-Knowledge based
- Resouces:
	- https://www.cnblogs.com/huangyc/p/10043749.html
- K Meng, D Bau, A Andonian, Y Belinkov. Locating and Editing Factual Associations in GPT. 
	- rank-1 update: w2 = w2 + uv' (Rome/Paris)
- M Geva, R Schuster, J Berant, O Levy. Transformer Feed-Forward Layers Are Key-Value Memories. EMNLP'21
- D Dai, L Dong, Y Hao, Z Sui, B Chang, F Wei. Knowledge Neurons in Pretrained Transformers. ACL'22
- External tool:
	- No trained retriever;
	- OpenAI: **WebGPT**: Browser-assisted question-answering with human feedback. 2021
	- DeepMind: **LaMDA**: Language Models for Dialog Applications. 2022
- Learn to retrieve (E2E, trial and error);
	- Problem setup: p(gold-answer|input, memory)
		- ∑memory p(mem|input)p(gold-answer|input,mem)
	- **ORQA**: K Lee, M Chang, K Toutanova. Latent Retrieval for Weakly Supervised Open Domain Question Answering. ACL'19
	- **REALM**: K Guu, K Lee, Z Tung, P Pasupat, M Chang. REALM: Retrieval-Augmented Language Model Pre-Training.

## Coreference Resolution in Two Steps
- Benchmarks:
	- http://corenlp.run/ (ask for coref in Annotations)
	- https://huggingface.co/coref/
- Evaluation:
	- Many different metrics: MUC, CEAF, LEA, B-CUBED, BLANC
- Generally two steps:
	- Detect the mentions (easy)
	- Cluster the mentions (hard)
- Legacy: Hobbs Algorithm 1976
- Knowledge-based Pronominal Coref
	- Hector Levesque, Ernest Davis, and Leora Morgenstern. The winograd schema challenge. PKDD'12
- Neural Coref:
	- Clark and Manning 2016
	- SOTA E2E: Kenton Lee et al. from UW (EMNLP 2017) et seq.
		- bi-LSTM;
	- SOTA Transformer:
		- SpanBERT, BERT-QA,
		- Dobrovolskii (2021): Word-Level Coreference Resolution. EMNLP'21

## QA
- Problem definition:
	- What information source does a system build on?
		- A text passage, all Web documents, knowledge bases, tables, images..
	- Question type: Factoid vs non-factoid, open-domain vs closed-domain, simple vs compositional, ..
	- Answer type: A short segment of text, a paragraph, a list, yes/no, ...
- Benchmark:
	- Z Yang, ..., C D Manning. **Hotpotqa**: A dataset for diverse, explainable multi-hop question answering. 2018
	- SQuAD;
- Legacy:
	- Simmons et al., 1964
	- 2011: IBM Watson beat Jeopardy champions
		- (1) Question processing, (2) Candidate answer generation, (3) Candidate answer scoring, and (4) Confidence merging and ranking.
- Backbone:
	- LSTM-based (16-18)
	- Almost all SOTA based on BERT; (19-)
- Knowledge-based:
	- FreeBase;
- Comprehension/Understanding: read and then answer;
	- K Hermann, T Kocisky, E Grefenstette, L Espeholt, W Kay, M Suleyman, and P Blunsom. Teaching machines to read and comprehend. NIPS'15
	- **BiDAF**: (Seo et al., 2017): Bidirectional Attention Flow for Machine Comprehension
	- (Jia and Liang, 2017): Adversarial Examples for Evaluating Reading Comprehension Systems
	- Densely Connected Attention Propagation for Reading Comprehension. NIPS'18
	- e-SNLI: Natural Language Inference with Natural Language Explanations (DeepMind). NIPS'18
	- (Sen and Saffari, 2020): What do Models Learn from Question Answering Datasets?
	- (Ribeiro et al., 2020): Beyond Accuracy: Behavioral Testing of NLP Models with CheckList
- Open-domain QA:
	- Closed domain: a specific domain (medicine, technical support)
	- Retriever-reader:
		- Chen et al., 2017. Reading Wikipedia to Answer Open-domain Questions
		- Lee et al., 2019. Latent Retrieval for Weakly Supervised Open Domain Question Answering
		- Karpukhin et al., 2020. Dense Passage Retrieval for Open-Domain Question Answering
		- Izacard and Grave 2020. Leveraging Passage Retrieval with Generative Models for Open Domain Question Answering
		- Roberts et al., 2020. How Much Knowledge Can You Pack Into the Parameters of a Language Model?
		- Seo et al., 2019. Real-Time Open-Domain Question Answering with Dense-Sparse Phrase Index
		- Lee et al., 2020. Learning Dense Representations of Phrases at Scale
- A Fan, Yacine Jernite, Ethan Perez, David Grangier, Jason Weston, and Michael Auli. Eli5: Long form question answering. 2019
- decaNLP: B McCann, N Keskar, C Xiong, and R Socher. The natural language decathlon: Multitask learning as question answering. 2018
- P Lewis, L Denoyer, and S Riedel. Unsupervised question answering by cloze translation. 2019
- Knowledge-based/augmented:
	- M Dunn, L Sagun, M Higgins, V Guney, V Cirik, and K Cho. Searchqa: A new q&a dataset augmented with context from a search engine. 2017

## Misc
- A Retrieve-and-Edit Framework for Predicting Structured Outputs. NIPS'18
- NIPS Tutorial:
	- Navigating with Graph Representations for Fast and Scalable Decoding of Neural Language Models