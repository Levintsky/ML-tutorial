# Bayesian Neural Network

## Legacy
- C Peterson. A mean field theory learning algorithm for neural networks. 1987
- G Hinton and D Camp. Keeping the neural networks simple by minimizing the description length of the weights. COLT'93

## Unclassified
- A Simple Baseline for Bayesian Uncertainty in Deep Learning. NIPS'19

## Bayesian NN (PRML Chapter 5.6)
- Assumptions: 2 Gaussian, weight w ~ N(0, alpha^(-1)), p(t\|x,w) ~ N(y(x,w), beta^(-1)). Then the posterior:
	<img src="/DL/images/bnn/bnn-bishop-1.png" alt="drawing" width="300"/>
- w-MAP (mode) can be found if alpha and beta known:
	<img src="/DL/images/bnn/bnn-bishop-2.png" alt="drawing" width="450"/>
- Build a local Gaussian for variance, then we have Gaussian approx:
	<img src="/DL/images/bnn/bnn-bishop-3.png" alt="drawing" width="400"/>
	<img src="/DL/images/bnn/bnn-bishop-4.png" alt="drawing" width="400"/>
- Predict:\
	<img src="/DL/images/bnn/bnn-bishop-5.png" alt="drawing" width="400"/>
- With Taylor expansion, we have\
	<img src="/DL/images/bnn/bnn-bishop-6.png" alt="drawing" width="450"/>
	<img src="/DL/images/bnn/bnn-bishop-7.png" alt="drawing" width="450"/>
	<img src="/DL/images/bnn/bnn-bishop-8.png" alt="drawing" width="450"/>

## Variational Inference
- Hinton, G. and Van Camp, D. Keeping neural networks simple by minimizing the description length of the weights. COLT'93
- David JC MacKay. Probable networks and plausible predictions—a review of practical bayesian methods for supervised neural networks. Network: Computation in Neural Systems, 6(3):469–505, 1995.
- Radford M Neal. Bayesian learning for neural networks. PhD thesis, Citeseer, 1995.
- Barber, D. and Bishop, C. M. Ensemble learning for multilayer networks. NIPS'98
- A Graves. Practical variational inference for neural networks. NIPS'11
	- fully factorized Gaussian posteriors which used a simple (but biased) gradient estimator
- **BBB (Bayes by Backprop)**: C Blundell, J Cornebise, K Kavukcuoglu, and D Wierstra. Weight uncertainty in neural network. ICML'15
	- Insight: treat weight w as distribution rather than point; Bayesian treatment: p(y|x)=E_p(w|D)[p(y|x,w)]
	- Code links: https://github.com/nitarshan/bayes-by-backprop
	- Variational learning of q(w|theta) to approximate p(w|D) with KL:\
		<img src="/DL/images/bnn/bbb1.png" alt="drawing" width="400"/>
	- Improved on [Alex 2011] with an unbiased gradient estimator using the reparameterization trick (VAE):\
		<img src="/DL/images/bnn/bbb2.png" alt="drawing" width="400"/>
	- Prior: theta wih Gaussian N(mu; rho); Gausian **posterior** q(w|theta) (slow-convergence):\
		<img src="/DL/images/bnn/bbb3.png" alt="drawing" width="400"/>
	- Scale-mixture Gausian **prior** P(w) for weight, Gaussian prior for bias (to solve slow-convergence):\
		<img src="/DL/images/bnn/bbb4.png" alt="drawing" width="400"/>
	- Contextual Bandits with Thompson Sampling:\
		<img src="/DL/images/bnn/bbb5.png" alt="drawing" width="400"/>
- Modeling correlations between weights with Gaussian variational posterior:
	- C Louizos and M Welling. Structured and efficient variational deep learning with matrix Gaussian posteriors. ICML'16
	- S Sun, C Chen, and L Carin. Learning structured weight uncertainty in Bayesian neural networks. AISTATS'17
	- G Zhang, S Sun, D Duvenaud, and R Grosse. Noisy natural gradient as variational inference. ICML'18
	- J Bae, G Zhang, and R Grosse. Eigenvalue corrected noisy natural gradient. arxiv'18
- Non-Gaussian variational posterior:
	- C Louizos and M Welling. Multiplicative normalizing flows for variational Bayesian neural networks. ICML'17
	- J Shi, S Sun, and J Zhu. Kernel implicit variational inference. ICLR'18
- Dropout as BNN:
	- Y Gal and Z Ghahramani. Dropout as a Bayesian approximation: Representing model uncertainty in deep learning. ICML'16
	- Y Gal, J Hron, A Kendall. Concrete Dropout. NIPS'17
- Decorrelate the gradients within a mini-batch for reducing variances during training:
	- D Kingma, T Salimans, and M Welling. Variational dropout and the local reparameterization trick. NIPS'15
		- Log-uniform priors;
	- C Louizos, K Ullrich, and M Welling. Bayesian compression for deep learning. NIPS'17
		- Log-uniform priors;
	- Soumya Ghosh, Jiayu Yao, and Finale Doshi-Velez. Structured variational learning of Bayesian neural networks with horseshoe priors.
		- Horse shoe priors;
	- Y Wen, P Vicol, J Ba, D Tran, and R Grosse. Flipout: Efficient pseudo-independent weight perturbations on mini-batches. arxiv'18
- SG-MCMC:
	- Li, C., Chen, C., Carlson, D., and Carin, L. Preconditioned stochastic gradient Langevin dynamics for deep neural networks. AAAI'16
	- Leimkuhler, B., Matthews, C., and Vlaar, T. Partitioned integrators for thermodynamic parameterization of neural networks. 2019
	- Heek, J. and Kalchbrenner, N. Bayesian inference for large scale image classification. ICLR'20
	- Zhang, R., Li, C., Zhang, J., Chen, C., and Wilson, A. G. Cyclical stochastic gradient MCMC for Bayesian deep learning. ICLR'20
- Florian Wenzel, Kevin Roth, Bastiaan S. Veeling, Jakub Swiatkowski, Linh Tran, Stephan Mandt, Jasper Snoek, Tim Salimans, Rodolphe Jenatton, Sebastian Nowozin. How Good is the Bayes Posterior in Deep Neural Networks Really? 2020
	- Predictive performance is improved significantly through the use of a **cold posterior**;
	- T<1: sharpening posterior, overcounting data by 1/T; T=1, true Bayes posterior;
	- Model:\
		<img src="/DL/images/bnn/cold-post-1.png" alt="drawing" width="300"/>\
		<img src="/DL/images/bnn/cold-post-2.png" alt="drawing" width="300"/>
	- lambda < 1 is equivalent to T < 1 (better prediction):\
		<img src="/DL/images/bnn/cold-post-3.png" alt="drawing" width="300"/>
	- Posterior using Langevin Dynamics:\
		<img src="/DL/images/bnn/cold-post-4.png" alt="drawing" width="400"/>
	- SG-MCMC (mini-batch), following Welling'11, SGHMC Chen'14\
		<img src="/DL/images/bnn/cold-post-5.png" alt="drawing" width="400"/>\
		<img src="/DL/images/bnn/cold-post-6.png" alt="drawing" width="400"/>\
		<img src="/DL/images/bnn/cold-post-7.png" alt="drawing" width="400"/>
	- Accurate SG-MCMC: 1. dU minibatch is unbiased with variance; 2. discretization error;
		- Layerwise-Preconditioning: M
		- Cyclical time stepping: step-size cycles; (cosine schedule following Zhang);
	- Algorithm:\
		<img src="/DL/images/bnn/cold-post-8.png" alt="drawing" width="400"/>
	- Experiments: ResNet-20 on CIFAR-10 (T<1/10), CNN-LSTM on IMDB (.01<T<.2);

## Functional Priors:
- D Flam-Shepherd, J Requeima, and D Duvenaud. Mapping Gaussian process priors to Bayesian neural networks. NIPSW'17
- D Hafner, D Tran, A Irpan, T Lillicrap, and J Davidson. Reliable uncertainty estimates in deep neural networks using noise contrastive priors. arxiv'18
- **NP**: M. Garnelo, J. Schwarz, D. Rosenbaum, F. Viola, D. J. Rezende, S. M. A. Eslami, and Y. Whye Teh. Neural processes. arxiv'18
- **VIP**: C Ma, Y Li, and J Hernández-Lobato. Variational implicit processes. arxiv'18
	- Reverse of fBNNs: they specify BNN priors and use GPs to approximate the posterior
- **FNP**: Christos Louizos, Xiahan Shi, Klamer Schutte, Max Welling. The Functional Neural Process. NIPS'19
	- inference over the weights of a neural network can be a daunting task due to the high dimensionality and posterior complexity
	- "bypass" the aforementioned issues is that of adopting a stochastic process, like GP;
	- https://github.com/AMLab-Amsterdam/FNP
- **fBNN**: S Sun, G Zhang, J Shi, R Grosse. Functional Variational Bayesian Neural Networks. ICLR'19

## Prediction Uncertainty
- Lakshminarayanan, B., Pritzel, A., and Blundell, C. Simple and scalable predictive uncertainty estimation using deep ensembles. NIPS'17
- Ovadia, Y., Fertig, E., Ren, J., Nado, Z., Sculley, D., Nowozin, S., Dillon, J. V., Lakshminarayanan, B., and Snoek, J. Can you trust your model’s uncertainty? evaluating predictive uncertainty under dataset shift. NIPS'19