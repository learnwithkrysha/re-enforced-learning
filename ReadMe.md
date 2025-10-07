# Coin Game - Reinforcement Learning

## Overview

This project implements a simple coin game using reinforcement learning (RL). The game is designed to demonstrate how an agent can learn optimal strategies through trial and error, using Q-learning to maximize its rewards.

## How the Coin Game Works

- The game consists of a player (agent) and a set of coins placed in an environment (e.g., a grid or a line).
- At each step, the agent can choose from a set of actions (e.g., move left, move right, pick up a coin).
- The goal is to collect as many coins as possible in the fewest moves.
- The environment provides feedback (rewards) based on the agent's actions (e.g., +1 for picking up a coin, 0 for moving to an empty space).
- The agent uses Q-learning to update its knowledge (Q-values) about which actions are best in each state.

## Q-Learning Algorithm

Q-learning is a model-free RL algorithm. The agent maintains a Q-table, where each entry Q(s, a) estimates the expected reward for taking action `a` in state `s`.

The Q-value update rule is:

$$
Q(s, a) \leftarrow Q(s, a) + \alpha [r + \gamma \max_{a'} Q(s', a') - Q(s, a)]
$$

Where:

- $s$ = current state
- $a$ = action taken
- $r$ = reward received
- $s'$ = next state
- $\alpha$ = learning rate
- $\gamma$ = discount factor

## Key Parameters and Their Effects

### 1. Learning Rate ($\alpha$)

- **Definition:** Controls how much new information overrides old information.
- **Effect:**
  - High $\alpha$ (e.g., 0.9): Q-values change quickly, learning is fast but can be unstable.
  - Low $\alpha$ (e.g., 0.1): Q-values change slowly, learning is stable but slow.
- **Example:**
  - If $\alpha=1$, the agent only considers the most recent experience.
  - If $\alpha=0$, the agent never updates its Q-values.

### 2. Discount Factor ($\gamma$)

- **Definition:** Determines the importance of future rewards.
- **Effect:**
  - High $\gamma$ (e.g., 0.9): Agent values future rewards, learns long-term strategies.
  - Low $\gamma$ (e.g., 0.1): Agent focuses on immediate rewards.
- **Example:**
  - If $\gamma=0$, the agent only cares about immediate rewards.
  - If $\gamma=1$, the agent considers future rewards as important as immediate ones.

### 3. Exploration Rate ($\epsilon$)

- **Definition:** Probability of choosing a random action (exploration) instead of the best-known action (exploitation).
- **Effect:**
  - High $\epsilon$ (e.g., 1.0): Agent explores a lot, learns about the environment.
  - Low $\epsilon$ (e.g., 0.01): Agent exploits known information, may miss better strategies.
- **Example:**
  - If $\epsilon=1$, the agent acts randomly.
  - If $\epsilon=0$, the agent always chooses the action with the highest Q-value.

## Example Scenario

Suppose the agent starts with no knowledge (Q-values are zero). It plays the game multiple times (episodes):

- With a high $\epsilon$, it tries different actions and discovers which ones lead to coins.
- As it learns, $\epsilon$ is reduced, so it starts exploiting the best actions it has found.
- The Q-table fills up with values that represent the expected reward for each action in each state.
- Over time, the agent learns the optimal path to collect all coins efficiently.

## How to Run

1. Ensure you have Python installed.
2. Run the main script:
   ```powershell
   python app.py
   ```
3. Adjust parameters (learning rate, discount factor, exploration rate) in the code to see how they affect learning.

## Conclusion

This coin game is a simple but powerful demonstration of reinforcement learning. By experimenting with different parameters, you can observe how the agent's learning and decision-making process changes, and how it ultimately learns to maximize its rewards.
