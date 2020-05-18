# Provable Attack and Defense

## Provable Attack
- Poisoning:
	- Targeted: Saeed Mahloujifar, Dimitrios I. Diochnos, and Mohammad Mahmoody. Learning under p-Tampering Attacks. ALT'18
		- Number of change O(pm), running time polynomial;
		- Probability: Omega(p)
	- Non-targeted: Koh, Steinhardt, Liang, 18
	- Computational Concentration of Measure: Optimal Bounds, Reductions, and More. SODA'20
		- Change O(m^0.5) training examples and replace them with other examples with correct label;
		- Probability: 1/poly(m) to 0.99;
- Evasion:
	- Specific distributions;
	- The Curse of Concentration in Robust Learning: Evasion and Poisoning Attacks from Concentration of Measure. AAAI'19
		- Number of change O(m^0.5), running time: existential;
	- Based on Optimal transport: Bhagoji, Cullina, Mittal, NIPS'19
- Adversarial Risk and Robustness: General Definitions and Implications for the Uniform Distribution. NIPS'18
- Can Adversarially Robust Learning Leverage Computational Hardness? ALT'19
- Universal Multi-party Poisoning Attacks. ICML'19
- Emprically Measuring Concentration: Fundamental Limits on Intrinsic Robustness. NeurIPS'19
- Adversarially Robust Learning Could Leverage Computational Hardness. ALT'20

## Provable Defense
- For Poissoning:
	- I. Diakonikolas, G. Kamath, D. Kane, J. Li, A. Moitra, A. Stewart. Robust Estimators in High Dimensions without the Computational Intractability. FOCS'16
	- Jacob Steinhardt, Pang Wei Koh, Percy Liang. Certified Defenses for Data Poisoning Attacks. NIPS'17
- For Evasion:
	- Daniel Cullina, Arjun Nitin Bhagoji, Prateek Mittal. PAC-learning in the presence of evasion adversaries. NIPS'18
	- Aditi Raghunathan, Jacob Steinhardt, Percy Liang. Certified Defenses against Adversarial Examples. 2018
	- Jeremy Cohen, Elan Rosenfeld, J. Zico Kolter. Certified Adversarial Robustness via Randomized Smoothing. ICML'19
