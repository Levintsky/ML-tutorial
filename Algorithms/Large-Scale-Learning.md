# Large-Scale ML

## Basics
- Training Parallelism
	- Data Parallelism: BSP, ASP, DDP
	- Model Parallelism
		- GeePS
	- Pipeline Parallelism: DP + MP;
		- GPipe, PipeDream;
	- Tensor Parallelism
- Mixture-of-Experts (MoE)
	- Ensemble learning (gated)
	- GShard
	- Switch Transformer;
- Other Memory Saving Designs
	- CPU Offloading: Rhu'16, unused data to CPU and read them back later;
	- Activation Recomputation: Chen'16
	- Mixed Precision Training: fp16 + fp32
		- Narang & Micikevicius et al. (2018)
	- Compression: compress intermediate result;
	- Memory Efficient Optimizer
		- Adafactor, SM3, ZeRO;
- Tutorial
	- https://lilianweng.github.io/posts/2021-09-25-train-large/
	- Hao Zhang, Lianmin Zheng, Zhuohan Li, Ion Stoica. Welcome to the "Big Model" Era: Techniques and Systems to Train and Serve Bigger Models. ICML'22
		- https://sites.google.com/view/icml-2022-big-model/home

## System
- Data parallel:
	- BSP: sync each batch;
	- ASP: synchronous;
	- **DDP**: PyTorch Distributed: Experiences on Accelerating Data Parallel Training. VLDB'20
		- Multiple gradients for one AllReduce;
- Model parallel:
	- **GeePS**: Henggang Cui, Hao Zhang, Gregory R. Ganger, Phillip B. Gibbons, Eric P. Xing. GeePS: Scalable deep learning on distributed GPUs with a GPU-specialized parameter server. EuroSys'16
- Pipeline parallel:
	- **GPipe**: Yanping Huang, Youlong Cheng, Ankur Bapna, Orhan Firat, Mia Xu Chen, Dehao Chen, HyoukJoong Lee, Jiquan Ngiam, Quoc V. Le, Yonghui Wu, Zhifeng Chen. GPipe: Efficient Training of Giant Neural Networks using Pipeline Parallelism. 19
		- D-para + M-para = Better efficiency; (fraction of bubble)
	- **PipeDream**: Narayanan et al. PipeDream: Generalized Pipeline Parallelism for DNN Training. SOSP'19
		- schedules each worker to alternatively process the forward and backward passes
	- Deepak Narayanan, Amar Phanishayee, Kaiyu Shi, Xie Chen, Matei Zaharia. Memory-Efficient Pipeline-Parallel DNN Training. ICML'21
- Tensor parallel:
	- Divide one tensor into multiple devices;
	- **Megatron-LM**: Shoeybi et al. Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism. 19
	- Narayanan et al. Efficient Large-Scale Language Model Training on GPU Clusters Using Megatron-LM. arxiv'21
- Deepak Narayanan, Mohammad Shoeybi, Jared Casper, Patrick LeGresley, Mostofa Patwary, Vijay Anand Korthikanti, Dmitri Vainbrand, Prethvi Kashinkunti, Julie Bernauer, Bryan Catanzaro, Amar Phanishayee, Matei Zaharia. Efficient Large-Scale Language Model Training on GPU Clusters Using Megatron-LM.
	- All parallel together;

## Ensemble
- Noam Shazeer, Azalia Mirhoseini, Krzysztof Maziarz, Andy Davis, Quoc Le, Geoffrey Hinton, Jeff Dean. Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer. 17
- Dmitry Lepikhin, HyoukJoong Lee, Yuanzhong Xu, Dehao Chen, Orhan Firat, Yanping Huang, Maxim Krikun, Noam Shazeer, Zhifeng Chen. GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding. arxiv'20
- **Switch Transformers**: William Fedus, Barret Zoph, Noam Shazeer. Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity. 21
- **Export Choice (EC)**: Yanqi Zhou, Tao Lei, Hanxiao Liu, Nan Du, Yanping Huang, Vincent Zhao, Andrew Dai, Zhifeng Chen, Quoc Le, James Laudon. Mixture-of-Experts with Expert Choice Routing. 22

## Memory Saving
- CPU Offloading:
	- Minsoo Rhu, Natalia Gimelshein, Jason Clemons, Arslan Zulfiqar, Stephen W. Keckler. vDNN: Virtualized Deep Neural Networks for Scalable, Memory-Efficient Neural Network Design. MICRO'16
- Activation Recomputation:
	- Training Deep Nets with Sublinear Memory Cost. arxiv'16
		- Activation recomputation (also known as activation checkpointing or gradient checkpointing;
		- is a smart yet simple idea to reduce memory footprint at the cost of computation time.
- Mixed Precision Training:
	- Paulius Micikevicius, Sharan Narang, Jonah Alben, Gregory Diamos, Erich Elsen, David Garcia, Boris Ginsburg, Michael Houston, Oleksii Kuchaiev, Ganesh Venkatesh, Hao Wu. Mixed Precision Training. ICLR'18
- Compression
	- Gist: Efficient Data Encoding for Deep Neural Network Training
- Memory Efficient Optimizer
	- Noam Shazeer, Mitchell Stern. Adafactor: Adaptive Learning Rates with Sublinear Memory Cost
	- **SM3**: Rohan Anil, Vineet Gupta, Tomer Koren, Yoram Singer. Memory-Efficient Adaptive Optimization.
	- **ZeRO**: Samyam Rajbhandari, Jeff Rasley, Olatunji Ruwase, Yuxiong He. ZeRO: Memory Optimizations Toward Training Trillion Parameter Models

## NIPS'18
- Sulaiman Alghunaim, Kun Yuan, Ali H Sayed. A Linearly Convergent Proximal Gradient Algorithm for Decentralized Optimization
- Edgar Dobriban, Sifan Liu. Asymptotics for Sketching in Least Squares Regression
- Shashank Rajput, Hongyi Wang, Zachary Charles, Dimitris Papailiopoulos. DETOX: A Redundancy-based Framework for Faster and More Robust Gradient Aggregation
- Cheng Meng, Yuan Ke, Jingyi Zhang, Mengrui Zhang, Wenxuan Zhong, Ping Ma. Large-scale optimal transport map estimation using projection pursuit
- Lin Chen, Hossein Esfandiari, Gang Fu, Vahab Mirrokni. Locality-Sensitive Hashing for f-Divergences: Mutual Information Loss and Beyond
- Jason Altschuler, Francis Bach, Alessandro Rudi, Jonathan Niles-Weed. Massively scalable Sinkhorn distances via the Nyström method
- Belhal Karimi, Hoi-To Wai, Eric Moulines, Marc Lavielle. On the Global Convergence of (Fast) Incremental Expectation Maximization Methods
- zengfeng Huang, Ziyue Huang, Yilei WANG, Ke Yi. Optimal Sparsity-Sensitive Bounds for Distributed Mean Estimation
- Debraj Basu, Deepesh Data, Can Karakus, Suhas Diggavi. Qsparse-local-SGD: Distributed SGD with Quantization, Sparsification and Local Computations
- Xiaoyun Li, Ping Li. Random Projections with Asymmetric Quantization
- Ping Li, Xiaoyun Li, Cun-Hui Zhang. Re-randomized Densification for One Permutation Hashing and Bin-wise Consistent Weighted Sampling
- Amirhossein Reisizadeh, Hossein Taheri, Aryan Mokhtari, Hamed Hassani, Ramtin Pedarsani. Robust and Communication-Efficient Collaborative Learning
- Ankit Singh Rawat, Jiecao Chen, Felix Xinnan Yu, Ananda Theertha Suresh, Sanjiv Kumar. Sampled Softmax with Random Fourier Features
- Tharun Kumar Reddy Medini, Qixuan Huang, Yiqiu Wang, Vijai Mohan, Anshumali Shrivastava. Extreme Classification in Log Memory using Count-Min Sketch: A Case Study of Amazon Search with 50M Products
- Vayer Titouan, Rémi Flamary, Nicolas Courty, Romain Tavenard, Laetitia Chapel. Sliced Gromov-Wasserstein
- Nikolas Ioannou, Celestine Mendler-Dünner, Thomas Parnell. SySCD: A System-Aware Parallel Coordinate Descent Algorithm
- Yanping Huang, Youlong Cheng, Ankur Bapna, Orhan Firat, Dehao Chen, Mia Chen, HyoukJoong Lee, Jiquan Ngiam, Quoc V Le, Yonghui Wu, zhifeng Chen. GPipe: Efficient Training of Giant Neural Networks using Pipeline Parallelism

## NLP
- J. Kaplan, S. McCandlish, T. Henighan, T. B. Brown, B. Chess, R. Child, S. Gray, A. Radford, J. Wu, and D. Amodei. Scaling laws for neural language models. arxiv'20
- J. Hoffmann, S. Borgeaud, A. Mensch, E. Buchatskaya, T. Cai, E. Rutherford, D. d. L. Casas, L. A. Hendricks, J. Welbl, A. Clark, et al. Training compute-optimal large language models. arxiv'22