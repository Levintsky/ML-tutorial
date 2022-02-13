# Mesh

## Legacy
- How to represent:
	- Voronoi diagram;
	- Delaunay triangulation;

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

## Direct mesh by downsample, upsample:
- Qingyang Tan, Lin Gao, Yu-Kun Lai, Jie Yang,and Shihong Xia. Mesh-based autoencoders for localized deformation component analysis. AAAI'18
	- https://github.com/aldehydecho/convMesh
- Qingyang Tan, Lin Gao, Yu-Kun Lai, and Shihong Xia. Meshvae: Variational autoencoders for deforming 3d mesh models. CVPR'18
- **Coma**: A. Ranjan, T. Bolkart, S. Sanyal, and M. J. Black. Generating 3D faces using convolutional mesh autoencoders. ECCV'18
	- https://coma.is.tue.mpg.de/
- **MeshCNN**: Rana Hanocka, Amir Hertz, Noa Fish, Raja Giryes, Shachar Fleishman, Daniel Cohen-Or. MeshCNN: A Network with an Edge. SIGGRAPH'19
	- https://ranahanocka.github.io/MeshCNN/
	- https://github.com/ranahanocka/MeshCNN/
	- https://docs.google.com/presentation/d/1yLZ6uyAujyF0MtFWofAMFgWQpWaDYqS8vkdge_lzk6g/edit#slide=id.g35f391192_00
	- Insight: edges + affinity from meshes;
	- Mesh-Conv:\
		<img src="/CV-3D/images/3d_output/mesh-conv.png" alt="drawing" width="400"/>
	- Mesh-Pool: remove edges to collapse (5 edges -> 2)\
		<img src="/CV-3D/images/3d_output/mesh-pool-1.png" alt="drawing" width="400"/>
		<img src="/CV-3D/images/3d_output/mesh-pool-2.png" alt="drawing" width="400"/>
	- Mesh-Unpool:\
		<img src="/CV-3D/images/3d_output/mesh-unpool.png" alt="drawing" width="400"/>

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
	- Supervision: mask + keypoitn + texture;
	<img src="/CV-3D/images/3d_output/cmr.png" alt="drawing" width="550"/>
- **Pixel2mesh**: Nanyang Wang, Yinda Zhang, Zhuwen Li, Yanwei Fu, Wei Liu, and Yu-Gang Jiang. Pixel2mesh: Generating 3d mesh models from single rgb images. ECCV'18
	- GCN to deform a ball; unpool to add more nodes and edges;
	- CD for supervision;
	- https://github.com/nywang16/Pixel2Mesh
	<img src="/CV-3D/images/3d_output/pixel2mesh-1.png" alt="drawing" width="500"/>
	<img src="/CV-3D/images/3d_output/pixel2mesh-2.png" alt="drawing" width="500"/>
- **Geometrics**: Edward J Smith, Scott Fujimoto, Adriana Romero, and David Meger. Geometrics: Exploiting geometric structure for graph-encoded objects. ICML'19
	- https://github.com/EdwardSmith1884/GEOMetrics
- **Pixel2mesh++**: Chao Wen, Yinda Zhang, Zhuwen Li, and Yanwei Fu. Pixel2mesh++: Multi-view 3d mesh generation via deformation. ICCV'19
	- https://github.com/walsvid/Pixel2MeshPlusPlus
	- Extension of Pixel2mesh;
	- First Pixel2mesh to get a coarse mesh;
	- Then iterative module to refine by multi-view with GCN;
- **Mesh R-CNN**: Georgia Gkioxari, Jitendra Malik, and Justin Johnson. Mesh R-CNN. ICCV'19
	- https://gkioxari.github.io/meshrcnn/
	- https://github.com/facebookresearch/meshrcnn
	- Problem setup: input single image, output a set of detected object instances, with a triangle mesh for each object.
	- Approach: Mask R-CNN, coarse voxel (initial mesh), mesh refinement;
		<img src="/CV-3D/images/3d_output/mesh-rcnn.png" alt="drawing" width="600"/>
	- Lift to 3D: w x h G-channel;
	- Cubify: voxel to triangular mesh (8 vertices, 18 edges, 12 faces); merge shared edges and vertices; eliminate interior ones;
	- Mesh refinement (similar to **Pixel2mesh**):
		- 1. vertex alignment, which extracts image features for vertices; (with camera intrinsic)
		- 2. graph convolution, which propagates information along mesh edges;
		- 3. vertex refinement， which updates vertex positions.
	- Supevision: similar to **Geometrics**; sample points, Chamfer-Distance;
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

## Piecewise surface
- **AtlasNet**. T. Groueix, M. Fisher, V. G. Kim, B. C. Russell, and M. Aubry. Atlasnet: A papier-mache approach to learning 3d surface generation. CVPR'18
	- https://github.com/ThibaultGROUEIX/AtlasNet
	- Input point cloud or image encoded by a NN as feature f(x)
	- Then, f(x) and points sampled on a rectangle reconstruct an atlas on shape x;
		- Multiple MLP for multiple patches (Atlas);

## Mesh from point cloud
- **DGP**: Francis Williams, Teseo Schneider, Claudio Silva, Denis Zorin, Joan Bruna, and Daniele Panozzo. Deep geometric prior for surface reconstruction. CVPR'19
	- Similar to deep-image-prior;
- Rana Hanocka, Gal Metzer, Raja Giryes, Daniel Cohen-Or. Point2Mesh: A Neural Self-Prior for Deformable Meshes. SIGGRAPH'20
	- Insight: coarse-to-fine MeshCNN:
		<img src="/CV-3D/images/3d_output/point2mesh.png" alt="drawing" width="500"/>
	- Loss: Mesh to Point Cloud Distance: Chamfer + differentiable sampler;
	- Loss: Beam-gap loss: to handle narrow deep cavity;
	- Implementation: iterative for K=1000 iterations by network, then pass to RWM [Huang'18] to generate manifold, watertight and non-interscting surface;
	- Runtime (per iteration): 0.23/0.59/4.7 sec on 2k/6k/40k faces;
- Cheng Lin, Changjian Li, Yuan Liu, Nenglun Chen, Yi-King Choi, Wenping Wang. Point2Skeleton: Learning Skeletal Representations from Point Clouds. CVPR'21
	- https://github.com/clinplayer/Point2Skeleton
	- Input: point cloud, Output: skeleton
	- Skeleton: medial axis transform (MAT)
	- Model:
		- Graph initialization: topological and recovery priors;
		- GAE link prediction: graph latent by self supervision
		- Mesh generation: use GAE prediction to refine the initial graph;
