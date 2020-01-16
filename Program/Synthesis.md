# Program Synthesis

## Basics
- Problem definition: Input/Output examples -> Program

## Unclassified
- Rudy Bunel, Alban Desmaison, Pushmeet Kohli, Philip H.S. Torr, M. Pawan Kumar. Adaptive Neural Compilation. 2016
- Alexander L. Gaunt, Marc Brockschmidt, Rishabh Singh, Nate Kushman, Pushmeet Kohli, Jonathan Taylor, Daniel Tarlow. TerpreT: A Probabilistic Programming Language for Program Induction. 2016
- Matej Balog, Alexander L. Gaunt, Marc Brockschmidt, Sebastian Nowozin, Daniel Tarlow. DeepCoder: Learning to Write Programs. ICLR'17
- Emilio Parisotto, Abdelrahman Mohamed, Rishabh Singh, Lihong Li, Denny Zhou, and Pushmeet Kohli. Neuro-Symbolic Program Synthesis. ICLR'17
- Matko Bošnjak, Tim Rocktäschel, Jason Naradowsky, Sebastian Riedel. Programming with a Differentiable Forth Interpreter. ICML'17
- **Robustfill**: Jacob Devlin, Jonathan Uesato, Surya Bhupatiraju, Rishabh Singh, Abdel-rahman Mohamed, and Pushmeet Kohli. Robustfill: Neural program learning under noisy i/o. ICML'17
	- https://www.microsoft.com/en-us/research/blog/deep-learning-program-synthesis/
	<img src = '/Program/images/robustfill.png' width = '400px'>
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
- **PQT**: Daniel A. Abolafia, Mohammad Norouzi, Jonathan Shen, Rui Zhao, Quoc V. Le. Neural Program Synthesis with Priority Queue Training. ICLR'18
	- https://github.com/tensorflow/models/tree/master/research/brain_coder
- Roy Fox, Richard Shin, Sanjay Krishnan, Ken Goldberg, Dawn Song, Ion Stoica. Parametrized Hierarchical Procedures for Neural Programming. ICLR'18
- Xinyun Chen, Chang Liu, Dawn Song. Towards Synthesizing Complex Programs from Input-Output Examples. ICLR'18
- Ashwin Kalyan, Abhishek Mohta, Oleksandr Polozov, Dhruv Batra, Prateek Jain, Sumit Gulwani. Neural-Guided Deductive Search for Real-Time Program Synthesis from Examples. 2018
	- Evaluate program 'goodness' and search potentially good program first;
- Richard Shin, Illia Polosukhin, Dawn Song. Improving Neural Program Synthesis with Inferred Execution Traces. NIPS'18
- Nagarajan Natarajan, Danny Simmons, Naren Datha, Prateek Jain, Sumit Gulwani. Learning Natural Programs from a Few Examples in Real-Time. AISTATS'19
- Xinyun Chen, Chang Liu, Dawn Song. Execution-Guided Neural Program Synthesis. ICLR'19
- Richard Shin, Neel Kant, Kavi Gupta, Chris Bender, Brandon Trabucco, Rishabh Singh, Dawn Song. Synthetic Datasets for Neural Program Synthesis. ICLR'19
- Cheng Fu, Huili Chen, Haolan Liu, Xinyun Chen, Yuandong Tian, Farinaz Koushanfar, Jishen Zhao. Coda: An End-to-End Neural Program Decompiler. NIPS'19
- Richard Shin, Marc Brockschmidt, Militadis Allamanis, Oleksandr Polozov. Program Synthesis and Semantic Parsing with Learned Code Idioms. ICLR'19
- Bailin Wang, Richard Shin, Xiaodong Liu, Oleksandr Polozov, Matthew Richardson. RAT-SQL: Relation-Aware Schema Encoding and Linking for Text-to-SQL Parsers. 2019
- Hui Shi, Yang Zhang, Xinyun Chen, Yuandong Tian, Jishen Zhao. Deep Symbolic Superoptimization Without Human Knowledge. ICLR'20

## Legacy
- Stephen Muggleton and Luc de Raedt. Inductive Logic Programming: Theory and Methods. 1994.
- Flash Fill (Excel)
- Oleksandr Polozov, Sumit Gulwani. FlashMeta: A Framework for Inductive Program Synthesis. 2015

## Sketching
- one manually provides a sketch of the program to be induced, which specifies a rough outline of its structure;
- Armando Solar Lezama. Program Synthesis By Sketching. 2008
- Kevin Ellis, Armando Solar-Lezama, Joshua B. Tenenbaum. Unsupervised Learning by Program Synthesis. NIPS'15
	- Formulation:\
		<img src = '/Program/images/unsup1.png' width = '400px'>
	- Algorithm:\
		<img src = '/Program/images/unsup2.png' width = '400px'>
	- Grammar:\
		<img src = '/Program/images/unsup3.png' width = '400px'>
	- SMT search space:\
		<img src = '/Program/images/unsup4.png' width = '400px'>

## SMT (Symbolic Search)
- Much progress has been made in the engineering of general-purpose symbolic
solvers for Satisfiability Modulo Theories (SMT) problems

## Applications
- Kevin Ellis, Armando Solar-Lezama, Joshua B. Tenenbaum. Unsupervised Learning by Program Synthesis. NIPS'15
- Univ of Edinburgh, Google Brain. HOUDINI: Lifelong Learning as Program Synthesis, NIPS 2018
	- Problem: lifelong learning
	- Neural libraries for lifelong learning
	- Functional programs represent deep architecture
	- Symbolic program synthesis to choose: which to re-use? put them together?
	- Differentiable, fine-tuned by gd
- **R3NN**: Emilio Parisotto, Abdel-rahman Mohamed, Rishabh Singh, Lihong Li, Dengyong Zhou, and Pushmeet Kohli. Neuro-symbolic program synthesis. ICLR'17
	- The first module, called the cross correlation I/O network, given a set of input-output examples, produces a continuous representation of the set of I/O examples. - The second module, the Recursive-Reverse-Recursive Neural Network (R3NN), given the continuous representation of the examples, synthesizes a program by incrementally expanding partial programs;
- NLP: reading comprehension:
	- Xinyun Chen, Chen Liang, Adams Wei Yu, Denny Zhou, Dawn Song, Quoc Le. Neural Symbolic Reader: Scalable Integration of Distributed and Symbolic Representations for Reading Comprehension. ICLR'20



## Unclassified
- Shao-Hua Sun, Hyeonwoo Noh, Sriram Somasundaram, and Joseph Lim. Neural program synthesis
from diverse demonstration videos. ICML'18