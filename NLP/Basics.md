# Basics of NLP

## Basics
- Word Embedding;
- Language model & representation;
- Downstream tasks;

## Benchmarks
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
	- Mandar Joshi, Eunsol Choi, Daniel S Weld, and Luke Zettlemoyer. Triviaqa: A large scale distantly supervised challenge dataset for reading comprehension. 2017
	- Adam Trischler, Tong Wang, Xingdi Yuan, Justin Harris, Alessandro Sordoni, Philip Bachman, and Kaheer Suleman. Newsqa: A machine comprehension dataset. 2016
	- Adam Trischler, Tong Wang, Xingdi Yuan, Justin Harris, Alessandro Sordoni, Philip Bachman, and Kaheer Suleman. Newsqa: A machine comprehension dataset.
- Hector Levesque, Ernest Davis, and Leora Morgenstern. The winograd schema challenge. PKDD'12
- Advice:
	- Rowan Zellers, Ari Holtzman, Elizabeth Clark, Lianhui Qin, Ali Farhadi, Yejin Choi. Evaluating Machines by their Real-World Language Use. 2020
		- Benchmark: Giving helpful advice;
		- http://rowanzellers.com/advice/

## Comprehension/Understanding
- Densely Connected Attention Propagation for Reading Comprehension. NIPS'18
- e-SNLI: Natural Language Inference with Natural Language Explanations (DeepMind). NIPS'18

## (Conditional) Generation
- Samy Bengio. Content preserving text generation with attribute controls. NIPS'18
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
	- OpenAI. Fine-tuning language models from human preferences. arXiv'19
		- Learn a reward function;
		- Use reward model for policy training;

## QA
- K Hermann, T Kocisky, E Grefenstette, L Espeholt, W Kay, M Suleyman, and P Blunsom. Teaching machines to read and comprehend. NIPS'15
- A Fan, Yacine Jernite, Ethan Perez, David Grangier, Jason Weston, and Michael Auli. Eli5: Long form question answering. 2019
- Bryan McCann, Nitish Shirish Keskar, Caiming Xiong, and Richard Socher. The natural language decathlon: Multitask learning as question answering. 2018
- Zhilin Yang, Peng Qi, Saizheng Zhang, Yoshua Bengio, William W Cohen, Ruslan Salakhutdinov, and Christopher D Manning. Hotpotqa: A dataset for diverse, explainable multi-hop question answering. 2018
- Patrick Lewis, Ludovic Denoyer, and Sebastian Riedel. Unsupervised question answering by cloze translation. 2019
- Knowledge-based/augmented:
	- M Dunn, L Sagun, M Higgins, V Guney, V Cirik, and K Cho. Searchqa: A new q&a dataset augmented with context from a search engine. 2017

## Summarization
- Abigail See, Peter J Liu, and Christopher D Manning. Get to the point: Summarization with pointer- generator networks. ACL'17

## Machine Translation
- Backbone:
	- LSTM:
		- **GMNT**: Y. Wu, et al. Google's Neural Machine Translation System: Bridging the Gap between Human and Machine Translation. 2016
			- WordPiece for Korean, Japanese
- Yonghui Wu, et al. Google’s neural machine translation system: Bridging the gap between human and machine translation. 2016
- M Johnson, et al. Googles multilingual neural machine translation system: Enabling zero-shot translation. TACL'17
- Generative Neural Machine Translation. NIPS'18

## Misc
- A Retrieve-and-Edit Framework for Predicting Structured Outputs. NIPS'18
- NIPS Tutorial:
	- Navigating with Graph Representations for Fast and Scalable Decoding of Neural Language Models