# Normalization Operators

## Batch-Norm
- **Batch Norm**: Sergey Ioffe and Christian Szegedy. Batch normalization: Accelerating deep network training by reducing internal covariate shift. In ICML, 2015.
<img src="/DL/images/batch-norm.png" alt="drawing" width="500"/>

- Class Conditioned BN:
	- Harm de Vries, Florian Strub, Jeremie Mary, Hugo Larochelle, Olivier Pietquin, and Aaron Courville. Modulating early visual processing by language. NIPS 2017.
- Takeru Miyato, Toshiki Kataoka, Masanori Koyama, and Yuichi Yoshida. **Spectral normalization** for generative adversarial networks. ICLR'18
- **Group Norm**: Y Wu, K He. Group Normalization. ECCV'18
<img src="/DL/images/group-norm1.png" alt="drawing" width="500"/>
<img src="/DL/images/group-norm2.png" alt="drawing" width="500"/>

## Layer-Norm
- J L Ba, J R Kiros, G E. Hinton. Layer Normalization. 2016
<img src="/DL/images/layer-norm1.png" alt="drawing" width="500"/>
<img src="/DL/images/layer-norm2.png" alt="drawing" width="600"/>

## Weight-Norm
- **Weight Norm**: Tim Salimans and Diederik Kingma. Weight normalization: A simple reparameterization to accelerate training of deep neural networks. In NIPS, 2016.
	- w = g * (v / ||v||)
	<img src="/DL/images/weight-norm.png" alt="drawing" width="500"/>

	- w is scale invariant to v, and the norm is always g
	- Data-dependent initialization (to make output with invariant scales)

## Instance Norm
- Dmitry Ulyanov, Andrea Vedaldi, Victor Lempitsky. Instance Normalization: The Missing Ingredient for Fast Stylization. 2017