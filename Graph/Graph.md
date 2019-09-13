# GNN, ML to reprsent Graph and Relation

## Survey
- Z Wu, S Pan, F Chen, G Long, C Zhang, P Yu. A Comprehensive Survey on Graph Neural Networks. 2018
	<img src="/Graph/images/gnn-survey.png" alt="drawing" width="500"/>

## Legacy
- Gori, M., Monfardini, G., and Scarselli, F. A new model for learning in graph domains. IJCNN 2005
- Scarselli, F., Gori, M., Tsoi, A. C., Hagenbuchner, M., and Monfardini, G. Computational capabilities of graph neural networks. TNN 2009
- Scarselli, F., Gori, M., Tsoi, A. C., Hagenbuchner, M., and Monfardini, G. The graph neural network model. TNN'09
- A. Micheli, “Neural network for graphs: A contextual constructive approach. TNN'09

## GCN (Convolutional)
- **GCN-layer**: T. N. Kipf and M. Welling, Semi-supervised classification with graph convolutional networks. ICLR'17
	<img src="/Graph/images/gcn-layer.png" alt="drawing" width="500"/>

- **Pooling**: M. Defferrard, X. Bresson, and P. Vandergheynst, “Convolutional neural networks on graphs with fast localized spectral filtering. NIPS'16
	<img src="/Graph/images/gcn-pool.png" alt="drawing" width="500"/>

- Spectral-based
- Spatial-based
- Pooling

## Graph Attention Network
- P. Velickovic, G. Cucurull, A. Casanova, A. Romero, P. Lio, and Y. Bengio, Graph attention networks. ICLR'17
	<img src="/Graph/images/gcn-attention.png" alt="drawing" width="500"/>

- J. Zhang, X. Shi, J. Xie, H. Ma, I. King, and D.-Y. Yeung, Gaan: Gated attention networks for learning on large and spatiotemporal graph. UAI'18
- J. B. Lee, R. Rossi, and X. Kong, “Graph classification using structural attention. KDD'18
- S. Abu-El-Haija, B. Perozzi, R. Al-Rfou, and A. A. Alemi, Watch your step: Learning node embeddings via graph attention. NIPS'18

## Graph Auto-Encoders
- S. Cao, W. Lu, and Q. Xu, Deep neural networks for learning graph representations. AAAI'16
- D. Wang, P. Cui, and W. Zhu, Structural deep network embedding. KDD'16
- C. Wang, S. Pan, G. Long, X. Zhu, and J. Jiang, Mgae: Marginalized graph autoencoder for graph clustering. CIMK'17
- W. Yu, C. Zheng, W. Cheng, C. C. Aggarwal, D. Song, B. Zong, H. Chen, and W. Wang, Learning deep network representations with adversarially regularized autoencoders. KDD'18
- S. Pan, R. Hu, G. Long, J. Jiang, L. Yao, and C. Zhang, Adversarially regularized graph autoencoder for graph embedding. IJCAI'18
- K. Tu, P. Cui, X. Wang, P. S. Yu, and W. Zhu, Deep recursive network embedding with regular equivalence. KDD'18

## Graph Spatial-Temporal Networks
- Y. Seo, M. Defferrard, P. Vandergheynst, and X. Bresson, Structured sequence modeling with graph convolutional recurrent networks, arXiv preprint arXiv:1612.07659, 2016.
- Y. Li, R. Yu, C. Shahabi, and Y. Liu, Diffusion convolutional recurrent neural network: Data-driven traffic forecasting, ICLR'18.
- B. Yu, H. Yin, and Z. Zhu, Spatio-temporal graph convolutional networks: A deep learning framework for traffic forecasting, IJCAI'18
- S. Yan, Y. Xiong, and D. Lin, Spatial temporal graph convolutional networks for skeleton-based action recognition, AAAI'18
- A. Jain, A. R. Zamir, S. Savarese, and A. Saxena, Structural-rnn: Deep learning on spatio-temporal graphs, CVPR'16

## GNN
- **DeepMind**:
	- A Santoro, D Raposo, D G.T. Barrett, M Malinowski, R Pascanu, P Battaglia, T Lillicrap. A simple neural network module for relational reasoning. 2017
		- V (vertices)
		- u (attributes)
		- E (edges)
		- Update and aggregate operator
	- P W. Battaglia, J B. Hamrick, V Bapst, A Sanchez-Gonzalez, V Zambaldi, M Malinowski, A Tacchetti, D Raposo, A Santoro, R Faulkner, C Gulcehre, F Song, A Ballard, J Gilmer, G Dahl, A Vaswani, K Allen, C Nash, V Langston, C Dyer, N Heess, D Wierstra, P Kohli, M Botvinick,O Vinyals, Y Li, R Pascanu. Relational inductive biases, deep learning, and graph networks. 2018
	- Y Li, C Gu, T Dullien, O Vinyals, P Kohli. Graph Matching Networks for Learning the Similarity of Graph Structured Objects. 2019
- **GNN**:
	- http://snap.stanford.edu/proj/embeddings-www/
- Semi-supervised classification with graph convolutional networks. NIPS 2015
- **GGNN**: Gated Graph Sequence Neural Networks. ICLR 2016
	- SOA?
- **Spectral**:
	- Convolutional Neural Networks on Graphs with Fast Localized Spectral Filtering, NIPS 2016
	- Semi-supervised classification with graph convolutional networks. ICLR 2017
- **FAIR**:
	- Spectral networks and locally connected networks on graphs. ICLR 2014
	- **GLoMo**: Unsupervisedly Learned Relational Graphs as Transferable Representations, 2018
	- Bronstein, M. M., Bruna, J., LeCun, Y., Szlam, A., and Vandergheynst, P. Geometric deep learning: going beyond euclidean data. SPM 2017
	- Wang, X., Girshick, R., Gupta, A., and He, K. Non-local neural networks. CVPR 2018
		- Combine self-attention in computer vision
- **MPNN**: Gilmer, J., Schoenholz, S. S., Riley, P. F., Vinyals, O., and Dahl, G. E. Neural message
passing for quantum chemistry. 2017
	- Combine GNN and Convolutional-GNN
- Kipf, T. N. and Welling, M. Semi-supervised classification with graph convolutional networks. ICLR 2017
- Capsule Graph Neural Network. ICLR'19

## Applications
- Learning to Act Properly: Predicting and Explaining Affordances from Images, 2018
- Raposo, D., Santoro, A., Barrett, D., Pascanu, R., Lillicrap, T., and Battaglia, P. (2017). Discovering
objects and their relations from entangled scene representations. ICLR Workshop 2017
- Garcia, V. and Bruna, J. (2018). Few-shot learning with graph neural networks. ICLR 2017
- Bordes, A., Usunier, N., Garcia-Duran, A., Weston, J., and Yakhnenko, O. Translating embeddings for modeling multi-relational data. NIPS 2013