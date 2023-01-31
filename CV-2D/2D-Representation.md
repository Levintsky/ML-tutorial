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

## Datasets
- **ISIN**: C Lu, H Su, Y Li, Y Lu, L Yi, CK Tang, L Guibas. Beyond Holistic Object Recognition: Enriching Image Understanding with Part States. CVPR'18
	- Part state dataset from PASCAL VOC: 15 object categories, 104,965 parts, 856 states from 19,437 images;

## Backbone
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

## Supervision
- cVAE: D Ritchie's;

## Unclassified
- J Wang, A Yuille. Semantic Part Segmentation using Compositional Model combining Shape and Appearance. CVPR'15
- v d Hengel, A., Russell, C., Dick, A., Bastian, J., Pooley, D., Fleming, L., Agapito, L.: Part-based modelling of compound scenes from images. CVPR'15