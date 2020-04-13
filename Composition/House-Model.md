# House/Building Modeling

## Optimization
- Hang Chu, Shenlong Wang, Raquel Urtasun, Sanja Fidler. HouseCraft- Building Houses from Rental Ads and Street Views. ECCV'16
	- http://www.cs.toronto.edu/housecraft
	- https://github.com/chuhang/HouseCraft (Matlab)
	- Problem setup: input approximate address, several geo-tagged StreetView images, floor plan; output geometry and location;\
		<img src = '/Composition/images/3d/house-craft1.png' width = '450'>
	- Dataset collection: 174 houses (The SydneyHouse Dataset from http://www.domain.com.au)
	- Assumption: h foundation height (h=0 means same as camera); all floors at the same height f; all doors including garage gate same height d; a=(au, al) as window's vertical starting and ending;
	- Estimate (x, y, h, f, d, a);
	- Formulation: estimation problem:\
		<img src = '/Composition/images/3d/house-craft2.png' width = '300'>

## Procedural Reconstruction
- Muller, P., Zeng, G., Wonka, P., Van Gool, L.: Image-based procedural modeling of facades. TOG'07
- Zebedin, L., Bauer, J., Karner, K., Bischof, H.: Fusion of feature-and area-based information for urban buildings modeling from aerial imagery. ECCV'08
- Furukawa, Y., Curless, B., Seitz, S.M., Szeliski, R.: Manhattan-world stereo. CVPR'09
- Sinha, S., Steedly, D., Szeliski, R. Piecewise planar stereo for image-based rendering. ICCV'09
- Chauve, A.L., Labatut, P., Pons, J.P.: Robust piecewise-planar 3d reconstruction and completion from large-scale unstructured point data. CVPR'10
- Jiang, H., Xiao, J.: A linear approach to matching cuboids in rgbd images. CVPR'13
- Xiao, J., Furukawa, Y. Reconstructing the world's museums. IJCV'14
- Wang, H., Zhang, W., Chen, Y., Chen, M., Yan, K.: Semantic de- composition and reconstruction of compound buildings with symmetric roofs from lidar data and aerial imagery. Remote Sensing'15
- **NPR**: Huayi Zeng, Jiaye Wu and Yasutaka Furukawa. Neural Procedural Reconstruction for Residential Buildings. ECCV'18
	- Problem setup: input aerial image + LiDAR; output: 5-step PM;\
		<img src = '/Composition/images/3d/npr1.png' width = '500'>
	- Each branch:\
		<img src = '/Composition/images/3d/npr2.png' width = '500'>
