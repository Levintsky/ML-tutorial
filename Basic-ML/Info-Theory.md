# Information Theory in Machine Learning

## Books
- David JC MacKay. Information theory, inference and learning algorithms. Cambridge university press, 2003.

## Classical
- **IB**: N. Tishby, F.C. Pereira, and W. Biale. The information bottleneck method. Allerton'99
- William Bialek, Ilya Nemenman, and Naftali Tishby. Predictability, complexity, and learning. Neural computation'01
- Susanne Still and William Bialek. How many clusters? an information-theoretic perspective. Neural computation'04
- David Barber Felix Agakov. The IM algorithm: a variational approach to information maximization. NIPS'04
- Noam Slonim, Gurinder Singh Atwal, Gasˇper Tkacˇik, and William Bialek. Information-based clustering. PNAS'05
- Ohad Shamir, Sivan Sabato, and Naftali Tishby. Learning and generalization with the information bottleneck. Theoretical Computer Science'10
- Stephanie E Palmer, Olivier Marre, Michael J Berry, and William Bialek. Predictive information in a sensory population. PNAS'15

## Deep Learning
- N. Tishby and N. Zaslavsky. Deep learning and the information bottleneck principle. In IEEE Information Theory Workshop, 2015
- Alessandro Achille and Stefano Soatto. Information dropout: Learning optimal representations through noisy computation. 2016.
- **DVIB**: A Alemi, I. Fischer, J V. Dillon, K Murphy. Deep Variational Information Bottleneck. ICLR'17
	- Formulation:\
		<img src="/Basic-ML/images/info-theory/dvib-1.png" alt="drawing" width="450"/>
	- The first term in RIB encourages Z to be predictive of Y;
	- The second term encourages Z to "forget" X;
	- Essentially it forces Z to act like a minimal sufficient statistic of X for predicting Y;
	- Formulation: we assume p(Z|X,Y) = p(Z|X), corresponding to the Markov chain Y ↔ X ↔ Z. This restriction means that our representation Z cannot depend directly on the labels Y. This opens the door to **unsupervised representation learning**;
	- I(z;y) lower-bound:\
		<img src="/Basic-ML/images/info-theory/dvib-2.png" alt="drawing" width="450"/>
	- I(z;x) upper-bound:\
		<img src="/Basic-ML/images/info-theory/dvib-3.png" alt="drawing" width="450"/>
	- Put together:\
		<img src="/Basic-ML/images/info-theory/dvib-4.png" alt="drawing" width="450"/>
	- Results on mnist: different classes;\
		<img src="/Basic-ML/images/info-theory/dvib-5.png" alt="drawing" width="450"/>
	- Connection with VAE: no Y, just index i=1/N, each item a class, then:\
		<img src="/Basic-ML/images/info-theory/dvib-6.png" alt="drawing" width="450"/>
- Gabriel Pereyra, George Tuckery, Jan Chorowski, and Lukasz Kaiser. Regularizing neural net- works by penalizing confident output predictions. ICLRW'17
- Theory on DL:
	- R. Shwartz-Ziv and N. Tishby. Opening the black box of deep neural networks via information. arXiv preprint arXiv:1703.00810, 2017
		- Deep networks undergo two distinct phases consisting of an initial fitting phase and a subsequent compression phase;
		- the compression phase is causally related to the excellent generalization performance of deep networks; 
		- the compression phase occurs due to the diffusion-like behavior of stochastic gradient descen
	- Andrew Michael Saxe, Yamini Bansal, Joel Dapello, Madhu Advani, Artemy Kolchinsky, Brendan Daniel Tracey, David Daniel Cox. On the Information Bottleneck Theory of Deep Learning. ICLR'18
