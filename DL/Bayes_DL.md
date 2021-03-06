# Bayesian Neural Network

## Basics
- Task:
	- Aleatoric (data) uncertainty : noise inherent in observations;
		- Can't be explained away;
		- Homoscedastic;
		- Heteroscedastic;
			- Predict output uncertainty sigma(x) as well as y(x);
			- Optimize L(theta)=sum|yi-f(xi)|/2sig(xi)^2 + log(sig(xi))^2
			- MAP: single value for theta;
		- Distribution over model;
	- Epistemic (model) uncertainty: uncertainty in model;
		- Can be explained away with more data;
		- Model weight with a prior (BNN);
		- Given X={x1, x2,...}, Y={y1, y2,...}, model p(W|X,Y) and p(y|fw(x));
		- Difficulty in inference: p(W|X,Y)=p(Y|X,W) | P(Y|X);
			- Approach 1: a simple q(theta) to approximate p(W|X,Y)
			- e.g. Dropout Inference;
	- Combine the two: aleatoric loss;
		- output f(xi) and sigma(xi);
		- Weight uncertainty and sampling with dropout;
- Resources
	- Yarin Gal. http://bdl101.ml/
	- NIPS'19 Tutorial: Deep Learning with Bayesian Principles.

## Output Uncertainty
- David A Nix and Andreas S Weigend. Estimating the mean and variance of the target probability distribution. Neural Networks'94
- Quoc V Le, Alex J Smola, and Stephane Canu. Heteroscedastic Gaussian process regression. ICML'05
- Lakshminarayanan, B., Pritzel, A., and Blundell, C. Simple and scalable predictive uncertainty estimation using deep ensembles. NIPS'17
- Ovadia, Y., Fertig, E., Ren, J., Nado, Z., Sculley, D., Nowozin, S., Dillon, J. V., Lakshminarayanan, B., and Snoek, J. Can you trust your model's uncertainty? evaluating predictive uncertainty under dataset shift. NIPS'19

## Approximate inference/Variational Inference for P(W|X,Y)
- C Peterson. A mean field theory learning algorithm for neural networks. 1987
- David JC MacKay. Probable networks and plausible predictions—a review of practical bayesian methods for supervised neural networks. Network: Computation in Neural Systems, 6(3):469–505, 1995.
- Radford M Neal. Bayesian learning for neural networks. PhD thesis, Citeseer, 1995.
- Barber, D. and Bishop, C. M. Ensemble learning for multilayer networks. NIPS'98
- A Graves. Practical variational inference for neural networks. NIPS'11
	- VI-based: Fully factorized Gaussian posteriors which used a simple (but biased) gradient estimator;
- **BBB (Bayes by Backprop)**: C Blundell, J Cornebise, K Kavukcuoglu, and D Wierstra. Weight uncertainty in neural network. ICML'15
	- Insight: VI-based; treat weight w as distribution rather than point; Bayesian treatment: p(y|x)=E_p(w|D)[p(y|x,w)]
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
- Jose Miguel Hernandez-Lobato, Yingzhen Li, Daniel Hernandez-Lobato, Thang Bui, and Richard E Turner. Black-box alpha divergence minimization. ICML'16
- Modeling correlations between weights with Gaussian variational posterior:
	- C Louizos and M Welling. Structured and efficient variational deep learning with matrix Gaussian posteriors. ICML'16
	- S Sun, C Chen, and L Carin. Learning structured weight uncertainty in Bayesian neural networks. AISTATS'17
	- G Zhang, S Sun, D Duvenaud, and R Grosse. Noisy natural gradient as variational inference. ICML'18
	- J Bae, G Zhang, and R Grosse. Eigenvalue corrected noisy natural gradient. arxiv'18
- Non-Gaussian variational posterior:
	- C Louizos and M Welling. Multiplicative normalizing flows for variational Bayesian neural networks. ICML'17
	- J Shi, S Sun, and J Zhu. Kernel implicit variational inference. ICLR'18
- Dropout Inf for BNN:
	- Insight:
		- Dropout variational inference is a practical approach for approximate inference in large and complex models. 
		- This inference is done by training a model with dropout before every weight layer, and by also performing dropout at test time to sample from the approximate posterior (stochastic forward passes, referred to as Monte Carlo dropout).
		- More formally, this approach is equivalent to performing approximate variational inference where we find a simple distribution q(W) in a tractable family which minimises the Kullback-Leibler (KL) divergence to the true model posterior p(W|X, Y).
		- Dropout can be interpreted as a variational Bayesian approximation, where the approximating distribution is a mixture of two Gaussians with small variances and the mean of one of the Gaussians is fixed at zero.
	- Yarin Gal and Zoubin Ghahramani. Bayesian convolutional neural networks with Bernoulli approximate variational inference. ICLRW'16
	- Y Gal and Z Ghahramani. Dropout as a Bayesian approximation: Representing model uncertainty in deep learning. ICML'16
		- SGD based;
	- Y Gal, J Hron, A Kendall. Concrete Dropout. NIPS'17
	- Alex Kendall, Yarin Gal. What Uncertainties Do We Need in Bayesian Deep Learning for Computer Vision? NIPS'17
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
- Various optimizers as Bayesian:
	- Summary:
		- Gradient descent is derived using a Gaussian with fixed covariance, and estimating the mean;
		- Newton’s method is derived using multivariate Gaussian;
		- RMSprop is derived using diagonal covariance;
		- Adam is derived by adding heavy-ball momentum term;
	- Khan and Lin. Conjugate-computation variational inference: Converting variational inference in non-conjugate models to inferences in conjugate models. AIstats'17
	- Khan, et al. Fast and scalable Bayesian deep learning by weight-perturbation in Adam. ICML'18
	- Lin, Wu, Mohammad Emtiyaz Khan, and Mark Schmidt. Fast and Simple Natural-Gradient Variational Inference with Mixture of Exponential-family Approximations. ICML'19
	- Khan et al., Approximate Inference Turns Deep Networks into Gaussian Processes. NIPS'19
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

## Unclassified
- Ritter et al. A scalable laplace approximation for neural networks. 2018
	- SGD-based;
- **SWAG**: Wesley J Maddox, Pavel Izmailov, Timur Garipov, Dmitry Vetrov, Andrew Gordon Wilson. A Simple Baseline for Bayesian Uncertainty in Deep Learning. NIPS'19
	- SGD-based;
- Osawa et al. Practical Deep Learning with Bayesian Principles. NeurIPS'19
	- https://github.com/team-approx-bayes/dl-with-bayes
	- Formulation of 2nd order: make use of dmu/dlambda = Hessian in exponential family dA/dLambda=mu, dmu/dLambda=Hessian;\
		<img src="/DL/images/bnn/bnn-opt.png" alt="drawing" width="400"/>

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

## Legacy on Bayesian as Optimization
- Formulation: can be derived by minimizing KL(q(theta\|lambda), p(data\|theta)p(theta))\
	<img src="/DL/images/bnn/bayes-opt-1.png" alt="drawing" width="300"/>
- Bayesian Statistics:
	- Jaynes, Edwin T. Information theory and statistical mechanics. Physical review 1957
	- Zellner, A. Optimal information processing and Bayes's theorem. The American Statistician 1988
	- Bissiri, Pier Giovanni, Chris C. Holmes, and Stephen G. Walker. A general framework for updating belief distributions. RSS: Series B (Statistical Methodology) (2016)
- PAC-Bayes:
	- Shawe-Taylor, John, and Robert C. Williamson. A PAC analysis of a Bayesian estimator. COLT'97
	- Alquier, Pierre. PAC-Bayesian bounds for randomized empirical risk minimizers. Mathematical Methods of Statistics 17.4 (2008): 279-304.
- Online-learning (Exponential Weight Aggregates)
	- Cesa-Bianchi, Nicolo, and Gabor Lugosi. Prediction, learning, and games. 2006.
- Free-energy principle:
	- Friston, K. The free-energy principle: a unified brain theory? Nature neuroscience (2010)

## Posterior Approximations
- Formulation:\
	<img src="/DL/images/bnn/bayes-opt-2.png" alt="drawing" width="300"/>
- Hinton, G. and Van Camp, D. Keeping neural networks simple by minimizing the description length of the weights. COLT'93
- Entropy-regularized/Maximum-entropy RL:
	- Williams, Ronald J., and Jing Peng. Function optimization using connectionist reinforcement learning algorithms. Connection Science 3.3 (1991): 241-268
	- Ziebart, Brian D. Modeling purposeful adaptive behavior with the principle of maximum causal entropy. Diss. figshare, 2010. (see chapter 5)

## Functional Priors
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
