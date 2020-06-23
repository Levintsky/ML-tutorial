# Graph Generative Networks

## Non-Learning
- Erdős, Rényi, 1960
- Barabási, Albert, 1999

## Others
- D Johnson. Learning graphical state transitions. ICLR'17
- B. Yu, H. Yin, and Z. Zhu, Spatio-temporal graph convolutional networks: A deep learning framework for traffic forecasting. IJCAI'18
- N. De Cao and T. Kipf, Molgan: An implicit generative model for small molecular graphs. arxiv'18
- A. Bojchevski, O. Shchur, D. Zugner, and S. Gunnemann, Net-gan: Generating graphs via random walks. ICML'18
- **NTG**: Hang Chu, Daiqing Li, David Acuna, Amlan Kar, Maria Shugrina, Xinkai Wei, Ming-Yu Liu, Antonio Torralba, Sanja Fidler. Neural Turtle Graphics for Modeling City Road Layouts. ICCV'19
	- https://nv-tlabs.github.io/NTG/

## VAE
- T. N. Kipf and M. Welling, Variational graph auto-encoders. 2016
	- http://tkipf.github.io/graph-convolutional-networks/
	- X: N x F (features on nodes); Adj: N x N;
	- Training:
		- Encoder: a bunch of layers of non-linear(W\*Laplacian\*X), get mu and sigma;
		- Sample z from N(mu, sigma) for decoder;
		- Decoder: (Linear - ReLU) x 3;
		- Decoder output reshaped as N x N, loss with ground truth Adj-GT;
		- Additional loss of KL-Div on mu, sigma;
	- Testing: directly sampling;\
		<img src="/Graph/images/gcn-vae.png" alt="drawing" width="500"/>
- Q Liu, M Allamanis, M Brockschmidt, and A Gaunt. Constrained Graph Variational Autoencoders for Molecule Design. NIPS'18
- Brute-Force VAE: M Simonovsky, N Komodakis. GraphVAE: Towards Generation of Small Graphs Using Variational Autoencoders. ICANN'18
- T. Ma, J. Chen, and C. Xiao, Constrained generation of semantically valid graphs via regularizing variational autoencoders. NIPS'18
- RvNN-VAE: M Li, A Patil, K Xu, S Chaudhuri, O Khan, A Shamir, C Tu, B Chen, D Cohen-Or, H Zhang. GRAINS: Generative Recursive Autoencoders for INdoor Scenes. SIGGRAPH'19

## Autoregressive
- **SMILES**: M Segler, T Kogej, C Tyrchan, and M P Waller. Generating focused molecule libraries for drug discovery with recurrent neural networks. 2017
	- RNN on domain-specific sequentializations of graphs;
- **GEG**: Y Li, O Vinyals, C Dyer, R Pascanu, P Battaglia. Learning Deep Generative Models of Graphs. ICML'18
	- (1) sample whether to add a new node of a particular type or terminate;
	- (2) we add a node of this type to the graph;
	- (3) check if any further edges are needed to connect the new node to the existing graph;
	- (4) we select a node in the graph and add an edge connecting the new node to the selected node. The algorithm goes back to step (3) and repeats until the model decides not to add another edge. 
	- Finally, the algorithm goes back to step (1) to add subsequent nodes.
- **GraphRNN**: J. You, R. Ying, X. Ren, W. L. Hamilton, and J. Leskovec, GraphRNN: A deep generative model for graphs. ICML'18
	- https://github.com/snap-stanford/GraphRNN
	- Graph-level RNN;
	- Edge-level RNN; (adjacency vector)
	- Evaluation: MMD (Maximum Mean Discrepancy)
- Wengong Jin, Regina Barzilay, and Tommi Jaakkola. Junction tree variational autoencoder for molecular graph generation. 2018
- Yujia Li, Oriol Vinyals, Chris Dyer, Razvan Pascanu, and Peter Battaglia. Learning deep generative models of graphs. 2018
- **GRAN**: R Liao, Y Li, Y Song, S Wang, W Hamilton, D Duvenaud, R Urtasun, R Zemel. Efficient Graph Generation with Graph Recurrent Attention Networks. NIPS'19
	- First to generate to scale up to 5K;
	- https://github.com/lrjconan/GRAN
	- Generate B rolls at a time;
	- Node representation: linear mapping for initial node feat;
	- GNN with Attentive Messages: add all augmented edges, run message passing in GNN, classification of the edges to decide y/n with GRU;
