# Time Series

## Unclassified
- Alexander Neitz, Giambattista Parascandolo, Stefan Bauer, Bernhard Schölkopf. Adaptive Skip Intervals: Temporal Abstraction for Recurrent Dynamical Models. NIPS'18
- Yifan Sun, Yaqi Duan, Hao Gong, Mengdi Wang. Learning low-dimensional state embeddings and metastable clusters from time series data. NIPS'19

## Tue Tutorial
- Precision and Recall for Time Series

## Sequential Data (PRML Chap 13)
- Markov Model;
- HMM:\
	<img src="/Bayes/images/time-series/hmm-1.png" alt="drawing" width="400"/>\
	<img src="/Bayes/images/time-series/hmm-2.png" alt="drawing" width="400"/>
	- Definition:\
		<img src="/Bayes/images/time-series/hmm-3.png" alt="drawing" width="400"/>
	- E-step:\
		<img src="/Bayes/images/time-series/hmm-4.png" alt="drawing" width="400"/>
	- M-step:\
		<img src="/Bayes/images/time-series/hmm-5.png" alt="drawing" width="400"/>
	- Forward-backward:
		- forward-backward algorithm (Rabiner, 1989), or the Baum-Welch algorithm (Baum, 1972), Alpha-Beta (Jordan, 2007);
		- Model:\
			<img src="/Bayes/images/time-series/hmm-6.png" alt="drawing" width="400"/>
		- Forward:\
			<img src="/Bayes/images/time-series/hmm-7.png" alt="drawing" width="400"/>
		- Backward:\
			<img src="/Bayes/images/time-series/hmm-7.png" alt="drawing" width="400"/>
	- Sum-product:
	- Viterbi algorithm: find most probable sequence (dynamic programming); assume initial probability, transition matrix of z and transition z to x known;
		<img src="/Bayes/images/time-series/viterbi.png" alt="drawing" width="400"/>
	- Autoregressive HMM;\
		<img src="/Bayes/images/time-series/ar-hmm.png" alt="drawing" width="400"/>
	- Input-output HMM;\
		<img src="/Bayes/images/time-series/io-hmm.png" alt="drawing" width="400"/>
	- Factorial HMM;\
		<img src="/Bayes/images/time-series/factorial-hmm.png" alt="drawing" width="400"/>
- Linear dynamics system;
	- Model, with model parameter **known**:\
		<img src="/Bayes/images/time-series/lds-1.png" alt="drawing" width="400"/>
	- With white noise:\
		<img src="/Bayes/images/time-series/lds-2.png" alt="drawing" width="400"/>
	- Kalman filter: infer z with known dynamics\
		<img src="/Bayes/images/time-series/kalman-1.png" alt="drawing" width="400"/>\
		<img src="/Bayes/images/time-series/kalman-2.png" alt="drawing" width="400"/>
	- Learning the dynamics:\
		<img src="/Bayes/images/time-series/lds-em-2.png" alt="drawing" width="400"/>
		- E-step: p(Z|X, theta-old);\
			<img src="/Bayes/images/time-series/lds-em-1.png" alt="drawing" width="400"/>
		- M-step:\
			<img src="/Bayes/images/time-series/lds-em-3.png" alt="drawing" width="400"/>
		- M-step 1: dynamics first;\
			<img src="/Bayes/images/time-series/lds-em-4.png" alt="drawing" width="400"/>
		- M-step 2: observation;\
			<img src="/Bayes/images/time-series/lds-em-5.png" alt="drawing" width="400"/>
	- Particle filter: sampling-importance-resampling (SIR)
		- SIR:\
			<img src="/Bayes/images/time-series/pf-1.png" alt="drawing" width="400"/>\
			<img src="/Bayes/images/time-series/pf-2.png" alt="drawing" width="400"/>
		- Sequential:
			<img src="/Bayes/images/time-series/pf-3.png" alt="drawing" width="400"/>

## Beam Search
- A MAP view:\
	<img src="/Bayes/images/time-series/beam-search.png" alt="drawing" width="400"/>

## Continuous Time Series with NN
- Hongyuan Mei and Jason M Eisner. The neural hawkes process: A neurally self-modulating multivariate point process. NIPS'17
- Zhengping Che, Sanjay Purushotham, Kyunghyun Cho, David Sontag, and Yan Liu. Recurrent Neural Networks for Multivariate Time Series with Missing Values. Scientific Report'18
- Cao, Wei, Wang, Dong, Li, Jian, Zhou, Hao, Li, Lei, and et al. Brits: Bidirectional recurrent imputation for time series. arxiv'18
- Alvin Rajkomar, Eyal Oren, Kai Chen, Andrew M. Dai, Nissan Hajaj, Peter J. Liu, Xiaobing Liu, Mimi Sun, Patrik Sundberg, Hector Yee, Kun Zhang, Gavin Duggan, Gerardo Flores, Michaela Hardt, Jamie Irvine, Quoc Le, Kurt Litsch, Jake Marcus, Alexander Mossin, and Jeff Dean. Scalable and accurate deep learning for electronic health records. 2018