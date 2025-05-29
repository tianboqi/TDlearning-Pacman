import random
from typing import Tuple, List
from .environment import GridWorld

class Policy:
    """Base policy class."""
    def get_action(self, env: GridWorld, state: Tuple[int, int]) -> Tuple[int, int]:
        raise NotImplementedError

class RandomPolicy(Policy):
    """Policy that always chooses random actions."""
    def get_action(self, env: GridWorld, state: Tuple[int, int]) -> Tuple[int, int]:
        return random.choice(env.legal_actions(state))

class EpsilonGreedyPolicy(Policy):
    """Epsilon-greedy policy."""
    def __init__(self, agent, epsilon: float):
        self.agent = agent
        self.epsilon = epsilon

    def get_action(self, env: GridWorld, state: Tuple[int, int]) -> Tuple[int, int]:
        if random.random() < self.epsilon:
            # Explore: choose random action
            return random.choice(env.legal_actions(state))
        else:
            # Exploit: choose best action based on value estimates
            legal_actions = env.legal_actions(state)
            best_value = float('-inf')
            best_action = None
            
            for action in legal_actions:
                next_state = (state[0] + action[0], state[1] + action[1])
                value = self.agent.value(next_state)
                if value > best_value:
                    best_value = value
                    best_action = action
            
            return best_action 