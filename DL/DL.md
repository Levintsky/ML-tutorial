# Deep Learning Models

## Tutorials
- Yann LeCun, Yoshua Bengio, and Geoffrey Hinton. Deep learning. nature, 521(7553):436, 2015.

## Books
- **Deep learning**: Ian Goodfellow, Yoshua Bengio, Aaron Courville, and Yoshua Bengio. volume 1. MIT press Cambridge, 2016.

## Dropout
- Nitish Srivastava, Geoffrey Hinton, Alex Krizhevsky, Ilya Sutskever, and Ruslan Salakhutdinov. Dropout: A simple way to prevent neural networks from overfitting. JMLR, 15:1929–1958, 2014
- Y Gal, J Hron, A Kendall. Concrete Dropout. NIPS'17
- Aidan N. Gomez, Ivan Zhang, Kevin Swersky, Yarin Gal, Geoffrey E. Hinton. Targeted Dropout. ICLR 2019
	- github.com/for-ai/TD

## Gumbel-Softmax
- E Jang, S Gu, B Poole. Categorical Reparameterization with Gumbel-Softmax. ICLR'17
<img src="/DL/images/gumbel-softmax.png" alt="drawing" width="500"/>
<img src="/DL/images/gumbel-softmax2.png" alt="drawing" width="500"/>

- Good summaries:
	- https://casmls.github.io/general/2017/02/01/GumbelSoftmax.html
	- https://www.zhihu.com/question/62631725
	- https://blog.csdn.net/a358463121/article/details/80820878
- Make sampling process differentiable;
- Wouter Kool, Herke van Hoof, Max Welling. Stochastic Beams and Where to Find Them: The Gumbel-Top-k Trick for Sampling Sequences Without Replacement. ICML'19 best paper honorable mention
