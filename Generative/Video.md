# Video Generation

## Autoregressive
- **VPN**: Kalchbrenner, Nal, Oord, Aaron van den, Simonyan, Karen, Danihelka, Ivo, Vinyals, Oriol, Graves, Alex, and Kavukcuoglu, Koray. Video pixel networks. 2016

## GAN
- **VGAN**: C. Vondrick, H. Pirsiavash, and A. Torralba. Generating videos with scene dynamics. NIPS'16
	- Spatial-temporal 3D CNN
- **TGAN**: M. Saito, E. Matsumoto, and S. Saito. Temporal generative adversarial nets with singular value clipping. ICCV'17
	- Jensen-Shannon diver- gence
- **MoCoGAN**: S. Tulyakov, M.-Y. Liu, X. Yang, and J. Kautz. MoCoGAN: Decomposing motion and content for video generation. CVPR'18
	- the content vector, zC, is sampled once and fixed
	- Then, a series of random variables [ε(1), ..., ε(K)] is sampled and mapped to a series of motion codes [z(1) , ..., z(K ) ] via the recurrent neural network RM;
	- A generator GI produces a frame, x, using the content and the motion vectors {zC, z(k)}
	- The discriminators, DI and DV, are trained on real and fake images and videos, respectively, sampled from the training set v and the generated set v.
	<img src="/Generative/images/video/mocogan.png" alt="drawing" width="500"/>

- **pix2pixHD**: T Wang, M Liu, J Zhu, A Tao, J Kautz, and B Catanzaro. 2017. High-Resolution Image Synthesis and Semantic Manipulation with Conditional GANs.

## Misc
- C Chan, S Ginosar, T Zhou, A Efros. **Everybody Dance Now**. 2018
	- Problem setup: change source subject to target (person to person)
	- Image-to-image translation
	- 1. Pose detection [5, 27, 35]: keypoints and lines between connected joints
	- 2. Global pose normalization: different people has different portion, linear mapping;
	- 3. Mapping from normalized pose stick figures to the target subject: pix2pixHD\
		<img src="/Generative/images/video/every-dance1.png" alt="drawing" width="600"/>
	- Loss design: pix2pixHD; D1, D2, D3: multi-scale:\
		<img src="/Generative/images/video/every-dance2.png" alt="drawing" width="600"/>
	- Temporal smoothness:\
		<img src="/Generative/images/video/every-dance3.png" alt="drawing" width="500"/>
	- Face GAN:\
		<img src="/Generative/images/video/every-dance4.png" alt="drawing" width="500"/>
	- Full objective:\
		<img src="/Generative/images/video/every-dance5.png" alt="drawing" width="500"/>	
- T Wang, M Liu, J Zhu, G Liu, A Tao, J Kautz, B Catanzaro. Video-to-Video Synthesis, 2018
- D. Chen, J. Liao, L. Yuan, N. Yu, and G. Hua. Coherent online video style transfer. ICCV'17
