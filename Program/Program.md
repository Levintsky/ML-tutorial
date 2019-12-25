# Program Synthesis

## Translation
- Tree-to-tree Neural Networks for Program Translation (Berkeley), NIPS 2018
	- Each language to parse tree as IR (intermediate representation);
	- Learn mapping function with tree-to-tree network;
	- Tree encoder for source language with Tree-LSTM;
	- Decoder: (1) attention; (2) source encoding; (3) combined encoding; (4) argmax + softmax;

## Applications: regard a problem as program synthesis
- Univ of Edinburgh, Google Brain. HOUDINI: Lifelong Learning as Program Synthesis, NIPS 2018
	- Problem: lifelong learning
	- Neural libraries for lifelong learning
	- Functional programs represent deep architecture
	- Symbolic program synthesis to choose: which to re-use? put them together?
	- Differentiable, fine-tuned by gd

## Input/Output examples -> Program
- L Zhang, G Rosenblatt, E Fetaya, R Liao, W Byrd, M Might, R Urtasun, R Zemel. Neural Guided Constraint Logic Programming for Program Synthesis, NIPS'18
	- https://github.com/xuexue/neuralkanren
	- Input: input/output examples
	- miniKanren as symbolic system
	- ML propose candidates program satisfying the candidates
- A Zohar, L Wolf. Automatic Program Synthesis of Long Programs with a Learned Garbage Collector, NIPS'18
	-  https://github.com/amitz25/PCCoder
	- Predict statement by statement
	- Garbage collection (things can be discarded)
	- Dynamic input
	- Prediction guided search

## Misc
- D Tran, M Hoffman, D Moore, C Suter, S Vasudevan, A Radul, M Johnson, R Saurous. Simple, Distributed, and Accelerated Probabilistic Programming. NIPS'18
- **Memory Augmented Policy Optimization for Program Synthesis and Semantic Parsing (Chen Liang)**
- Backpropagation with Callbacks: Foundations for Efficient and Expressive Differentiable Programming
- Autoconj: Recognizing and Exploiting Conjugacy Without a Domain-Specific Language
- K Ellis, L Morales, M Sablé-Meyer, A Solar-Lezama, J Tenenbaum. Learning Libraries of Subroutines for Neurally–Guided Bayesian Program Induction, NIPS'18
	- DSL (Domain specific language)
    - Program search: neural network
    - EC2 (ECC, for Explore/Compress/Compile)
- DeepProbLog: Neural Probabilistic Logic Programming
- **Improving Neural Program Synthesis with Inferred Execution Traces (Dawn Song)**
- Le Song, Learning Loop Invariants for Program Verification, NIPS 2018
	- A structured external memory representation which encodes the program; a Graph-Neural-Network;
	- A multi-step autoregressive model for incremental loop invariant construction; MDP;
	- An attention component that mimics the varying focus in each step.
	- Reinforcement learning with A2C;
	- https://github.com/PL-ML/code2inv
