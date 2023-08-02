# Video Understanding

## Resources
- Dahua Lin:
	- https://drive.google.com/file/d/1hX6myOOpRF1hT0Qcb4Vje7EVsUGTeZF_/view
	- https://youtu.be/gxh4tT0JD_A

## Unclassified
- D Lin. Trajectory Convolution for Action Recognition. NIPS'18
- A summary: https://zhuanlan.zhihu.com/p/149340496

## Benchmarks
- Google:
	- YouTube-8M: A Large-Scale Video Classification Benchmark
		- https://research.google.com/youtube8m/
		- 6.1 Million, 350,000 hours
		- 2.6 billion audio/visual features
		- 3,862 classes (from knowledge graph: https://developers.google.com/knowledge-graph/)
	- kinetics: W. Kay, et.al. 2017
	- **AVA**: CVPR'18
		- https://research.google.com/ava/index.html
		- 80 categories
		- 15 min long clips from 430 movies
		- 1.62M action labels
- Other large-scale:
	- Something-something: ICCV'17
		- Need to understand physical interactions
	- ActivityNet: CVPR-15
	- Charades ECCV'16
- MSVD: D Chen, W Dolan. Collecting Highly Parallel Data for Paraphrase Evaluation. ACL'11
	- 2,089 videos; 85,550 English descriptions
- HMDB-51: MIT. HMDB: a large video database for human motion recognition. ICCV'11
	- 51 categories, 7,000 annotated
- UCF-101: K. Soomro, A. R. Zamir, and M. Shah. Ucf101: A dataset of 101 human actions classes from videos in the wild. 2012
	- 101 categories, 13k clips, 27 hours
- **Sports-1M**: A Karpathy; et.al. CVPR'14;
	- 1 Million videos, 487 classes x (1k-3k) videos per class; test: 70% training, 10% val, 20% testing;
	- 360 x 640 resolution
- **ACT**: X. Wang, A. Farhadi, and A. Gupta. Actions transformations. CVPR'16
- **Kinetics**: Quo Vadis, Action Recognition? A New Model and the Kinetics Dataset, CVPR'17
	- 240k train, 20k val, 400 action classes, 10s each clip;
	- Classification;
	- De-duplicate: word synonymy; class by class, a clip per video + inception-V1 feature after average pooling, 25 sampled frames, cosine similarity matrix;
	- Dataset bias: gender
	- Baseline: ConvNet + LSTM, Two-Stream, 3D ConvNets
- **Slac**: H. Zhao, Z. Yan, H. Wang, L. Torresani, and A. Torralba. Slac: A sparsely labeled dataset for action classification and localization. 
- **YouCook II**: L Zhou, C Xu, and J Corso. Towards automatic learning of procedures from web instructional videos. AAAI'18
- Google. Moments in time dataset: one million videos for event understanding. PAMI'19

## Backbone
- Legacy/Hand-Designed
	- P. Dollar, V. Rabaud, G. Cottrell, and S. Belongie. Behavior recognition via sparse spatio-temporal features. ICCV'05
	- STIP: I. Laptev and T. Lindeberg. Space-time interest points. ICCV 2003
	- S. Sadanand and J. Corso. Action bank: A high-level representation of activity in video. CVPR 2012
	- H. Wang and C. Schmid. Action recognition with improved trajectories. ICCV'13
- CNN-2d + pooling
	- 2-stream: K Simonyan and A Zisserman. Two-stream convolutional networks for action recognition in videos. NIPS'14
		- rgb-cnn + flow-cnn
	- A Zisserman, C Feichtenhofer, A Pinz. Convolutional two-stream network fusion for video action recognition. CVPR'16
	- SlowFast: C Feichtenhofer, H Fan, J Malik, K He. SlowFast Networks for Video Recognition, ICCV'19
- CNN + RNN:
	- J Donahue, et. al. Long-term recurrent convolutional networks for visual recognition and description. CVPR'15
	- Joe Yue-Hei Ng, et. al. Beyond short snippets: Deep networks for video classification. CVPR'15
- CNN + Transformer:
	- X Wang, et. al. Non-local Neural Networks, CVPR'18
	- VideoBERT: ICCV'19
		- Vector-quantization: S3D for feature extraction;
		- WordPiece for text (ASR API);
		- BLEU-4 1.42 to 5.42 on YouCook II;
- Conv3D, C3D
	- A Karpathy, et. al. Large-scale video classification with convolutional neural networks. CVPR'14
	- C3D: D Tran, L Bourdev, R Fergus, L Torresani, and M Paluri. Learning spatiotemporal features with 3d convolutional networks. ICCV'15

## Classification, Action Recognition
- Matching, Attentional, optical flow:
	- M Shan and N Atanasov. A spatiotemporal model with visual attention for video classification. 2017
	- **CPNet**: X Liu, J Lee, H Jin. Learning Video Representations from Correspondence Proposals. CVPR'19 oral
		- Insight: hard attention by kNN;
		- https://github.com/xingyul/cpnet
		- Model:\
			<img src="/CV-2D/images/video/cpnet-1.png" alt="drawing" width="400"/>
		- Correspondence Embedding layer:\
			<img src="/CV-2D/images/video/cpnet-2.png" alt="drawing" width="400"/>
- C3D:
	- ArtNet: L Wang, W Li, W Li, and L Van Gool. Appearance-and-relation networks for video classification. CVPR'18
		- Insight: C3D w/o correspondence, then concat;
	- M Zolfaghari, K Singh, and T Brox. Eco: Efficient convolutional network for online video understanding. ECCV'18
	- S3D: S Xie, C Sun, J Huang, Z Tu, and K Murphy. Rethinking spatiotemporal feature learning for video understanding. ECCV'18
		- I3D (inflate the 2D conv in Inception)
		- Bottom-Heavy-I3D: 3D temporal-conv at bottom, 2D-Conv at top
		- Top-Heavy-I3D: 2D-conv at bottom, 3D temporal-conv at top (faster, more accurate)
		- S3D: 7x7x7 Conv -> 1x7x7 Conv + 7x1x1 Conv
		- With optical-flow: 77.2% top-1, 93.0% top-5
	- R(2+1)D: Meta. A closer look at spatiotemporal convolutions for action recognition. CVPR'18
	- CSN: Meta. Video Classification with Channel-Separated Convolutional Networks. ICCV'19
		- Bottleneck: 1x1x1 -> 3x3x3 -> 1x1x1
		- ip-CSN: 1x1x1 -> 1x1x1 -> 3x3x3(dw) -> 1x1x1
		- ir-CSN: 1x1x1 -> 1x1x1 -> 3x3x3(dw) -> 1x1x1
		- Group Convolution.
		- Experiments:
			- Kinetics: 71.8% (ip-CSN, res-101), 71.3% (ir-CSN, res-101), 70.6% (ResNet3D); 78.5% top1, 93.4% top5 with Sports1M pretrain
			- Sports1M: 75.5%, 92.7% (ir-CSN res-152)
	- Meta. A Multigrid Method for Efficiently Training Video Models. CVPR'20
	- Meta. Audiovisual SlowFast Networks for Video Recognition. arxiv'20
	- X3D: C Feichtenhofer. X3D: Expanding Architectures for Efficient Video Recognition. CVPR'20
- MSRA:
	- X Zhu, Y Wang, J Dai, L Yuan, and Y Wei. Flow-Guided Feature Aggregation for Video Object Detection. ICCV'17
	- X Zhu, J Dai, L Yuan, and Y Wei. Towards High Performance Video Object Detection. CVPR'18 
	- Z Zhang, Dazhi Cheng, X Zhu, S Lin, and J Dai. Integrated Object Detection and Tracking with Tracklet-Conditioned Detection. 2018
- P3D: Z. Qiu, T. Yao, and T. Mei. Learning spatio-temporal representation with pseudo-3d residual networks. ICCV 2017
- ARTNet: H. Wang and C. Schmid. Action recognition with improved trajectories. CVPR 2018
- K. Hara, H. Kataoka, and Y. Satoh. Can spatiotemporal 3d cnns retrace the history of 2d cnns and imagenet? CVPR 2018
- MFNet: Y. Chen, Y. Kalantidis, J. Li, S. Yan, and J. Feng. Multi-fiber networks for video recognition. ECCV'18.
- R Gao, B Xiong, K Grauman. Im2Flow: Motion Hallucination from Static Images for Action Recognition. CVPR'18

## Multimodal
- MIT. Soundnet: Learning sound representations from unlabeled video. NIPS 2016.
- MIT. Visually indicated sounds. CVPR 2016
- MIT. Ambient sound provides supervision for visual learning. ECCV 2016
- Instructional:
	- Google. What's cooking? interpreting cooking videos using text, speech and vision. NAACL 2015
	- Unsupervised learning from narrated instruction videos. CVPR'16

## Video Caption
- Video caption: https://github.com/xiadingZ/video-caption.pytorch
- Stanford. Dense-Captioning events in videos. ICCV 2017
- Salesforce. End-to-end dense video captioning with masked transformer. CVPR'18
	- SOA on YouCook II dataset
- A. Rohrbach, et. al. Coherent multi-sentence video description with variable level of detail. GCPR'14

## Video Prediction
- Google, Berkeley:
	- Google. Stochastic variational video prediction. ICLR 2018
	- Google. Stochastic adversarial video prediction. 2018
- FAIR:
	- M. Mathieu, C. Couprie, and Y. LeCun. Deep multi-scale video prediction beyond mean square error. ICLR 2016
	- E. Denton and R. Fergus. Stochastic video generation with a learned prior. ICML'18
- MoCoGAN: S Tulyakov, M Liu, X Yang, and J Kautz. MoCoGAN: Decomposing motion and content for video generation.
- CMU:
	- CMU. An uncertain future: Forecasting from static images using variational autoencoders. ECCV'16
	- CMU. Shuffle and learn: unsupervised learning using temporal order verification. ECCV'16
- MIT:
	- T. Xue, J. Wu, K. Bouman, and B. Freeman. Visual dynamics: Probabilistic future frame synthesis via cross convolutional networks. NIPS 2016
	- C. Vondrick, H. Pirsiavash, and A. Torralba. Generating videos with scene dynamics. In NeurIPS, 2016.
- R Villegas, A Pathak, H Kannan, D Erhan, Q Le, H Lee. High Fidelity Video Prediction with Large Stochastic Recurrent Neural Networks. NIPS'19
