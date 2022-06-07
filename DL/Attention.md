# Attention Model

## Attention Layers
- Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Łukasz Kaiser, and Illia Polosukhin. Attention is all you need. NIPS'17
	- A very good intro: http://jalammar.github.io/illustrated-transformer/
	- Explanation with Pytorch: http://nlp.seas.harvard.edu/2018/04/03/attention.html
	- https://github.com/Kyubyong/transformer
	- Pytorch: https://github.com/jadore801120/attention-is-all-you-need-pytorch
		<img src="/NLP/images/transformer1.png" alt="drawing" width="500"/>
		<img src="/NLP/images/transformer2.png" alt="drawing" width="600"/>
- Tao Y, Sun Q, Du Q, et al. Nonlocal Neural Networks, Nonlocal Diffusion and Nonlocal Modeling. NIPS'18
	- Insight: non-local attention has damping effect (eigenvalue decreases during training);
	- Change formulation to make up the damping;
- Paul Michel, Omer Levy, Graham Neubig. Are Sixteen Heads Really Better than One?. NeurIPS'19
	- https://github.com/pmichel31415/are-16-heads-really-better-than-1
	- At test time, a lot of head can be removed;
	- Greedy alg for pruning;

## NIPS'19
- Yi Tay, Anh Tuan Luu, Aston Zhang, Shuohang Wang, Siu Cheung Hui. Compositional De-Attention Networks
- Simao Herdade, Armin Kappeler, Kofi Boakye, Joao Soares. Image Captioning: Transforming Objects into Words
- Drew Hudson, Christopher Manning. Learning by Abstraction: The Neural State Machine
- Karlis Freivalds, Emīls Ozoliņš, Agris Šostaks. Neural Shuffle-Exchange Networks - Sequence Processing in O(n log n) Time
- Vighnesh Shiv, Chris Quirk. Novel positional encodings to enable tree-based transformers
- Da Xu, Chuanwei Ruan, Evren Korpeoglu, Sushant Kumar, Kannan Achan. Self-attention with Functional Time Representation Learning
- Boris Knyazev, Graham W Taylor, Mohamed Amer. Understanding Attention and Generalization in Graph Neural Networks

## Position Encoding
- Original in transformer:\
	<img src="/NLP/images/pos-enc.png" alt="drawing" width="500"/>	
- Learned Position Encoding: Jonas Gehring, Michael Auli, David Grangier, Denis Yarats, Yann N. Dauphin. Convolutional Sequence to Sequence Learning. 2017
- Xiangxiang Chu, Bo Zhang, Zhi Tian, Xiaolin Wei, and Huaxia Xia. Do we really need explicit position encodings for vision transformers? arxiv'21
	- https://github.com/Meituan-AutoML/CPVT

## NLP
- Good Summaries
	- https://lilianweng.github.io/lil-log/2018/06/24/attention-attention.html
	- https://lilianweng.github.io/lil-log/2019/01/31/generalized-language-models.html
	- https://lilianweng.github.io/lil-log/2020/04/07/the-transformer-family.html
	- https://zhuanlan.zhihu.com/p/109992475
- Legacy:
	- D Bahdanau, K Cho, and Y Bengio. Neural machine translation by jointly learning to align and translate. arxiv'14
	- **ELMO**: Matthew E. Peters, Mark Neumann, Mohit Iyyer, Matt Gardner, Christopher Clark, Kenton Lee, Luke Zettlemoyer. Deep contextualized word representations. NAACL'18
		- https://allennlp.org/elmo
		- ELMo (Embeddings from Language Models)
		- bidirectional LSTM, predict next/last word
- Rami Al-Rfou, Dokook Choe, Noah Constant, Mandy Guo, Llion Jones. Character-Level Language Modeling with Deeper Self-Attention. AAAI'19
- Self-supervised learning:
	- **BERT**: Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova. BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding. ACL'19
		- **Bidirectional Transformer** as model (L=12 for Base, L=24 for Large);
		- **Embedding**: sum of following three;
			- **WorldPiece** (Wu et al 2016): 30,000 tokens;
			- Learned positional embedding;
			- Segment embedding; (same sentence share same emb?)
		- Pretrain tasks:
			- Masked LM (15%): in the 15%, 10% replaced with other words, 10% unchanged, 80% [MASK]. So the model has to attend to every word.
			- Given two sentences concatenated together. Predict if B is next to A (50%). Achieve 97-98% accuracy;
		- Pretrain:
			- BooksCorpus (800M) + Wiki (2,500M), 1 Billion only sentence level;
			- BERT-BASE: 4 Cloud TPUs (16 chips), 4 days;
			- BERT-LARGE: 4 Cloud TPUs (64 chips), 4 days;
		- Fine-tunning:
			- First token [CLS], finally used as classifier after FC and softmax;
		<img src = '/Weak-Unsupervised/images/bert.png' width = '600px'>
	- Y You, J Li, J Hseu, X Song, J Demmel, C Hsieh. Reducing BERT Pre-Training Time from 3 Days to 76 Minutes. 2019
		- Batch-size: 64k - 32k
		- Optimizer: **LAMB** (Layer-wise Adaptive Moments optimizer for Batch training)
		- Iteration: 1m -> 8,599
	- **RoBERTa**: Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike Lewis, Luke Zettlemoyer, Veselin Stoyanov. RoBERTa: A Robustly Optimized BERT Pretraining Approach. 2019
		- Difference from BERT:
			- More data (160G v.s. Bert 16G): Books Corpus + English Wikipedia 16GB; CC-New (76G); OpenWebText (38G); Stories (31GB);
		- More Steps; (500k steps)
		- Large Batch; (8000 v.s. BERT 256)
		- ADAM (0.98 v.s. BERT 0.999)
	- **GPT**: A Radford, K Narasimhan, T Salimans, I Sutskever. Improving Language Understanding by Generative Pre-Training. 2018
		- https://github.com/openai/finetune-transformer-lm
		- Causal Transformer;
		- Semi-supervised fine-tuning;
		- Pretrain: BooksCorpus dataset;
		- 12 x self-attention (Transformer);
	- R Al-Rfou, D Choe, N Constant, M Guo, L Jones. Character-Level Language Modeling with Deeper Self-Attention. 2018
		- 64 transformer layers (deep, multi-head self-attention + fc x 2);
		- Mask for causal attention;
		- Auxiliary loss:
			- Multiple prediction (predict every character in the sequence)
			- Intermediate layer losses (deep supervision)
			- Multiple targets
		- 235 million parameters, dropout (0.55)
	- **GPT-2**: A Radford, J Wu, R Child, D Luan, D Amodei, I Sutskever. Language Models are Unsupervised Multitask Learners. 2018
		- Input representation: Byte Pair Encoding (BPE) (Sennrich et al., 2015); A Character-Level Decoder without Explicit Segmentation for Neural Machine Translation (Yoshua Bengio)
		- Layer normalization: moved to the input of each sub-block
		- additional layer normalization: after the final self attention block
		- 48 layers of transformer
	- R Child, S Gray, A Radford, and I Sutskever. Generating long sequences with sparse transformers. 2019
	- **GPT-3**: Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel M. Ziegler, Jeffrey Wu, Clemens Winter, Christopher Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever, Dario Amodei. Language Models are Few-Shot Learners. 2020
		- https://github.com/openai/gpt-3
		- 175B parameters, 45T training data;
- Neil Houlsby, Andrei Giurgiu, Stanislaw Jastrzebski, Bruna Morrone, Quentin de Laroussilhe, Andrea Gesmundo, Mona Attariyan, Sylvain Gelly. Parameter-Efficient Transfer Learning for NLP. ICML'19
	- Adapter module
- **Transformer-XL**: Z Dai, Z Yang, Y Yang, J Carbonell, Q Le, R Salakhutdinov. Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context. 2019
	- https://github.com/kimiyoung/transformer-xl
	- Insight: improved attention span; (Improved on Rami Al-Rfou et.al. 2018 [Character-level language modeling with deeper self-attention])
	- Dynamic masking;
	- Fixed-length segment; hidden state reuse\
		<img src = '/NLP/images/transformer-xl.png' width = '600px'>
	- Relative position encoding:\
		<img src = '/NLP/images/transformer-xl-2.png' width = '600px'>
- **XLNet**: Zhilin Yang, Zihang Dai, Yiming Yang, Jaime Carbonell, Ruslan Salakhutdinov, Quoc V. Le. XLNet: Generalized Autoregressive Pretraining for Language Understanding. 2019
	- https://github.com/zihangdai/xlnet
- Sainbayar Sukhbaatar, Edouard Grave, Piotr Bojanowski, Armand Joulin. Adaptive Attention Span in Transformers. 2019
- **Universal Transformers**: Mostafa Dehghani, Stephan Gouws, Oriol Vinyals, Jakob Uszkoreit, Łukasz Kaiser. Universal Transformer. ICLR'19
	- Transformer + RNN;
- Zhenzhong Lan, Mingda Chen, Sebastian Goodman, Kevin Gimpel, Piyush Sharma, Radu Soricut. ALBERT: A Lite BERT for Self-supervised Learning of Language Representations.
- **Google-T5**: https://ai.googleblog.com/2020/02/exploring-transfer-learning-with-t5.html
	- Transfer learning;
- **Reformer**: Nikita Kitaev, Łukasz Kaiser, Anselm Levskaya. Reformer: The Efficient Transformer. ICLR'20
	- LSH instead of fc for speed;

## Vision: Backbone
- **SENet**: Jie Hu, Li Shen, Gang Sun. Squeeze-and-Excitation Networks. CVPR'18
	- Insight: channel-wise scaling (learn by MLP);
	- https://github.com/hujie-frank/SENet
	- Winner of ILSVR'17
	- Model: channel-wise selection/attention;
		- For a HxWxC feature x, calculate channel-wise W 1x1xC;
		- Then apply the weight channel-wise: W x
- Xiaolong Wang, Ross Girshick, Abhinav Gupta, and Kaiming He. Non-local neural networks. CVPR'18
	- Task: video classification;
	- CNN on each frame, then transformer to catch long-range dependency;
- CNN+Transformer for aggregation/attention/...;
	- Yuhui Yuan and Jingdong Wang. Ocnet: Object context network for scene parsing. arxiv'18
		- Task: semantic segmentation;
		- Model: transformer for context aggregation;
			- Global attention: divide pixels into subgroups and self-attention in each subgroup;
			- Local attention: in each local grid;
	- Han Hu, Zheng Zhang, Zhenda Xie, and Stephen Lin. Local relation networks for image recognition. ICCV'19
		- Transformer as **local aggregation** layer;
		- SA for the weights;
	- Yue Cao, Jiarui Xu, Stephen Lin, Fangyun Wei, and Han Hu. Gcnet: Non-local networks meet squeeze-excitation networks and beyond. ICCVW'19
		- https://github.com/xvjiarui/GCNet
		- squeeze-excitation like hard attention instead of soft-attention to save memory;
		- Traditional NL-Net: HW x HW; GCNet: HW x 1 x 1; learn to weight (excite);
	- DANet: Jun Fu, Jing Liu, Haijie Tian, Yong Li, Yongjun Bao, Zhiwei Fang, and Hanqing Lu. Dual attention network for scene segmentation. CVPR'19
		- https://github.com/junfu1115/DANet/
		- Task: semantic segmenation;
		- Two channels of SA, then fuse: Position Attention + channel Attention;
	- Minghao Yin, Zhuliang Yao, Yue Cao, Xiu Li, Zheng Zhang, Stephen Lin, and Han Hu. Disentangled non-local neural networks. ECCV'20
		- Unary attention (SE-Net based) + binary attention (pairwise);
	- **BoTNet**: Aravind Srinivas, Tsung-Yi Lin, Niki Parmar, Jonathon Shlens, Pieter Abbeel, and Ashish Vaswani. Bottleneck transformers for visual recognition. arxiv'21
- Pure attention & ViT series:
	- Prajit Ramachandran, Niki Parmar, Ashish Vaswani, Irwan Bello, Anselm Levskaya, and Jon Shlens. Stand-alone self-attention in vision models. NIPS'19
		- Attention only, no CNN;
		- ImageNet: 77%, not bad;
	- Hengshuang Zhao, Jiaya Jia, and Vladlen Koltun. Exploring self-attention for image recognition. CVPR'20
		- Compare two SA:
			- Pairwise: yi = sum alpha(xi, xj) beta(xj), treat as set, permutation-invariant;
			- Patchwise: yi = sum alpha(X_Ri)j beta(xj), not set or perm-inv, strictly more powerful;
		- ImageNet: 77.1% patchwise;
	- Irwan Bello, Barret Zoph, Ashish Vaswani, Jonathon Shlens, and Quoc V. Le. Attention augmented convolutional networks, 2020
	- **ViT**: Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov, Dirk Weissenborn, Xiaohua Zhai, Thomas Unterthiner, Mostafa Dehghani, Matthias Minderer, Georg Heigold, Sylvain Gelly, Jakob Uszkoreit, and Neil Houlsby. An image is worth 16x16 words: Transformers for image recognition at scale. ICLR'21
		- https://github.com/google-research/vision_transformer
		- ImageNet: top-1 77.9%(ViT-B), 76.5%(ViT-L);
		- Requires Large training dataset pretraining;
	- **DeiT**: Hugo Touvron, Matthieu Cord, Matthijs Douze, Francisco Massa, Alexandre Sablayrolles, and Herve Jegou. Training data-efficient image transformers & distillation through attention. ICML'21
		- Improved on ViT and train with a single machine in 3 days;
		- Token-based distillation, teacher-student network;
			- Hard label distillation on class and token labels;
		- ImageNet: top-1 79.8%(DeiT-S), 83.1%(DeiT-B);
	- ViT-FRCNN: Josh Beal, Eric Kim, Eric Tzeng, Dong Huk Park, Andrew Zhai, and Dmitry Kislyuk. Toward transformer-based object detection. arxiv'20
		- Low perf;
		- CNN/ViT-encoder - Reshape as feature map - RPN;
	- Sixiao Zheng, Jiachen Lu, Hengshuang Zhao, Xiatian Zhu, Zekun Luo, Yabiao Wang, Yanwei Fu, Jianfeng Feng, Tao Xiang, Philip HS Torr, et al. Rethinking semantic segmentation from a sequence-to-sequence perspective with transformers. arxiv'20
		- Low perf;
		- https://github.com/fudan-zvg/SETR
		- ViT-backbone, then upsampling for finer-res like FPN;
		- ADE20K: 50.28% mIoU
	- Li Yuan, Yunpeng Chen, Tao Wang, Weihao Yu, Yujun Shi, Francis EH Tay, Jiashi Feng, and Shuicheng Yan. Tokens-to-token vit: Training vision transformers from scratch on imagenet. arxiv'21
		- Make training-from-scratch work, not requiring pretraining;
	- Kai Han, An Xiao, Enhua Wu, Jianyuan Guo, Chunjing Xu, and Yunhe Wang. Transformer in transformer. NeurIPS'21
		- Local smaller patches (word);
		- Larger patches (sentences);
	- **PVT**: Wenhai Wang, Enze Xie, Xiang Li, Deng-Ping Fan, Kaitao Song, Ding Liang, Tong Lu, Ping Luo, and Ling Shao. Pyramid vision transformer: A versatile backbone for dense prediction without convolutions. arxiv'21
		- https://github.com/whai362/PVT
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
- **Vision: Head**
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

## Vision: others
- Rendering:
	- Joshua Tobin, Wojciech Zaremba, Pieter Abbeel. Geometry-Aware Neural Rendering. NeurIPS'19
- Recurrent attention:
	- V Mnih, N Heess, A Graves, et al. Recurrent models of visual attention. NIPS'14
	- J Fu, H Zheng, and T Mei. Look closer to see better: Recurrent attention convolutional neural network for fine-grained image recognition. CVPR'17
- Unclassified:
	- J Ba, V Mnih, and K Kavukcuoglu. Multiple object recognition with visual attention. arxiv'14
	- T Xiao, Y Xu, K Yang, J Zhang, Y Peng, and Z Zhang. The application of two-level attention models in deep convolutional neural network for fine-grained image classification. CVPR'15
	- M Chung, S Cho. Cram: Clued recurrent attention model. arxiv'18
	- A Ablavatski, S Lu, and J Cai. Enriched deep recurrent visual attention model for multiple object recognition. WACV'17
	- H Zheng, J Fu, T Mei, and J Luo. Learning multi-attention convolutional neural network for fine-grained image recognition. ICCV'17
	- F Wang, M Jiang, C Qian, S Yang, C Li, H Zhang, X Wang, and X Tang. Residual attention network for image classification. arxiv'17
	- Yunpeng Chen, Yannis Kalantidis, Jianshu Li, Shuicheng Yan, Jiashi Feng. A2-Nets: Double Attention Networks. NIPS'18

## Attention in RL
- **GTrXL**: Emilio Parisotto, H. Francis Song, Jack W. Rae, Razvan Pascanu, Caglar Gulcehre, Siddhant M. Jayakumar, Max Jaderberg, Raphael Lopez Kaufman, Aidan Clark, Seb Noury, Matthew M. Botvinick, Nicolas Heess, Raia Hadsell. Stabilizing Transformers for Reinforcement Learning.