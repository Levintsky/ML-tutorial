# Real Time Strategies

## Starcraft
- https://github.com/TorchCraft/TorchCraft
- Starcraft II:
	- https://deepmind.com/blog/alphastar-mastering-real-time-strategy-game-starcraft-ii/
	- https://github.com/deepmind/pysc2
	- Challenge
		- Game theory: StarCraft is a game where, just like rock-paper-scissors, there is no single best strategy.
		- Imperfect information
		- Long term planning
		- Real time
		- Large action space
	- Network
		- Transformer Torso (Deep reinforcement learning with relational inductive biases, ICLR'19)
		- Deep LSTM core
		- Auto-regressive policy head with a pointer network
		- a centralised value baseline (Counterfactual Multi-Agent Policy Gradients AAAI'18)
		- Warm-start: supervised learning with human data
		- Population-based training;
- FAIR: Forward Modeling for Partial Observation Strategy Games - A StarCraft Defogger. NIPS'18
	- **POMDP**
- Jonas Gehring (FAIR)
	- Starcraft
	- LSTM for each unit;
	- Train stage I: off-policy;
	- Stage II: on-policy;
	
## Dota
- **OpenAI Five**:
	- https://openai.com/blog/openai-five/
	- **Long time horizons**: Dota games run at 30 frames per second for an average of 45 minutes, resulting in 80,000 ticks per game. OpenAI Five observes every fourth frame, yielding 20,000 moves;
	- **Partially-observed state**: Units and buildings can only see the area around them. The rest of the map is covered in a fog hiding enemies and their strategies.
	- **High-dimensional, continuous action space**: In Dota, each hero can take dozens of actions, and many actions target either another unit or a position on the ground. 170,000 possible actions per hero (not all valid each tick, such as using a spell on cooldown)
	- **High-dimensional, continuous observation space**: Dota is played on a large continuous map containing ten heroes, dozens of buildings, dozens of NPC units, and a long tail of game features such as runes, trees, and wards. Valve’s Bot API as 20,000 (mostly floating-point) numbers representing all information a human is allowed to access
	- Pure from selfplay.\
		<img src="/RL/images/rts/openai-five.png" alt="drawing" width="600"/>
	- **Model structure**: Each of OpenAI Five’s networks contain a single-layer, 1024-unit LSTM that sees the current game state (extracted from Valve’s Bot API) and emits actions through several possible action heads.
	- **Exploration**
	- **Coordination**
	- Distributed training system: **Rapid**, could be applied to any gym environment
		- Workers **push** data of game play
		- Optimizer: P100 GPU, PPO with Adam, batch size 4096, BPTT 16 time steps, NCCL to average gradients (previously with MPI allreduce)
		- Eval workers: 2500 CPUs, v.s. hardcoded scripted bots and self\
			<img src="/RL/images/rts/openai-five-rapid.png" alt="drawing" width="600"/>
	- **Difference versus humans**: 150-170 actions per minute;
	- **Binary rewards can give good performance.**
	- **Creep blocking can be learned from scratch.**
	- **We’re still fixing bugs**