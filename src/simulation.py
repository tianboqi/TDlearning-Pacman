from typing import Optional
from .environment import GridWorld
from .agent import TDAgent
from .policies import RandomPolicy, EpsilonGreedyPolicy
from .config import EPSILON

def simulate(env: GridWorld, agent: TDAgent, episodes: int, policy_type: str = "random") -> None:
    """
    Run N episodes using the specified policy.
    
    Args:
        env: The grid world environment
        agent: The TD learning agent
        episodes: Number of episodes to run
        policy_type: Either "random" or "epsilon-greedy"
    """
    # Create policy
    if policy_type == "random":
        policy = RandomPolicy()
    elif policy_type == "epsilon-greedy":
        policy = EpsilonGreedyPolicy(agent, EPSILON)
    else:
        raise ValueError(f"Unknown policy type: {policy_type}")

    # Run episodes
    for _ in range(episodes):
        state = env.reset()
        done = False
        while not done:
            action = policy.get_action(env, state)
            next_state, reward, done = env.step(action)
            agent.update(state, reward, next_state)
            state = next_state 