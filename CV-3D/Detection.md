# 3D Detection

## Point Cloud
- **PointNet++**: Deep Hierarchical Feature Learning on Point Sets in a Metric Space, Charles R. Qi, Li Yi, Hao Su, Leonidas J. Guibas, NIPS 2017
	- **Classification mode**: [SA module x 3] + FC_layers;
	- SA module #1, #2: xyz, features = model(xyz, features=None), xyz: (B, 2048, 3)
		- Gather operation (furtherest point sampling): from 2048 points, select 512 centers as new_xyz (B, 512, 3)
		- Group-Query-MLP x 3 (with different radius)
			- Group and Query: to (B, d, 512, nS), dim: feature dim; each 512 centers will be assigned nS=16 members
			- Shared MLPs: with dim like [d, 32, 32, 64], output (B, 64, 512, nS), implement FC with 2D-Conv with kernel-size (1, 64)
			- Max-pooling along last dimension (B, 64, 512)
		- After SA-1: xyz=(B, 512, 3), feat=(B, 320, 512)
		- After SA-2: xyz=(B, 128, 3), feat=(B, 640, 128)
	- SA module #3:
		- No gather operation: new_xyz=None
		- GroupAll: (B, 643, 1, nS), 643=640+3, nS=128
		- Shared MLPs: (B, 1024, 1)
	- FC_layers: [1024, 512, 256, nClass]
	- Finally a 256-dim feature
	- **Semantic Segmentation mode**: [SA-module x3] + [FP-modules x4] + [Conv1d x2]
	- FP-modules are used to interpolate features back;
	```python
	feat[i-1] = self.FP_modules[i](xyz[i-1], xyz[i], feat[i-1], feat[i])
	```
	
	- With shape: (B, n, 3), (B, m, 3), (B, C1, n), (B, C2, m), returns (B, mlp[-1], n)
- **PointNet**: Charles R. Qi, Wei Liu, Chenxia Wu, Hao Su, Leonidas Guibas. Frustum PointNets for 3D Object Detection from RGB-D Data, CVPR 2018

## 3D Bounding Box from Images
- R-CNN (ROI, then pose regression):
	- S. Tulsiani and J. Malik. Viewpoints and keypoints. CVPR'15
	- A. Mousavian, D. Anguelov, J. Flynn, and J. Kosecka. 3d bounding box estimation using deep learning and geometry. CVPR'17
- Viewpoint-dependent detector, pose estimation by clustering 3D:
	- Y. Xiang, W. Choi, Y. Lin, and S. Savarese. Data-driven 3d voxel patterns for object category recognition. CVPR'15
	- Y. Xiang, W. Choi, Y. Lin, and S. Savarese. Subcategory-aware convolutional neural networks for object proposals and detection. WACV'17

## 3D Box from Depth
- S. Song and J. Xiao. Sliding shapes for 3d object detection in depth images. ECCV'14
- S. Song and J. Xiao. Deep sliding shapes for amodal 3d ob- ject detection in rgb-d images. ECCV'16
- B. Li. 3d fully convolutional network for vehicle detection in point cloud. IROS'16
- **VeloFCN**: B. Li, T. Zhang, and T. Xia. Vehicle detection from 3d lidar using fully convolutional network. arxiv'16

## 2D-3D Fusion
- **MV3D**: X. Chen, H. Ma, J. Wan, B. Li, and T. Xia. Multi-view 3d object detection network for autonomous driving. CVPR'17
- A Mousavian, D Anguelov, J Flynn, J Kosecka. 3d bounding box estimation using deep learning and geometry. CVPR'17
- **PointFusion**: D Xu, D Anguelov, A Jain. PointFusion: Deep Sensor Fusion for 3D Bounding Box Estimation. CVPR'18
	<img src="/CV-3D/images/pointfusion.png" alt="drawing" width="600"/>

	- Input: RGB + 3D point cloud
	- Output: 3 x 8 corner points
	- Global fusion (baseline): (1 x 3072) -> MLP (512, 128, 128) -> 1x8x3 (L1-loss)
	- Dense fusion:
	- STN
	- Experiments: KITTI, AP-3D