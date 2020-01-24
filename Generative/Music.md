# Music Generation

## Magenta Team (Google)
- **Magenta**:
	- https://github.com/tensorflow/magenta/tree/master/magenta/models
- **COCONet**: Cheng-Zhi Anna Huang, Tim Cooijmans, Adam Roberts, Aaron Courville, Douglas Eck, Counterpoint by Convolution
	- Blocked Gibbs Sampling
	- https://github.com/tensorflow/magenta/tree/master/magenta/models/coconet
- **Audio Deepdream**: Adam Roberts, Cinjon Resnick, Diego Ardila, Doug Eck. Audio Deepdream: Optimizing raw audio with convolutional networks. ISMIR'16
	- Follow DeepDream [8] in images;
	- Use 1d-conv x 6, following Van den Oord [13]
	- Input: 30-second clips, output 100-dim CF (collaborative filtering);
	- WALS
- **Note-RNN**: Natasha Jaques, Shixiang Gu, Richard E. Turner, Douglas Eck. Generating Music by Fine-Tuning Recurrent Neural Networks with Reinforcement Learning. NIPS'16 Workshop
	- DQN
	- LSTM to predict next note (monophonic melody)
	- Reward design: r(s, a) = logp(a|s) + 1/c rMT(a,s), i.e., music theory reward
	- Connection to SOC (Stochastic Optimal Control);
- Engel, J., Hoffman, M., and Roberts, A. Latent constraints: Learning to generate conditionally from unconditional generative models. 2017
- **NSynth**: Engel, J., Resnick, C., Roberts, A., Dieleman, S., Eck, D., Simonyan, K., and Norouzi, M. Neural audio synthesis of musical notes with wavenet autoencoders. ICML'17
- Roberts, A., Engel, J., Oore, S., and Eck, D. (eds.). Learning Latent Representations of Music to Generate Interactive Musical Palettes, 2018.
- **MusicVAE**: Adam Roberts, Jesse Engel, Colin Raffel, Curtis Hawthorne, Douglas Eck. A Hierarchical Latent Vector Model for Learning Long-Term Structure in Music. ICML'18
	- https://github.com/tensorflow/magenta/tree/master/magenta/models/music_vae
	- https://storage.googleapis.com/magentadata/papers/musicvae/index.html
	- beta-VAE
	- Desired: 1. similar latent z produces semantically similar x; 2. disentangled;
	- Recurrent-VAE: used to have a problem, RNN ignores z and decode;
	- Encoder:
		- Bidirectional-RNN: mean, variance;
	- Decoder:
		- Hierarchical: conductor + output;
- C Hawthorne, A Stasyuk, Adam Roberts, Ian Simon, Cheng-Zhi Anna Huang, Sander Dieleman, Erich Elsen, Jesse Engel, Douglas EckEnabling Factorized Piano Music Modeling and Generation with the MAESTRO Dataset. ICLR'19

## DeepMind
- Dieleman, S., van den Oord, A., and Simonyan, K. The chal- lenge of realistic music generation: modelling raw audio at scale. NIPS'18

## OpenAI
- MuseNet

## Unclassified
- Hang Chu, Raquel Urtasun, Sanja Fidler. Song From PI: A Musically Plausible Network for Pop Music Generation. ICLR'17
	- https://chuhang.github.io/projects/songfrompi/index.html
- DeepMind. The challenge of realistic music generation: modelling raw audio at scale. NIPS'18
- Francis Bach. SING: Symbol-to-Instrument Neural Generator. NIPS'18
