# 3D Understanding and Synthesis

## Tutorials
- https://github.com/timzhang642/3D-Machine-Learning

## Basics
- **Chamfer distance** (a strong baseline)
	- Sum of closest point distances
	- Asymmetric
	- For Hausdorff distance, simply a distance transform?

## SOA
- P.-S. Wang, Y. Liu, Y.-X. Guo, C.-Y. Sun, and X. Tong. OCNN: Octree-based convolutional neural networks for 3D shape analysis. TOG 2017
- Y. Wang, Y. Sun, Z. Liu, S. E. Sarma, M. M. Bronstein, and J. M. Solomon. Dynamic graph cnn for learning on point clouds. 2018
- X. Wang, B. Zhou, H. Fang, X. Chen, Q. Zhao, and K. Xu. Learning to group and label fine-grained shape components. SIGGRAPH Asia 2018
- Z. Wang and F. Lu. VoxSegNet: Volumetric CNNs for semantic part segmentation of 3D shapes. 2018
- Z. Wu, X. Wang, D. Lin, D. Lischinski, D. Cohen-Or, and H. Huang. Structure-aware generative network for 3d-shape modeling. 2018
- Y. Xu, T. Fan, M. Xu, L. Zeng, and Y. Qiao. SpiderCNN: Deep learning on point sets with parameterized convolutional filters. ECCV 2018
- L. Yi, H. Su, X. Guo, and L. J. Guibas. SyncSpecCNN: Synchronized spectral CNN for 3D shape segmentation. CVPR 2017

## Co-Segmentation
- R. Hu, L. Fan, and L. Liu. Co-segmentation of 3D shapes via subspace clustering. CGF 2012
- Y. Wang, S. Asafi, O. Van Kaick, H. Zhang, D. Cohen-Or, and B. Chen. Active co-analysis of a set of shapes. TOG 2012

## Part
- R. Hu, W. Li, O. Van Kaick, A. Shamir, H. Zhang, and H. Huang. Learning to predict part mobility from a single static snapshot. TOG 2017
- R. Hu, O. van Kaick, B. Wu, H. Huang, A. Shamir, and H. Zhang. Learning how objects function via co-analysis
of interactions. TOG 2016
- R. Hu, Z. Yan, J. Zhang, O. van Kaick, A. Shamir, H. Zhang, and H. Huang. Predictive and generative neural networks for object functionality. CGF 2018
- **Hao Su Summary**: http://cseweb.ucsd.edu/~haosu/slides/PartInduction.pdf
- **ISIN**: Cewu Lu, Hao Su, Yongyi Lu, Li Yi, Chi-Keung Tang, Leonidas Guibas. Beyond Holistic Object Recognition: Enriching Image Understanding with Part States. CVPR 2018
	- Objerect Part-State Dataset
	- Iterative Part-state Inference Network (ISIN)

## Classification
- Voxel:
	- **ModelNet**: Z. Wu, S. Song, A. Khosla, F. Yu, L. Zhang, X. Tang and J. Xiao. 3D ShapeNets: A Deep Representation for Volumetric Shapes
		- Predict next best angle (most uncertain by max entropy diff)
	- D Maturana and S Scherer. VoxNet: A 3D Convolutional Neural Network for Real-Time Object Recognition. IROS 2015
		- https://github.com/dimatura/voxnet
- 2D images:
	- Hang Su, Subhransu Maji, Evangelos Kalogerakis, Erik Learned-Miller. Multi-view Convolutional Neural Networks for 3D Shape Recognition. ICCV 2015
		- https://github.com/jongchyisu/mvcnn_pytorch
		- Multi-view pooling
	- DeepPano: Deep Panoramic Representation for 3-D Shape Recognition.
- Multi-mode:
	- Vishakh Hegde, Reza Zadeh. FusionNet: 3D Object Classification Using Multiple Data Representations. NIPS 2016
	- Charles R. Qi, Hao Su, Matthias Nießner Angela Dai Mengyuan Yan Leonidas J. Guibas. Volumetric and Multi-View CNNs for Object Classification on 3D Data. CVPR'16
		- https://github.com/charlesq34/

## Understanding, Classification
- Robotics (grasping, with touch):
	- M. Bjorkman, Y. Bekiroglu, V. Hogman, and D. Kragic, Enhancing visual perception of shape through tactile glances, IROS 2013.
	- 3D Shape Perception from Monocular Vision, Touch, and Shape Priors, Shaoxiong Wang, Jiajun Wu, Xingyuan Sun, Wenzhen Yuan, William T. Freeman, Joshua B. Tenenbaum, and Edward H. Adelson
	- W. Yuan, S. Dong, and E. H. Adelson, Gelsight: High-resolution robot tactile sensors for estimating geometry and force, Sensors 2017.
- Representation for Voxel data:
	- R Girdhar, D F Fouhey, M Rodriguez, and A Gupta. Learning a predictable and generative vector representation for objects. ECCV'16.
	- H Su, S Maji, E Kalogerakis, and E Learned-Miller. Multi-view convolutional neural networks for 3d shape recognition. ICCV'15
	- C R Qi, H Su, M Niessner, A Dai, M Yan, and L J Guibas. Volumetric and multi-view cnns for object classification on 3d data. CVPR'16.
- 3D-Conv:
	- Daniel Maturana and Sebastian Scherer. Voxnet: A 3d convolutional neural network for real-time object recognition. IROS'15.
	- N Sedaghat, M Zolfaghari, E Amiri, T Brox. Orientation-boosted voxel nets for 3D object recognition. BMVC'17
	- J Wu, T Xue, J J Lim, Y Tian, J B Tenenbaum, A Torralba, and W T Freeman. Single image 3d interpreter network. ECCV'16.
	- Uber-AI-Lab: An intriguing failing of convolutional neural networks and the CoordConv solution
- Unsupervised:
	- Danilo Jimenez Rezende, SM Eslami, Shakir Mohamed, Peter Battaglia, Max Jaderberg, and Nicolas Heess. Unsupervised learning of 3d structure from images. NIPS'16.
- **3d-r2n2**: A unified approach for single and multi-view 3d object reconstruction
- T. Groueix, M. Fisher, V. G. Kim, B. Russell, and M. Aubry. AtlasNet: A Papier-Mach ˆ e Approach to Learning 3D Surface Generation. CVPR 2018
- J. Gwak, C. B. Choy, M. Chandraker, A. Garg, and S. Savarese. Weakly supervised 3d reconstruction with adversarial constraint. 3DV 2017
- S. Savarese and L. Fei-Fei. 3d generic object categorization, localization and pose estimation, ICCV 2017
- X. Yan, J. Yang, E. Yumer, Y. Guo, and H. Lee. Perspective transformer nets: Learning single-view 3d object reconstruction without 3d supervision. In NIPS, 2016.
