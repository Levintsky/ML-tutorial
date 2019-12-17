# Procedural Modeling

## Problem Definition
- Generate something with grammar

## Legacy
- **CGA**: Pascal Müller, Peter Wonka, Simon Haegler, Andreas Ulmer, Luc Van Gool. Procedural Modeling of Buildings. SIGGRAPH'06

## ML based
- **NGPM**: Daniel Ritchie, Anna Thomas, Pat Hanrahan, Noah Goodman. Neurally-Guided Procedural Models: Amortized Inference for Procedural Graphics Programs using Neural Networks. NIPS 2016
	- https://github.com/dritchie/adnn
- Kevin Ellis, Daniel Ritchie, Armando Solar-Lezama, Josh Tenenbaum. Learning to Infer Graphics Programs from Hand-Drawn Images, NIPS 2018
	- Noisy input (data augmentation)
	- Combining NGPM [4] and Attend-Infer-Repeat [5]
	- Learn a loss function?
	- DSL [11]
	- Prefer shorter program (with explicit reward)
	- Sketch-tool [1] to refine program