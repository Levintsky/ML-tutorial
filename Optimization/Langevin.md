# Langevin Dynamics

## Basics
- X. Cheng, N. Chatterji, P. Bartlett, and M. I. Jordan. Underdamped Langevin MCMC: A non-asymptotic analysis. COLT'18
	- Underdamped form of Langevin ~ Nesterov acceleration on simplex of probability measures
- X. Cheng, Yin, D., P. Bartlett, and M. I. Jordan. In H. Daumé III and A. Singh (Eds.), Stochastic gradient and Langevin processes. ICML'20
- W. Mou, Y.-A. Ma, M. Wainwright, P. Bartlett, and M. I. Jordan. High-order Langevin diffusion yields an accelerated MCMC algorithm. JMLR'21
- R. Calandra and S. Chiappa (Eds.), N. Chatterji, J. Diakonikolas, M. I. Jordan, and P. Bartlett. Langevin Monte Carlo without smoothness. AISTATS'20
	- Smoothness isn't necessary;
- Quantitative W1 convergence of Langevin-like stochastic processes with non-convex potential state-dependent noise. X. Cheng, Yin, D., P. Bartlett, and M. I. Jordan. arxiv.org/abs/1907.03215, 2019.
- X. Cheng, N. Chatterji, Y. Abbasi-Yadkori, P. Bartlett, and M. I. Jordan. Sharp convergence rates for Langevin dynamics in the nonconvex setting. arxiv.org/abs/1805.01648, 2018.

## RL/MAB
- E. Mazumdar, A. Pacchiano, Y.-A. Ma, P. Bartlett, and M. I. Jordan. In H. Daumé III and A. Singh (Eds.), On Thompson sampling with Langevin algorithms. ICML'20
	- Langevin based achieved logarithmic regret;
	- Normal SGD won't converge;
