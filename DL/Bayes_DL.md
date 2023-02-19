# Bayesian Neural Network

## Basics
- Task:
	- Probability calibration: ECE
- Aleatoric (data) uncertainty
- Epistemic (model) uncertainty
- Steps:
	- Prior: p(w)
	- Posterior: p(w|D)
	- Prediction: Bayesian Model Averaging (BMA)
		- p(y|x,D) = ∫.w p(y|x,w)p(w|D)dw
- Posterior Approximation:
	- Laplace Approximation: MAP+Gaussian [BBB, ICML'15], tri-diagonal [KFAC, 18]
	- VI
	- MCMC
	- Geometrically Inspired Methods 
- Resources
	- Y Gal. http://bdl101.ml/
	- NIPS'19 Tutorial: Deep Learning with Bayesian Principles.
	- A Filos et al. Benchmarking Bayesian Deep Learning with Diabetic Retinopathy Diagnosis.
	- Y Gal. Uncertainty in deep learning. 2016

## Preliminaries
- Aleatoric (data) uncertainty: noise inherent in observations;
	- Can't be explained away;
	- Homoscedastic;
	- Heteroscedastic;
		- Predict output uncertainty σ(x) as well as y(x);
		- Optimize L(θ)=∑|yi-f(xi)|/2σ(xi)^2 + log(σ(xi))^2
		- MAP: single value for θ;
	- Distribution over model;
- Epistemic (model) uncertainty: uncertainty in model;
	- Can be explained away with more data;
	- Model weight with a prior (BNN);
	- Given X={x1, x2,...}, Y={y1, y2,...}, model p(W|X,Y) and p(y|fw(x));
	- Difficulty in inference: p(W|X,Y)=p(Y|X,W) | P(Y|X);
		- Approach 1: a simple q(θ) to approximate p(W|X,Y)
		- e.g. Dropout Inference;
- Combine the two: aleatoric loss;
	- output f(xi) and σ(xi);
	- Weight uncertainty and sampling with dropout;

## Bayesian NN 
- Standard Bayesian: minimizing KL(q(θ;λ), p(data|θ)p(θ))
	- argmin E.q(θ)[l(θ)] - H(q)
- PRML-5.6
- Assumptions: all Gaussian
	- Weight: w ~ N(0, α^(-1))
	- Target: p(t|x,w) ~ N(y(x,w), β^(-1)).
- Then the posterior:
	- p(w|D,α,β) ∝ p(w|α)p(D|w,β)
- w-MAP (mode) with α and β known:
	- lnp(w|D) = -α/2 w†w - β/2 ∑[y(xi-w)-ti]^2
- Build a local Gaussian for variance, then we have Gaussian approx:
	- A = -∇∇p(w|D,α,β) = αI + βH
	- q(w|D) = N(w|w.MAP, A^-1)
- Predict: p(t|x,D) = ∫p(t|x,w)q(w|D)dw
- With Taylor expansion, we have
	- y(x, w) ~ y(x, w.MAP) + g†(w-w.MAP), with g = ∇y(x,w)
	- p(t|x, w, β) ~ N(t|y(x,w), β^(-1))
	- p(t|x, w, α, β) ~ N(t|y(x,w), σ(x)^2)
		- σ(x)^2 = β^(-1) + g†A^(-1)g
- Laplace Approximation:
	- D MacKay. Bayesian interpolation. NC'92
	- D MacKay. Bayesian model comparison and backprop nets. NIPS'92
	- D MacKay. A practical Bayesian framework for backpropagation networks. NC'92
	- H Ritter, A Botev, and D Barber. A scalable laplace approximation for neural networks. ICLR'18
	- H Ritter, A Botev, and D Barber. Online structured laplace approximations for overcoming catastrophic forgetting. NeurIPS'18

## VI
- A Graves. Practical variational inference for neural networks. NIPS'11
	- VI-based: Fully factorized Gaussian posteriors which used a simple (but biased) gradient estimator;
- M Hoffman, et al. Stochastic variational inference. JMLR'13
- R Ranganath, S Gerrish, and D Blei. Black box variational inference. AISTATS'14
- A Kucukelbir, et al. Automatic differentiation variational inference. JMLR'17
- Y Yao, et al. Yes, but did it work?: Evaluating variational inference. ICML'18
- Y Wang and D Blei. Frequentist consistency of variational Bayes. JASA'19
- J Knoblauch, J Jewson, and T Damoulas. Generalized variational inference. arxiv'19
- Bounds:
	- Hernández-Lobato, J Miguel, and R Adams. Probabilistic backpropagation for scalable learning of bayesian neural networks. ICML'15
	- Hernández-Lobato, J. M., et al. Black-Box α-divergence minimization. ICML'16
	- R Ranganath, et al. Operator variational inference. NeurIPS'16
	- Y Li, and R Turner. Rényi divergence variational inference. NeurIPS'16
	- F Futami, I Sato, and M Sugiyama. Variational inference based on robust divergences. arxiv'17
	- Dieng, A Bousso, et al. Variational Inference via χ Upper Bound Minimization. NeurIPS'17
	- R Bamler, et al. Perturbative black box variational inference. NeurIPS'17
	- L Ambrogioniet al. Wasserstein variational inference. NeurIPS'18
	- A Wu, et al. Deterministic variational inference for robust bayesian neural networks. ICLR'19
	- D Tang, and R Ranganath. The Variational Predictive Natural Gradient. ICML'19
- Techniques:
	- BBB ICML'15
	- M Fortunato, C Blundell, and O Vinyals. Bayesian recurrent neural networks. WiML Workshop'17
	- F Huszár. Variational inference using implicit distributions. arXiv'17

## Dropout Inf for BNN
- Insight:
	- Dropout VI is practical in large and complex models. 
	- This inference is done by training a model with dropout before every weight layer, and by also performing dropout at test time to sample from the approximate posterior (stochastic forward passes, referred to as Monte Carlo dropout).
	- More formally, this approach is equivalent to performing approximate variational inference where we find a simple distribution q(W) in a tractable family which minimises the Kullback-Leibler (KL) divergence to the true model posterior p(W|X, Y).
	- Dropout can be interpreted as a variational Bayesian approximation, where the approximating distribution is a mixture of two Gaussians with small variances and the mean of one of the Gaussians is fixed at zero.
- D Kingma, T Salimans, and M Welling. Variational dropout and the local reparameterization trick. NIPS'15
- Y Gal and Z Ghahramani. Bayesian convolutional neural networks with Bernoulli approximate variational inference. ICLRW'16
- Y Gal and Z Ghahramani. Dropout as a Bayesian approximation: Representing model uncertainty in deep learning. ICML'16
	- SGD based;
- Y Li, and Y Gal. Dropout inference in Bayesian neural networks with α-divergences. ICML'17
- Y Gal, J Hron, A Kendall. Concrete Dropout. NIPS'17
- A Kendall, Y Gal. What Uncertainties Do We Need in Bayesian Deep Learning for Computer Vision? NIPS'17
- Hron, Jiri, A Matthews, and Z Ghahramani. Variational gaussian dropout is not bayesian. NeurIPS BDL Workshop'17
- Hron, Jiri, A Matthews, and Zoubin Ghahramani. Variational Bayesian dropout: pitfalls and fixes. ICML'18

## Prediction Uncertainty, Probability Calibration
- Resources: https://treszkai.github.io/2019/09/26/overconfidence
- Evaluation: EXPECTED CALIBRATION ERROR (ECE)
- D Nix and A Weigend. Estimating the mean and variance of the target probability distribution. Neural Networks'94
- Q Le, A Smola, and S Canu. Heteroscedastic Gaussian process regression. ICML'05
- A Niculescu-Mizil and R Caruana. Predicting good probabilities with supervised learning. ICML'05
	- Well calibrated;
- C Guo, G Pleiss, Y Sun, K Weinberger. On Calibration of Modern Neural Networks. ICML'17
	- Neural Networks are over confident;
- B Lakshminarayanan, A Pritzel, C Blundell. Simple and scalable predictive uncertainty estimation using deep ensembles. NIPS'17
- Ovadia, Y., Fertig, E., Ren, J., Nado, Z., Sculley, D., Nowozin, S., Dillon, J. V., Lakshminarayanan, B., and Snoek, J. Can you trust your model's uncertainty? evaluating predictive uncertainty under dataset shift. NIPS'19

## Optimization as VI
- Summary:
	- Gradient descent is derived using a Gaussian with fixed covariance, and estimating the mean;
	- Newton's method is derived using multivariate Gaussian;
	- RMSprop is derived using diagonal covariance;
	- Adam is derived by adding heavy-ball momentum term;
- Khan and Lin. Conjugate-computation variational inference: Converting variational inference in non-conjugate models to inferences in conjugate models. AIstats'17
- Khan, et al. Fast and scalable Bayesian deep learning by weight-perturbation in Adam. ICML'18
- W Lin, M Khan, and M Schmidt. Fast and Simple Natural-Gradient Variational Inference with Mixture of Exponential-family Approximations. ICML'19
- Khan et al., Approximate Inference Turns Deep Networks into Gaussian Processes. NIPS'19
- K Osawa, et al. Practical deep learning with bayesian principles. NeurIPS'19
- SG-MCMC:
	- Li, C., Chen, C., Carlson, D., and Carin, L. Preconditioned stochastic gradient Langevin dynamics for deep neural networks. AAAI'16
	- Leimkuhler, B., Matthews, C., and Vlaar, T. Partitioned integrators for thermodynamic parameterization of neural networks. 2019
	- Heek, J. and Kalchbrenner, N. Bayesian inference for large scale image classification. ICLR'20
	- Zhang, R., Li, C., Zhang, J., Chen, C., and Wilson, A. G. Cyclical stochastic gradient MCMC for Bayesian deep learning. ICLR'20
- F Wenzel, K Roth, B Veeling, J Swiatkowski, L Tran, S Mandt, J Snoek, T Salimans, R Jenatton, S Nowozin. How Good is the Bayes Posterior in Deep Neural Networks Really? 2020
	- Predictive performance is improved significantly through the use of a **cold posterior**;
	- T<1: sharpening posterior, overcounting data by 1/T; T=1, true Bayes posterior;
	- Model:\
		<img src="/DL/images/bnn/cold-post-1.png" alt="drawing" width="300"/>\
		<img src="/DL/images/bnn/cold-post-2.png" alt="drawing" width="300"/>
	- λ < 1 is equivalent to T < 1 (better prediction):\
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
	- Experiments: ResNet-20 on CIFAR-10 (T<1/10), CNN-LSTM on IMDB T (.01,.2);

## Approximate inference/Variational Inference for P(W|X,Y)
- C Peterson. A mean field theory learning algorithm for neural networks. 1987
- D MacKay. Probable networks and plausible predictions—a review of practical bayesian methods for supervised neural networks. 1995.
- R Neal. Bayesian learning for neural networks. PhD thesis, Citeseer, 1995.
- D Barber and C Bishop. Ensemble learning for multilayer networks. NIPS'98
- **BBB (Bayes by Backprop)**: C Blundell, J Cornebise, K Kavukcuoglu, and D Wierstra. Weight uncertainty in neural network. ICML'15
	- https://github.com/nitarshan/bayes-by-backprop
	- Variational learning of KL(q(w|θ)|p(w|D)) with KL:
		- θ = argmin KL(q|p) = KL(q(w|θ)|p(w)) - E.q[logp(D|w)]
	- VAE-style gradient estimator, improved on [Alex 2011]:
		- ∂E.q()/∂θ = E.q(ε)[∂f(w,θ)/∂w ∂w/∂θ + ∂f(w,θ)/∂θ]
	- Prior: θ wih Gaussian N(μ; ρ); Gausian **posterior** q(w|θ) (slow-convergence):\
		<img src="/DL/images/bnn/bbb3.png" alt="drawing" width="400"/>
	- Scale-mixture Gausian **prior** P(w) for faster convergence):
		- P(w) = ∏πN(wj|0,σ1^2)+(1-π)N(wj|0,σ2^2)
	- Contextual Bandits with Thompson Sampling:
		- Sample weight w ~ q(w|θ)
		- Receive the context x;
		- Pick action a to minimize E.p(r|x,a,w)[r];
		- Receive reward r;
		- Update θ;
- Modeling correlations between weights with Gaussian variational posterior:
	- C Louizos and M Welling. Structured and efficient variational deep learning with matrix Gaussian posteriors. ICML'16
	- S Sun, C Chen, and L Carin. Learning structured weight uncertainty in Bayesian neural networks. AISTATS'17
	- G Zhang, S Sun, D Duvenaud, and R Grosse. Noisy natural gradient as variational inference. ICML'18
	- J Bae, G Zhang, and R Grosse. Eigenvalue corrected noisy natural gradient. arxiv'18
- Non-Gaussian variational posterior:
	- C Louizos and M Welling. Multiplicative normalizing flows for variational Bayesian neural networks. ICML'17
	- J Shi, S Sun, and J Zhu. Kernel implicit variational inference. ICLR'18
- Decorrelate the gradients within a mini-batch for reducing variances during training:
	- D Kingma, T Salimans, and M Welling. Variational dropout and the local reparameterization trick. NIPS'15
		- Log-uniform priors;
	- C Louizos, K Ullrich, and M Welling. Bayesian compression for deep learning. NIPS'17
		- Log-uniform priors;
	- S Ghosh, J Yao, and F Doshi-Velez. Structured variational learning of Bayesian neural networks with horseshoe priors.
		- Horse shoe priors;
	- Y Wen, P Vicol, J Ba, D Tran, and R Grosse. Flipout: Efficient pseudo-independent weight perturbations on mini-batches. arxiv'18

## Unclassified
- **SWAG**: W Maddox, P Izmailov, T Garipov, D Vetrov, A Wilson. A Simple Baseline for Bayesian Uncertainty in Deep Learning. NIPS'19
	- SGD-based;
- Osawa et al. Practical Deep Learning with Bayesian Principles. NeurIPS'19
	- https://github.com/team-approx-bayes/dl-with-bayes
	- Formulation of 2nd order: make use of dμ/dλ = Hessian in exponential family dA/dλ=μ, dμ/dλ=Hessian;\
		<img src="/DL/images/bnn/bnn-opt.png" alt="drawing" width="400"/>

## Legacy on Bayesian as Optimization
- Bayesian Statistics:
	- E Jaynes. Information theory and statistical mechanics. Physical review 1957
	- A Zellner. Optimal information processing and Bayes's theorem. The American Statistician 1988
	- Bissiri, P Giovanni, C Holmes, and S Walker. A general framework for updating belief distributions. RSS: Series B 2016
- Online-learning (Exponential Weight Aggregates)
	- Cesa-Bianchi, Nicolo, and Gabor Lugosi. Prediction, learning, and games. 2006.
- Free-energy principle:
	- Friston, K. The free-energy principle: a unified brain theory? Nature neuroscience (2010)

## Posterior Approximations
- Hinton, G. and Van Camp, D. Keeping neural networks simple by minimizing the description length of the weights. COLT'93
- Entropy-regularized/Maximum-entropy RL:
	- R Williams and J Peng. Function optimization using connectionist reinforcement learning algorithms. Connection Science 3.3 (1991): 241-268
	- Ziebart, Brian D. Modeling purposeful adaptive behavior with the principle of maximum causal entropy. Diss. figshare, 2010. (see chapter 5)

## Functional Priors
- D Flam-Shepherd, J Requeima, and D Duvenaud. Mapping Gaussian process priors to Bayesian neural networks. NIPSW'17
- D Hafner, D Tran, A Irpan, T Lillicrap, and J Davidson. Reliable uncertainty estimates in deep neural networks using noise contrastive priors. arxiv'18
- **NP**: M. Garnelo, J. Schwarz, D. Rosenbaum, F. Viola, D. J. Rezende, S. M. A. Eslami, and Y. Whye Teh. Neural processes. arxiv'18
- **VIP**: C Ma, Y Li, and J Hernández-Lobato. Variational implicit processes. arxiv'18
	- Reverse of fBNNs: they specify BNN priors and use GPs to approximate the posterior
- **FNP**: C Louizos, X Shi, K Schutte, M Welling. The Functional Neural Process. NIPS'19
	- inference over the weights of a neural network can be a daunting task due to the high dimensionality and posterior complexity
	- "bypass" the aforementioned issues is that of adopting a stochastic process, like GP;
	- https://github.com/AMLab-Amsterdam/FNP
- **fBNN**: S Sun, G Zhang, J Shi, R Grosse. Functional Variational Bayesian Neural Networks. ICLR'19
