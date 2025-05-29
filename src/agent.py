from typing import Tuple
from .environment import GridWorld
from .config import ALPHA, GAMMA

class TDAgent:
    """Tabular TD(0) Agent."""
    def __init__(self, env: GridWorld):
        self.alpha = ALPHA
        self.gamma = GAMMA
        # value table initialised to zero
        self.V = [[0.0 for _ in range(env.height)] for _ in range(env.width)]

    def value(self, s: Tuple[int, int]) -> float:
        """Get the value of a state."""
        x, y = s
        return self.V[x][y]

    def update(self, s: Tuple[int, int], r: float, s_next: Tuple[int, int]) -> None:
        """Update the value function using TD(0) update rule."""
        x, y = s
        nx, ny = s_next
        self.V[x][y] += self.alpha * (r + self.gamma * self.V[nx][ny] - self.V[x][y]) 