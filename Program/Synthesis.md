# Program Synthesis

## Basics
- Problem definition: Input/Output examples -> Program

## Unclassified
- **Robustfill**: Jacob Devlin, Jonathan Uesato, Surya Bhupatiraju, Rishabh Singh, Abdel-rahman Mohamed, and Pushmeet Kohli. Robustfill: Neural program learning under noisy i/o. ICML'17
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

## Unclassified
- Shao-Hua Sun, Hyeonwoo Noh, Sriram Somasundaram, and Joseph Lim. Neural program synthesis
from diverse demonstration videos. ICML'18