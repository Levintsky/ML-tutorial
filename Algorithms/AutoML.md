# AutoML, Architecture Search

## Basics
- Search-space:
	- Whole architecture;
	- Cell;
	- Data augmentation: successful nice ideas
	- Activation functions;
- Search approach:
	- RL-based;
	- Evolution;
	- ENAS/DART; (weight-sharing)
	- Bayesian optimization;
	- Random search;
- Metric:
	- GPU-hours;
- Benchmark:
	- https://openml.github.io/automlbenchmark/results.html
- Most successful application:
	- On mobile: **MnasNet** in industry;
	- MobileNetV3;
	- Song Han: ProxylessNAS: Direct Neural Architecture Search on Target Task and Hardware
	- FBNet: Hardware-Aware Efficient ConvNet Design via Differentiable Neural Architecture Search
- Tradeoff:
	- EfficientNet, EfficientDet;

## Summary
- M Wistuba, A Rawat, Te Pedapati. A Survey on Neural Architecture Search. 2019
- https://github.com/hibayesian/awesome-automl-papers
- https://github.com/markdtw/awesome-architecture-search
- NIPS Tutorial: https://nips.cc/Conferences/2018/Schedule?showEvent=10979
	- Frank Hutter
- Zhihu:
	- https://zhuanlan.zhihu.com/p/71547478
	- https://zhuanlan.zhihu.com/p/42924585
	- https://zhuanlan.zhihu.com/p/57404166
- SMBO: https://zhuanlan.zhihu.com/p/53826787

## Unclassfied
- Catherine Wong, Neil Houlsby, Yifeng Lu, Andrea Gesmundo. Transfer Learning with Neural AutoML. NIPS'18
- Jianlong Chang, xinbang zhang, Yiwen Guo, Gaofeng Meng, Shiming Xiang, Chunhong Pan. DATA: Differentiable ArchiTecture Approximation. NIPS'19
- Yukang Chen, Tong Yang, Xiangyu Zhang, Gaofeng Meng, Xinyu Xiao, Jian Sun. DetNAS: Backbone Search for Object Detection. NIPS'19

## Search Space
- Search whole neural net:
	- **Nas**: Barret Zoph, Quoc V. Le. Neural architecture search with reinforcement learning, ICLR'17
- Search cell:
	- **NasNet**: Barret Zoph, Vijay Vasudevan, Jonathon Shlens, Quoc V. Le. Learning transferable architectures for scalable image recognition. CVPR'18
		- Search normal cell and reduction cell;
	- Zhong, Zhao, Yan, Junjie, and Liu, Cheng-Lin. Practical network blocks design with q-learning. AAAI'18
	- **ENAS**: H Pham, M. Guan, B. Zoph, Q. Le. Efficient neural architecture search via parameter sharing. ICML'18
	- **AmoebaNet**: E. Real, Q. Le. 2018 Regularized evolution for image classifier architecture search. AAAI'19
	**The Evolved Transformer**: David R. So, Chen Liang, Quoc V. Le. The Evolved Transformer. 2019
		- Search encoder/decoder cells;
- Seach a subpath from a supernet:
	- **PathLevel-EAS**: H Cai, S Han: Path-Level Network Transformation for Efficient Architecture Search, ICML'18
- Search **data augmentation**:
	- Ekin D. Cubuk, Barret Zoph, Jonathon Shlens, Quoc V. Le. RandAugment: Practical automated data augmentation with a reduced search space. 2019
		- https://github.com/tensorflow/tpu/tree/master/models/
		- Insight: no need for a separate proxy task;
		- Insight: just 2 hyperparameter (N, M)\
			<img src="/AutoML-Meta/images/rand-augment.png" alt="drawing" width="500"/>
		- 85% imagenet; 0.3% mAP improvement;
- Search activation function:
	- **swish**: Prajit Ramachandran, Barret Zoph, and Quoc V. Le. Searching for activation functions. ICLR'18
- H2O: https://github.com/h2oai/h2o-3
- Insight: Anti AutoML;
- Saining Xie, Kaiming He. Exploring Randomly Wired Neural Networks for Image Recognition. ICCV'19
	- Network generators: g(theta), g: residual, theta: layers, ...
	- Randomly wired NN (ER/BA/WS)
		- Aggregation: linear weight learned to combine
		- Transformation: ReLU - Conv - BN;
		- Distribution;
		- Single input/output;
		- Stages: progressive downsample;
	- Experiments (ImageNet 1000, 1.28M train, 50k val):
		- Baselines: MobileNet, ShuffleNet;
- I. Radosavovic, J. Johnson, S. Xie, W.-Y. Lo, and P. Dollar. On network design spaces for visual recognition. ICCV'19
- **RegNet**: Ilija Radosavovic, Raj Prateek Kosaraju, Ross Girshick, Kaiming He, Piotr Dollar. Designing Network Design Spaces. CVPR'20
	- https://github.com/facebookresearch/pycls
	- AnyNetX;
	- Does not use SE and Swish;
	- Auto-AutoML, better result than;

## Search Approach
- DNAS (differentiable):
	- **DARTS**: Hanxiao Liu, Karen Simonyan, Yiming Yang. DARTS: Differentiable Architecture Search. ICLR'19
		- Insight: fully differentiable, reduce cost to a few GPU days;
		- Continuous relaxation:\
			<img src="/AutoML-Meta/images/darts.png" alt="drawing" width="400"/>
		- 2.83% error CIFAR, 73.1% ImageNet top-1
		- 56.1 Perplexity PTB
		- https://github.com/quark0/darts
	- **GDAS**: Xuanyi Dong, Yi Yang. Searching for A Robust Neural Architecture in Four GPU Hours. CVPR'19
		- Gumbel-softmax trick to sample from different op outputs!
		- https://github.com/D-X-Y/AutoDL-Projects
- RL
	- Basics:
		- 400 GPUs, 3-4 days;
			<img src="/AutoML-Meta/images/automl-rl.jpg" alt="drawing" width="500"/>
	- **Nas**: Barret Zoph, Quoc V. Le. Neural architecture search with reinforcement learning, ICLR'17
		- RNN for model architecture hyperparameter;
		- Based on Policy-Gradient (REINFORCE); accuracy as reward with baseline for variance reduction;
		- CNN and recurrent cell;
	- **NasNet**: Barret Zoph, Vijay Vasudevan, Jonathon Shlens, Quoc V. Le. Learning transferable architectures for scalable image recognition. CVPR'18
		- https://github.com/tensorflow/models/tree/master/research/slim/nets/nasnet
		- Search-space: in **Normal cell**, **reduction-cell**:
			- 1x7, 3x3, 5x5, 1x1 convolution, pooling, ...
		- Model: recursively do:
			- Step 1. Select a hidden state f created in previous blocks;
			- Step 2. Select a second hidden state;
			- Step 3. Select an operation to apply for Step 1; 
			- Step 4. Select an operation to apply for Step 2;
			- Step 5. Select a method to combine Step 3 and 4 to create a new;
		- ImageNet: 82.7% top-1, 96% top-5;
	- **MetaQNN**: Baker, B.; Gupta, O.; Naik, N.; and Raskar, R. Designing neural network architectures using reinforcement learning. ICLR'17
		- https://github.com/bowenbaker/metaqnn
		- Q-learning based: e-greedy, experience replay;
		- Action space: adding different layers, stopping;
	- **swish**: Prajit Ramachandran, Barret Zoph, and Quoc V. Le. Searching for activation functions. ICLR'18
		- Model: combining unary and binary op:\
			<img src="/AutoML-Meta/images/swish-1.png" alt="drawing" width="400"/>
			<img src="/AutoML-Meta/images/swish-2.png" alt="drawing" width="400"/>
		- Learning: Exhaustive search + RL;
		- Discovery: swish op: f() = x sigma(beta x)
	- Zhong, Zhao, Yan, Junjie, and Liu, Cheng-Lin. Practical network blocks design with q-learning. AAAI'18
		- Search method: Q-Learning;
		- Search space: block-wise;
		- Experiments: 3 days, 32 GPUs; CIFAR-10: 3.54%;
	- Augmentation:
		- **AutoAugment**: Ekin Dogus Cubuk, Barret Zoph, Dandelion Mane, Vijay Vasudevan, and Quoc V. Le. AutoAugment: Learning augmentation policies from data. CVPR'19
			- Model: REINFORCE (PPO); RNN Controller;
			- 16 operations: ShearX/Y, TranslateX/Y, Rotate, AutoContrast, Invert, Equalize, Solarize, Posterize, Contrast, Color, Brightness, Sharpness, Cutout [12], Sample Pairing;
				- Hyperparameters: discretize 10 bins;
		- Barret Zoph, Ekin D Cubuk, Golnaz Ghiasi, Tsung-Yi Lin, Jonathon Shlens, Quoc V Le. Learning Data Augmentation Strategies for Object Detection. 2019
			- https://github.com/tensorflow/tpu/tree/master/models/official/detection
			- Operation:
				- **Color operations**: Distort color channels, without impacting the locations of the bounding boxes;
				- **Geometric operations**: Geometrically distort the image, which correspondingly alters the location and size of the bounding box annotations;
				- **Bounding box operations**: only distort pixel content contained within the bounding box annotations;
			- Learning: RNN + PPO;
			- 5K subset as proxy;
			- 20K augmentation policies. The search employed 400 TPUs over 48 hours; 
			- COCO: +2.3 mAP; SOTA 50.7 mAP;
	- Detection:
		- **Nas-fpn**: Golnaz Ghiasi, Tsung-Yi Lin, Quoc V. Le. Nas-fpn: Learning scalable feature pyramid architecture for object detection. CVPR'19
			- Search space:
				- Step 1. Select a feature layer hi from candidates.
				- Step 2. Select another feature layer hj from candidates without replacement.
				- Step 3. Select the output feature resolution.
				- Step 4. Select a binary op to combine hi and hj selected in Step 1 and Step 2 and generate a feature layer with the resolution selected in Step 3.
			- Learning: RNN + PPO;\
				<img src="/AutoML-Meta/images/nas-fpn1.png" alt="drawing" width="400"/>
				<img src="/AutoML-Meta/images/nas-fpn2.png" alt="drawing" width="500"/>
- Evolution
	- Basics:
		- https://ai.googleblog.com/2018/03/using-evolutionary-automl-to-discover.html
		- Component and Logics:
			- Initialization
			- Parent selection
			- Recombination
			- Mutation
			- Survivor Selection
		<img src="/AutoML-Meta/images/automl-evo.jpg" alt="drawing" width="500"/>
		<img src="/AutoML-Meta/images/automl-ea2.jpg" alt="drawing" width="500"/>
	- Legacy:
		- K. Stanley and R. Miikkulainen. Evolving neural networks through augmenting topologies. Evolutionary Computation, 10(2):99–127, 2002. 2
		- D. Floreano, P. Durr, and C. Mattiussi. Neuroevolution: from architectures to learning. Evolutionary Intelligence, 1(1):47–62, 2008
	- Real, E.; Moore, S.; Selle, A.; Saxena, S.; Suematsu, Y. L.; Le, Q.; and Kurakin, A. 2017. Large-scale evolution of image classifiers. ICML'17
	- **AmoebaNet**: E. Real, Q. Le. 2018 Regularized evolution for image classifier architecture search. AAAI'19
		- **Aging evolution**: each genotype has an **age**, always remove the oldest one;
			<img src="/AutoML-Meta/images/AmoebaNet-2.png" alt="drawing" width="400"/>	
		- Search in cell space (CNN = cells x n): each cell 2 inputs, 1 output; (Unlike Nas has normal and reduction cell);
			<img src="/AutoML-Meta/images/AmoebaNet-3.png" alt="drawing" width="400"/>	
		- Mutations: (op or edge);\
			<img src="/AutoML-Meta/images/AmoebaNet-1.png" alt="drawing" width="350"/>	
		- Details:
			- Possible ops: none (identity); 3x3, 5x5 and 7x7 separable (sep.) convo- lutions (convs.); 3x3 average (avg.) pool; 3x3 max pool; 3x3 dilated (dil.) sep. conv.; 1x7 then 7x1 conv. 
			- Evolved with P=100, S=25;
			- During the search phase, each model trained for 25 epochs; N=3/F=24, 1GPU;
	- **The Evolved Transformer**: David R. So, Chen Liang, Quoc V. Le. The Evolved Transformer. 2019
		- **Tournament selection** architecture search and **warm start** it with the Transformer
		- Init with transformer (6 x encoder-cell, 8 x decoder)
		- Search space for encoder and decoder cells:
			- five branch-level search fields (input, normalization, layer, output dimension and activation)
			- one block-level search field (combiner function)
			- one cell-level search field (number of cells).
				<img src="/AutoML-Meta/images/evolve-transformer.png" alt="drawing" width="400"/>	
		- **PDH** (progressive dynamic hurdles);
			- More expensive than Cifar: 1 train: ∼300K training steps, or 10 hours, in the base size when using a single Google TPU V.2 chip;
			- Progressive to save time: fitness greater than h1 after s0 + s1 steps of training are granted an additional s2 number of train steps
		- Search result:\
			<img src="/AutoML-Meta/images/evolve-transformer-1.png" alt="drawing" width="400"/>	
			<img src="/AutoML-Meta/images/evolve-transformer-2.png" alt="drawing" width="400"/>	
		- Experiments: **SOTA** BLEU score of 29.8 on WMT'14 En-De;
			- WMT 2014, Eng-Deu, Eng-Fre, ..., 0.7 BLEU improvement over Transformer on Eng-Deu;
	- Genetic:
		- **TPOT**: https://github.com/EpistasisLab/tpot

## Parameter Sharing (Important Trick!)
- **EAS**: H Cai, T Chen: Efficient architecture search by network transformation, AAAI 2018
	- Initialize with DenseNet, evolve by widen and deepen;
	- State: low-dimensional representation for each architecture;
	- Search space
		- Net2Wider Actor: more units/filters for FC/CNN; (simultaneously decide for **each** layer)
		- Net2Deeper: insert an identity layer in between to keep functionality;
	- Train: RL + RNN-Meta-Controller:\
		<img src="/AutoML-Meta/images/eas.png" alt="drawing" width="400"/>	
	- CIFAR-10: 4.23%, SVHN 1.73%
	- https://github.com/han-cai/eas
- **PathLevel-EAS**: H Cai, S Han: Path-Level Network Transformation for Efficient Architecture Search, ICML'18
	- Insight: meta-controller to modify the path topology of the given network while keeping the merits of reusing weights;
	- Search space: split and replication, replace identity with conv;
	- Search/optimization approach: Tree-LSTM;\
		<img src="/AutoML-Meta/images/path-eas-1.png" alt="drawing" width="400"/>	
		<img src="/AutoML-Meta/images/path-eas-2.png" alt="drawing" width="400"/>
	- Train: ADAM + **REINFORCE**;
	- https://github.com/han-cai/PathLevel-EAS
- **ENAS**: H Pham, M. Guan, B. Zoph, Q. Le. Efficient neural architecture search via parameter sharing. ICML'18
	- Key contribution: Parameter sharing;
	- Search space: CNN, RNN cell design;\
		<img src="/AutoML-Meta/images/enas.png" alt="drawing" width="400"/>
	- Train: ADAM + **REINFORCE**;
	- Experiments: Penn TreeBank: 55.8 Perplexity, CIFAR-10: 2.89%
	- https://github.com/melodyguan/enas/tree/2734eb2657847f090e1bc5c51c2b9cbf0be51887
	- https://github.com/carpedm20/ENAS-pytorch

## Bayesian Optimization
- Performance Prediction;
	- Baker, Bowen, Otkrist, Gupta, Raskar, Ramesh, and Naik, Nikhil. Accelerating neural architecture search using performance prediction. Arxiv, 1705.10823, 2017b.
	- Bowen Baker, Otkrist Gupta, Ramesh Raskar, Nikhil Naik. Accelerating Neural Architecture Search using Performance Prediction. ICLR 2018 Workshop
- **Auto-WEKA**: Lars Kotthoff, Chris Thornton, Holger Hoos, Frank Hutter, and Kevin Leyton-Brown. Auto-WEKA 2.0: Automatic model selection and hyperparameter optimization in WEKA. JMLR'17
	- https://github.com/automl/autoweka
- Eric Xing: Neural architecture search with bayesian optimisation and optimal transport. NIPS 2018
	- Gaussian Process to predict performance from history
	- Measure Network distance from graph theory
	- https://github.com/kirthevasank/nasbot

## Automated ML for other Algorithms
- autoxgboost: Janek Thomas, Stefan Coors and Bernd Bischl (2018). Automatic Gradient Boosting. ICMLW'18
	- https://github.com/ja-thomas/autoxgboost

## Other Applications
- Kary Ho, Andrew Gilbert, Hailin Jin, John Collomosse. Neural Architecture Search for Deep Image Prior. 2020

## Google		
- DeepMind:
	- Brock, Andrew, Lim, Theodore, Ritchie, James M., and Weston, Nick. SMASH: one-shot model architecture search through hypernetworks. ICLR'18.

## Optimization Approaches
- H Liu, K Simonyan, et.al. Hierarchical representations for efficient architecture search, ICLR 2018
- Lingxi Xie and Alan Yuille. Genetic CNN. ICCV'17
	- https://github.com/aqibsaeed/Genetic-CNN
- AutoKeras 2018: Efficient Neural Architecture Search with Network Morphism
- Ye-Hoon Kim, Bhargava Reddy, Sojung Yun, and Chanwon Seo. Nemo : Neuro-evolution with multiobjective optimization of deep neural network for speed and accuracy. ICML'17 Workshop
- Surrogate Model-Based Optimization (SMBO)
	<img src="/AutoML-Meta/images/smbo.jpg" alt="drawing" width="500"/>

	- **PNAS**: C. Liu, B. Zoph, J Shlens, W. Hua, A Yuille, K. Murphy. Progressive neural architecture search. 2017
		- Start from simple;
	- Negrinho, Renato and Gordon, Geoff: Deeparchitect: Automatically designing and training deep architectures, CVPR 2017
		- MCTS
		- https://github.com/negrinho/deep_architect
	- Renqian Luo, Fei Tian, Tao Qin, Enhong Chen, and Tie-Yan Liu. Neural architecture optimization.
- One-Shot Architecture Search

## misc
- Thomas Elsken, Jan-Hendrik Metzen, Frank Hutter. Simple and efficient architecture search for Convolutional Neural Networks. Invited to ICLR'18 Workshop
