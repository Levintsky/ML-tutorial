# Auto-Regressive

## Legacy
- **NADE**: H Larochelle and I Murray. The neural autoregressive distribution estimator. AISTATS'11
	- RBM
- **RNADE**: B Uria, I Murray and H Larochelle. RNADE: The real-valued neural autoregressive density-estimator. NIPS'13.
	- RBM
- **MADE**: M Germain, K Gregor, I Murray, and H Larochelle. MADE: Masked autoencoder for distribution estimation. ICML'15.
- Theis, Lucas and Bethge, Matthias. Generative image modeling using spatial lstms. 2015
- Parmar, N., Vaswani, A., Uszkoreit, J., Kaiser, Ł., Shazeer, N., and Ku, A. Image transformer. ICML'18
	- code available in tensor2tensor
	- Block of local attention
	- [h, 3w, d], 3w: width + channel, d=256
		<img src="/Generative/images/autor/image-transformer1.png" alt="drawing" width="400"/>
	- Self-attention
		- 1D local attention
		- 2D local attention: raster-scan of sub-blocks, within each sub-block, raster-scan again for pixels
		<img src="/Generative/images/autor/image-transformer2.png" alt="drawing" width="400"/>
- **PixelRNN** A Oord, N Kalchbrenner and K Kavukcuoglu. Pixel recurrent neural networks. ICML'16.
- **PixelCNN**, A Oord, N Kalchbrenner, L Espeholt, O Vinyals, A Graves, et al. Conditional image generation with pixelcnn decoders, NIPS'16
	- Gated CNN (split the output, one as signal one as sigmoid gate, then element-wise product)
	<img src="/Generative/images/autor/pixelcnn.png" alt="drawing" width="700"/>
- **ByteNet**: N Kalchbrenner, L Espeholt, K Simonyan, A v d Oord, A Graves, and K Kavukcuoglu. Neural machine translation in linear time. 2016
	<img src="/Generative/images/autor/bytenet.png" alt="drawing" width="550"/>
- **VPN**: Kalchbrenner, Nal, Oord, Aaron van den, Simonyan, Karen, Danihelka, Ivo, Vinyals, Oriol, Graves, Alex, and Kavukcuoglu, Koray. Video pixel networks. 2016
- Reed, S., Oord, A., Kalchbrenner, N., Colmenarejo, S. G., Wang, Z., Chen, Y., Belov, D., and Freitas, N. Parallel multiscale autoregressive density estimation. ICML'17.
	- Conditional indenpendence, parallel
	- Sample complexity reduces O(N) to O(logN)
	- Coarse-to-fine: 4 x 4 first
	- Upscale 6 times to 8 x 8 to 16 x 16 to ... to 256 x 256
		<img src="/Generative/images/autor/parallel1.png" alt="drawing" width="400"/>\
		<img src="/Generative/images/autor/parallel2.png" alt="drawing" width="400"/>
- **MAF**: G. Papamakarios et al. Masked auto-regressive flow for density estimation, NIPS'17
	- Order matters!
	<img src="/Generative/images/autor/maf1.png" alt="drawing" width="500"/>
	<img src="/Generative/images/autor/maf2.png" alt="drawing" width="500"/>
- Menick, J. and Kalchbrenner, N. Generating high fidelity images with subscale pixel networks and multidimensional upscaling. 2018
	- Ordering
	- Multi-scale upsampling
	- 3-bit to 8-bit, most significant first\
		<img src="/Generative/images/autor/fidelity.png" alt="drawing" width="400"/>

## OpenAI
- **IAF**: D Kingma and T Salimans. Improving variational inference with inverse autoregressive flow. NIPS'16
	- https://github.com/openai/iaf
	- Inverse version of Rezende, D. and Mohamed, S. Variational inference with normalizing flows. ICML'15
	- Still a VAE, but the encoder will generate a sequence of (z0, z1, ..., zT)
		<img src="/Generative/images/autor/iaf1.png" alt="drawing" width="600"/>
		<img src="/Generative/images/autor/iaf2.png" alt="drawing" width="600"/>
- **Pixel-CNN++**, PixelCNN++: Improving the PixelCNN with Discretized Logistic Mixture Likelihood and Other Modifications. ICLR'17
	- Model architecture: U-Net\
		<img src="/Generative/images/autor/pixelcnnpp.png" alt="drawing" width="700"/>
	- Color distribution observes a mixture of logistic:\
		<img src="/Generative/images/autor/pixelcnnpp2.png" alt="drawing" width="400"/>\
		<img src="/Generative/images/autor/pixelcnnpp3.png" alt="drawing" width="400"/>
	- Loss function design: cdf observes Mixture of Logistic distribution, with decomposed r-g-b;
    - Implementation: Blind spot;
	- Architecture:
		- Init 1-layer shifted Conv-2D
		```python
		u_list  = [self.u_init(x)]
		ul_list = [self.ul_init[0](x) + self.ul_init[1](x)]
		```
		- **up_layers**: (PixelCNNLayer-up x 3), down-scale twice with a 1 conv stride = (2, 2); followed by **down_layers**: (PixelCNNLayer-down x 3), up-scale twice with a 1-layer deconv stride = (2, 2)
		```python
		for i in range(3):
		    # resnet block
		    u_out, ul_out = self.up_layers[i](u_list[-1], ul_list[-1])
		    u_list  += u_out
		    ul_list += ul_out
		    if i != 2: 
		        # downscale (only twice)
		        u_list  += [self.downsize_u_stream[i](u_list[-1])]
		        ul_list += [self.downsize_ul_stream[i](ul_list[-1])]
		u  = u_list.pop()
		ul = ul_list.pop()
		for i in range(3):
		    # resnet block
		    u, ul = self.down_layers[i](u, ul, u_list, ul_list)
		    # upscale (only twice)
		    if i != 2 :
		        u  = self.upsize_u_stream[i](u)
		        ul = self.upsize_ul_stream[i](ul)
		x_out = self.nin_out(F.elu(ul))
		```
		- Each up_layer or down_layer contains two streams: a **u_stream** and a **ul_stream**: 5 * gated-resnet; Two streams interleaves during forward every time
		```python
		u_list, ul_list = [], []
		for i in range(self.nr_resnet):
		    u  = self.u_stream[i](u)
		    ul = self.ul_stream[i](ul, a=u)
		    u_list  += [u]
		    ul_list += [ul]
		return u_list, ul_list
		```
- **PixelSNAIL**: Chen, X., Mishra, N., Rohaninejad, M., and Abbeel, P. Pixelsnail: An improved autoregressive generative model. ICML'18
	- https://github.com/neocxi/pixelsnail-public
	- Use the technique **SNAIL** proposed in [N Mishra, M Rohaninejad, X Chen, and P Abbeel. A simple neural attentive meta-learner. In NIPS 2017 Workshop on Meta-Learning, 2017.]
	- Dilated/strided Convolution helps;
	- Zigzag ordering;
	- Built on Transformer;
	- Key modules:
		- Residual blocks (Causal-Conv + ResNet + ELU)
		- Attention blocks
		<img src="/Generative/images/autor/pixel-snail1.png" alt="drawing" width="400"/>
		<img src="/Generative/images/autor/pixel-snail2.png" alt="drawing" width="400"/>
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
		<img src="/Generative/images/autor/sparse-transformer1.png" alt="drawing" width="400"/>\
		<img src="/Generative/images/autor/sparse-transformer2.png" alt="drawing" width="200"/>

## Others
- **PixelVAE**: I Gulrajani, K Kumar, F Ahmed, A Ali Taiga, F Visin, D Vazquez, and A Courville. PixelVAE: A latent variable model for natural images. ICLR'17
	<img src="/Generative/images/autor/pixel-vae1.png" alt="drawing" width="400"/>
	<img src="/Generative/images/autor/pixel-vae2.png" alt="drawing" width="400"/>

## Audio
- B. Uria, I. Murray, S. Renals, C. Valentini-Botinhao, and J. Bridle. Modelling acoustic feature dependencies with artificial neural networks: Trajectory-RNADE. ICASSP'15
- **Wave-net**: Van Den Oord, A., Dieleman, S., Zen, H., Simonyan, K., Vinyals, O., Graves, A., Kalchbrenner, N., Senior, A., and Kavukcuoglu, K. Wavenet: A generative model for raw audio. 2016
- Mehri, S., Kumar, K., Gulrajani, I., Kumar, R., Jain, S., Sotelo, J., Courville, A., and Bengio, Y. Samplernn: An unconditional end-to-end neural audio generation model. 2016
- Nal Kalchbrenner, Erich Elsen, Karen Simonyan, Seb Noury, Norman Casagrande, Edward Lockhart, Florian Stimberg, Aaron van den Oord, Sander Dieleman, and Koray Kavukcuoglu. Efficient neural audio synthesis. 2018