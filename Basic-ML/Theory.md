# Learining Theory

## Resources
- Shai Shalev-Shwartz and Shai Ben-David. Understanding Machine Learning- From Theory to Algorithms. 2014

## PAC Basics
- Generalization error: E(h, D)
- Empirical error: E^(h,D)
- Inequalities:
	- Jensen: f() convex, then f(E(x)) <= E(f(x))
	- Hoeffding: m sample, P(|E^x-Ex|>=eps) <= exp(-2m eps^2)
	- McDiarmid: suppose sup|f(x1,..xi,..)-f(x1,..xi',..)|<=c, then p(|f(x)-f(xi')|>=eps)<=exp(-2eps^2/sum_i(ci^2))
- Algorithm: L
- Concept: C: X to Y;
- Mapping: h: X to Y;
- Hypothesis space: H, containing all h;
- Separable/consistent: all correct
- Non-separable/consistent:
- PAC-identify: 0 < eps, delta < 1, P(E(h)<=eps)>=1-delta, then L can identify concept C from H;
- PAC-learnable: exist algorithm L, poly s.t. m>=poly(1/eps, 1/delta, |x|, |c|), L can PAC-identify C;
	- Insight: L can identify C, with error at most eps, with prob 1-delta;
- PAC-learning algirthm;
- Sample Compexity: minimum m, s.t. m>=poly();
- Case 1: separable:
	- m >= (ln|H| + ln(1/delta))/eps, O(1/m) convergence;
	- Intuition, a bad h() with generalization error > eps, but do well on training set is at most exp(-m eps);
- Case 2: non-separable:
	- p(E^(h)-E(h)>=eps)<= exp(-2m eps^2) (Hoeffding)
	- Agnostic PAC learnable: suppose h' best in hypothesis space, then L can learn P(E(h)-E(h')<=eps)>=1-delta;
- VC-dimension:
	- Growth function: all number of possibilities pi(H,m)=max{|(h(x1),...,h(xm)|h in H}
	- Dichotomy:
	- Shattering: m samples, at most 2^m possibilites. Every assignment: dichotomy, pi(H,m)=2^m, then D is shattered;
	- VC-dim: max m s.t. pi(H,m)=2^m;
	- Theorem: VC(H)=d, then P(E(h)-E^(h)) has a bound;
	- VC dimentionality is **distribution independent**;
- Rademacher complexity:
	- A tighter bound (distribution dependent);
	- Given z1, ..., zm, E_sig (sup_h (sig1 h(x1)+sig2 h(x2)+...)/m), where sig is a random variable half +1, half -1;
- Stability:
	- Three costs: l(L,D) generalization; l^(L,D) empirical; l(L,D-i) leave-one-out;
	- beta-uniform stability: |l(L,D)-l(L,D-i)| <= beta;
	- ERM (empirical-risk-minimization)
	- Theorem: algorithm L ERM and beta-stable, then hypothesis H learnable;

## PAC-Bayes
- Currently the best theory to explain NN generalization;
- Legacy:
	- Shawe-Taylor J, Williamson R C. A PAC analysis of a Bayesian estimator[C]//Proceedings of the tenth annual conference on Computational learning theory. ACM, 1997
	- David McAllester. Some PAC-Bayesian theorems. COLT'98
		- Concept space observes any distribution D;
		- Prior in hypothesis space H;
		- Measure of C and H space;
		- U: a subspace of H;
		- P(E(U)<=...)>=1-delta; E(U) is generalization error;
	- David McAllester. Some PAC-Bayesian theorems. Machine Learning'99
		- First paper on PAC-Bayes;
	- McAllester D A. PAC-Bayesian model averaging. COLT'99
	- McAllester D A. PAC-Bayesian stochastic model selection. Machine Learning'03
	- Seeger M. Pac-bayesian generalisation error bounds for gaussian process classification. JMLR'03
	- Shawe-Taylor J, Langford J. PAC-Bayes & margins. NIPS'03
	- Langford J. Tutorial on practical prediction theory for classification. JMLR'05
	- Germain P, Lacasse A, Laviolette F, et al. PAC-Bayesian learning of linear classifiers. ICML'09
	- Catoni O. PAC-Bayesian supervised classification: the thermodynamics of statistical learning. arxiv'07
- For NN:
	- PL Bartlett, DJ Foster, MJ Telgarsky. Spectrally-normalized margin bounds for neural networks. NIPS'17
	- N Golowich, A Rakhlin, O Shamir. Size-independent sample complexity of neural networks
	- Behnam Neyshabur, Srinadh Bhojanapalli, Nathan Srebro. A pac-bayesian approach to spectrally-normalized margin bounds for neural networks. ICLR'18
	- Y Li, Y Liang. Learning overparameterized neural networks via stochastic gradient descent on structured data. NIPS'18
	- R Novak, Y Bahri, DA Abolafia, J Pennington. Sensitivity and generalization in neural networks: an empirical study. arxiv'18
	- Z Allen-Zhu, Y Li, Y Liang. Learning and generalization in overparameterized neural networks, going beyond two layers. NIPS'19

## Mixture
- Nearly tight sample complexity bounds for learning mixtures of Gaussians via sample compression schemes

## Optimization
- Chi Jin, Lydia T. Liu, Rong Ge, Michael I. Jordan. On the Local Minima of the Empirical Risk. NIPS'18

## Unclassified
- Why Is My Classifier Discriminatory? NIPS'18

## NIPS'19 Learning Theory
- Fengxiang He, Tongliang Liu, Dacheng Tao. Control Batch Size and Learning Rate to Generalize Well: Theoretical and Empirical Evidence
- Colin Wei, Tengyu Ma. Data-dependent Sample Complexity of Deep Neural Networks via Lipschitz Augmentation
- Kevin Bello, Jean Honorio. Exact inference in structured prediction
- Bryon Aragam, Arash Amini, Qing Zhou. Globally optimal score-based learning of directed acyclic graphs in high-dimensions
- Sushrut Karmalkar, Adam Klivans, Pravesh Kothari. List-decodable Linear Regression
- Chenri Ni, Nontawat Charoenphakdee, Junya Honda, Masashi Sugiyama. On the Calibration of Multiclass Classification with Rejection
- Pascale Gourdeau, Varun Kanade, Marta Kwiatkowska, James Worrell. On the Hardness of Robust Classification
- Chen Dan, Hong Wang, Hongyang Zhang, Yuchen Zhou, Pradeep Ravikumar. Optimal Analysis of Subset-Selection Based L_p Low-Rank Approximation
- Matthew Holland. PAC-Bayes under potentially heavy tails
- Yihe Dong, Samuel Hopkins, Jerry Li. Quantum Entropy Scoring for Fast Robust Mean Estimation and Improved Outlier Detection
- Vaishnavh Nagarajan, J. Zico Kolter. Uniform convergence may be unable to explain generalization in deep learning
- Brian Axelrod, Ilias Diakonikolas, Alistair Stewart, Anastasios Sidiropoulos, Gregory Valiant. A Polynomial Time Algorithm for Log-Concave Maximum Likelihood via Locally Exponential Families
- Gaël Letarte, Pascal Germain, Benjamin Guedj, Francois Laviolette. Dichotomize and Generalize: PAC-Bayesian Binary Activated Deep Neural Networks
- Karl Krauth, Stephen Tu, Benjamin Recht. Finite-time Analysis of Approximate Policy Iteration for the Linear Quadratic Regulator
- Dylan Foster, Spencer Greenberg, Satyen Kale, Haipeng Luo, Mehryar Mohri, Karthik Sridharan. Hypothesis Set Stability and Generalization
- Marco Loog, Tom Viering, Alexander Mey. Minimizers of the Empirical Risk and Risk Monotonicity
- Sauptik Dhar, Vladimir Cherkassky, Mohak Shah. Multiclass Learning from Contradictions
- Abi Komanduru, Jean Honorio. On the Correctness and Sample Complexity of Inverse Reinforcement Learning
- Gilad Yehudai, Ohad Shamir. On the Power and Limitations of Random Features for Understanding Neural Networks
- Amir Najafi, Shin-ichi Maeda, Masanori Koyama, Takeru Miyato. Robustness to Adversarial Perturbations in Learning from Incomplete Data
- Fernando Gama, Alejandro Ribeiro, Joan Bruna. Stability of Graph Scattering Transforms
- Yaqi Duan, Tracy Ke, Mengdi Wang. State Aggregation Learning from Markov Transition Data
- Nika Haghtalab, Cameron Musco, Bo Waggoner. Toward a Characterization of Loss Functions for Distribution Learning
