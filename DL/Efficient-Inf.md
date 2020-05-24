# Mobile Vision, Fast

## Sequential Inference
- Yang Song, Chenlin Meng, Renjie Liao, Stefano Ermon. Nonlinear Equation Solving: A Faster Alternative to Feedforward Computation. 2020

## Fast
- Separable:
	-  F. Chollet. Xception: Deep learning with depthwise separable convolutions. CVPR'17

## Prune/Compress
- Chen Lin, Zhao Zhong, Wei Wu, Junjie Yan. Synaptic Strength For Convolutional Neural Network. NIPS'18
- **Song Han**:
	- S. Han, H. Mao, and W. J. Dally. Deep compression: Compressing deep neural networks with pruning, trained quantization and huffman coding. 2015
	- S. Han, J. Pool, J. Tran, and W. Dally. Learning both weights and connections for efficient neural network. NIPS'15
	- **Squeezenet**: F. N. Iandola, S. Han, M. W. Moskewicz, K. Ashraf, W. J.Dally, and K. Keutzer. Squeezenet: Alexnet-level accuracy with 50x fewer parameters and 0.5 mb model size. 2016
	- Song Han, Xingyu Liu, Huizi Mao, Jing Pu, Ardavan Pedram, Mark A Horowitz, and William J Dally. EIE: efficient inference engine on compressed deep neural network. ISCA'16
	- Song Han, Huizi Mao, and William J Dally. Deep compression: Compressing deep neural networks with pruning, trained quantization and huffman coding. ICLR'16
	- Xingyu Liu, Jeff Pool, Song Han, William J. Dally. Efficient Sparse-Winograd Convolutional Neural Networks. ICLR'18
		- Winograd's minimal filtering algorithm (Lavin, 2015) and network pruning (Han et al., 2015)
- Quantization:
	- D. Soudry, I. Hubara, and R. Meir. Expectation backpropagation: Parameter-free training of multilayer neural networks with continuous or discrete weights. NIPS'14
	- M. Rastegari, V. Ordonez, J. Redmon, and A. Farhadi. Xnornet: Imagenet classification using binary convolutional neural networks. ECCV'16
	- J. Wu, C. Leng, Y. Wang, Q. Hu, and J. Cheng. Quantized convolutional neural networks for mobile devices. CVPR'16
	- A. Zhou, A. Yao, Y. Guo, L. Xu, and Y. Chen. Incremental network quantization: Towards lossless cnns with lowprecision weights. 2017
	- S. Zhou, Y. Wu, Z. Ni, X. Zhou, H. Wen, and Y. Zou. Dorefa-net: Training low bitwidth convolutional neural networks with low bitwidth gradients. 2016
- Factorization:
	- M. Jaderberg, A. Vedaldi, and A. Zisserman. Speeding up convolutional neural networks with low rank expansions. 2014
	- J. Jin, A. Dundar, and E. Culurciello. Flattened convolutional neural networks for feedforward acceleration.
- W. Wen, C. Wu, Y. Wang, Y. Chen, and H. Li. Learning structured sparsity in deep neural networks. NIPS'16

## NIPS'19
- Weizhe Hua, Yuan Zhou, Christopher De Sa, Zhiru Zhang, G. Edward Suh. Channel Gating Neural Networks
- Zhijian Liu, Haotian Tang, Yujun Lin, Song Han. Point-Voxel CNN for Efficient 3D Deep Learning
- Zhonghui You, Kun Yan, Jinmian Ye, Meng Ma, Ping Wang. Gate Decorator: Global Filter Pruning Method for Accelerating Deep Convolutional Neural Networks
- Georgios Detorakis, Sourav Dutta, Abhishek Khanna, Matthew Jerry, Suman Datta, Emre O Neftci. Inherent Weight Normalization in Stochastic Neural Networks
- Shangyu Chen, Wenya Wang, Sinno Jialin Pan. MetaQuant: Learning to Quantize by Learning to Penetrate Non-differentiable Quantization
- Shupeng Gui, Haotao N Wang, Haichuan Yang, Chen Yu, Zhangyang Wang, Ji Liu. Model Compression with Adversarial Robustness: A Unified Optimization Framework
- Yixing Xu, Yunhe Wang, Hanting Chen, Kai Han, Chunjing XU, Dacheng Tao, Chang Xu. Positive-Unlabeled Compression on the Cloud
