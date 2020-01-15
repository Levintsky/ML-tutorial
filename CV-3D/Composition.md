# Part/Primitive/Compositional Model

## Summaries
- Hao Su: http://cseweb.ucsd.edu/~haosu/slides/PartInduction.pdf
- Part:
	- Descriptive
	- Concise
	- Interpretable

## Legacy
- Representing Shape for Recognition, Marr and Nishihara (1978)

## Co-Segmentation
- R. Hu, L. Fan, and L. Liu. Co-segmentation of 3D shapes via subspace clustering. CGF 2012
- Y. Wang, S. Asafi, O. Van Kaick, H. Zhang, D. Cohen-Or, and B. Chen. Active co-analysis of a set of shapes. TOG 2012

## 2D
- **ISIN**: Cewu Lu, Hao Su, Yongyi Lu, Li Yi, Chi-Keung Tang, Leonidas Guibas. Beyond Holistic Object Recognition: Enriching Image Understanding with Part States. CVPR 2018
	- Objerect Part-State Dataset
	- Iterative Part-state Inference Network (ISIN)

## Unsupervised (Reconstruction)
- S. Tulsiani, H. Su, L. J. Guibas, A. A. Efros, and J. Malik. Learning shape abstractions by assembling volumetric primitives. CVPR 2017
	- Input: voxel; output: mesh parts (triangles);
	- Unsupervised?
	- Each part (z, q, t): z, shape; q rotation; t translation;
	- Loss design:
		- Coverage loss: distance of primitives; penalize to confirm O in Pm
		- Consistency loss:
	- Variable number of primitives: (z, q, t, p), p binary for existence
	- REINFORCE; parsimony reward for fewer parts
	- Experiment: ShapeNet, 32x32x32, ADAM;

## Weak-Supervision
- M. Sung, H. Su, R. Yu, and L. Guibas. Deep functional dictionaries: Learning consistent semantic structures on 3D models from functions. NIPS'18
	- Input n points; output: n x k dictionary; weak annotation (inconsistent/unnamed annotation);
	- Structured sparsity;
	- https://github.com/mhsung/deep-functional-dictionaries
	- Different deep dictionaries;
	- Applications with adaptation in co-segmentation, keypoint correspondence, smooth functional approximation (modeled as constraint);
	- Given an input X, At = A(X; theta) to get basis
	- Solve x = argmin||At x - f||^2 s.t. C(x)
	- Update theta = theta - eta * d L(A(X, theta); f, x) / dx

## SSL
- Idea: Mobility-based part structure induction
- Li Yi, Haibin Huang, Difan Liu, Evangelos Kalogerakis, Hao Su, Leonidas Guibas. Deep Part Induction from Articulated Object Pairs. SIGGRAPH Asia'18
	- https://github.com/ericyi/articulated-part-induction

## Functionality
- R. Hu, W. Li, O. Van Kaick, A. Shamir, H. Zhang, and H. Huang. Learning to predict part mobility from a single static snapshot. TOG 2017
- R. Hu, O. van Kaick, B. Wu, H. Huang, A. Shamir, and H. Zhang. Learning how objects function via co-analysis of interactions. TOG 2016
- R. Hu, Z. Yan, J. Zhang, O. van Kaick, A. Shamir, H. Zhang, and H. Huang. Predictive and generative neural networks for object functionality. CGF 2018
