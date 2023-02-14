# Theory

## Theory on Batch RL
- J Chen, N Jiang. Information-Theoretic Considerations in Batch Reinforcement Learning. ICML'19

## Theory on Imitation Learning
- W Sun, A Venkatraman, G Gordon, B Boots, A Bagnell. Deeply AggreVaTeD: Differentiable Imitation Learning for Sequential Prediction. ICML'17

## Theory on Exploration + Tabular MDP
- Tabular MDP: minimax results;
	- Azar, Mohammad Gheshlaghi, Ian Osband, and Remi Munos. Minimax regret bounds for reinforcement learning. ICML'17 (regret)
	- Dann, C., Li, L., Wei, W., and Brunskill, E. Policy certificates: Towards accountable reinforcement learning. ICML'19 (PAC)
- Instance-dependence bounds for tabular MDPs
	- Zanette and Brunskill. Tighter problem-dependent regret bounds in reinforcement learning without domain knowledge using value function bounds. ICML'19
	- Simchowitz and Jamieson. Non-asymptotic gap-dependent regret bounds for tabular MDPs. NeurIPS'19.
- Strong theoretical bounds for RL with function approximation:
	- Jin, Yang, Wang, and Jordan. Provably efficient reinforcement learning with linear function approximation. COLT'20.
	- Many others, including our work (lead by Andrea Zanette), and Mengdi Wang's lab.

## Theory Analysis
- R Sutton, D McAllester, S Singh, Y Mansour. Policy Gradient Methods for Reinforcement Learning with Function Approximation. NIPS'00.
	- Contributions: Established policy gradient theorem and showed convergence of policy gradient algorithm for arbitrary policy classes.
- Tsitsiklis and Van Roy. An Analysis of Temporal-Difference Learning with Function Approximation. TAC'97.
	- Contributions: Variety of convergence results and counter-examples for value-learning methods in RL.
- Reinforcement Learning of Motor Skills with Policy Gradients, Peters and Schaal, 2008. 
	- Contributions: Thorough review of policy gradient methods at the time, many of which are still serviceable descriptions of deep RL methods.
- Approximately Optimal Approximate Reinforcement Learning, Kakade and Langford, 2002.
	- Contributions: Early roots for monotonic improvement theory, later leading to theoretical justification for TRPO and other algorithms.

## Theory
- On the Sample Complexity of the Linear Quadratic Regulator. NIPS'18
