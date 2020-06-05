# Video Understanding

## Unclassified
- Dahua Lin. Trajectory Convolution for Action Recognition. NIPS'18

## Benchmarks
- Google:
	- **Sports-1M**: Andrej Karpathy; George Toderici; Sanketh Shetty; Thomas Leung; Rahul Sukthankar; Li Fei-Fei. Large-scale Video Classification with Convolutional Neural Networks. CVPR 2014;
		- 1 Million videos, 487 classes x (1k-3k) videos per class; test: 70% training, 10% val, 20% testing;
		- 360 x 640 resolution
	- **YouTube-8M**: Sami Abu-El-Haija, Nisarg Kothari, Joonseok Lee, Paul Natsev, George Toderici, Balakrishnan Varadarajan, Sudheendra Vijayanarasimhan. YouTube-8M: A Large-Scale Video Classification Benchmark
		- https://research.google.com/youtube8m/
		- 6.1 Million, 350,000 hours
		- 2.6 billion audio/visual features
		- 3,862 classes (from knowledge graph: https://developers.google.com/knowledge-graph/)
	- **Kinetics**: Quo Vadis, Action Recognition? A New Model and the Kinetics Dataset, CVPR 2017
		- 240k train, 20k val, 400 action classes, 10s each clip;
		- Classification;
		- De-duplicate: word synonymy; class by class, a clip per video + inception-V1 feature after average pooling, 25 sampled frames, cosine similarity matrix;
		- Dataset bias: gender
		- Baseline: ConvNet + LSTM, Two-Stream, 3D ConvNets
	- W. Kay, J. Carreira, K. Simonyan, B. Zhang, C. Hillier, S. Vijayanarasimhan, F. Viola, T. Green, T. Back, P. Natsev, et al. The kinetics human action video dataset. 2017
	- **AVA**: C. Gu, C. Sun, D. A. Ross, C. Vondrick, C. Pantofaru, Y. Li, S. Vijayanarasimhan, G. Toderici, S. Ricco, R. Sukthankar, et al. AVA: A video dataset of spatio-temporally localized atomic visual actions. CVPR 2018
		- https://research.google.com/ava/index.html
		- 80 categories
		- 15 min long clips from 430 movies
		- 1.62M action labels
- Other large-scale:
	- **Something something**: Goyal, R., Kahou, S.E., Michalski, V., Materzynska, J., Westphal, S., Kim, H., Haenel, V., Fruend, I., Yianilos, P., Mueller-Freitag, M., et al.: The something something video database for learning and evaluating visual common sense. ICCV 2017
		- Need to understand physical interactions
	- **Activitynet**: F. Caba Heilbron, V. Escorcia, B. Ghanem, and J. C. Niebles. Activitynet: A large-scale video benchmark for human activity understanding. CVPR 2015
	- **Charades**: Sigurdsson, G.A., Varol, G., Wang, X., Farhadi, A., Laptev, I., Gupta, A.: Hollywood in homes: Crowdsourcing data collection for activity understanding. ECCV 2016
- **HMDB-51**: H. Kuehne, H. Jhuang, E. Garrote, T. Poggio, and T. Serre. HMDB: a large video database for human motion recognition. ICCV 2011
	- 51 categories, 7,000 annotated
- **UCF-101**: K. Soomro, A. R. Zamir, and M. Shah. Ucf101: A dataset of 101 human actions classes from videos in the wild. 2012
	- 101 categories, 13k clips, 27 hours
- **MPII-Pose**: M. Andriluka, L. Pishchulin, P. Gehler, and B. Schiele. 2d human pose estimation: New benchmark and state of the art analysis. CVPR 2014
	- 25k images, 40k people
	- 410 human activities
- **ACT**: X. Wang, A. Farhadi, and A. Gupta. Actions transformations. CVPR 2016
- M. Monfort, A. Andonian, B. Zhou, K. Ramakrishnan, S.A. Bargal, Y. Yan, L. Brown, Q. Fan, D. Gutfreund, C. Vondrick, et al. Moments in time dataset: one million videos for event understanding. TPAMI, 2019.
- **Slac**: H. Zhao, Z. Yan, H. Wang, L. Torresani, and A. Torralba. Slac: A sparsely labeled dataset for action classification and localization. 
- **YouCook II**: L. Zhou, C. Xu, and J. J. Corso. Towards automatic learning of procedures from web instructional videos. AAAI 2018
- **Cooking**: David Chen, William Dolan. Collecting Highly Parallel Data for Paraphrase Evaluation. ACL 2011
	- 2,089 videos; 85,550 English descriptions

## Legacy, Hand-Designed
- P. Dollar, V. Rabaud, G. Cottrell, and S. Belongie. Behavior recognition via sparse spatio-temporal features. ICCV'05
- **STIP**: I. Laptev and T. Lindeberg. Space-time interest points. ICCV 2003
- S. Sadanand and J. Corso. Action bank: A high-level representation of activity in video. CVPR 2012
- H. Wang and C. Schmid. Action recognition with improved trajectories. ICCV 2013

## Classification, Action Recognition
- Matching, Attentional, optical flow:
	- Karen Simonyan and Andrew Zisserman. Two-stream convolutional networks for action recognition in videos. NIPS'14
	- Andrew Zisserman Christoph Feichtenhofer, Axel Pinz. Convolutional two-stream network fusion for video action recognition. CVPR'16
	- M Shan and N Atanasov. A spatiotemporal model with visual attention for video classification. 2017
	- X Wang, R Girshick, A Gupta, K He. Non-local Neural Networks, CVPR'18
		- Video classification
		- THW 512 dimension, attention with every other location
		- Softmax sum;
		<img src="/CV-2D/images/video/non-local.png" alt="drawing" width="500"/>
	- **CPNet**: Xingyu Liu, Joon-Young Lee, Hailin Jin. Learning Video Representations from Correspondence Proposals. CVPR'19 oral
		- Insight: hard attention by kNN;
		- https://github.com/xingyul/cpnet
		- Model:\
			<img src="/CV-2D/images/video/cpnet-1.png" alt="drawing" width="400"/>
		- Correspondence Embedding layer:\
			<img src="/CV-2D/images/video/cpnet-2.png" alt="drawing" width="400"/>
	- C Feichtenhofer, H Fan, J Malik, K He. SlowFast Networks for Video Recognition, ICCV'19
		- Slow pathway: 2 fps;
		- Fast pathway: 16 fps; lightweight computation; (same net, small hyper)
		<img src="/CV-2D/images/video/slowfast.png" alt="drawing" width="500"/>
	- New attention:
		- https://github.com/takatosp1/pytorch-CycleGAN-and-pix2pix/commit/d10e1f6b090ee5efb1fa5418c47ba16389f4d4b4#diff-ac5552fd6a3c08ad22387efbe42d137d
	- C Sun, A Myers, C Vondrick, K Murphy and C Schmid. VideoBERT: A Joint Model for Video and Language Representation Learning. ICCV'19
		- Vector-quantization: S3D for feature extraction;
		- WordPiece for text (ASR API);
		- BLEU-4 1.42 to 5.42 on YouCook II;
		<img src="/CV-2D/images/video/videobert-1.png" alt="drawing" width="600"/>
		<img src="/CV-2D/images/video/videobert-2.png" alt="drawing" width="600"/>
- C3D:
	- Andrej Karpathy, George Toderici, Sanketh Shetty, Thomas Leung, Rahul Sukthankar, and Li Fei-Fei. Large-scale video classification with convolutional neural networks. CVPR'14
	- Du Tran, Lubomir Bourdev, Rob Fergus, Lorenzo Torresani, and Manohar Paluri. Learning spatiotemporal features with 3d convolutional networks. ICCV'15
	- **ArtNet**: Limin Wang, Wei Li, Wen Li, and Luc Van Gool. Appearance-and-relation networks for video classification. CVPR'18
		- Insight: C3D w/o correspondence, then concat;
		<img src="/CV-2D/images/video/artnet.png" alt="drawing" width="600"/>
	- Mohammadreza Zolfaghari, Kamaljeet Singh, and Thomas Brox. Eco: Efficient convolutional network for online video understanding. ECCV'18
	- **S3D**: S. Xie, C. Sun, J. Huang, Z. Tu, and K. Murphy. Rethinking spatiotemporal feature learning for video understanding. ECCV'18
		- I3D (inflate the 2D conv in Inception)
		- Bottom-Heavy-I3D: 3D temporal-conv at bottom, 2D-Conv at top
		- Top-Heavy-I3D: 2D-conv at bottom, 3D temporal-conv at top (faster, more accurate)
		- S3D: 7x7x7 Conv -> 1x7x7 Conv + 7x1x1 Conv
		- With optical-flow: 77.2% top-1, 93.0% top-5
		<img src="/CV-2D/images/video/s3d-1.png" alt="drawing" width="600"/>
		<img src="/CV-2D/images/video/s3d-2.png" alt="drawing" width="600"/>
	- **R(2+1)D**: D. Tran, H. Wang, L. Torresani, J. Ray, Y. LeCun, and M. Paluri. A closer look at spatiotemporal convolutions for action recognition. CVPR'18
	- **CSN**: Du Tran. Video Classification with Channel-Separated Convolutional Networks. ICCV'19
		- Bottleneck: 1x1x1 -> 3x3x3 -> 1x1x1
		- ip-CSN: 1x1x1 -> 1x1x1 -> 3x3x3(dw) -> 1x1x1
		- ir-CSN: 1x1x1 -> 1x1x1 -> 3x3x3(dw) -> 1x1x1
		- Group Convolution.
		- Experiments:
			- Kinetics: 71.8% (ip-CSN, res-101), 71.3% (ir-CSN, res-101), 70.6% (ResNet3D); 78.5% top1, 93.4% top5 with Sports1M pretrain
			- Sports1M: 75.5%, 92.7% (ir-CSN res-152)
		<img src="/CV-2D/images/video/csn1.png" alt="drawing" width="450"/>
		<img src="/CV-2D/images/video/csn2.png" alt="drawing" width="450"/>
	- Chao-Yuan Wu, Ross Girshick, Kaiming He, Christoph Feichtenhofer, Philipp Krähenbühl. A Multigrid Method for Efficiently Training Video Models. CVPR'20
	- Fanyi Xiao, Yong Jae Lee, Kristen Grauman, Jitendra Malik, Christoph Feichtenhofer. Audiovisual SlowFast Networks for Video Recognition. arxiv'20
	- **X3D**: Christoph Feichtenhofer. X3D: Expanding Architectures for Efficient Video Recognition. CVPR'20
- RNN, LSTM:
	- Jeffrey Donahue, Lisa Anne Hendricks, Sergio Guadarrama, Marcus Rohrbach, Subhashini Venugopalan, Kate Saenko, and Trevor Darrell. Long-term recurrent convolutional networks for visual recognition and description. CVPR'15
	- Joe Yue-Hei Ng, Matthew Hausknecht, Sudheendra Vijayanarasimhan, Oriol Vinyals, Rajat Monga, and George Toderici. Beyond short snippets: Deep networks for video classification. CVPR'15
- MSRA:
	- X Zhu, Y Wang, J Dai, L Yuan, and Y Wei. Flow-Guided Feature Aggregation for Video Object Detection. ICCV'17
	- X Zhu, J Dai, L Yuan, and Y Wei. Towards High Performance Video Object Detection. CVPR'18 
	- Z Zhang, Dazhi Cheng, X Zhu, S Lin, and J Dai. Integrated Object Detection and Tracking with Tracklet-Conditioned Detection. 2018
- **P3D**: Z. Qiu, T. Yao, , and T. Mei. Learning spatio-temporal representation with pseudo-3d residual networks. ICCV 2017
- **ARTNet**: H. Wang and C. Schmid. Action recognition with improved trajectories. CVPR 2018
- K. Hara, H. Kataoka, and Y. Satoh. Can spatiotemporal 3d cnns retrace the history of 2d cnns and imagenet? CVPR 2018
- **MFNet**: Y. Chen, Y. Kalantidis, J. Li, S. Yan, and J. Feng. Multi-fiber networks for video recognition. ECCV'18.
- R Gao, B Xiong, K Grauman. Im2Flow: Motion Hallucination from Static Images for Action Recognition. CVPR'18

## Multimodal
- Y. Aytar, C. Vondrick, and A. Torralba. Soundnet: Learning sound representations from unlabeled video. NIPS 2016.
- A. Owens, P. Isola, J. McDermott, A. Torralba, E. H. Adelson, and W. T. Freeman. Visually indicated sounds. CVPR 2016
- A. Owens, J. Wu, J. H. McDermott, W. T. Freeman, and A. Torralba. Ambient sound provides supervision for visual learning. ECCV 2016
- Instructional:
	- J. Malmaud, J. Huang, V. Rathod, N. Johnston, A. Rabinovich, and K. Murphy. What's cooking? interpreting cooking videos using text, speech and vision. NAACL 2015
	- J.-B. Alayrac, P. Bojanowski, N. Agrawal, J. Sivic, I. Laptev, and S. Lacoste-Julien. Unsupervised learning from narrated instruction videos. CVPR'16

## Video Caption
- Video caption: https://github.com/xiadingZ/video-caption.pytorch
- R. Krishna, K. Hata, F. Ren, L. Fei-Fei, and J. C. Niebles. Dense-Captioning events in videos. ICCV 2017
- **SOA**: L. Zhou, Y. Zhou, J. J. Corso, R. Socher, and C. Xiong. End-to-end dense video captioning with masked transformer. CVPR 2018
	- SOA on YouCook II dataset
- A. Rohrbach, M. Rohrbach, W. Qiu, A. Friedrich, M. Pinkal, and B. Schiele. Coherent multi-sentence video description with variable level of detail. GCPR 2014

## Video Prediction
- Google, Berkeley:
	- M. Babaeizadeh, C. Finn, D. Erhan, R. H. Campbell, and S. Levine. Stochastic variational video prediction. ICLR 2018
	- A. X. Lee, R. Zhang, F. Ebert, P. Abbeel, C. Finn, and S. Levine. Stochastic adversarial video prediction. 2018
- FAIR:
	- M. Mathieu, C. Couprie, and Y. LeCun. Deep multi-scale video prediction beyond mean square error. ICLR 2016
	- E. Denton and R. Fergus. Stochastic video generation with a learned prior. ICML 2018
- NVIDIA:
	- **MoCoGAN**: S. Tulyakov, M.-Y. Liu, X. Yang, and J. Kautz. MoCoGAN: Decomposing motion and content for video generation.
- CMU:
	- J. Walker, C. Doersch, A. Gupta, and M. Hebert. An uncertain future: Forecasting from static images using variational autoencoders. ECCV 2016
	- I. Misra, C. L. Zitnick, and M. Hebert. Shuffle and learn: unsupervised learning using temporal order verification. In ECCV, 2016
- MIT:
	- T. Xue, J. Wu, K. Bouman, and B. Freeman. Visual dynamics: Probabilistic future frame synthesis via cross convolutional networks. NIPS 2016
	- C. Vondrick, H. Pirsiavash, and A. Torralba. Generating videos with scene dynamics. In NeurIPS, 2016.
- Ruben Villegas, Arkanath Pathak, Harini Kannan, Dumitru Erhan, Quoc V Le, Honglak Lee. High Fidelity Video Prediction with Large Stochastic Recurrent Neural Networks. NIPS'19
