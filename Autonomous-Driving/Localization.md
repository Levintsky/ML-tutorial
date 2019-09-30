# Localization

## Problem Definition
- Point clouds + HD-map;

## Alg
- J Levinson, M Montemerlo, and S Thrun. Map-based precision vehicle localization in urban environments. RSS'07
- E Javanmardi, M Javanmardi, Y Gu, and S Kamijo. Autonomous vehicle self-localization based on probabilistic planar surface map and multi-channel LiDAR in urban area. ITSC'18
- **GILL**: I Barsan, S Wang, A Pokrovsky, and R Urtasun. Learning to localize using a lidar intensity map. CoRL'18
	- Real-time localization with centimeter level accuracy;
	<img src="/Autonomous-Driving/images/localization/gill.png" alt="drawing" width="600"/>

- X Wei, I Barsan, S Wang, J Martinez, R Urtasun. Learning to Localize Through Compressed Binary Maps. CVPR'19
	- Motivation: HD-Map too large fro storage; (900G for LA, 168T for USA)
	- Learn to binarize the map features;
	- Run-length encoding on top of Huffman coding;
	- Image compression (DL-based): encoding - quantization - decoding;
	<img src="/Autonomous-Driving/images/localization/binary1.png" alt="drawing" width="600"/>
	<img src="/Autonomous-Driving/images/localization/binary2.png" alt="drawing" width="600"/>
