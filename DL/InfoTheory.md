# Information Theory in ML

## Resources
- https://lilianweng.github.io/lil-log/2017/09/28/anatomize-deep-learning-with-information-theory.html
- Information Theory in Deep Learning (Youtube): https://www.youtube.com/watch?v=bLqJHjXihK8&feature=youtu.be

## Basic Concepts
- Markov Chain
- Kullback–Leibler (KL) Divergence
- Mutual Information: I(X; Y)
- Data Processing Inequality (DPI): X->Y->Z, then I(X;Y)>=I(X;Z)
- Reparametrization invariance: Two invertible functions f1, f2, then I(X;Y)=I(f1(X);f2(Y))
- Information Plane Theorem:
	- X-axis: The sample complexity of Ti is determined by the encoder mutual information I(X;Ti). Sample complexity refers to how many samples you need to achieve certain accuracy and generalization.
	- Y-axis: The accuracy (generalization error) is determined by the decoder mutual information I(Ti;Y).\
		<img src="/DL/images/info-theory/info-plane.png" alt="drawing" width="450"/>
- Two Optimization Phases:
	- Among early epochs, the mean values are three magnitudes larger than the standard deviations. After a sufficient number of epochs, the error saturates and the standard deviations become much noisier afterward. The further a layer is away from the output, the noisier it gets, because the noises can get amplified and accumulated through the back-prop process (not due to the width of the layer).
		<img src="/DL/images/info-theory/two-opt-phase.png" alt="drawing" width="450"/>

## Learning Theory
- Old Generalization Bounds:
	- Read https://mostafa-samir.github.io/ml-theory-pt1/ and https://mostafa-samir.github.io/ml-theory-pt2/ for ML theory;
		<img src="/DL/images/info-theory/old-bound.png" alt="drawing" width="450"/>
- New Input compression bound:
		<img src="/DL/images/info-theory/new-bound.png" alt="drawing" width="450"/>
