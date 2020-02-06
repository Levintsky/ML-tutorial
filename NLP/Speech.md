# Speech Recognition

## Benchmarks
- **Librispeech**: Librispeech: an asr corpus based on public domain audio books. ICASSP'15
	- http://www.openslr.org/11

## Input Features
- MMFC (Mel-Filterbanks)
- Power-spectrum
- Raw-wave

## Models
- **HMM/GMM**
	- Woodland, P. C., And Young, S. J. The htk tied-state continuous speech recogniser. In
Eurospeech (1993).
- ** DNN-Legacy**
	- Hinton. et.al. Deep neural networks for acoustic modeling in speech recognition: The shared views of four research groups. SPM 2012
- **CNN**
	- Sercu, Lecun. Very deep multilingual convolutional neural networks for lvcsr. arXiv preprint arXiv:1509.08967 (2015).
	- Joint training of convolutional and nonconvolutional neural networks. ICASSP'14 
- **RNN**
	- Alex Graves. Speech recognition with deep recurrent neural networks. ICASSP'13
- ReLU
	- M. Zeiler, M. Ranzato, R. Monga, M. Mao, K. Yang, Q. V. Le, P. Nguyen,
A. Senior, V. Vanhoucke, J. Dean, and G. Hinton. On rectified linear units for
speech processing. ICASSP'13
- **CTC**
	- A loss function without parameter, to choose the alignment with the best score
	- Alex Graves. Connectionist temporal classification: labelling unsegmented sequence data with recurrent neural networks. ICML 2006.
	- Open source by Baidu-Research: https://github.com/baidu-research/warp-ctc
- Beam Search

## SOAs
- **Google**
	- W. Chan, N. Jaitly, Q. V. Le, and O. Vinyals. Listen, attend and spell. arxiv, 2015
- **Baidu Deep-Speech**:
	- Deep speech: Scaling up end-to-end speech recognition. arXiv preprint arXiv:1412.5567 (2014).
	- Deep speech 2: End-to-end speech recognition in english and mandarin. arXiv preprint arXiv:1512.02595 (2015).
	- All use power-spectrum as input.
	- Neural Voice Cloning with a Few Samples. NIPS'18
- **FAIR**:
	- Ronan: Estimating phoneme class conditional probabilities from raw speech signal using convolutional neural networks. 2013
	- Ronan: Wav2Letter: an End-to-End ConvNet-based Speech Recognition System
		- Raw wave: input
		- Hyperbolic tangent, HardTanh, ReLU: similar result
		- Fully 1d-conv
	- Ronan: End-to-End Speech Recognition From the Raw Waveform, 2018
	- Ronan: To Reverse the Gradient or Not: An Empirical Comparison of Adversarial and Multi-task Learning in Speech Recognition, 2018
- Eesen: End-to-end speech recognition using deep RNN models and wfst-based decoding. arXiv 2015.
- The ibm 2015 english conversational telephone speech recognition system.

## TTS
- van den Oord, A., et al. WaveNet: A Generative Model for Raw Audio. NIPS'16
	- Dilated Conv\
		<img src = '/NLP/images/wavenet1.png' width = '500px'>
	- ResNet\
		<img src = '/NLP/images/wavenet2.png' width = '500px'>
- Transfer Learning from Speaker Verification to Multispeaker Text-To-Speech Synthesis. NIPS'18
