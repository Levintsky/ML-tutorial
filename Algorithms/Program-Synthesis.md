# Program Synthesis

## Problem Definition
- Problem definition:
	- Input/Output examples -> Program
	- Task description -> Program
- Goal:
	- More productive: N. D. Matsakis and F. S. Klock. The Rust language. ACM SIGAda Ada Letters'14
	- More accessible: M. Resnick. Scratch: programming for all. CACM'09
- Challenge:
	- Large structured search space;
	- High false positive rate; (lack of tests)
- Database:
	- IOI, ICPC, 
	- Google Code Jam;
	- Facebook Hacker Cup;
	- E. Caballero, OpenAI, and I. Sutskever. Description2Code Dataset'16
	- Codeforce: https://codeforces.com/ (500k+ active users)
		- A. Ebtekar. How to interpret contest ratings. https://codeforces.com/blog/entry/68288, 2021
	- DeepMind: https://github.com/deepmind/code_contests
	- **APPS**: D. Hendrycks, S. Basart, S. Kadavath, M. Mazeika, A. Arora, E. Guo, C. Burns, S. Puranik, H. He, D. Song, et al. Measuring coding challenge competence with APPS. arxiv'21
		- 10k problems
- Metric:
	- n@k: n submissions from k samples per problems;
- https://sunblaze-ucb.github.io/program-synthesis/index.html
- https://github.com/topics/program-synthesis
- Tutorials:
	- https://www.youtube.com/watch?v=Q_Gyca1O1Lw
- Armando Solar-Lezama: https://people.csail.mit.edu/asolar/
- Dawn Song: https://people.eecs.berkeley.edu/~dawnsong/
- MSR (Sriram Rajamani): https://www.microsoft.com/en-us/research/people/sriram/

## Legacy
- Survey:
	- S. Gulwani, O. Polozov, R. Singh, et al. Program synthesis. Foundations and Trends® in Programming Languages, 4(1-2):1–119, 2017
	- Stephen Muggleton and Luc de Raedt. Inductive Logic Programming: Theory and Methods. 1994.
- Flash Fill (Excel)
- O Polozov, S Gulwani. FlashMeta: A Framework for Inductive Program Synthesis. 2015
- Translation:
	- Always through an IR (intermediate representation);
	- Tree-to-tree translation (recursive NN);
	- X Chen, C Liu, D Song. Tree-to-tree Neural Networks for Program Translation, NIPS 2018
	- C Fu, H Chen, H Liu, X Chen, Y Tian, F Koushanfar, J Zhao. Coda: An End-to-End Neural Program Decompiler. NIPS'19
- Search in DSL+short snippets
	- SMT: symbolic search
	- M. Bruch, M. Monperrus, and M. Mezini. Learning from examples to improve code completion systems. ACM SIGSOFT'09
	- S. Gulwani. Automating string processing in spreadsheets using input-output examples. ACM Sigplan'11
	- Menon, A., Tamuz, O., Gulwani, S., Lampson, B., and Kalai, A. A machine learning framework for programming by example. ICML'13
	- V. Raychev, M. Vechev, and E. Yahav. Code completion with statistical language models. SIGPLAN'14
	- Osera, P.-M. and Zdancewic, S. Type-and-example-directed program synthesis. ACM SIGPLAN'15
	- A Kalyan, A Mohta, O Polozov, D Batra, P Jain, S Gulwani. Neural-Guided Deductive Search for Real-Time Program Synthesis from Examples. 2018
	- R Fox, R Shin, S Krishnan, K Goldberg, D Song, and I Stoica. Parametrized hierarchical procedures for neural programming. ICLR'18
	- Sun, S.-H., Noh, H., Somasundaram, S., and Lim, J. Neural program synthesis from diverse demonstration videos. ICML'18
- Deductive:
	- C. C. Green. Application of theorem proving to problem solving. IJCAI'69.
	- Z. Manna and R. J. Waldinger. Toward automatic program synthesis. CACM'71
- Input/output-based:
	- S. Gulwani. Automating string processing in spreadsheets using input-output examples. ACM Sigplan Notice'11
	- E Parisotto, A Mohamed, R Singh, L Li, D Zhou, and P Kohli. Neuro-Symbolic Program Synthesis. ICLR'17
	- X Chen, C Liu, D Song. Towards Synthesizing Complex Programs from Input-Output Examples. ICLR'18
- Sketch-based (skeleton provided): one manually provides a sketch of the program to be induced, which specifies a rough outline of its structure;
	- A. Solar-Lezama. Program synthesis by sketching. University of California, Berkeley, 2008.
	- K Ellis, A Solar-Lezama, J Tenenbaum. Unsupervised Learning by Program Synthesis. NIPS'15
- Completion:
	- R. Robbes and M. Lanza. How program history can improve code completion. ICSE'08
	- A. Hindle, E. T. Barr, Z. Su, M. Gabel, and P. Devanbu. On the naturalness of software. ICSE'12
		- Program as n-grams.
	- G. A. Aye, S. Kim, and H. Li. Learning autocompletion from real-world datasets. 
- Execution:
	- NPI: S Reed and N Freitas. Neural programmer-interpreters. ICLR'16
	- M Bosnjak, T Rocktaschel, J Naradowsky, S Riedel. Programming with a Differentiable Forth Interpreter. ICML'17
	- J Cai, R Shin, and D Song. Making neural programming architectures generalize via recursion. ICLR'17

## Decoder (Transformer)
- Syntax-tree first (then to program):
	- W. Ling, P. Blunsom, E. Grefenstette, K. M. Hermann, T. Kočiský, F. Wang, and A. Senior. Latent predictor networks for code generation. ACL'16
		- Pointer network;
	- P. Yin and G. Neubig. A syntactic neural model for general-purpose code generation. ACL'17
		- RNN-based;
- Simple Code in Python
	- **Robustfill**: J Devlin, J Uesato, S Bhupatiraju, R Singh, A Mohamed, and P Kohli. Robustfill: Neural program learning under noisy i/o. ICML'17
	- C Clement, D Drain, J Timcheck, A Svyatkovskiy, and N Sundaresan. PyMT5: multi-mode translation of natural language and Python code with transformers. arxiv'20
	- Z. Feng, D. Guo, D. Tang, N. Duan, X. Feng, M. Gong, L. Shou, B. Qin, T. Liu, D. Jiang, et al. CodeBERT: a pre-trained model for programming and natural languages. EMNLP'20
	- J. Austin, A. Odena, M. Nye, M. Bosma, H. Michalewski, D. Dohan, E. Jiang, C. Cai, M. Terry, Q. Le, et al. Program synthesis with large language models. arxiv'21
	- **Codex**: M. Chen, J. Tworek, H. Jun, Q. Yuan, H. P. d. O. Pinto, J. Kaplan, H. Edwards, Y. Burda, N. Joseph, G. Brockman, et al. Evaluating large language models trained on code. arxiv'21
		- **Codex**: https://openai.com/blog/openai-codex/
		- GPT-3 on public github codebase;
		- HumanEval to avoid fp;
- A. Svyatkovskiy, S. K. Deng, S. Fu, and N. Sundaresan. IntelliCode compose: Code generation using transformer. '20
- I. Drori and N. Verma. Solving linear algebra by program synthesis. arxiv'21
	- Codex for math problems solving;
- L. Tang, E. Ke, N. Singh, N. Verma, and I. Drori. Solving probability and statistics problems by program synthesis. arxiv'21
- **AlphaCode**: Competition-Level Code Generation with AlphaCode. Nature'22
	- Model:
		- P(Y|X), X: language description (1,536 tokens)
		- Y: 768 tokens;
		- Multi-Query Attn (Shazeer 19): K/V share heads;
		- SentencePiece tokenizer (Kudo and Richardson, 2018);
	- Pretraining: 715GB codes, multiple languages;
		- Masked language modeling loss for encoder (Devlin'18);
		- Next token loss for decoder;
		- AdamW optimizer (Loshchilov Hutter '17)
	- Finetuning:
		- GOLD (Pang, He): offline RL;
		- Conditioned on right/wrong solution in training, right only in sampling;
		- Tempering: divide output logits by T < 1 to make sharper;
	- Generate large sample sets;
	- Filtering;
		- Remove 99% wrong solutions;
		- Clustering: a separate test input generation model;
- Guided search:
	- M Balog, A Gaunt, M Brockschmidt, S Nowozin, D Tarlow. DeepCoder: Learning to Write Programs. ICLR'17
- Generate program sketch:
	- V. Murali, L. Qi, S. Chaudhuri, and C. Jermaine. Neural sketch learning for conditional program generation. '17
	- D. Guo, A. Svyatkovskiy, J. Yin, N. Duan, M. Brockschmidt, and M. Allamanis. Learning to generate code sketches. arxiv'21
- Pseudo-code to code:
	- S. Kulal, P. Pasupat, K. Chandra, M. Lee, O. Padon, A. Aiken, and P. S. Liang. Spoc: Search-based pseudocode to code. NeurIPS'19
- Programatic policy in RL:
	- D. Trivedi, J. Zhang, S.-H. Sun, and J. J. Lim. Learning to synthesize programs as interpretable and generalizable policies. NeurIPS'21

## Unclassified
- R Bunel, A Desmaison, P Kohli, P Torr, M Kumar. Adaptive Neural Compilation. 2016
- A Gaunt, M Brockschmidt, R Singh, N Kushman, P Kohli, J Taylor, D Tarlow. TerpreT: A Probabilistic Programming Language for Program Induction. 2016
- M Bošnjak, T Rocktäschel, J Naradowsky, S Riedel. Programming with a Differentiable Forth Interpreter. ICML'17
- L Zhang, G Rosenblatt, E Fetaya, R Liao, W Byrd, M Might, R Urtasun, R Zemel. Neural Guided Constraint Logic Programming for Program Synthesis, NIPS'18
	- https://github.com/xuexue/neuralkanren
	- Input: input/output examples
	- miniKanren as symbolic system
	- ML propose candidates program satisfying the candidates
- A Zohar, L Wolf. Automatic Program Synthesis of Long Programs with a Learned Garbage Collector, NIPS'18
	- https://github.com/amitz25/PCCoder
	- Predict statement by statement
	- Garbage collection (things can be discarded)
	- Dynamic input
	- Prediction guided search
- **PQT**: D Abolafia, M Norouzi, J Shen, R Zhao, Q. Le. Neural Program Synthesis with Priority Queue Training. ICLR'18
	- https://github.com/tensorflow/models/tree/master/research/brain_coder
- S Sun, H Noh, S Somasundaram, and J Lim. Neural program synthesis from diverse demonstration videos. ICML'18
- R Fox, R Shin, S Krishnan, K Goldberg, D Song, I Stoica. Parametrized Hierarchical Procedures for Neural Programming. ICLR'18
- R Shin, I Polosukhin, D Song. Improving Neural Program Synthesis with Inferred Execution Traces. NIPS'18
- N Natarajan, D Simmons, N Datha, P Jain, S Gulwani. Learning Natural Programs from a Few Examples in Real-Time. AISTATS'19
- X Chen, C Liu, D Song. Execution-Guided Neural Program Synthesis. ICLR'19
- R Shin, N Kant, K Gupta, C Bender, B Trabucco, R Singh, D Song. Synthetic Datasets for Neural Program Synthesis. ICLR'19
- R Shin, M Brockschmidt, M Allamanis, O Polozov. Program Synthesis and Semantic Parsing with Learned Code Idioms. ICLR'19
- B Wang, R Shin, X Liu, O Polozov, M Richardson. RAT-SQL: Relation-Aware Schema Encoding and Linking for Text-to-SQL Parsers. 2019
- H Shi, Y Zhang, X Chen, Y Tian, J Zhao. Deep Symbolic Superoptimization Without Human Knowledge. ICLR'20

## Applications
- Univ of Edinburgh, Google Brain. HOUDINI: Lifelong Learning as Program Synthesis, NIPS 2018
	- Problem: lifelong learning
	- Neural libraries for lifelong learning
	- Functional programs represent deep architecture
	- Symbolic program synthesis to choose: which to re-use? put them together?
	- Differentiable, fine-tuned by gd
- NLP: reading comprehension:
	- X Chen, C Liang, A Yu, D Zhou, D Song, Q Le. Neural Symbolic Reader: Scalable Integration of Distributed and Symbolic Representations for Reading Comprehension. ICLR'20
- CV: search a program:
	- NGSI: S Lu, J Mao, J Tenenbaum, J Wu. Neurally-Guided Structure Inference. ICML'19
		- https://github.com/desire2020/NGSI
		- Key insight: search-based, exhaustive -> neural guided;
		- The algorithm builds the hierarchical structure by recursively choosing the production rule to expand a non-terminal symbol;
		- Application 1: Matrix decomposition. F = MG + G. M: selection; first G: Gaussian of cluster center; 2nd G: i.i.d Noise;
		- Application 2: Program parsing. Build on Xinyun 2018 with while loop.