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
	- H Zhang, L Zheng, Z Li, I Stoica. Welcome to the "Big Model" Era: Techniques and Systems to Train and Serve Bigger Models. ICML'22
		- https://sites.google.com/view/icml-2022-big-model/home

## System
- Data parallel:
	- BSP: sync each batch;
	- ASP: synchronous;
	- **DDP**: PyTorch Distributed: Experiences on Accelerating Data Parallel Training. VLDB'20
		- Multiple gradients for one AllReduce;
- Model parallel:
	- **GeePS**: H Cui, H Zhang, G Ganger, P Gibbons, E Xing. GeePS: Scalable deep learning on distributed GPUs with a GPU-specialized parameter server. EuroSys'16
- Pipeline parallel:
	- **GPipe**: Y Huang, Y Cheng, A Bapna, O Firat, M Chen, D Chen, H Lee, J Ngiam, Q Le, Y Wu, Z Chen. GPipe: Efficient Training of Giant Neural Networks using Pipeline Parallelism. 19
		- D-para + M-para = Better efficiency; (fraction of bubble)
	- **PipeDream**: Narayanan et al. PipeDream: Generalized Pipeline Parallelism for DNN Training. SOSP'19
		- schedules each worker to alternatively process the forward and backward passes
	- D Narayanan, A Phanishayee, K Shi, X Chen, M Zaharia. Memory-Efficient Pipeline-Parallel DNN Training. ICML'21
- Tensor parallel:
	- Divide one tensor into multiple devices;
	- **Megatron-LM**: Shoeybi et al. Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism. 19
- DataBricks. Efficient Large-Scale Language Model Training on GPU Clusters Using Megatron-LM. arxiv'21
	- All parallel together;

## Ensemble
- Google-Brain: Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer. 17
- Google-Brain: GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding. arxiv'20
- **Switch Transformers**: Google-Brain:  Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity. 21
- **Export Choice (EC)**: Google-Brain:  Mixture-of-Experts with Expert Choice Routing. 22

## Memory Saving
- CPU Offloading:
	- M Rhu, N Gimelshein, J Clemons, A Zulfiqar, S Keckler. vDNN: Virtualized Deep Neural Networks for Scalable, Memory-Efficient Neural Network Design. MICRO'16
- Activation Recomputation:
	- Training Deep Nets with Sublinear Memory Cost. arxiv'16
		- Activation recomputation (also known as activation checkpointing or gradient checkpointing;
		- is a smart yet simple idea to reduce memory footprint at the cost of computation time.
- Mixed Precision Training:
	- NVIDIA, Baidu. Mixed Precision Training. ICLR'18
- Compression
	- Gist: Efficient Data Encoding for Deep Neural Network Training
- Memory Efficient Optimizer
	- N Shazeer, M Stern. Adafactor: Adaptive Learning Rates with Sublinear Memory Cost
	- **SM3**: R Anil, V Gupta, T Koren, Y Singer. Memory-Efficient Adaptive Optimization.
	- **ZeRO**: S Rajbhandari, J Rasley, O Ruwase, Y He. ZeRO: Memory Optimizations Toward Training Trillion Parameter Models

## Platforms

## Basics
- Good resources:
	- https://zhuanlan.zhihu.com/p/29032307
	- https://zhuanlan.zhihu.com/p/30976469
- B Pearlmutter, J Siskind. Reverse-Mode AD in a Functional Framework: Lambda the Ultimate Backpropagator. TOPLAS'08
- Conal Elliott. The simple essence of automatic differentiation. 2018

## DL
- DistBelief:
	- J Dean, et. al. Large Scale Distributed Deep Networks. NIPS'12
		- data parallelism + model parallelism
- Pytorch:
	- A Paszke, et. al. Automatic differentiation in PyTorch. NIPS-W'17
	- Ad Paszke, et. al. PyTorch: An Imperative Style, High-Performance Deep Learning Library. NIPS'19
- Tensorflow:
	- M Abadi, et al. TensorFlow: A system for large-scale machine learning. OSDI'16
	- **Debug**: A Odena, I Goodfellow. TensorFuzz: Debugging Neural Networks with Coverage-Guided Fuzzing. ICML'19
	- **Supercomputer**: Mesh-TensorFlow: Deep Learning for Supercomputers. NIPS'18
- Keras:
	- F Chollet et al. Keras. https://keras.io, 2015
- Chainer:
	- S Tokui, K Oono, S Hido, and J Clayton. Chainer: a next-generation open source framework for deep learning. NIPS Workshop'15
	- T Akiba, K Fukuda, and S Suzuki. ChainerMN: Scalable Distributed Deep Learning Framework. NeurIPS Workshop'17
- Jax:
	- J Bradbury, et. al. JAX: composable transformations of Python+NumPy programs, 2018a.
		- http://github.com/google/jax
	- J Bradbury, et. al. Stax, a flexible neural net specification library in jax, 2018b.
		- https://github.com/google/jax/blob/master/jax/experimental/stax.py

## Distributed ML
- Optimization/Statistical Learning view (convergence analysis):
	- **SSP**: Eric Xing. More Effective Distributed ML via a Stale Synchronous Parallel Parameter Server. NIPS'13
		- stale synchronous parallelSSP
- Algorithm, modeling view (improving a specific model):
	- W Neiswanger, C Wang, E Xing. Asymptotically Exact, Embarrassingly Parallel MCMC. UAI'14.
	- J Yuan, F Gao, Q Ho, W Dai, J Wei, X Zheng, E Xing, T Liu, W Ma. LightLDA: Big Topic Models on Modest Compute Clusters. WWW'15.
	- K Li, J Chen, W Chen, J Zhu. SaberLDA: Sparsity-Aware Learning of Topic Models on GPUs. ASPLOS 2017.
- System view: consistency, fault tolerance, communication, storage, resource management, programming model;
- Application view:
	- E Xing, et. al. Petuum: A new Platform for Distributed Machine Learning on Big Data. IEEE Transactions on Big Data'15
	- E Xing, et. al. Strategies and Principles of Distributed Machine Learning on Big Data. Engineering'16.
- Open sources:
	- https://github.com/sailing-pmls/bosen
	- https://github.com/sailing-pmls/pmls-caffe

## Distributed DL
- A Coates, B Huval, T Wang, D Wu, B Catanzaro, A Ng. Deep Learning with COTS HPC, ICML'13
	- data parallelism + model parallelism
- How to model parallel?
	- J Kim, Q Ho, S Lee, X Zheng, W Dai, G Gibson, E Xing. STRADS: A Distributed Framework for Scheduled Model Parallel Machine Learning. EuroSys 2016.
- Parameter server:
	- T Chilimbi, Y Suzue, J Apacible, and K Kalyanaraman. Project Adam: Building an Efficient and Scalable Deep Learning Training System. OSDI'14.
- Petuum:
	- Managed Communication and Consistency for Fast Data-Parallel Iterative Analytics. SoCC 2015.
	- GeePS: Scalable Deep Learning on Distributed GPUs with a GPU-Specialized Parameter Server. Eurosys 2016.
	- Poseidon: An Efficient Communication Architecture for Distributed Deep Learning on GPU Clusters. ATC 2017.

## Distributed
- M Yu, Z Lin, K Narra, S Li, Y Li, N Kim, A Schwing, M Annavaram, S Avestimehr. GradiVeQ: Vector Quantization for Bandwidth-Efficient Gradient Aggregation in Distributed CNN Training. NIPS'18
- J Wangni, J Wang, J Liu, T Zhang. Gradient Sparsification for Communication-Efficient Distributed Optimization. NIPS'18
- cpSGD: Communication-efficient and differentially-private distributed SGD. NIPS'18
- HOGWILD!-Gibbs can be PanAccurate. NIPS'18