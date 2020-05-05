# Navigation Tasks

## Core Problems
- Exploration

## SOA
- T Chen, S Gupta, and A Gupta. Learning exploration policies for navigation. 2019
- Devendra Singh Chaplot, Dhiraj Gandhi, Saurabh Gupta, Abhinav Gupta, Ruslan Salakhutdinov. Learning to Explore using Active Neural SLAM. ICLR'20
	- https://github.com/devendrachaplot/Neural-SLAM
	- https://www.cs.cmu.edu/~dchaplot/projects/neural-slam.html
	- Insight: combination of classics and deep learning, analytical path planners with learned SLAM module;
	- Winner of the CVPR 2019 Habitat PointGoal Navigation Challenge;

## Unclassified
- Speaker-Follower Models for Vision-and-Language Navigation. NIPS'18

## Navigation Challenge and Benchmark
- VizDoom 2016
- DeepMind Lab 2016
- HoME 2017
- House 3D 2018
- Chalet 2018
- AI2-THOR 2017
- Realistic: Matterport, AdobeIndoorNav, Stanford 2D-3D-S, Scannet, Gibson, MINOS
- **Habitat**: M Savva, A Kadian, O Maksymets, Y Zhao, E Wijmans, B Jain, J Straub, J Liu, V Koltun, J Malik, D Parikh and D Batra. Habitat: A Platform for Embodied AI Research. ICCV'19
	- Tasks: Embodied QA, Language grounding, navigation;
	- Simulator: MatterPort3D, Gibson, Replic; https://github.com/facebookresearch/habitat-sim
	- Habitat-API: https://github.com/facebookresearch/habitat-api
- **StreetLearn**: P Mirowski, A Banki-Horvath, K Anderson, D Teplyashin, K Hermann, M Malinowski, M Grimes, K Simonyan, K Kavukcuoglu, A Zisserman, R Hadsell. The StreetLearn Environment and Dataset. 2019
	- Google Street View;
	- http://streetlearn.cc.

## CMU
- Devendra Singh Chaplot, Saurabh Gupta, A Gupta, R Salakhutdinov. Modular Visual Navigation using Active Neural Mapping. ICLR'19

## DeepMind:
- **DeepMind-Lab**: Learning to navigate in complex environments. ICLR'17
- Jake Bruce, Niko Sünderhauf, Piotr Mirowski, Raia Hadsell, Michael Milford. Learning Deployable Navigation Policies at Kilometer Scale from a Single Traversal. 2018
	- Key insight: real robot;
- A Banino, C Barry, B Uria, C Blundell, T Lillicrap, P Mirowski, A Pritzel, M Chadwick, T Degris, J Modayil, G Wayne, H Soyer, F Viola, B Zhang, R Goroshin, N Rabinowitz, R Pascanu, C Beattie, S Petersen, A Sadik, S Gaffney, H King, K Kavukcuoglu, D Hassabis, R Hadsell, D Kumaran. Vector-based Navigation using Grid-like Representations in Artificial Agents. Nature'18
- P Mirowski. et.al. Learning to navigate in cities without a map. NIPS'18
- K Hermann, M Malinowski, P Mirowski, A Banki-Horvath, K Anderson, R Hadsell. Learning to Follow Directions in Street View. AAAI'20
	- Input: front-view images (Google street-view), instructions; output: policy;
	- CNN-RNN;

## VIN
- Good summaries:
	- https://zhuanlan.zhihu.com/p/25515755
	- https://zhuanlan.zhihu.com/p/24478944
- **VIN**: Aviv Tamar, Yi Wu, Garrett Thomas, Sergey Levine, Pieter Abbeel. Value Iteration Network. NIPS'16
	<img src="/RL/images/navigation/vin1.png" alt="drawing" width="600"/>
	<img src="/RL/images/navigation/vin2.png" alt="drawing" width="600"/>
- **GVIN**: S Niu, S Chen, H Guo, C Targonski, M Smith, J Kovačević. Generalized Value Iteration Networks: Life Beyond Lattices. AAAI'18
	<img src="/RL/images/navigation/gvin.png" alt="drawing" width="600"/>
- Sources:
	- https://github.com/kentsommer/pytorch-value-iteration-networks

## Embodied AI
- Y Wu, Y Tian. Training Agent for First-Person Shooter Game with Actor-Critic Curriculum Learning. ICLR'17
	- VizDoom, known map;
	- Batch A3C;
- **House3D**: Y Wu, Y Wu, G Gkioxari, Y Tian. Building generalizable agents with a realistic and rich 3D environment. 2018
	- https://github.com/facebookresearch/House3D
	- https://github.com/jxwuyi/HouseNavAgent
- Baidu XWorld:
	- Zihang Dai: https://github.com/zihangdai/pytorch_xworld
- Intel:
	- **Learning to Act by Predicting the Future**, ICLR 2017
		- Alexey Dosovitskiy, Vladlen Koltun
		- Win the 2nd Vizdoom competition

## Codes 
- GA3C:
	- https://github.com/tgangwani/GA3C-DeepNavigation
- pycolab:
	- https://github.com/deepmind/pycolab
