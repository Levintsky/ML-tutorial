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
	<img src="/Generative/images/mocogan.png" alt="drawing" width="500"/>

## Misc
- Caroline Chan, Shiry Ginosar, Tinghui Zhou, Alexei Efros. **Everybody Dance Now**. 2018
