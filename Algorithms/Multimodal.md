# Multimodal Learning

## Platform
- **Habitat**: M Savva, A Kadian, O Maksymets, Y Zhao, E Wijmans, B Jain, J Straub, J Liu, V Koltun, J Malik, D Parikh and D Batra. Habitat: A Platform for Embodied AI Research. ICCV'19
	- Tasks: Embodied QA, Language grounding, navigation;
	- Simulator: MatterPort3D, Gibson, Replic; https://github.com/facebookresearch/habitat-sim
	- Habitat-API: https://github.com/facebookresearch/habitat-api

## Dataset
- Large Vision + Language 
	- Karan Desai and Justin Johnson. VirTex: Learning Visual Representations from Textual Annotations. 2020
	- Mert Bulent Sariyildiz, Julien Perez, and Diane Larlus. Learning Visual Representations with Caption Annotations. 2020
	- Yuhao Zhang, Hang Jiang, Yasuhide Miura, Christopher D. Manning, and Curtis P. Langlotz. Contrastive Learning of Medical Visual Representations from Paired Images and Text. 2020
	- Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark, Gretchen Krueger, and Ilya Sutskever. Learning Transferable Visual Models From Natural Language Supervision. 2021
	- Norman Mu, Alexander Kirillov, David Wagner, and Saining Xie. SLIP: Self-supervision meets Language-Image Pre-training. 2021
	- Andreas Fürst, Elisabeth Rumetshofer, Viet Thuong Tran, Hubert Ramsauer, Fei Tang, Johannes Lehner, D P Kreil, Michael K Kopp, Günter Klambauer, Angela Bitto-Nemling, and Sepp Hochreiter. CLOOB: Modern Hopfield Networks with InfoLOOB Outperform CLIP, 2022.

## Text-based Generation
- Shizhan Zhu, Sanja Fidler, Raquel Urtasun, Dahua Lin, Chen Change Loy. Be Your Own Prada: Fashion Synthesis with Structural Coherence. ICCV'17
	- Problem setup: input image + text; output new image (focus on fashion);\
		<img src = '/Generative/images/gan/prada1.png' width = '400'>
	- Model: two GANS:\
		<img src = '/Generative/images/gan/prada2.png' width = '400'>
- **Attngan**: T. Xu, P. Zhang, Q. Huang, H. Zhang, Z. Gan, X. Huang, and X. He. Attngan: Fine-grained text to image generation with attentional generative adversarial networks. CVPR'18
- Text-Adaptive Generative Adversarial Networks: Manipulating Images with Natural Language. NIPS'18
- Yonsei University, Text-Adaptive Generative Adversarial Networks: Manipulating Images with Natural Language, NIPS'18
- **DALL-E**: Aditya Ramesh, Mikhail Pavlov, Gabriel Goh, Scott Gray, Chelsea Voss, Alec Radford, Mark Chen, and Ilya Sutskever. Zero-Shot Text-to-Image Generation. 2021
	- https://github.com/openai/DALL-E
	- Stage 1: dVAE, 256x256-dVAE-32x32x8192 tokens; train φ and θ;
	- Stage 2: concatenate 256 BPE-encoded text tokens with the 32 × 32 = 1024 image tokens, and train an autoregressive transformer pψ(y, z).
	- x: image; y: caption; z: latent;
	- ln pθ,ψ(x, y) >= Ez∼qφ(z|x) ln pθ(x|y,z)−βKL(qφ(y,z|x), pψ(y,z))
		- Latent distribution qφ(z|x): 32x32 dVAE, K=8192 tokens, with Gumbel trick;
		- Image distribution pθ(x|y,z): Log-laplace NLL loss;
		- Text token joint distribution: pψ(y, z); 12-billion parameter sparse transformer
- **GLIDE**: Alex Nichol, Prafulla Dhariwal, Aditya Ramesh, Pranav Shyam, Pamela Mishkin, Bob McGrew, Ilya Sutskever, and Mark Chen. GLIDE: Towards Photorealistic Image Generation and Editing with Text-Guided Diffusion Models. 2021
	- https://github.com/openai/glide-text2im.
	- CLIP-guidance v.s. classifier-free guidance;

## Embedding, Feature Learning
- Protocol:
	- BERT-based:
		- VilBert, VisualBERT, VL-BERT, UNITER, OSCAR, VideoBERT, ActBERT, Unicoder-VL, LXMERT, MERLOT, HERO, ALBEF, ...
	- Dual-encoder contrastive:
		- CLIP, ALIGN, CoCa, Florence, MIL-NCE, BASIC, LiT, FILIP, MMV;
	- VL models;
		- SimVLM, Virtex, MAGMA, Frozen, VisualGPT, ClipClap, VC-GPT, CM3, BLIP, Uni-Perceiver, VL-BART, VL-T5, VLM, Flamingo;
- BERT-style:
	- **ViLBERT**: Jiasen Lu, Dhruv Batra, Devi Parikh, Stefan Lee. ViLBERT: Pretraining Task-Agnostic Visiolinguistic Representations for Vision-and-Language Tasks. NeurIPS'19
	- **VideoBERT**: C Sun, A Myers, C Vondrick, K Murphy and C Schmid. VideoBERT: A Joint Model for Video and Language Representation Learning. ICCV'19
	- Gunnar A. Sigurdsson, Jean-Baptiste Alayrac, Aida Nematzadeh, Lucas Smaira, Mateusz Malinowski, João Carreira, Phil Blunsom, Andrew Zisserman. Visual Grounding in Video for Unsupervised Word Translation. 2020
		- Extend VideoBert to multilingual
	- Liunian Harold Li, Mark Yatskar, Da Yin, Cho-Jui Hsieh, Kai-Wei Chang. VisualBERT: A Simple and Performant Baseline for Vision and Language.
	- Weijie Su, Xizhou Zhu, Yue Cao, Bin Li, Lewei Lu, Furu Wei, Jifeng Dai. VL-BERT: Pre-training of Generic Visual-Linguistic Representations. ICLR'20
	- Yen-Chun Chen, Linjie Li, Licheng Yu, Ahmed El Kholy, Faisal Ahmed, Zhe Gan, Yu Cheng, Jingjing Liu. UNITER: UNiversal Image-TExt Representation Learning. ECCV'20
	- Xiujun Li, Xi Yin, Chunyuan Li, Pengchuan Zhang, Xiaowei Hu, Lei Zhang, Lijuan Wang, Houdong Hu, Li Dong, Furu Wei, Yejin Choi, Jianfeng Gao. Oscar: Object-Semantics Aligned Pre-training for Vision-Language Tasks
- Dual-encoder contrastive:
	- **CLIP**: Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark, Gretchen Krueger, and Ilya Sutskever. Learning Transferable Visual Models From Natural Language Supervision. 2021
	- **ALIGN**: Chao Jia, Yinfei Yang, Ye Xia, Yi-Ting Chen, Zarana Parekh, Hieu Pham, Quoc V. Le, Yunhsuan Sung, Zhen Li, Tom Duerig. ALIGN: Scaling Up Visual and Vision-Language Representation Learning With Noisy Text Supervision. ICML'21
	- CoCa: Jiahui Yu, Zirui Wang, Vijay Vasudevan, Legg Yeung, Mojtaba Seyedhosseini, Yonghui Wu. CoCa: Contrastive Captioners are Image-Text Foundation Models.
	- **Florence**: Lu Yuan, Dongdong Chen, Yi-Ling Chen, Noel Codella, Xiyang Dai, Jianfeng Gao, Houdong Hu, Xuedong Huang, Boxin Li, Chunyuan Li, Ce Liu, Mengchen Liu, Zicheng Liu, Yumao Lu, Yu Shi, Lijuan Wang, Jianfeng Wang, Bin Xiao, Zhen Xiao, Jianwei Yang, Michael Zeng, Luowei Zhou, Pengchuan Zhang. Florence: A New Foundation Model for Computer Vision.
	- **MIL-NCE**: Antoine Miech, Jean-Baptiste Alayrac, Lucas Smaira, Ivan Laptev, Josef Sivic, Andrew Zisserman. End-to-End Learning of Visual Representations from Uncurated Instructional Videos.
		- https://www.di.ens.fr/willow/research/mil-nce/
- Visual LM: vision+prefix -> predict postfix text;
	- **VirTex**: Karan Desai, Justin Johnson. VirTex: Learning Visual Representations from Textual Annotations. CVPR'21
	- **SimVLM**: Zirui Wang, Jiahui Yu, Adams Wei Yu, Zihang Dai, Yulia Tsvetkov, Yuan Cao. SimVLM: Simple Visual Language Model Pretraining with Weak Supervision. ICLR'22
	- MAGMA – Multimodal Augmentation of Generative Models through Adapter-based Finetuning.
	- Jun Chen, Han Guo, Kai Yi, Boyang Li, Mohamed Elhoseiny. VisualGPT: Data-efficient Adaptation of Pretrained Language Models for Image Captioning. CVPR'22
	- **Flamingo**: a Visual Language Model for Few-Shot Learning. 2022
- Retrieval:
	- IBM, Dialog-based Interactive Image Retrieval, NIPS'18
- Downstream tasks:
	- Sheng Shen, Liunian Harold Li, Hao Tan, Mohit Bansal, Anna Rohrbach, Kai-Wei Chang, Zhewei Yao, and Kurt Keutzer. How Much Can CLIP Benefit Vision-and-Language Tasks?

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
- Metrics:
	- BLEU, METEOR, ROUGE-L, CIDEr
- Benchmarks:
	- MSCOCO
	- http://www.sohu.com/a/313942390_651893?sec=wd
	- **Visual genome**: Connecting language and vision using crowd-sourced dense image annotations.
	- Visual Dialog. CVPR 2017
		- https://visualqa.org/challenge.html
	- GQA:
		- Yuke Zhu, Oliver Groth, Michael Bernstein, Li Fei-Fei. Visual7W: Grounded Question Answering in Images. 2017
		- https://cbmm.mit.edu/research/projects-thrust/vision-and-language/grounded-question-answering
		- Object-level grounding;
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
- VQA:
	- Misc:
		- Learning Conditioned Graph Structures for Interpretable Visual Question Answering. NIPS'18
		- Out of the Box: Reasoning with Graph Convolution Nets for Factual Visual Question Answering. NIPS'18
		- Jin-Hwa Kim, Jaehyun Jun, Byoung-Tak Zhang. Bilinear Attention Networks. NIPS'18
	- Vqa: Visual question answering. ICCV 2015.
	- Devi, Dhruv: Visual Dialog. CVPR 2017
		- https://visualqa.org/challenge.html
	- A-star best performer:
		- LSTM for the question to encode a vector;
		- Vector as query, do attention, softmax, sum on CNN spatial feature;
		- Vector produces all answers (VQA has an answer set);
	- **MAC**: D Hudson, C Manning. Compositional Attention Networks for Machine Reasoning. ICLR'18
		- MAC recurrent unit
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

## Visual Reasoning
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
- **VCR**: Visual Commonsense Reasoning. CVPR'19

## RL + Language
- Program Guided
	- Shao-Hua Sun, Te-Lin Wu, Joseph J. Lim. Program Guided Agent. ICLR'20
		- Input: perception (2D) + DSL program;
		- Output: action;
- Navigation
	- H Yu, H Zhang, W Xu. A Deep Compositional Framework for Human-like Language Acquisition in Virtual Environment. 2017
	- K M Hermann, F Hill, S Green, F Wang, R Faulkner, H Soyer, D Szepesvari, W M Czarnecki, M Jaderberg, D Teplyashin, M Wainwright, C Apps, D Hassabis, P Blunsom. Grounded Language Learning in a Simulated 3D World
		- Instruction based
		<img src="/RL/images/navigation/language-based.png" alt="drawing" width="500"/>
- Deep Reinforcement Learning with a Natural Language Action Space
- Gated-Attention Architectures for Task-Oriented Language Grounding
- Language Understanding for Text-based Games using Deep Reinforcement Learning, EMNLP 2015
- https://github.com/devendrachaplot/DeepRL-Grounding
