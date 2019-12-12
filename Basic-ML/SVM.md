# SVM

## Classical SVM
- For Lagrange Dual, check opt.pdf

## Structured-SVM
- http://www.csc.kth.se/cvap/cvg/rg/materials/magnus_004_slides.pdf
- Generalize classical SVM to structured output;
- Learn linear weight w for the loss/utility < w, phi(x, y) >
	- with desired loss delta(y, y')
	- argmin w, s.t. ||w||^2 + C max(y) (delta(y, ygt) + w (phi(x,y)-phi(x,ygt)))
- Special case: ranking-SVM;