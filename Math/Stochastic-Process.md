# Stochastic Process

## Basics
- A stochastic process is a collection of random variables indexed by time.
- Stationary: P(X_k+h-X_h) and P(X_h) is the same;
- Markov Chain: P(X_n+1=i|Xn, Xn-1, ..., X0)=P(X_n+1=i|Xn)
	- Transition prob: Pij = P(Xn+1=j|Xn=i) 
	- Transition matrix: column sum-to-1;
	- A stationary distribution: pi=Api
- Martingale: E(Xt+1|Ft)=Xt
	- Our expectated gain in the process is zero at all times
	- Random walk is a martingale;
- Stopping time: Given a stochastic process {X0, X1, }, a non-negative integer-valued random variable tau is called a stopping time if for every integer k >=0,  the event tau <= k depends only on the events X0, X1, · · · , Xk.

## Point Process
- http://www.stat.columbia.edu/~liam/teaching/neurostat-fall19/uri-eden-point-process-notes.pdf
- Definition:
	- Probability on point set;
	- 2^N;
- Tutorial:
	- http://learning.mpi-sws.org/tpp-icml18/
	- https://dahuasky.wordpress.com/2010/04/11/%E7%A9%BA%E9%97%B4%E7%82%B9%E8%BF%87%E7%A8%8B%E4%B8%8E%E9%9A%8F%E6%9C%BA%E6%B5%8B%E5%BA%A6%EF%BC%88%E4%B8%80%EF%BC%89%EF%BC%9A%E4%BB%8E%E6%95%B0%E6%98%9F%E6%98%9F%E8%AF%B4%E8%B5%B7/
- Determinantal Point Process:
	- Tutorials:
		- https://youtu.be/o6xbYsOMtFU
	- Definition:
		- P(Y) ~ det(Ly)
		- L(i,j) = (gi, gj) feature inner product
	- Volumes and Gram Matrices: Vol(g(i), i in Y) = ||g(1)|| Vol(Proj g(i): i in Y - {1})
		<img src="/Basic-ML/images/stochastic-process/dpp0.png" alt="drawing" width="300"/>
	- Alex Kulesza, Ben Taskar. Determinantal point processes for machine learning. 2013
	- http://people.csail.mit.edu/stefje/fall15/notes_lecture21.pdf
	- L-ensemble; another definition (unnormalized) and relation with original K-defintion; \
		<img src="/Basic-ML/images/stochastic-process/dpp1.png" alt="drawing" width="150"/>
		<img src="/Basic-ML/images/stochastic-process/dpp2.png" alt="drawing" width="300"/>
		<img src="/Basic-ML/images/stochastic-process/dpp3.png" alt="drawing" width="400"/>
	- Property: \
		<img src="/Basic-ML/images/stochastic-process/dpp4.png" alt="drawing" width="400"/>
	- Sampling: \
		<img src="/Basic-ML/images/stochastic-process/dpp5.png" alt="drawing" width="400"/>
	- Application: to generate/encourage **diversity**, each pair of samples are **negative-correlated**;


## Infectious Disease
- Herbert W. Hethcote. The Mathematics of Infectious Diseases. SIAM Review'00
	- The model:\
		<img src="/Basic-ML/images/stochastic-process/mseir-graph.png" alt="drawing" width="400"/>
	- Notations:\
		<img src="/Basic-ML/images/stochastic-process/mseir-notation.png" alt="drawing" width="300"/>
	- The SIR formulation:\
		<img src="/Basic-ML/images/stochastic-process/sir.png" alt="drawing" width="400"/>
	- MSEIR model and formulations:\
		<img src="/Basic-ML/images/stochastic-process/mseir-graph-2.png" alt="drawing" width="400"/>\
		<img src="/Basic-ML/images/stochastic-process/mseir-eqn.png" alt="drawing" width="400"/>
