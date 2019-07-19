# Autonomous Driving

## Modules
- HD Maps;
- Localization: to HD maps by centimeter accuracy;
- Perception: CNN;
- Prediction: predict other vehicles (RNN?)
- Planning: prediction + routing;
- Control;

## MIT
- Deep Traffic
	- https://selfdrivingcars.mit.edu/deeptraffic/
- Deep Tesla
- Devices:
	- External:
		- Radar
		- Visible-light camera;
		- LIDAR;
		- Infrared camera;
		- GPS/IMU
		- CAN
		- Audio
	- Internal:
		- Visible-light camera
		- Infrared camera
		- Audio

## RL
- M Bojarski, D Del Testa, D Dworakowski, B Firner, B Flepp, P Goyal, L D. Jackel, M Monfort, U Muller, J Zhang, X Zhang, J Zhao, K Zieba. End to End Learning for Self-Driving Cars. 2016

## Waymo
- Mayank Bansal, Alex Krizhevsky, Abhijit Ogale. ChauffeurNet: Learning to Drive by Imitating the Best and Synthesizing the Worst. 2018
	- Inputs: roadmap, traffic lights, speed limit, route, current agent box, dynamic boxes, past agent poses, future agent poses
	- **Imitation Learning**
	- Loss design:
		- Agent position, heading and box prediction;
		- Meta prediction: speed, subpixel
		- Collision Loss: overlap of the predicted agent box with all scene objects
		- On road loss
		- Geometry loss
