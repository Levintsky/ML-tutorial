## Vision + Language

## Multimodal Learning
- C Sun, A Myers, C Vondrick, K Murphy and C Schmid. VideoBERT: A Joint Model for Video and Language Representation Learning. ICCV'19
- Gunnar A. Sigurdsson, Jean-Baptiste Alayrac, Aida Nematzadeh, Lucas Smaira, Mateusz Malinowski, João Carreira, Phil Blunsom, Andrew Zisserman. Visual Grounding in Video for Unsupervised Word Translation. 2020
	- Extend VideoBert to multilingual
- Yonsei University, Text-Adaptive Generative Adversarial Networks: Manipulating Images with Natural Language, NIPS 2018
- IBM, Dialog-based Interactive Image Retrieval, NIPS 2018

## Vision + Action
- Speaker-Follower Models for Vision-and-Language Navigation (NIPS 2018)
	- Speaker Model (generate diverse instruction for data augmentation)
	- Follower Model
- TOUCHDOWN: Natural Language Navigation and Spatial Reasoning in Visual Street Environment, NIPS 2018
	- Navigate based on instructions
	- Find the TouchDown, describe, with LINGUNet
	- Good way to collect data

## Image/Video Caption
- Good Tutorials
	- https://www.leiphone.com/news/201805/aQXoPMX51DD1C7VC.html
- Benchmark
	- MSCOCO
	- http://www.sohu.com/a/313942390_651893?sec=wd
- Unclassified
	- Partially-Supervised Image Captioning. NIPS'18
	- Dahua Lin. A Neural Compositional Paradigm for Image Captioning. NIPS'18
	- Weakly Supervised Dense Event Captioning in Videos. NIPS'18
	- Answerer in Questioner's Mind: Information Theoretic Approach to Goal-Oriented Visual Dialog. NIPS'18
	- Fenglin Liu, Yuanxin Liu, Xuancheng Ren, Xiaodong He, Xu Sun. Aligning Visual Regions and Textual Concepts for Semantic-Grounded Image Representations. NIPS'19
- Misc
	- **NeuralTalk**: A. Karpathy. https://github.com/karpathy/neuraltalk
	- A. Karpathy and L. Fei-Fei. Deep visual-semantic alignments for generating image descriptions. CVPR 2015
	- R. Krishna, K. Hata, F. Ren, L. Fei-Fei, and J. C. Niebles. Dense-Captioning events in videos. ICCV 2017
	- G. Kulkarni, V. Premraj, S. Dhar, S. Li, Y. Choi, A. C. Berg, and T. L. Berg. Baby talk: Understanding and generating image descriptions. CVPR 2011
	- J. Lu, J. Yang, D. Batra, and D. Parikh. Neural baby talk. CVPR 2018
	- O Vinyals, A Toshev, S Bengio, D Erhan. **Show and Tell**: Lessons learned from the 2015 MSCOCO Image Captioning Challenge. 2015
	- K. Xu, J. Ba, R. Kiros, K. Cho, A. C. Courville, R. Salakhutdinov, R. S. Zemel, and Y. Bengio. Show, attend and tell: Neural image caption generation with visual attention. In ICML, 2015.
	- **NMN**: Jacob Andreas, Marcus Rohrbach, Trevor Darrell, and Dan Klein. Deep compositional question answering with neural module networks. CVPR'16.
	- C. Wang, H. Yang, C. Bartz, and C. Meinel. Image captioning with deep bidirectional lstms. ACMMM'16
		- Training: bidirectional;
		- Inference: uni-directional; Beam search in each direction; BiDirectional RNNs to rescore candidates;
	- **BiBS**: Bidirectional Beam Search: Forward-Backward Inference in Neural Sequence Models for Fill-in-the-Blank Image Captioning. CVPR'17
	- Novel Visual Concept (NVC) dataset https://github.com/mjhucla/NVC-Dataset
		- TF-mRNN: https://github.com/mjhucla/TF-mRNN
		- mRNN-CR: https://github.com/mjhucla/mRNN-CR

# VQA, Image/Video Caption

## Metrics
- BLEU
- METEOR
- ROUGE-L
- CIDEr

## Benchmark
- **CLEVR**
- **Visual genome**: Connecting language and vision using crowd-sourced dense image annotations.
- Visual Dialog. CVPR 2017
	- https://visualqa.org/challenge.html
- GQA:
	- Yuke Zhu, Oliver Groth, Michael Bernstein, Li Fei-Fei. Visual7W: Grounded Question Answering in Images. 2017
	- https://cbmm.mit.edu/research/projects-thrust/vision-and-language/grounded-question-answering
	- Object-level grounding;

## Unclassified
- Learning Conditioned Graph Structures for Interpretable Visual Question Answering. NIPS'18
- Out of the Box: Reasoning with Graph Convolution Nets for Factual Visual Question Answering. NIPS'18
- Jin-Hwa Kim, Jaehyun Jun, Byoung-Tak Zhang. Bilinear Attention Networks. NIPS'18

## VQA
- MSR:
	- Vqa: Visual question answering. ICCV 2015.
- **FAIR**:
	- Devi, Dhruv: Visual Dialog. CVPR 2017
		- https://visualqa.org/challenge.html
	- A-star best performer:
		- LSTM for the question to encode a vector;
		- Vector as query, do attention, softmax, sum on CNN spatial feature;
		- Vector produces all answers (VQA has an answer set);
- Stanford:
	- **MAC**: D Hudson, C Manning. Compositional Attention Networks for Machine Reasoning. ICLR'18
		- MAC recurrent unit
- Berkeley:
	- **MCB**: A Fukui, D H Park, D Yang, A Rohrbach, T Darrell, M Rohrbach. Multimodal Compact Bilinear Pooling for VQA. EMNLP'16
- **SOA**: P Anderson, X He, C Buehler, D Teney, M Johnson, S Gould, L Zhang. Bottom-up and top-down attention for image captioning and visual question answering. CVPR'18
	- Faster RCNN + ResNet-101
- **MUREL**. Remi Cadene, Hedi Ben-younes, Matthieu Cord, Nicolas Thome. MUREL: Multimodal Relational Reasoning for Visual Question Answering. 2019
	- https://github.com/Cadene/murel.bootstrap.pytorch
- Baselines:
	- https://github.com/Cyanogenoid/pytorch-vqa
- Counting:
	- Learning to Count Objects in Natural Images for Visual Question Answering, ICLR 2018
		- https://github.com/Cyanogenoid/vqa-counting
- Attention:
	- Z. Yang, X. He, J. Gao, L. Deng, and A. J. Smola. Stacked attention networks for image question answering. CVPR'16

## Reasoning
- **NMN**: J Andreas, M Rohrbach, T Darrell, D Klein. Neural Module Networks. CVPR'16
	- Compositional reasoning;
- Justin Johnson, Judy Hoffman, Bharath Hariharan, Laurens van der Maaten, Li Fei-Fei, C. Lawrence Zitnick, Ross Girshick. Inferring and Executing Programs for Visual Reasoning. ICCV'17
	- Insight: program generator + execution engine; built on NMN; train by REINFORCE;
	- Algorithm:\
		<img src="/Grounding/images/vqa-exe.png" alt="drawing" width="400"/>
	- Program generator: LSTM seq2seq, output predicted program z;
	- Execution engine: input program z and image x, a=phi(x, z).
- Kexin Yi, Jiajun Wu, Chuang Gan, Antonio Torralba, Pushmeet Kohli and Joshua B. Tenenbaum. Neural-Symbolic VQA: Disentangling Reasoning from Vision and Language Understanding, NIPS 2018
	- An interpretable VQA model that disentangles language reasoning from visual understanding
	- For visual understanding, first perform objects segmentation and then learn to obtain structural scene representation (with supervision) such as color, size, shape, position.
	- For language reasoning, they learn to translate natural language question into a deterministic program such as filter_shape(scene, large) or count(scene). 
	- Finally, they execute the program on the structural scene representation to obtain the final answer
	- 99.8% on CLEVR

## Reasoning
- **VCR**: Visual Commonsense Reasoning. CVPR'19
