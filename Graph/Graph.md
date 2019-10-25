# GNN, ML to reprsent Graph and Relation

## Survey
- Slides: http://helper.ipam.ucla.edu/publications/dlt2018/dlt2018_14506.pdf
- Z Wu, S Pan, F Chen, G Long, C Zhang, P Yu. A Comprehensive Survey on Graph Neural Networks. 2018
	<img src="/Graph/images/gnn-survey.png" alt="drawing" width="500"/>
- Z Zhang, P Cui and W Zhu. Deep Learning on Graphs: A Survey. 2018

## Legacy
- Gori, M., Monfardini, G., and Scarselli, F. A new model for learning in graph domains. IJCNN 2005
- Scarselli, F., Gori, M., Tsoi, A. C., Hagenbuchner, M., and Monfardini, G. Computational capabilities of graph neural networks. TNN 2009
- Scarselli, F., Gori, M., Tsoi, A. C., Hagenbuchner, M., and Monfardini, G. The graph neural network model. TNN'09
- A. Micheli, Neural network for graphs: A contextual constructive approach. TNN'09

## Toronto (Renjie Liao)
- R Li, M Tapaswi, R Liao, J Jia, R Urtasun, S Fidler. Situation Recognition with Graph Neural Networks. ICCV'17
	- https://github.com/liruiyu/ggnn
- X Qi, R Liao, J Jia, S Fidler, R Urtasun. 3D Graph Neural Networks for RGBD Semantic Segmentation, ICCV'17
	- https://github.com/xjqicuhk/3DGNN
- R Liao, M Brockschmidt, D Tarlow, A Gaunt, R Urtasun, R Zemel. Graph Partition Neural Networks for Semi-Supervised Classification, ICLRW'18
	- https://github.com/Microsoft/graph-partition-neural-network-samples
- R Liao, Z Zhao, R Urtasun, R Zemel. LanczosNet: Multi-Scale Deep Graph Convolutional Networks. ICLR'19
	- https://github.com/lrjconan/LanczosNetwork
- K Yoon, R Liao, Y Xiong, L Zhang, E Fetaya, R Urtasun, R Zemel, X Pitkow. Inference in Probabilistic Graphical Models by Graph Neural Networks. ICMLW'19
- **GRAN**: R Liao, Y Li, Y Song, S Wang, W Hamilton, D Duvenaud, R Urtasun, R Zemel. Efficient Graph Generation with Graph Recurrent Attention Networks. NIPS'19
	- First to generate to scale up to 5K;
	- https://github.com/lrjconan/GRAN

## GCN (Convolutional)
- Spectral-based:
	- Eigen-decomposition: O(N^3) computation, O(N^2) memory, not efficient for big graphs;
	- **Spectral CNN**: J Bruna, W Zaremba, A Szlam and Y LeCun. Spectral networks and locally connected networks on graphs. ICLR'14
	- **ChebNet**: M Defferrard, X Bresson and P Vandergheynst. Convolutional Neural Networks on Graphs with Fast Localized Spectral Filtering, NIPS'16
		- Problem: classify graph on fixed graph;
		- Localized in space; pooling;
		- https://github.com/mdeff/cnn_graph (Tensorflow-official)
		- https://github.com/xbresson/spectral_graph_convnets (Pytorch)
		- Fast localized filter: Graph Fourier Transform;
		- Graph Coarsening;
		<img src="/Graph/images/gcn-pool.png" alt="drawing" width="500"/>
	- **GCN-layer**: T. N. Kipf and M. Welling, Semi-supervised classification with graph convolutional networks. ICLR'17
		- Problem: classify nodes;
		- First order approximation of ChebNet;
		- https://github.com/tkipf/gcn
		- https://github.com/tkipf/pygcn (PyTorch)
		<img src="/Graph/images/gcn-layer.png" alt="drawing" width="500"/>
	- **AGCN**: R. Li, S. Wang, F. Zhu, and J. Huang, Adaptive graph convolutional neural networks. AAAI'18
		- Augment a graph with a residual graph, incurs expensive computation;
- Spatial-based:
	- Recurrent-based: recursively update node representations until convergence;
		- **GGNN** (Gated Graph Neural Networks): K. Cho, B. Van Merriënboer, C. Gulcehre, D. Bahdanau, F. Bougares, H. Schwenk, and Y. Bengio, Learning phrase representations using rnn encoder-decoder for statistical machine translation. EMNLP'14
		- **SSE** (Stochastic Steady-state Embedding): H. Dai, Z. Kozareva, B. Dai, A. Smola, and L. Song, Learning steady-states of iterative algorithms over graphs. ICLR'18
	- Composition-based:
		- **MPNN**: Gilmer, J., Schoenholz, S. S., Riley, P. F., Vinyals, O., and Dahl, G. E. Neural message passing for quantum chemistry. 2017
			- Combine GNN and Convolutional-GNN
		- **GraphSage**: W. Hamilton, Z. Ying, and J. Leskovec, Inductive representation learning on large graphs. NIPS'17
			- Introduce aggregation function;
		- **DCNN**: J. Atwood and D. Towsley, Diffusion-convolutional neural networks, NIPS'16
	- **LGCN**: H. Gao, Z. Wang, and S. Ji, Large-scale learnable graph convolutional networks. KDD'18
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
- **FAIR**:
	- **GLoMo**: Unsupervisedly Learned Relational Graphs as Transferable Representations, 2018
	- Bronstein, M. M., Bruna, J., LeCun, Y., Szlam, A., and Vandergheynst, P. Geometric deep learning: going beyond euclidean data. SPM 2017
	- Wang, X., Girshick, R., Gupta, A., and He, K. Non-local neural networks. CVPR 2018
		- Combine self-attention in computer vision
- Capsule Graph Neural Network. ICLR'19

## Applications
- Learning to Act Properly: Predicting and Explaining Affordances from Images, 2018
- Raposo, D., Santoro, A., Barrett, D., Pascanu, R., Lillicrap, T., and Battaglia, P. (2017). Discovering
objects and their relations from entangled scene representations. ICLR Workshop 2017
- Garcia, V. and Bruna, J. (2018). Few-shot learning with graph neural networks. ICLR 2017
- Bordes, A., Usunier, N., Garcia-Duran, A., Weston, J., and Yakhnenko, O. Translating embeddings for modeling multi-relational data. NIPS 2013