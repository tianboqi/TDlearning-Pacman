# Grid and display settings
GRID_W, GRID_H = 8, 8            # grid size
TILE = 60                        # pixels per tile

# Learning parameters
ALPHA = 0.10                     # TD learning-rate
GAMMA = 0.90                     # discount
EPSILON = 0.2                    # exploration rate for epsilon-greedy policy

# Value bounds for visualization
V_MIN = 1e-4                     # smallest value we consider "non-zero"
V_MAX = 1.0                      # expected upper bound of V

# Game settings
START = (0, 7)                   # Pac-Man spawn
GOAL = (7, 0)                    # reward tile
WALLS = {(7, 1),(7, 2),(7, 2),(7, 3),(7, 4),(7, 5),(7, 6), (7, 7),
         (0, 5),(1, 5),(2, 5),(3, 5),(4, 5),
         (4, 0),(4, 1),(4, 2),
         (0, 2),(1, 2)}          # impassable cells 