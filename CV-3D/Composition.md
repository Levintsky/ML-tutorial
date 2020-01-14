# Part/Primitive/Compositional Model

- M. Sung, H. Su, R. Yu, and L. Guibas. Deep functional dictionaries: Learning consistent semantic structures on 3D models from functions. NIPS'18
	- Input n points; output: n x k dictionary;
	- Structured sparsity;
	- https://github.com/mhsung/deep-functional-dictionaries
	- Different deep dictionaries;
	- Applications with adaptation in co-segmentation, keypoint correspondence, smooth functional approximation (modeled as constraint);
	- Given an input X, At = A(X; theta) to get basis
	- Solve x = argmin||At x - f||^2 s.t. C(x)
	- Update theta = theta - eta * d L(A(X, theta); f, x) / dx