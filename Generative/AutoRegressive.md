# Auto-Regressive

## Legacy
- **NADE**: Larochelle, Hugo and Murray, Iain. The neural autoregressive distribution estimator. AISTATS 2011
- **RNADE**: Uria, Benigno, Murray, Iain, and Larochelle, Hugo. RNADE: The real-valued neural autoregressive density-estimator. In NIPS, 2013.
- Theis, Lucas and Bethge, Matthias. Generative image modeling using spatial lstms. 2015

## Google
- Parmar, N., Vaswani, A., Uszkoreit, J., Kaiser, Ł., Shazeer, N., and Ku, A. Image transformer. 2018
	- code available in tensor2tensor
	- Block of local attention
	- [h, 3w, d], 3w: width + channel, d=256
	- Self-attention
		- 1D local attention
		- 2D local attention: raster-scan of sub-blocks, within each sub-block, raster-scan again for pixels
<img src="/Generative/images/image-transformer1.png" alt="drawing" width="400"/>
<img src="/Generative/images/image-transformer2.png" alt="drawing" width="400"/>

## DeepMind
- **Pixel-RNN** Oord, A. v. d., Kalchbrenner, N., and Kavukcuoglu, K. Pixel recurrent neural networks. In ICML, 2016.
- **Pixel-CNN**, Aaron van den Oord, Nal Kalchbrenner, Lasse Espeholt, Oriol Vinyals, Alex Graves, et al. Conditional
image generation with pixelcnn decoders, NIPS 2016
- Kalchbrenner, Nal, Espeholt, Lasse, Simonyan, Karen, Oord, Aaron van den, Graves, Alex, and Kavukcuoglu, Koray. Neural machine translation in linear time. 2016
- **VPN**: Kalchbrenner, Nal, Oord, Aaron van den, Simonyan, Karen, Danihelka, Ivo, Vinyals, Oriol, Graves, Alex, and Kavukcuoglu, Koray. Video pixel networks. 2016
- Reed, S., Oord, A., Kalchbrenner, N., Colmenarejo, S. G., Wang, Z., Chen, Y., Belov, D., and Freitas, N. Parallel multiscale autoregressive density estimation. ICML'17.
	- Conditional indenpendence, parallel
	- Sample complexity reduces O(N) to O(logN)
	- Coarse-to-fine: 4 x 4 to 8 x 8 to 16 x 16 to ... to 256 x 256
<img src="/Generative/images/parallel1.png" alt="drawing" width="400"/>
<img src="/Generative/images/parallel2.png" alt="drawing" width="400"/>
- Menick, J. and Kalchbrenner, N. Generating high fidelity images with subscale pixel networks and multidimensional upscaling. 2018
	- Ordering
	- Multi-scale upsampling
	- 3-bit to 8-bit, most significant first
<img src="/Generative/images/fidelity.png" alt="drawing" width="400"/>

## OpenAI
- Kingma, Diederik P and Salimans, Tim. Improving variational inference with inverse autoregressive flow. In NIPS, 2016.
- **Pixel-CNN++**, ICLR 2017
	- Mixture of Logistic distribution;
    - Implementation: Blind spot;
	- UNet shortcut;
	- PixelCNNLayer-up:
		- u-list: 5 * gated-resnet
		- ul-list: 5 * gated-resnet
<img src="/Generative/images/pixelcnnpp.png" alt="drawing" width="400"/>
- **PixelSNAIL**: Chen, X., Mishra, N., Rohaninejad, M., and Abbeel, P. Pixelsnail: An improved autoregressive generative model. ICML'18
	- code available;
	- Use the technique **SNAIL** proposed in [Mishra, Nikhil, Rohaninejad, Mostafa, Chen, Xi, and Abbeel, Pieter. A simple neural attentive meta-learner. In NIPS 2017 Workshop on Meta-Learning, 2017.]
	- Dilated/strided Convolution helps;
	- Zigzag ordering;
	- Built on Transformer;
	- Key modules:
		- Residual blocks (Causal-Conv + ResNet + ELU)
		- Attention blocks
<img src="/Generative/images/pixel-snail1.png" alt="drawing" width="400"/>
<img src="/Generative/images/pixel-snail2.png" alt="drawing" width="400"/>
- R. Child, S. Gray, A. Radford, I. Sutskever. Generating Long Sequences with Sparse Transformers. 2019
	- Observation: 128-layer image transformer on Cifar, very sparse attention
		- Two variations:
			- Previous l locations, and every l-th location, O(n^.5), working for images and videos;
			- Fixed attention pattern;
	- Sparse factorization of attention matrix, attention-matrix: O(n^2) to O(n^1.5)
	- Architecture and initialization for deeper networks
	- Recompute attention matrix to save memory;
	- Fast attention kernel for training;
	- Experiments:
		- Cifar-10
		- Text (EnWik8)
		- ImageNet (64x64)
		- Classical music
<img src="/Generative/images/sparse-transformer1.png" alt="drawing" width="400"/>
<img src="/Generative/images/sparse-transformer2.png" alt="drawing" width="400"/>

## Audio
- **Wave-net**: Van Den Oord, A., Dieleman, S., Zen, H., Simonyan, K., Vinyals, O., Graves, A., Kalchbrenner, N., Senior, A., and Kavukcuoglu, K. Wavenet: A generative model for raw audio. 2016
- Mehri, S., Kumar, K., Gulrajani, I., Kumar, R., Jain, S., Sotelo, J., Courville, A., and Bengio, Y. Samplernn: An unconditional end-to-end neural audio generation model. 2016
- Nal Kalchbrenner, Erich Elsen, Karen Simonyan, Seb Noury, Norman Casagrande, Edward Lockhart, Florian Stimberg, Aaron van den Oord, Sander Dieleman, and Koray Kavukcuoglu. Efficient neural audio synthesis. 2018