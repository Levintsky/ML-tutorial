# Map-Automation

## Road/Lane
- Gellert Mattyus, Shenlong Wang, Sanja Fidler and Raquel Urtasun. Enhancing Road Maps by Parsing Aerial Images Around the World. ICCV'15
	- Problem setup: aerial image + OSM as input (only centerline, not accurate), optimize offset (h1, h2, ...) and width (y1, y2, ...);
	- Cost function:\
		<img src="/Autonomous-Driving/images/mapping/osm-cost.png" alt="drawing" width="400"/>
	- Algorithm:\
		<img src="/Autonomous-Driving/images/mapping/osm-bcd.png" alt="drawing" width="400"/>
- Gellert Mattyus, Shenlong Wang, Sanja Fidler, Raquel Urtasun. HD Maps: Fine-grained Road Segmentation by Parsing Ground and Aerial Images. CVPR'16
- G Mattyus, W Luo and R Urtasun. DeepRoadMapper: Extracting Road Topology From Aerial Images. ICCV'17
- Min Bai, Gellert Mattyus, Namdar Homayounfar, Shenlong Wang, Shrinidhi Kowshika Lakshmikanth, Raquel Urtasun. Deep Multi-Sensor Lane Detection. IROS'18
- Namdar Homayounfar, Wei-Chiu Ma, Shrinidhi Kowshika Lakshmikanth, Raquel Urtasun. Hierarchical Recurrent Attention Networks for Structured Online Maps. CVPR'18
	- Problem setup: input: sparse point cloud (BEV); output: structured lanes;
	- Algorithm:\
	<img src="/Autonomous-Driving/images/mapping/hran1.png" alt="drawing" width="400"/>
	- Structured loss:\
	<img src="/Autonomous-Driving/images/mapping/hran2.png" alt="drawing" width="400"/>
- M. Bai, G. Mattyus, N. Homayounfar, S. Wang, S. K. Lakshmikanth, R. Urtasun. Deep Multi-Sensor Lane Detection. IROS'18
- J Liang, N Homayounfar, WC Ma, S Wang, R Urtasun. Convolutional Recurrent Network for Road Boundary Extraction. CVPR'19

## Crosswalk
- Convolutional Recurrent Network for Road Boundary Extraction [Justin Liang]
- J. Liang, R. Urtasun. End-to-End Deep Structured Models for Drawing Crosswalks. ECCV'18
	- Input: image + LiDAR;
	- Output: polygons;\
		<img src="/Autonomous-Driving/images/mapping/deep-struct-cw1.png" alt="drawing" width="400"/>
	- 1. CNN to predict semantic segmentation, semantic edge information as well as crosswalk directions;
	- 2. These outputs are then used to form a structured prediction problem, whose inference results are our final crosswalk drawings;
		- Input the road centerlines, the intersection polygon, as well as the three feature maps from CNN;
		- Exaustive search to solve:\
		<img src="/Autonomous-Driving/images/mapping/deep-struct-cw2.png" alt="drawing" width="400"/>
	- Dataset: OpenStreetMap (OSM);

## Building
- **DSAC**: D. Marcos, D. Tuia, B. Kellenberger, L. Zhang, M. Bai, R. Liao and R. Urtasun. Learning deep structured active contours end-to-end. CVPR'18
	- https://github.com/dmarcosg/DSAC
	- Input: image; intermediate output: active contour terms;
	- Final output: contour for instance segmentation;
	- Initial polygon: manual, or automatic;
	<img src="/Autonomous-Driving/images/mapping/dsac.png" alt="drawing" width="400"/>

## Unclassified
- Learning to Map by Discovering Lane Topology [Namdar]
- 3D-LaneNet: End-to-End 3D Multiple Lane Detection [ICCV'19, Namdar]
- Globally consistent map [Joey Yu];
- Deep structured 3D Estimation [Mini-Conf];
	- Input: stereo images, LiDAR; Output: Pose, Shape
- Robust Dense Mapping for Large-Scale Dynamic Environments [ICRA'18, Barsan]
