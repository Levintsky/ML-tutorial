# Generative Models

## Benchmark
- **Omniglot**
	- Lake, B. M., Salakhutdinov, R., and Tenenbaum, J. B. Human-level concept learning through probabilistic program induction. Science, 2015.
	- Lake, B. M., Ullman, T. D., Tenenbaum, J. B., and Gershman, S. J. Building machines that learn and think like people. Behavioral and Brain Sciences, 40, 2017.

## Recurrent, Progressive	
- Greg Mori. Probabilistic Neural Programmed Networks for Scene Generation, NIPS 2018
	- Input: text-based programs
    - Output: rendered images
    - PNP-Net

## Recurrent, Sequential, Order-Aware
- D. Ha. Recurrent Net Dreams Up Fake Chinese Characters in Vector Format with TensorFlow, 2015
- **sketch-RNN**: Ha, D. and Eck, D. A neural representation of sketch drawings. ICLR'18
	- https://magenta.tensorflow.org/sketch_rnn
	- QuickDrow dataset: https://quickdraw.withgoogle.com/
		- 70k training, 2.5k val, 2.5k test
	- A sketch is a lit of point (dx, dy, p1, p2, p3), p1: touching, p2: lifted, p3: end
	- Model: seq-2-seq-VAE [2, 15]
	- **Encoder**: bidirectional-RNN, concatenated as h, output mean and variance
	- then output z with reparametrization trick;
	- **Decoder**: S0=[0,0,1,0,0], a x, y ~ GMM trained together
	- Loss:
		- Reconstruction loss: Ls for (dx, dy)
		- Lp for (p1, p2, p3)
		- KL: z with zero-mean, unit-variance Gaussian
- Xie, N., Hachiya, H., and Sugiyama, M. Artist agent: A reinforcement learning approach to automatic stroke generation in oriental ink painting. ICML 2012
	- Ink Painting.
	- Brush as an agent. Train with REINFORCE.
	- Search space: 6-dim.
	- Immediate reward: smoothness

## DeepMind
- **DRAW**: K. Gregor, I. Danihelka, A. Graves, D. Jimenez Rezende, D. Wierstra. DRAW: A Recurrent Neural Network For Image Generation. ICML 2015
	- https://github.com/ericjang/draw
	- https://github.com/chenzhaomin123/draw_pytorch
- Karol Gregor, Frederic Besse, Danilo Jimenez Rezende, Ivo Danihelka, and Daan Wierstra. Towards conceptual compression. NIPS 2016.
	- Convolutional DRAW.
	- Two RNN: one encoder, one decoder;
	- Compression: best reconstruction given budget
	- VAE loss for regularization
	- Step-by-step refine
- **SPRIAL**. Y. Ganin, T. Kulkarni, Igor Babuschkin, S. M. Ali Eslami, Oriol Vinyals. SPIRAL: Synthesizing Programs for Images using Reinforced Adversarial Learning. ICML'18
- **NPI**:  Scott Reed and Nando de Freitas. Neural programmer-interpreters. ICLR'16
- **AIR**: Attend, Infer, Repeat: Fast Scene Understanding with Generative Models. NIPS 2016
	- An RNN to handle multiple-object (variable length)
	- Latent variable z to describe if there is new object or not
	- Monte Carlo sampling
- Sequential Attend, Infer, Repeat: Generative Modelling of Moving Objects, NIPS 2018
- **Sketch**:
	- Image-to-Markup Generation with Coarse-to-Fine Attention. ICML 2017
