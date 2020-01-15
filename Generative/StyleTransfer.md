# Style Transfer

## Unclassified, New
- Unsupervised Image-to-Image Translation Using Domain-Specific Variational Information Bound. NIPS'18
- A Unified Feature Disentangler for Multi-Domain Image Translation and Manipulation. NIPS'18
- Yoshua Bengio. Image-to-image translation for cross-domain disentanglement. NIPS'18
- Unsupervised Learning of Artistic Styles with Archetypal Style Analysis. NIPS'18
- Han Shu, Yunhe Wang, Xu Jia, Kai Han, Hanting Chen, Chunjing Xu, Qi Tian, Chang Xu. Co-Evolutionary Compression for Unpaired Image Translation. ICCV'19
- Interactive Sketch & Fill: Multiclass Sketch-to-Image Translation. ICCV'19
- Attribute-Driven Spontaneous Motion in Unpaired Image Translation. ICCV'19
- Aggregation via Separation: Boosting Facial Landmark Detector With Semi-Supervised Style Translation. ICCV'19
- Few-Shot Unsupervised Image-to-Image Translation. ICCV'19

## Tutorial
- Y Jing, Y Yang, Z Feng, J Ye, Y Yu, and M Song. Neural Style Transfer: A Review. TVCG 2018
	- https://www.jiqizhixin.com/articles/2018-05-15-5
	- https://github.com/ycjing/Neural-Style-Transfer-Papers
		<img src="/Generative/images/transfer/style-transfer.png" alt="drawing" width="600"/>
- Style-Transfer in text: https://github.com/fuzhenxin/Style-Transfer-in-Text

## Classic
- **CRN**: Q Chen, V Koltun. Photographic Image Synthesis with Cascaded Refinement Networks. ICCV'17
	- https://github.com/WojciechMormul/crn
	- Input: semantic labels (m x n x c), c-classes;
	- Output: high resolution images (1k x 2k)
	- High-capacity required: 105M parameters;
	- Multi-resolution refinement; (4 x 8 -> 8 x 16 -> ...)
	- Network Architecture\
		<img src="/Generative/images/transfer/crn.png" alt="drawing" width="500"/>
	- Loss design: L1-norm of conv1-2, conv2-2, conv3-2, conv4-2, and conv5-2 in VGG-19;
	- Diversity loss:
		- produce 3k channels rather than 3;
		- Hindsight loss for multiple choices: loss between the best and the ground-truth;\
		<img src="/Generative/images/transfer/crn2.png" alt="drawing" width="400"/>
	- Implement framework
	```python
	def forward(self, semantics):
		x = semantics[0]
		semantic = None
		for i in range(modules_num):
			if i > 0: semantic = semantics[i]
			x = self.refinements_modules[i](x, semantic)
		return x
	# refinement module
	def forward(self, x, semantic):
		if self.first_module == False:
			x = self.upsample(x) # nn.Upsample()
			x = torch.cat([semantic, x], 1)
		# [conv - lnorm - lrelu]x2 - conv
		x = self.convmodule(x)
		return x
	# main loop
	# image, label as input
	gen_images_concat = net(label) # generate from semantic labels
	gen_images = []
	for i in range(k_diversed):
		gen_images.append(gen_images_concat[:,i*3:(i+1)*3,:,:])
	image_vgg19_layers = vgg19(image)
	gen_images_vgg19_layers = []
	for gen_image in gen_images:
		gen_images_vgg19_layers.append(vgg19(gen_image))
	mask_vgg19_layers = []
	for i in range(-len(image_vgg19_layers), 0): # take as many pyramid layers from mask as needed for loss
		mask_vgg19_layers.append(label[i])
	loss = diverse_loss(gen_images_vgg19_layers, image_vgg19_layers, mask_vgg19_layers)
	```

- **Cycle-GAN**: Zhu, J.-Y., Park, T., Isola, P., and Efros, A. A. Unpaired image-to-image translation using cycle-consistent adversarial networks. CVPR'17
	- https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix
	- **G**: X -> Y; discriminator: D_Y; **F**: Y -> X; discriminator: D_X;
	- Loss design:
		- Adversarial loss: E[logD_Y(y)] + E[log(1-D_Y(G(x)))]; Similar loss for D_X;
		- Consistency loss: ||F(G(x))-x|| + ||G(F(y))-y|| with L1 norm
		<img src="/Generative/images/transfer/cycle-gan.png" alt="drawing" width="400"/>
	- Implementation design:
	```python
	class CycleGANModel(nn.Module):
		def forward(self):
			self.fake_B = self.netG_A(self.real_A)  # G_A(A)
			self.rec_A = self.netG_B(self.fake_B)   # G_B(G_A(A))
			self.fake_A = self.netG_B(self.real_B)  # G_B(B)
			self.rec_B = self.netG_A(self.fake_A)   # G_A(G_B(B))
		def backward_G(self):
			self.loss_G_A = self.criterionGAN(self.netD_A(self.fake_B), True)
			self.loss_G_B = self.criterionGAN(self.netD_B(self.fake_A), True)
			self.loss_cycle_A = self.criterionCycle(self.rec_A, self.real_A) * lambda_A
			self.loss_cycle_B = self.criterionCycle(self.rec_B, self.real_B) * lambda_B
			self.loss_G = self.loss_G_A + self.loss_G_B + self.loss_cycle_A + self.loss_cycle_B + self.loss_idt_A + self.loss_idt_B
			self.loss_G.backward()
		def optimize_parameters(self):
			self.forward() # forward F, G
			# optimize G, netG_A, netG_B
			self.optimizer_G.zero_grad()
			self.backward_G.()
			self.optimizer_G.step()
			# DA, DB
			self.optimizer_D.zero_grad()
			self.backward_D_A()
			self.backward_D_B()
			self.optimizer_D.step()
	```
- **pix2pix**: Isola, P., Zhu, J.-Y., Zhou, T., and Efros, A. A. Image-to-image translation with conditional adversarial networks. CVPR'17
	- Insight: Conditional GAN + supervised transfer tranining;
	- **Conditional GAN**: notice the original input is provided!\
		<img src="/Generative/images/transfer/pix2pix3.png" alt="drawing" width="250"/>
	- Loss design:
		<img src="/Generative/images/transfer/pix2pix1.png" alt="drawing" width="250"/>
		<img src="/Generative/images/transfer/pix2pix2.png" alt="drawing" width="330"/>
	- Model:
	```python
	class Pix2pix(nn.Module):
		def forward(self):
			self.fake_B = self.netG(self.real_A)  # G(A)
		def backward_D(self):
			# conditional-GAN for D!
			fake_AB = torch.cat((self.real_A, self.fake_B), 1)
			pred_fake = self.netD(fake_AB.detach())
			self.loss_D_fake = self.criterionGAN(pred_fake, False)
			real_AB = torch.cat((self.real_A, self.real_B), 1)
			pred_real = self.netD(real_AB)
			self.loss_D_real = self.criterionGAN(pred_real, True)
			self.loss_D = (self.loss_D_fake + self.loss_D_real) * 0.5
			self.loss_D.backward()
		def backward_G(self):
			# First, G(A) should fake the discriminator
			fake_AB = torch.cat((self.real_A, self.fake_B), 1)
			pred_fake = self.netD(fake_AB)
			self.loss_G_GAN = self.criterionGAN(pred_fake, True)
			# Second, G(A) = B
			self.loss_G_L1 = self.criterionL1(self.fake_B, self.real_B) * self.opt.lambda_L1
			# combine loss and calculate gradients
			self.loss_G = self.loss_G_GAN + self.loss_G_L1
			self.loss_G.backward()
		def optimize_parameters(self):
			self.forward() # forward F, G
			self.optimizer_G.zero_grad()
			self.backward_G.()
			self.optimizer_G.step()
			self.optimizer_D.zero_grad()
			self.backward_D()
			self.optimizer_D.step()
	```

## Image Optimization-based
- Parametric:
	- Content loss: intermediate layer square-loss (F1-F2)^2
	- Style loss: 2nd order (G1-G2)^2
		<img src="/Generative/images/transfer/neural-style1.png" alt="drawing" width="250"/>
	- L. A. Gatys, A. S. Ecker, and M. Bethge, Texture Synthesis Using Convolutional Neural Networks. NIPS'15
	- L. A. Gatys, A. S. Ecker, and M. Bethge, A neural algorithm of artistic style. 2015
	- L. A. Gatys, A. S. Ecker, and M. Bethge, Image style transfer using convolutional neural networks, CVPR'16
	- G. Berger and R. Memisevic, Incorporating long-range consistency in cnn-based texture generation, ICLR'17
	- A. Mahendran and A. Vedaldi, Understanding deep image representations by inverting them, CVPR'15
	- A. Mordvintsev, C. Olah, and M. Tyka, “Inceptionism: Going deeper into neural networks,” 2015 [Online]. Available: https://research.googleblog.com/2015/06/inceptionism-going-deeper-into-neural.html
	- Visualizing deep convolutional neural networks using natural pre-images, IJCV'16
	- Y. Li, N. Wang, J. Liu, and X. Hou, Demystifying neural style transfer. IJCAI'17
		- Theoretically, Gram is similar to minimize MMD (mean and variance matches)
	- S. Li, X. Xu, L. Nie, and T.-S. Chua, “Laplacian-steered neural style transfer, ACMMM'07
	- V. M. Patel, R. Gopalan, R. Li, and R. Chellappa, Visual domain adaptation: A survey of recent advances, SPM'15.
- Non-Parametric:
	-  C. Li and M. Wand, Combining markov random fields and convolutional neural networks for image synthesis, CVPR'16

## Model-based
- **PSPM** (Per-Style-Per-Model)
	- J. Johnson, A. Alahi, and L. Fei-Fei, Perceptual losses for realtime style transfer and super-resolution. ECCV'16
	- D. Ulyanov, V. Lebedev, A. Vedaldi, and V. Lempitsky, Texture networks: Feed-forward synthesis of textures and stylized images. ICML'16
	- D. Ulyanov, A. Vedaldi, and V. Lempitsky, Improved texture networks: Maximizing quality and diversity in feed-forward stylization and texture synthesis. CVPR'17
		- **Instance-Normalization**
	- C. Li and M. Wand, Precomputed real-time texture synthesis with markovian generative adversarial networks. ECCV'16
- **MSPM** (Multiple-Style-Per-Model):
	- **CIN**: V. Dumoulin, J. Shlens, and M. Kudlur, A learned representation for artistic style, ICLR'17
		- CIN (Conditional Instance Normalization)
	- D. Chen, L. Yuan, J. Liao, N. Yu, and G. Hua, Stylebank: An explicit representation for neural image style transfer, CVPR'17
	- Y. Li, F. Chen, J. Yang, Z. Wang, X. Lu, and M.-H. Yang, Diversified texture synthesis with feed-forward networks, CVPR'17
	-  H. Zhang and K. Dana, Multi-style generative network for realtime transfer, 2017
- **ASPM** (Arbitrary-Style-Per-Model):
	- T. Q. Chen and M. Schmidt, Fast patch-based style transfer of arbitrary style. NIPS Workshop'16
	- Xun Huang, Serge Belongie. Arbitrary Style Transfer in Real-time with Adaptive Instance Normalization. ICCV'17
		- **Real-time ASPM**
		- Adaptive Instance Normalization (AdaIN)
	- G Ghiasi, H Lee, M Kudlur, V Dumoulin, J Shlens. Exploring the Structure of a Real-time, Arbitrary Neural Artistic Stylization Network. BMVC'17
	- Yijun Li, Chen Fang, Jimei Yang, Zhaowen Wang, Xin Lu, and Ming-Hsuan Yang. Universal Style Transfer via Feature Transforms. NIPS'17

## 3D Point Cloud

## Legacy
- NPR (non-photorealistic rendering):
	- B. Gooch and A. Gooch, Non-photorealistic rendering. 2001
	- T. Strothotte and S. Schlechtweg, Non-photorealistic computer graphics: modeling, rendering, and animation. 2002
	- P. Rosin and J. Collomosse, Image and video-based artistic stylisation. 2012
- SBR (Stroke-based rendering):
	- A. Hertzmann, Painterly rendering with curved brush strokes of multiple sizes. SIGGRAPH'98
- Texture Transfer:
	- A. A. Efros and W. T. Freeman, Image quilting for texture synthesis and transfer. SIGGRAPH'01
	- I. Drori, D. Cohen-Or, and H. Yeshurun, Example-based style synthesis. CVPR'03
	- O. Frigo, N. Sabater, J. Delon, and P. Hellier, “Split and match: Example-based adaptive patch sampling for unsupervised style transfer, CVPR'16
	- M. Elad and P. Milanfar, Style transfer via texture synthesis. TIP'17
- EBR (Example-based):
	- **Image Analogy**: A. Hertzmann, C. E. Jacobs, N. Oliver, B. Curless, and D. H. Salesin, Image analogies. SIGGRAPH'01