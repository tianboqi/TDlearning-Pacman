from typing import Tuple, Dict, List
from .config import GRID_W, GRID_H, WALLS, START, GOAL

class GridWorld:
    """Grid constructed from config.py"""

    ACTIONS: Dict[str, Tuple[int, int]] = {
        "UP":    (0, -1),
        "DOWN":  (0, 1),
        "LEFT":  (-1, 0),
        "RIGHT": (1, 0),
    }

    def __init__(self):
        self.width, self.height = GRID_W, GRID_H
        self.walls = set(WALLS)
        self.start = START
        self.goal = GOAL
        self.state = self.start

    def reset(self) -> Tuple[int, int]:
        """Reset the environment to initial state."""
        self.state = self.start
        return self.state

    def step(self, action: Tuple[int, int]) -> Tuple[Tuple[int, int], float, bool]:
        """Take a step; return (next_state, reward, done)."""
        x, y = self.state
        dx, dy = action
        nx, ny = x + dx, y + dy

        # wall / boundary check
        if (0 <= nx < self.width and 0 <= ny < self.height and
                (nx, ny) not in self.walls):
            self.state = (nx, ny)   # legal move

        reward = 1.0 if self.state == self.goal else 0.0
        done = (self.state == self.goal)
        return self.state, reward, done

    def legal_actions(self, state: Tuple[int, int]) -> List[Tuple[int, int]]:
        """Return list of dx,dy pairs that keep agent in bounds & off walls."""
        x, y = state
        actions = []
        for dx, dy in self.ACTIONS.values():
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.width and 0 <= ny < self.height and (nx, ny) not in self.walls:
                actions.append((dx, dy))
        return actions 