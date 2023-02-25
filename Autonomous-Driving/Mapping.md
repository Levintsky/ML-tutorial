# Map-Automation

## Road/Lane
- Uber-ATG. Enhancing Road Maps by Parsing Aerial Images Around the World. ICCV'15
	- Problem setup: aerial image + OSM as input (only centerline, not accurate), optimize offset (h1, h2, ...) and width (y1, y2, ...);
- Uber-ATG. HD Maps: Fine-grained Road Segmentation by Parsing Ground and Aerial Images. CVPR'16
- Uber-ATG. DeepRoadMapper: Extracting Road Topology From Aerial Images. ICCV'17
- Uber-ATG. Deep Multi-Sensor Lane Detection. IROS'18
- Uber-ATG. Hierarchical Recurrent Attention Networks for Structured Online Maps. CVPR'18
	- Problem setup: input: sparse point cloud (BEV); output: structured lanes;
	- Backbone: encoder - decoder - polyline-RNN
	- Structured loss:
- Uber-ATG. Deep Multi-Sensor Lane Detection. IROS'18
- Uber-ATG. Convolutional Recurrent Network for Road Boundary Extraction. CVPR'19
- Learning to Map by Discovering Lane Topology [Namdar]
- 3D-LaneNet: End-to-End 3D Multiple Lane Detection [ICCV'19, Namdar]

## Crosswalk
- Convolutional Recurrent Network for Road Boundary Extraction [Justin Liang]
- Uber-ATG. End-to-End Deep Structured Models for Drawing Crosswalks. ECCV'18
	- Input: image + LiDAR;
	- Output: polygons;
	- Backbone: CNN
	- Predict: sem-seg, sem-edge, crosswalk directions;
	- Structured optimize: exaustive search to solve:
	- Dataset: OpenStreetMap (OSM);

## Building
- DSAC: Uber-ATG. Learning deep structured active contours end-to-end. CVPR'18
	- https://github.com/dmarcosg/DSAC
	- Input: image; intermediate output: active contour terms;
	- Final output: contour for instance segmentation;
	- Initial polygon: manual, or automatic;

## Unclassified
- Globally consistent map [Joey Yu];
- Deep structured 3D Estimation [Mini-Conf];
	- Input: stereo images, LiDAR; Output: Pose, Shape
- Robust Dense Mapping for Large-Scale Dynamic Environments [ICRA'18, Barsan]
