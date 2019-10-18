# Flow based Approaches

## Good Summaries
- https://lilianweng.github.io/lil-log/2018/10/13/flow-based-deep-generative-models.html
- https://blog.evjang.com/2018/01/nf1.html
- https://blog.evjang.com/2018/01/nf2.html
- http://akosiorek.github.io/ml/2018/04/03/norm_flows.html

## Problem Definition
- GAN and VAE can't model p(x), because sum p(x|z)p(z) is hard!
- Important! change of variable theorem: 

## Normalizing Flows
- **Normalizing flows**: D. J. Rezende and S. Mohamed. Variational inference with normalizing flows. ICML'15
- NF Models:
	- **NICE**: L Dinh, D Krueger, and Y Bengio. Non-linear Independent Component Estimation. ICLRW'15
	- **MADE**: M Germain, K Gregor, I Murray, and H Larochelle. Made: Masked autoencoder for distribution estimation. ICML'15
	- **RealNVP**: Laurent Dinh, Jascha Sohl-Dickstein, Samy Bengio. Density estimation using Real NVP. ICLR'17
	- **Glow**: D Kingma, P Dhariwal. Glow: Generative Flow with Invertible 1x1 Convolutions. 2018
		- actnorm - invertible-1x1 conv - affine-coupling-layer
	- J Su, G Wu. f-VAEs: Improve VAEs with Conditional Flows. 2018
- Autoregressive:
	- **IAF**: Kingma, D. P., Salimans, T., Jozefowicz, R., Chen, X., Sutskever, I., and Welling, M. Improved variational inference with inverse autoregressive flow. NIPS'16
	- **MAF**: G Papamakarios, T Pavlakou, I Murray. Masked Autoregressive Flow for Density Estimation. 2018
