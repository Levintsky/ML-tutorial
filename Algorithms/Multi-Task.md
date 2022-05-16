# Multitask Learning

## Benchmarks
- RL:
	- Sokoban: S. Racanière, T. Weber, D. Reichert, L. Buesing, A. Guez, D. Jimenez Rezende, A. Puigdomènech Badia, O. Vinyals, N. Heess, Y. Li, et al. Imagination-augmented agents for deep reinforcement learning. NIPS'17
	- Meta-World: T. Yu, D. Quillen, Z. He, R. Julian, K. Hausman, C. Finn, and S. Levine. Meta-World: A benchmark and evaluation for multi-task and meta reinforcement learning. CoRL'20
	- K. Cobbe, C. Hesse, J. Hilton, and J. Schulman. Leveraging procedural generation to benchmark reinforcement learning. ICML'20
	- Language + RL;
		- BabyAI: M. Chevalier-Boisvert, D. Bahdanau, S. Lahlou, L. Willems, C. Saharia, T. H. Nguyen, and Y. Ben- gio. BabyAI: A platform to study the sample efficiency of grounded language learning.
	- Continuous Control:
		- DM-Suite: S. Tunyasuvunakool, A. Muldal, Y. Doron, S. Liu, S. Bohez, J. Merel, T. Erez, T. Lillicrap, N. Heess, and Y. Tassa. dm_control: Software and tasks for continuous control. Software Impacts, 6:100022, 2020.
	- Navigation (Vision):
		- DM-Lab: C. Beattie, J. Z. Leibo, D. Teplyashin, T. Ward, M. Wainwright, H. Küttler, A. Lefrancq, S. Green, V. Valdés, A. Sadik, et al. DeepMind lab. '16
	- Atari:
		- ALE: M. G. Bellemare, Y. Naddaf, J. Veness, and M. Bowling. The arcade learning environment: An evaluation platform for general agents. JAIR'13
	- Modular RL: W. Huang, I. Mordatch, and D. Pathak. One policy to control them all: Shared modular policies for agent-agnostic control. ICML'20
	- K. Zolna, A. Novikov, K. Konyushkova, C. Gulcehre, Z. Wang, Y. Aytar, M. Denil, N. de Freitas, and S. Reed. Offline learning from demonstrations and unlabeled experience. arxiv'20
- Language+RL:
	- BabyAI: M. Chevalier-Boisvert, D. Bahdanau, S. Lahlou, L. Willems, C. Saharia, T. H. Nguyen, and Y. Bengio. BabyAI: A platform to study the sample efficiency of grounded language learning.
- Language:
	- MassiveText: J. W. Rae, S. Borgeaud, T. Cai, K. Millican, J. Hoffmann, F. Song, J. Aslanides, S. Henderson, R. Ring, S. Young, et al. Scaling language models: Methods, analysis & insights from training gopher.

## AGI
- Basics:
	- Problem setup: same network with same weights, multiple problems;
- R. Sutton. The bitter lesson. Incomplete Ideas (blog), 13:12, 2019.
- **Gato**: Scott Reed, Konrad Żołna, Emilio Parisotto, Sergio Gómez Colmenarejo, Alexander Novikov, Gabriel Barth-Maron, Mai Giménez, Yury Sulsky, Jackie Kay, Jost Tobias Springenberg, Tom Eccles, Jake Bruce, Ali Razavi, Ashley Edwards, Nicolas Heess, Yutian Chen, Raia Hadsell, Oriol Vinyals, Mahyar Bordbar and Nando de Freitas. A Generalist Agent. 2022
	- Tokenization:
		- Text: SentencePiece (Kudo and Richardson, 2018), 32,000 subwords;
		- Image: ViT - rasterize order;
		- Discrete values (Atari actions): row-major serialization, [0, 1024)
		- Continuous (Torque, ...): mu-law encoded to -1 ~ +1, discretized to 1024 bins:
			- 𝐹(𝑥) = sgn(𝑥) log(|𝑥|𝜇 + 1.0)/log(𝑀𝜇 + 1.0)
	- Embedding:
		- Text, disc/cont obs/action: LUT;
		- Image: 1 ResNet block;
	- Backbone:
		- Transformer: 1.18B parameters;
		- Layer norm: pre-norm; Activtion: GEGLU;
		- Position encoding: relative patch encoding;
	- Training:
		- Masked autoregressive loss: log𝑝𝜃(𝑠1, ..., 𝑠𝐿) = ∑︁log𝑝𝜃(𝑠𝑙|𝑠1, ..., 𝑠𝑙−1)
		- 16x16 TPU v3, 1M steps, batch-size 512, token l=1024, 4 days;
	- Deployment: transformer-XL memory;
	- Which task?
		- Domain indicator;
		- Prompt condition: 25% prompt; half