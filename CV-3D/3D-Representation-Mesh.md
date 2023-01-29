# Mesh

## Legacy
- How to represent:
	- Voronoi diagram;
	- Delaunay triangulation;

## Misc
- L. Ladicky, O. Saurer, S. Jeong, F. Maninchedda, and M. Pollefeys. From point clouds to mesh using regression. ICCV'17

## Legacy: Marching Cubes;
- Given function defining +/- as outside inside, output the surface (mesh);
- Insight: go through each cube independently, lookup table (2 ^ 8 = 256 cases), handle the surface accordingly by lookup, adapt to find a better surface;
- http://www.cs.carleton.edu/cs_comps/0405/shape/marching_cubes.html
- **Marching cubes**: W. E. Lorensen and H. E. Cline. Marching cubes: A high resolution 3d surface construction algorithm. SIGGRAPH'87
	- Input: mask; output: mesh triangulation;
- https://www.boristhebrave.com/2018/04/15/marching-cubes-tutorial/
- https://www.boristhebrave.com/2018/04/15/marching-cubes-3d-tutorial/
- https://github.com/BorisTheBrave/mc-dc

## Legacy: Poisson Surface Reconstruction
- Input: given **discrete** points with known **oriented normals**, construct continuous watertight surface with **implicit function** that best match the normal;
	- Image the function is defined on the 3D space as
		- f(x) = 0 outside
		- f(x) = 1 inside;
		- grad(f(x)) oriented normals on surface;
		- Goal: get f(x) everywhere;
		- Smoothing (convolve with Gaussian kernel);
		- grad(f(x)) = smoothed (normal)
		- Min square solution: Laplacian(f(x)) = grad (normal)
		- To get f(x): marching cube on the oct-tree;
- M. M. Kazhdan, M. Bolitho, and H. Hoppe. Poisson surface reconstruction. SGP'06
- M. M. Kazhdan and H. Hoppe. Screened poisson surface reconstruction. SIGGRAPH'13
- Legacy: deform an initial mesh;
	- Similar to active-contour, leads to local minima;
	- Andrei Sharf, Thomas Lewiner, Ariel Shamir, Leif Kobbelt, and Daniel Cohen-Or. 2006. Competing fronts for coarse–to–fine surface reconstruction. CGF'06
- Legacy:
	- Hugues Hoppe. Progressive meshes. SIGGRAPH'96
	- F. Bernardini, J. Mittleman, H. Rushmeier, C. Silva, and G. Taubin. The ball-pivoting algorithm for surface reconstruction. TVCG'99
	- F. Calakli and G. Taubin. SSD: smooth signed distance surface reconstruction. CGF'11

## Backbone
- MLP:
	- Qingyang Tan, Lin Gao, et. al. Variational Autoencoders for Deforming 3D Mesh Models. CVPR'18
		- RIMD encoder, MLP decoder;
- GNN/GCN:
	- **Pixel2mesh**: Nanyang Wang, et. al. ECCV'18
		- GCN to deform a ball; unpool to add more nodes and edges;
		- https://github.com/nywang16/Pixel2Mesh
	- MeshCNN: R Hanocka, D Cohen-Or. SIGGRAPH'19
		- Mesh-Conv/Pool/Unpool;
	- Point2Mesh: R Hanocka, D Cohen-Or. SIGGRAPH'20

- Model on PC and preserve connection:
	- AtlasNet CVPR'18;
- Convert to mesh with a separate model:
	**Mesh R-CNN**: G Gkioxari, J Malik, and J Johnson. Mesh R-CNN. ICCV'19

## Supervision
- VAE:
	- Qingyang Tan, CVPR'18
- Pointwise:
	- CD/EMD: Pixel2mesh; AtlasNet; Point2Mesh;
	- Query some points: Point2Mesh (differentiable sampler);
	- Beam-gap loss: to handle narrow deep cavity;

## Direct mesh by downsample, upsample:
- Qingyang Tan, Lin Gao, Yu-Kun Lai, Jie Yang,and Shihong Xia. Mesh-based autoencoders for localized deformation component analysis. AAAI'18
	- https://github.com/aldehydecho/convMesh
- **Coma**: A. Ranjan, T. Bolkart, S. Sanyal, and M. J. Black. Generating 3D faces using convolutional mesh autoencoders. ECCV'18
	- https://coma.is.tue.mpg.de/

## Deformation-based
- DeformNet: A Kuryenkov, J Ji, A Garg, V Mehta, J Gwak, C Choy, S Savarese. DeformNet: Free-Form Deformation Network for 3D Shape Reconstruction from a Single Image. 2017
	- Check CAD/template-based method;
- Q Tan, L Gao, Y Lai, J Yang and S Xia. Mesh-based Autoencoders for Localized Deformation Component Analysis. 2017
	- AutoEncoder;
	- Input: multiple mesh; output: new mesh synthesis (deformation);
	- Point feature: manually designed;
	- Encoder: GCN;
	- Decoder: mirrored encoder?
- **cmr**: Angjoo Kanazawa, Shubham Tulsiani, Alexei A Efros, and Jitendra Malik. Learning category-specific mesh reconstruction from image collections. ECCV'18
	- https://github.com/akanazawa/cmr
	- Input: image; Output mesh;
	- Model:
		- Encoder: image -> 2D-CNN to get latent feature shared by three output modules;
		- Output: 1. camera pose; 2. deformation for each vertice; 3. texture;
	- Supervision: mask + keypoint + texture;
	<img src="/CV-3D/images/3d_output/cmr.png" alt="drawing" width="550"/>
- **Geometrics**: Edward J Smith, Scott Fujimoto, Adriana Romero, and David Meger. Geometrics: Exploiting geometric structure for graph-encoded objects. ICML'19
	- https://github.com/EdwardSmith1884/GEOMetrics
- **Pixel2mesh++**: Chao Wen, Yinda Zhang, Zhuwen Li, and Yanwei Fu. Pixel2mesh++: Multi-view 3d mesh generation via deformation. ICCV'19
	- https://github.com/walsvid/Pixel2MeshPlusPlus
	- Extension of Pixel2mesh;
	- First Pixel2mesh to get a coarse mesh;
	- Then iterative module to refine by multi-view with GCN;
- Charlie Nash, Yaroslav Ganin, S. M. Ali Eslami, and Peter W. Battaglia. PolyGen: An autoregressive generative model of 3d meshes. ICML'19
	- https://github.com/deepmind/deepmind-research/tree/master/polygen
	- **Transformer** on points and faces;
- CAD-Deform: Vladislav Ishimtsev, Alexey Bokhovkin, Alexey Artemov, Savva Ignatyev, Matthias Niessner, Denis Zorin. CAD-Deform: Deformable Fitting of CAD Models to 3D Scans. ECCV'20
	- Energy-based;
	- https://github.com/alexeybokhovkin/CAD-Deform

## Mesh from other representations (with differentiable op):
- Y. Liao, S. Donne, and A. Geiger. Deep marching cubes: Learning explicit surface representations. CVPR'18
	- Differentiable Marching Cubes;
- **NMC**: Zhiqin Chen and Hao Zhang, Neural Marching Cubes. TOG'21
	- https://github.com/czq142857/NMC

## Mesh from point cloud
- **DGP**: Francis Williams, Teseo Schneider, Claudio Silva, Denis Zorin, Joan Bruna, and Daniele Panozzo. Deep geometric prior for surface reconstruction. CVPR'19
	- Similar to deep-image-prior;
- Cheng Lin, Changjian Li, Yuan Liu, Nenglun Chen, Yi-King Choi, Wenping Wang. Point2Skeleton: Learning Skeletal Representations from Point Clouds. CVPR'21
	- https://github.com/clinplayer/Point2Skeleton
	- Input: point cloud, Output: skeleton
	- Skeleton: medial axis transform (MAT)
	- Model:
		- Graph initialization: topological and recovery priors;
		- GAE link prediction: graph latent by self supervision
		- Mesh generation: use GAE prediction to refine the initial graph;
