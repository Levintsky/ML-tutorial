## 2D Composiontal/Template Modeling

## Goal
- Tokenize to parts for functional/semantics/...:
	- ISIN [Su Hao, CVPR'18]
- Progressive: one-at-a-time
	- Latex: separate steps to group to a shorter program;
- Holistic:
	- De-rendering/2d-3d-2d:
		- PGM: Picture, DG-ICN; [Kulkarni]; de-rendering, VON, NSCL, PGIM [MIT, Jiajun]
	- Program:
		- Ritchie: NGPM
		- P Kohli: R3NN;
	- Scene-graph: sg2im [J Johnson, cvpr'18]
	- Grammar: Songchun's
- Applications:
	- Indoor: D Ritchie's series;
	- H Chu, S Wang, R Urtasun, S Fidler. HouseCraft- Building Houses from Rental Ads and Street Views. ECCV'16
		- http://www.cs.toronto.edu/housecraft
		- https://github.com/chuhang/HouseCraft (Matlab)
		- Dataset: 174 houses (http://www.domain.com.au)
		- Input: approx address, several geo-tagged images;
		- Output: geometry and location (x, y, h, f, d, a);
	- Procedural reconstruction: NPR ECCV'18;

## Datasets
- **ISIN**: C Lu, H Su, Y Li, Y Lu, L Yi, CK Tang, L Guibas. Beyond Holistic Object Recognition: Enriching Image Understanding with Part States. CVPR'18
	- Part state dataset from PASCAL VOC: 15 object categories, 104,965 parts, 856 states from 19,437 images;

## Backbone
- CNN:
	- NPR: H Zeng, J Wu and Y Furukawa. Neural Procedural Reconstruction for Residential Buildings. ECCV'18
- CNN + RNN
	- ISIN
- GNN:
	- Scene-graph: sg2im;
- Progressive: one-object at a time
	- Neural scene de-rendering. CVPR'17
	- Deep-Synth. SIGGRAPH'18
	- Latex: NeurIPS'18
	- D. Ritchie series;
- Predefined templates/energy:
	- Gupta, A., Efros, A.A., Hebert, M.: Blocks world revisited: Image understanding using qualitative geometry and mechanics. ECCV'10
	- HouseCraft: ECCV'16
- Procedural reconstruction:
	- Muller, P., Zeng, G., Wonka, P., Van Gool, L.: Image-based procedural modeling of facades. TOG'07
	- Zebedin, L., Bauer, J., Karner, K., Bischof, H.: Fusion of feature-and area-based information for urban buildings modeling from aerial imagery. ECCV'08
	- Furukawa, Y., Curless, B., Seitz, S.M., Szeliski, R.: Manhattan-world stereo. CVPR'09
	- Sinha, S., Steedly, D., Szeliski, R. Piecewise planar stereo for image-based rendering. ICCV'09
	- Chauve, A.L., Labatut, P., Pons, J.P.: Robust piecewise-planar 3d reconstruction and completion from large-scale unstructured point data. CVPR'10
	- Jiang, H., Xiao, J.: A linear approach to matching cuboids in rgbd images. CVPR'13
	- Xiao, J., Furukawa, Y. Reconstructing the world's museums. IJCV'14
	- Wang, H., Zhang, W., Chen, Y., Chen, M., Yan, K.: Semantic de- composition and reconstruction of compound buildings with symmetric roofs from lidar data and aerial imagery. Remote Sensing'15

## Supervision
- cVAE: D Ritchie's;

## Unclassified
- J Wang, A Yuille. Semantic Part Segmentation using Compositional Model combining Shape and Appearance. CVPR'15
- v d Hengel, A., Russell, C., Dick, A., Bastian, J., Pooley, D., Fleming, L., Agapito, L.: Part-based modelling of compound scenes from images. CVPR'15