# Recurrent Neural Network

## Unclassified
- Nan Rosemary Ke, Anirudh Goyal, Olexa Bilaniuk, Jonathan Binas, Michael C. Mozer, Chris Pal, Yoshua Bengio. Sparse Attentive Backtracking: Temporal Credit Assignment Through Reminding. NIPS'18
- Iryna Korshunova, Jonas Degrave, Ferenc Huszár, Yarin Gal, Arthur Gretton, Joni Dambre. BRUNO: A Deep Recurrent Model for Exchangeable Data. NIPS'18
- Aditya Kusupati, Manish Singh, Kush Bhatia, Ashish Kumar, Prateek Jain, Manik Varma. FastGRNN: A Fast, Accurate, Stable and Tiny Kilobyte Sized Gated Recurrent Neural Network. NIPS'18
- Kevin Liang, Guoyin Wang, Yitong Li, Ricardo Henao, Lawrence Carin. Kernel-Based Approaches for Sequence Modeling: Connections to Neural Methods. NIPS'19	
- Giancarlo Kerg, Kyle Goyette, Maximilian Puelma Touzel, Gauthier Gidel, Eugene Vorontsov, Yoshua Bengio, Guillaume Lajoie. Non-normal Recurrent Neural Network (nnRNN): learning long time dependencies while improving expressivity with transient dynamics. NIPS'19

## Legacy
- S. Hochreiter and J. Schmidhuber. Long short-term memory. Neural Computation'97
- **GRU**: K. Cho, B. van Merrienboer, D. Bahdanau, and Y. Bengio. On the properties of neural machine translation: Encoderdecoder approaches. 2014

## RNN
- Hinton. et.al. Deep neural networks for acoustic modeling in speech recognition: The shared views of four research groups. SPM'12
- G. E. Dahl, D. Yu, L. Deng, and A. Acero, Contextdependent pre-trained deep neural networks for largevocabulary speech recognition. Audio, Speech, and Language Processing. 2012
- D. Bahdanau, K. Cho, and Y. Bengio. Neural machine translation by jointly learning to align and translate. 2014
- K. Cho, B. Van Merriënboer, C. Gulcehre, D. Bahdanau, F. Bougares, H. Schwenk, and Y. Bengio. Learning phrase representations using rnn encoder-decoder for statistical machine translation. 2014
- N. Kalchbrenner and P. Blunsom. Recurrent continuous translation models. EMNLP'13
- O. Vinyals and Q. V. Le. A neural conversational model. 2015

## BiRNN
- M. Berglund, T. Raiko, M. Honkala, L. Karkkainen, A. Vetek, and J. Karhunen, Bidirectional recurrent neural networks as generative models. NIPS'15
	- Problem setup: generating missing data in time series data in an unsupervised setting using Bidirectional RNNs;
	- Two approaches proposed: GSN; NADE;
-  Z. Huang, W. Xu, and K. Yu. Bidirectional lstm-crf models for sequence tagging. 2015
- H. Sak, A. Senior, K. Rao, and F. Beaufays. Fast and accurate recurrent neural network acoustic models for speech recognition. 2015
- C. Wang, H. Yang, C. Bartz, and C. Meinel. Image captioning with deep bidirectional lstms. CoRR'16
- **BiBS**: Bidirectional Beam Search: Forward-Backward Inference in Neural Sequence Models for Fill-in-the-Blank Image Captioning. CVPR'17
	- Model: left-right:\
		<img src="/DL/images/rnn/bibs-1.png" alt="drawing" width="500"/>
	- Inference:\
		<img src="/DL/images/rnn/bibs-2.png" alt="drawing" width="400"/>
	- Algorithm:\
		<img src="/DL/images/rnn/bibs-3.png" alt="drawing" width="400"/>

## Beam Search
- Ronan Collobert, Awni Hannun, Gabriel Synnaeve. A fully differentiable beam search decoder. ICML'19
- Wouter Kool, Herke van Hoof, Max Welling. Stochastic Beams and Where to Find Them: The Gumbel-Top-k Trick for Sampling Sequences Without Replacement. ICML'19 best paper honorable mention
