# Human Template Modeling

## Unclassified
- L. Wei, Q. Huang, D. Ceylan, E. Vouga, and H. Li. Dense human body correspondences using convolutional networks. CVPR'16

## 3D Human Templates
- Joints for a human;
- **SMPL**: M. Loper, N. Mahmood, J. Romero, G. Pons-Moll, and M. J. Black. SMPL: A skinned multi-person linear model. TOG'15
	- Key idea: Template mesh **T** (6,890 x 3) with 6,890 vertices (23 joints + 1 whole) with blended weight **W** (6,890 x 24, influence of rotation joint k on vertex i), joint **J** (24 x 6,890, rest vertices to rest joints), shape-blended shapes **S** (6,890 x 3 x 10), pose blended shapes **P** (6,890 x 3 x 207);
	- https://smpl.is.tue.mpg.de/ (python code available)
	- https://github.com/CalciferZh/SMPL (pytorch version)
	- Model:\
		<img src = '/Composition/images/3d/smpl-full.png' width = '400'>
	- Given new pose theta (24, 3), beta (10,), global translation (3,), a new mesh is generated as:
		- 1. shape blending: v-shaped = S x beta + template (6,890 x 3)
		- 2. map to joint: J = J x v_shaped (24 x 3)
		- 3. Pose: R = Rodrigues(theta) (24 x 3 x 3)
		- 4. Pose: v_posed = v_shaped + P x (R-I), where (R-I) of shape 207 (23 x 3 x 3, first dim global so skipped?)
		- 5. Kinematic tree (parent joint on child joint) 24 x 2 integer matrix; apply chain rotation to get results (24 x 4 x 4); obtain T = W x results (6,890 x 4 x 4) 
		- 6. Rest shapes: cat(v_posed, ones) (6,890 x 4)
		- 7. Final: v = T x v_posed + translation (6,890 x 3)
	- Parametrized model of 3D human shape: yaw, pitch, roll of human body joints; parameters control deformation of body skin; a fixed number of n=6,890 3D mesh vertex coordinates:\
		<img src = '/Composition/images/3d/smpl.png' width = '400'>
	- where the 3D point Xi equals the normalized bar(Xi), beta mixture of skin s(m,i) and skeleton pose p(n,i);
- F. Bogo, A. Kanazawa, C. Lassner, P. Gehler, J. Romero, and M. J. Black. Keep it SMPL: Automatic estimation of 3D human pose and shape from a single image. ECCV'16
	- Template matching.
- Hsiao-Yu Fish Tung, Hsiao-Wei Tung, Ersin Yumer, Katerina Fragkiadaki. Self-supervised Learning of Motion Capture. NIPS'17
	- https://github.com/htung0101/3d_smpl (Tensorflow)
	- Input: a video sequence, 2D body joint heatmaps; output a neural net predicts body parameters for SMPL 3D human mesh;
	- Training: 1. pretrained with synthetic data; 2. finetuned with self-supervised loss (keypoints, 2D segmentation, 2D optical flow);\
		<img src = '/Composition/images/3d/ssl-mocap.png' width = '500'>
	- Evaluation: 3D dense human shape tracking in SURREAL, H3.6M;
- Meysam Madadi, Hugo Bertiche and Sergio Escalera. SMPLR: Deep SMPL reverse for 3D human pose and shape recovery. 2019