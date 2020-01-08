# Program Synthesis

## Program Translation
- Xinyun Chen, Chang Liu, Dawn Song. Tree-to-tree Neural Networks for Program Translation, NIPS 2018
	- Each language to parse tree as IR (intermediate representation);
	- Learn mapping function with tree-to-tree network;
	- Tree encoder for source language with Tree-LSTM;
	- Decoder: (1) attention; (2) source encoding; (3) combined encoding; (4) argmax + softmax;

## Execution
- **NPI**: Scott Reed and Nando De Freitas. Neural programmer-interpreters. ICLR'16
- Matko Bosnjak, Tim Rocktaschel, Jason Naradowsky, Sebastian Riedel. Programming with a Differentiable Forth Interpreter. ICML'17
- Jonathon Cai, Richard Shin, and Dawn Song. Making neural programming architectures generalize via recursion. ICLR'17

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
