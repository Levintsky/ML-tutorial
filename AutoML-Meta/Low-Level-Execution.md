# Optimize Tensor Program

## Auto-TVM:
- Tianqi Chen and Thierry Moreau and Ziheng Jiang and Lianmin Zheng and Eddie Yan. TVM: An Automated End-to-End Optimizing Compiler for Deep Learning. OSDI 2018
- Tianqi Chen and Lianmin Zheng and Eddie Yan and Ziheng Jiang and Thierry Moreau and Luis Ceze and Carlos Guestrin and Arvind Krishnamurthy. Learning to Optimize Tensor Programs. NIPS 2018
	- Input: a program, output: an efficient execution;
	- Model 1: GBT (XGBoost);
	- Model 2: TreeGRU; (Kai Sheng Tai, Richard Socher, and Christopher D Manning. Improved semantic representations from tree-structured long short-term memory networks.)
	- Loss: ranking loss;
	- Optimization process (Sub-Modular): simulated annealing to collect candidates; diversity-aware optimization;
	- Transfer Learning;

## Polyhedral:
- Uday Bondhugula, Albert Hartono, J. Ramanujam, and P. Sadayappan. A practical automatic polyhedral parallelizer and locality optimizer. SIGPLAN, PLDI 2008
- **Tensor comprehension**: Nicolas Vasilache, Oleksandr Zinenko, Theodoros Theodoridis, Priya Goyal, Zachary DeVito, William S. Moses, Sven Verdoolaege, Andrew Adams, and Albert Cohen. Tensor comprehensions: Frameworkagnostic high-performance machine learning abstractions. CoRR 2018
- Sven Verdoolaege, Juan Carlos Juega, Albert Cohen, José Ignacio Gómez, Christian Tenllado, and Francky Catthoor. Polyhedral parallel code generation for cuda. ACM 2013
- **Halide**: Jonathan Ragan-Kelley, Connelly Barnes, Andrew Adams, Sylvain Paris, Frédo Durand, and Saman Amarasinghe. Halide: A language and compiler for optimizing parallelism, locality, and recomputation in image processing pipelines. PLDI 2013

## Black box:
- **FFTW**: M. Frigo and S. G. Johnson. Fftw: an adaptive software architecture for the fft. ICASSP 1998
-  Daniel Golovin, Benjamin Solnik, Subhodeep Moitra, Greg Kochanski, John Karro, and D. Sculley. Google vizier: A service for black-box optimization. KDD 2017
- **Atlas**: R. Clint Whaley and Jack J. Dongarra. Automatically tuned linear algebra software. 1998

## DSL:
- Fredrik Kjolstad, Shoaib Kamil, Stephen Chou, David Lugato, and Saman Amarasinghe. The tensor algebra compiler. OOPSLA 2017
- **Weld**: Shoumik Palkar, James J. Thomas, Deepak Narayanan, Anil Shanbhag, Rahul Palamuttam, Holger Pirk, Malte Schwarzkopf, Saman P. Amarasinghe, Samuel Madden, and Matei Zaharia. Weld: Rethinking the interface between data-intensive applications. PLDI CoRR 2017
- Michel Steuwer, Toomas Remmelg, and Christophe Dubach. Lift: A functional data-parallel ir for high-performance gpu code generation. CGO 2017
- Arvind K. Sujeeth, HyoukJoong Lee, Kevin J. Brown, Hassan Chafi, Michael Wu, Anand R. Atreya, Kunle Olukotun, Tiark Rompf, and Martin Odersky. Optiml: An implicitly parallel domain-specific language for machine learning. ICML 2011
