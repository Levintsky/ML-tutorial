# Attention Model

## NIPS'19
- Paul Michel, Omer Levy, Graham Neubig. Are Sixteen Heads Really Better than One?
- Yi Tay, Anh Tuan Luu, Aston Zhang, Shuohang Wang, Siu Cheung Hui. Compositional De-Attention Networks
- Joshua Tobin, Wojciech Zaremba, Pieter Abbeel. Geometry-Aware Neural Rendering
- Simao Herdade, Armin Kappeler, Kofi Boakye, Joao Soares. Image Captioning: Transforming Objects into Words
- Drew Hudson, Christopher Manning. Learning by Abstraction: The Neural State Machine
- Karlis Freivalds, Emīls Ozoliņš, Agris Šostaks. Neural Shuffle-Exchange Networks - Sequence Processing in O(n log n) Time
- Vighnesh Shiv, Chris Quirk. Novel positional encodings to enable tree-based transformers
- Da Xu, Chuanwei Ruan, Evren Korpeoglu, Sushant Kumar, Kannan Achan. Self-attention with Functional Time Representation Learning
- Boris Knyazev, Graham W Taylor, Mohamed Amer. Understanding Attention and Generalization in Graph Neural Networks

## NLP
- Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Łukasz Kaiser, and Illia Polosukhin. Attention is all you need. NIPS'17

## Vision: Backbone
- Xiaolong Wang, Ross Girshick, Abhinav Gupta, and Kaiming He. Non-local neural networks. CVPR'18
- Yuhui Yuan and Jingdong Wang. Ocnet: Object context network for scene parsing. arxiv'18
- Han Hu, Zheng Zhang, Zhenda Xie, and Stephen Lin. Local relation networks for image recognition. ICCV'19
- Yue Cao, Jiarui Xu, Stephen Lin, Fangyun Wei, and Han Hu. Gcnet: Non-local networks meet squeeze-excitation networks and beyond. ICCVW'19
- Jun Fu, Jing Liu, Haijie Tian, Yong Li, Yongjun Bao, Zhiwei Fang, and Hanqing Lu. Dual attention network for scene segmentation. CVPR'19
- Prajit Ramachandran, Niki Parmar, Ashish Vaswani, Irwan Bello, Anselm Levskaya, and Jon Shlens. Stand-alone self-attention in vision models. NIPS'19
- Hengshuang Zhao, Jiaya Jia, and Vladlen Koltun. Exploring self-attention for image recognition. CVPR'20
- Irwan Bello, Barret Zoph, Ashish Vaswani, Jonathon Shlens, and Quoc V. Le. Attention augmented convolutional networks, 2020
- Josh Beal, Eric Kim, Eric Tzeng, Dong Huk Park, Andrew Zhai, and Dmitry Kislyuk. Toward transformer-based object detection. arxiv'20
	- Low perf;
- Sixiao Zheng, Jiachen Lu, Hengshuang Zhao, Xiatian Zhu, Zekun Luo, Yabiao Wang, Yanwei Fu, Jianfeng Feng, Tao Xiang, Philip HS Torr, et al. Rethinking semantic segmentation from a sequence-to-sequence perspective with transformers. arxiv'20
	- Low perf;
- Minghao Yin, Zhuliang Yao, Yue Cao, Xiu Li, Zheng Zhang, Stephen Lin, and Han Hu. Disentangled non-local neural networks. ECCV'20
- Aravind Srinivas, Tsung-Yi Lin, Niki Parmar, Jonathon Shlens, Pieter Abbeel, and Ashish Vaswani. Bottleneck transformers for visual recognition. arxiv'21
- ViT series:
	- **ViT**: Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov, Dirk Weissenborn, Xiaohua Zhai, Thomas Unterthiner, Mostafa Dehghani, Matthias Minderer, Georg Heigold, Sylvain Gelly, Jakob Uszkoreit, and Neil Houlsby. An image is worth 16x16 words: Transformers for image recognition at scale. ICLR'21
		- https://github.com/google-research/vision_transformer
		- ImageNet: top-1 77.9%(ViT-B), 76.5%(ViT-L);
		- Requires Large training dataset;
	- **DeiT**: Hugo Touvron, Matthieu Cord, Matthijs Douze, Francisco Massa, Alexandre Sablayrolles, and Herve Jegou. Training data-efficient image transformers & distillation through attention. ICML'21
		- ImageNet: top-1 79.8%(DeiT-S), 83.1%(DeiT-B);
	- Li Yuan, Yunpeng Chen, Tao Wang, Weihao Yu, Yujun Shi, Francis EH Tay, Jiashi Feng, and Shuicheng Yan. Tokens-to-token vit: Training vision transformers from scratch on imagenet. arxiv'21
	- Xiangxiang Chu, Bo Zhang, Zhi Tian, Xiaolin Wei, and Huaxia Xia. Do we really need explicit position encodings for vision transformers? arxiv'21
	- Kai Han, An Xiao, Enhua Wu, Jianyuan Guo, Chunjing Xu, and Yunhe Wang. Transformer in transformer. arxiv'21
	- Wenhai Wang, Enze Xie, Xiang Li, Deng-Ping Fan, Kaitao Song, Ding Liang, Tong Lu, Ping Luo, and Ling Shao. Pyramid vision transformer: A versatile backbone for dense prediction without convolutions. arxiv'21
- **Swin Transformer**: Ze Liu, Yutong Lin, Yue Cao, Han Hu, Yixuan Wei, Zheng Zhang, Stephen Lin, Baining Guo. Swin Transformer: Hierarchical Vision Transformer using Shifted Windows. ICCV'21
	- MARR prize winner; beats old SOTA a lot on all detection and segmentation tasks;
	- Key insight:
		- Shifted window: always linear to image size (ViT square), cyclic shift to speed up;
		- Multi-scale by patch merging;
		- Relative position bias;
	- For object detection:
		- HTC++, instaboost, multi-scale training, soft-NMS;
	- https://github.com/microsoft/Swin-Transformer
	- https://youtu.be/udY0GlYXXbE
	- Perf:
		- ImageNet: top-1 81.3%(Swin-T), 84.5%(Swin-L), better than EffNet, RegNet, ViT, DeiT;
		- COCO (mini-val): AP-box 58.0%, AP-Mask 50.4%, better than Cascade R-CNN, ATSS, RepPoint, Sparse R-CNN;
		- COCO (test): AP-box 58.7%, AP-Mask 51.1%
		- ADE20K Seg: 53.5 mIoU, 62.8 test score, based on UperNet (mmseg);

## Vision: Head
- Han Hu, Jiayuan Gu, Zheng Zhang, Jifeng Dai, and Yichen Wei. Relation networks for object detection. CVPR'18
	- https://github.com/msracver/Relation-Networks-for-Object-Detection
	- Relative position encoding: log(dx/w), log(dy/h)
- Jiayuan Gu, Han Hu, Liwei Wang, Yichen Wei, and Jifeng Dai. Learning region features for object detection. ECCV'18
- Detection:
	- Nicolas Carion, Francisco Massa, Gabriel Synnaeve, Nicolas Usunier, Alexander Kirillov, and Sergey Zagoruyko. End-to-End Object Detection with Transformers. ECCV'20
		- https://github.com/facebookresearch/detr
		- CNN ResNet-50 backbone - encoder (with modified position enc) - decoder (learned-fixed-queries) - FFN;
			<img src="/NLP/images/detr-1.png" alt="drawing" width="450"/>	
			<img src="/NLP/images/detr-2.png" alt="drawing" width="450"/>	
			<img src="/NLP/images/detr-3.png" alt="drawing" width="450"/>
	- Cheng Chi, Fangyun Wei, and Han Hu. Relationnet++: Bridging visual representations for object detection via transformer decoder. NeurIPS'20