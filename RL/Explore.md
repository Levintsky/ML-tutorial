# Exploration, Exploitation

## From spinningup
- Intrinsic motivation: VIME, CTS/PixelCNN/hash-based pseudo-count; EX2; ICM; Burda; RND;
- Unsupervised: VIC; DIAYN; VALOR;

## Classics
- lec-17, 18 (CS-294, Sergey Levine)
- Approach 1: **UCB** (Upper Confidence Bounds)
    - Intuition: try each arm until you are sure it's not great:
        - a = argmax μa + √(2lnT/N(a))
        - Reg(T) ~ O(logT), provably as good as any algorithm
- Approach 2: **Thompson Sampling**:
    - An easy tutorial: https://github.com/andrecianflone/thompson/blob/master/thompson.ipynb
    - O Chapelle, L Li. An Empirical Evaluation of Thompson Sampling, NIPS'11
    - D Russo, B V Roy, A Kazerouni, and I Osband. A Tutorial on Thompson Sampling. 2017
- Approach 3: Information Gain:
    - D Russo, B V Roy. Learning to Optimize via Information-Directed Sampling. NIPS'14
        - IG(z,y|a) = E_y[H(p(z))-H(p(z)|y)|a], how much we learn about z from action a;
        - y = ra, z = θa (parameters of model p(ra))
        - g(a) = IG(θa,ra|a), information gain about a;
        - ∆a = E[r(a∗)-r(a)], expected suboptimality of a;
        - Choose a based on argmin_a ∆a^2/g(a),
            - Numerator ∆a^2: don't take suboptimal actions you know;
            - Denominator g(a): dont' take action you won't learn anything;
- In Q-learning:
    - ∆w = α(r(s)+γmaxQˆ(s',a';w)−Qˆ(s,a;w))∇wQˆ(s,a;w)
    - ∆w = α(r(s)+r(s,a)+γmaxQˆ(s',a';w)−Qˆ(s,a;w))∇wQˆ(s,a;w)
        - r(s,a): uncertainty;
- Summary\
    <img src="/RL/images/xx/xx-sum.png" alt="drawing" width="500"/>

## With NN
- Pseudo-count:
    - **CTS**: DeepMind. Unifying Count-Based Exploration and Intrinsic Motivation, NIPS'16
        - CTS model (Bellemare, M., Veness, J., and Talvitie, E. (2014). Skip context tree switching. ICML'14);
        - Enhance the reward r with rareness of next state N(s), r'=r+β/√(N(s)+ε):
            <img src="/RL/images/xx/xx-pseudo.png" alt="drawing" width="500"/>
- **EX2**: J Fu, J D. Co-Reyes, S Levine. EX2: Exploration with Exemplar Models for Deep Reinforcement Learning, NIPS'17
    - https://github.com/justinjfu/exemplar_models
    - Exemplar-classifier for seen/unseen:\
        <img src="/RL/images/xx/xx-ex2-1.png" alt="drawing" width="400"/>
    - Model archetecture (amortized rather than one each model)\
        <img src="/RL/images/xx/xx-ex2-2.png" alt="drawing" width="400"/>
    - Put together:\
        <img src="/RL/images/xx/xx-ex2-3.png" alt="drawing" width="400"/>
- Thompson Sampling:
    - Mandel, Liu, Brunskill, Popovic. Thompson sampling over representation & parameters. IJCAI'16
    - I Osband, C Blundell, A Pritzel, B V Roy. Deep Exploration via Bootstrapped DQN, NIPS'16
        - Train C DQN agents using bootstrapped samples; (expensive to train C nn);
        - Shared network Q with K outputs {Qk}k=1..K, masking distribution M:
            - Initial state s0;
            - k ~ Uniform(1,..,K); (choose a head)
            - for t=1..T do
                - Pick a = argmaxQk(st,a); (pick based on the head)
                - st+1, rt;
                - Sample bootstrap mask mt ~ M;
                - Add (st,at,rt+1,st+1,mt) to replay buffer;
    - Efficient Exploration through Bayesian Deep Q-Networks. NeurIPS workshop 2017
        - Use deep NN with last layer as Bayesian linear regression;

## Unclassified
- Stadie, Levine, Abbeel (2015). Incentivizing Exploration in Reinforcement Learning with Deep Predictive Models.

## Curiosity, Intrinsic Reward
- Sergey. Visual Reinforcement Learning with Imagined Goals. NIPS'18
- Learning to Play With Intrinsically-Motivated, Self-Aware Agents. NIPS'18
- S Singh. On Learning Intrinsic Rewards for Policy Gradient Methods. NIPS'18
- Y Burda, H Edwards, D Pathak, A Storkey, T Darrell, A Efros. Large-Scale Study of Curiosity-Driven Learning. ICLR'19
    - Contribution: Systematic analysis of how surprisal-based intrinsic motivation performs in a wide variety of environments.

## Unsupervised Option Discovery
- R Sutton, D Precup, and S Singh. Between mdps and semi-mdps: A framework for temporal abstraction in reinforcement learning. AI'99
- T Jung, D Polani, and P Stone. Empowerment for continuous agent—environment systems. Adaptive Behavior, 19(1):16–39, 2011.
- S Mohamed and D J Rezende. Variational information maximisation for intrinsically motivated reinforcement learning. NIPS'15
- R Fox, S Krishnan, I Stoica, and K Goldberg. Multi-Level Discovery of Deep Options. 2017
- DeepMind. Learning an embedding space for transferable robot skills. ICLR'18
    - Insight: a discriminability objective is equivalent to maximizing the mutual information between the latent skill z and some aspect of the corresponding trajectory;
    - Setting: with many tasks and reward function

## Unclassified
- https://blog.openai.com/reinforcement-learning-with-prediction-based-rewards/
- https://blog.openai.com/learning-montezumas-revenge-from-a-single-demonstration/
- Exploration in Structured Reinforcement Learning. NIPS'18
- Improving Exploration in Evolution Strategies for Deep Reinforcement Learning via a Population of Novelty-Seeking Agents. NIPS'18
- Diversity-Driven Exploration Strategy for Deep Reinforcement Learning. NIPS'18
