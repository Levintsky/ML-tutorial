# Platforms

## Basics
- Good resources:
	- https://zhuanlan.zhihu.com/p/29032307
	- https://zhuanlan.zhihu.com/p/30976469

## DL
- DistBelief:
	- Jeffrey Dean, Greg Corrado, Rajat Monga, Kai Chen, Matthieu Devin, Mark Mao, Marc'aurelio Ranzato, Andrew Senior, Paul Tucker, Ke Yang, Quoc V. Le, Andrew Y. Ng. Large Scale Distributed Deep Networks. NIPS'12
		- data parallelism + model parallelism
- Pytorch:
	- Adam Paszke, Sam Gross, Soumith Chintala, Gregory Chanan, Edward Yang, Zachary DeVito, Zeming Lin, Alban Desmaison, Luca Antiga, and Adam Lerer. Automatic differentiation in PyTorch. NIPS-W'17
	- Adam Paszke, Sam Gross, Francisco Massa, Adam Lerer, James Bradbury, Gregory Chanan, Trevor Killeen, Zeming Lin, Natalia Gimelshein, Luca Antiga, Alban Desmaison, Andreas Kopf, Edward Yang, Zachary DeVito, Martin Raison, Alykhan Tejani, Sasank Chilamkurthy, Benoit Steiner, Lu Fang, Junjie Bai. Soumith Chintala. PyTorch: An Imperative Style, High-Performance Deep Learning Library. NIPS'19
- Tensorflow:
	- Martín Abadi, Paul Barham, Jianmin Chen, Zhifeng Chen, Andy Davis, Jeffrey Dean, Matthieu Devin, Sanjay Ghemawat, Geoffrey Irving, Michael Isard, et al. TensorFlow: A system for large-scale machine learning. OSDI'16
	- **Debug**: Augustus Odena, Ian Goodfellow. TensorFuzz: Debugging Neural Networks with Coverage-Guided Fuzzing. ICML'19
	- **Supercomputer**: Mesh-TensorFlow: Deep Learning for Supercomputers. NIPS'18

## Distributed ML
- Optimization/Statistical Learning view (convergence analysis):
	- **SSP**: Qirong Ho, James Cipar, Henggang Cui, Seunghak Lee, Jin Kyu Kim, Phillip B. Gibbons, Garth A. Gibson, Greg Ganger, Eric P. Xing. More Effective Distributed ML via a Stale Synchronous Parallel Parameter Server. NIPS'13
		- stale synchronous parallel（SSP
- Algorithm, modeling view (improving a specific model):
	- Asymptotically Exact, Embarrassingly Parallel MCMC. Willie Neiswanger, Chong Wang, Eric P. Xing. UAI 2014.
	- LightLDA: Big Topic Models on Modest Compute Clusters. Jinhui Yuan, Fei Gao, Qirong Ho, Wei Dai, Jinliang Wei, Xun Zheng, Eric P. Xing, Tie-yan Liu, Wei-Ying Ma. WWW 2015.
	- SaberLDA: Sparsity-Aware Learning of Topic Models on GPUs. Kaiwei Li, Jianfei Chen, Wenguang Chen, Jun Zhu. ASPLOS 2017.
- System view: consistency, fault tolerance, communication, storage, resource management, programming model;
- Application view:
	- Eric P. Xing, Qirong Ho, Wei Dai, Jin Kyu Kim, Jinliang Wei, Seunghak Lee, Xun Zheng, Pengtao Xie, Abhimanu Kumar, and Yaoliang Yu. Petuum: A new Platform for Distributed Machine Learning on Big Data. IEEE Transactions on Big Data'15
	- Eric P. Xing, Qirong Ho, Pengtao Xie, Wei Dai. Strategies and Principles of Distributed Machine Learning on Big Data. Engineering'16.
- Open sources:
	- https://github.com/sailing-pmls/bosen
	- https://github.com/sailing-pmls/pmls-caffe

## Distributed DL
- Deep Learning with COTS HPC, Adam Coates, Brody Huval, Tao Wang, David Wu, Bryan Catanzaro, Andrew Ng. ICML'13
	- data parallelism + model parallelism
- How to model parallel?
	- Jin Kyu Kim, Qirong Ho, Seunghak Lee, Xun Zheng, Wei Dai, Garth A. Gibson, Eric P. Xing. STRADS: A Distributed Framework for Scheduled Model Parallel Machine Learning. EuroSys 2016.
	- Azalia Mirhoseini, Hieu Pham, Quoc V. Le, Benoit Steiner, Rasmus Larsen, Yuefeng Zhou, Naveen Kumar, Mohammad Norouzi, Samy Bengio, Jeff Dean. Device Placement Optimization with Reinforcement Learning. ICML'17
- Parameter server:
	- Trishul Chilimbi, Yutaka Suzue, Johnson Apacible, and Karthik Kalyanaraman. Project Adam: Building an Efficient and Scalable Deep Learning Training System. OSDI 2014.
- Petuum:
	- Managed Communication and Consistency for Fast Data-Parallel Iterative Analytics. Jinliang Wei, Wei Dai, Aurick Qiao, Qirong Ho, Henggang Cui, Gregory R. Ganger, Phillip B. Gibbons, Garth A. Gibson, Eric P. Xing. SoCC 2015.
	- GeePS: Scalable Deep Learning on Distributed GPUs with a GPU-Specialized Parameter Server. Henggang Cui, Hao Zhang, Gregory R. Ganger, Phillip B. Gibbons, Eric P. Xing. Eurosys 2016.
	- Poseidon: An Efficient Communication Architecture for Distributed Deep Learning on GPU Clusters. Hao Zhang, Zeyu Zheng, Shizhen Xu, Wei Dai, Qirong Ho, Xiaodan Liang, Zhiting Hu, Jinliang Wei, Pengtao Xie, Eric P. Xing. ATC 2017.

## Distributed
- Mingchao Yu, Zhifeng Lin, Krishna Narra, Songze Li, Youjie Li, Nam Sung Kim, Alexander Schwing, Murali Annavaram, Salman Avestimehr. GradiVeQ: Vector Quantization for Bandwidth-Efficient Gradient Aggregation in Distributed CNN Training. NIPS'18
- Jianqiao Wangni, Jialei Wang, Ji Liu, Tong Zhang. Gradient Sparsification for Communication-Efficient Distributed Optimization. NIPS'18
- cpSGD: Communication-efficient and differentially-private distributed SGD. NIPS'18
- HOGWILD!-Gibbs can be PanAccurate. NIPS'18