# Fairness, Autonomy Security

## Basics
- Fairness:
	- Free from bias;
	- Confidence score;
	- Tradeoff between false positives and fase negatives;
- Privacy:
	- Can't access data;
	- Differential privacy;

## Tutorials
- ICML'21: https://sites.google.com/view/ResponsibleAITutorial

## RL
- DeepMind. Social Influence as Intrinsic Motivation for Multi-Agent Deep Reinforcement Learning. ICML'19 best paper honorable mention
- DeepMind. Offline Contextual Bandits with High Probability Fairness Guarantees. NIPS'19
	- Fairness constraint:
		- gf(θ) = 1/|F|Σ(RI(f) - E[R|f]) - εf
		- gm(θ) = 1/|M|Σ(RI(m) - E[R|m]) - εm

## Fairness
- S Vasudevan, K Kenthapadi. LiFT: A Scalable Framework for Measuring Fairness in ML Applications. CIKM'20
	- https://github.com/linkedin/LiFT

## Privacy
- M Bun, T Steinke. Average-Case Averages: Private Algorithms for Smooth Sensitivity and Mean Estimation. NIPS'18
- K Chaudhuri, J Imola, A Machanavajjhala. Capacity Bounded Differential Privacy.