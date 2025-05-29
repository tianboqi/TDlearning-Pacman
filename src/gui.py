import pygame
import sys
import math
from typing import Tuple
from .environment import GridWorld
from .agent import TDAgent
from .config import TILE, V_MIN, V_MAX

def lerp_color(v: float) -> pygame.Color:
    """
    Fixed log-scale colour map:
       low V  → blue,   mid → yellow,   high → red.
    """
    v_clipped = max(V_MIN, min(V_MAX, v))
    t = math.log(v_clipped / V_MIN) / math.log(V_MAX / V_MIN)  # 0-->1

    if t <= 0.5:                  # blue  → yellow
        f = t / 0.5               # 0-->1
        r = int(255 * f)
        g = int(255 * f)
        b = int(255 * (1 - f))
    else:                         # yellow → red
        f = (t - 0.5) / 0.5
        r = 255
        g = int(255 * (1 - f))
        b = 0
    return pygame.Color(r, g, b)

def draw_pacman(surface, pos, radius, direction):
    """
    Draw Pac-Man as a yellow sector (wedge) facing the given direction.
    
    Args:
        surface   : Pygame surface
        pos       : (x, y) center position
        radius    : Radius of Pac-Man
        direction : (dx, dy) movement direction (will default to (1,0) if zero)
    """
    x, y = pos
    mouth_angle = math.pi * 7 / 8  # 45° opening
    segments = 30              # smoothness of arc

    # default direction (right) if agent is stationary
    dx, dy = direction
    if dx == 0 and dy == 0:
        dx, dy = (1, 0)

    angle_center = math.atan2(dy, -dx)  # invert x for screen coords
    angle1 = angle_center - mouth_angle
    angle2 = angle_center + mouth_angle

    points = [pos]  # center of the wedge

    # arc points along the sector edge
    for i in range(segments + 1):
        t = angle1 + i * (angle2 - angle1) / segments
        px = x + radius * math.cos(t)
        py = y - radius * math.sin(t)  # y is flipped in Pygame
        points.append((px, py))

    pygame.draw.polygon(surface, (255, 255, 0), points)


class PacmanGUI:
    def __init__(self, env: GridWorld, agent: TDAgent):
        pygame.init()
        self.screen = pygame.display.set_mode((env.width * TILE, env.height * TILE))
        pygame.display.set_caption("Pac-Man TD Learning")
        self.clock = pygame.time.Clock()
        self.env = env
        self.agent = agent

    def run(self):
        state = self.env.reset()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

                    # map arrow key to action
                    action = None
                    if event.key == pygame.K_UP:
                        action = (0, -1)
                    elif event.key == pygame.K_DOWN:
                        action = (0, 1)
                    elif event.key == pygame.K_LEFT:
                        action = (-1, 0)
                    elif event.key == pygame.K_RIGHT:
                        action = (1, 0)

                    if action and action in self.env.legal_actions(state):
                        next_state, reward, done = self.env.step(action)
                        self.agent.update(state, reward, next_state)
                        state = next_state
                        if done:                       # reached goal
                            state = self.env.reset()   # new episode
                        self.last_direction = action  # Store for drawing

            self._draw(state)
            pygame.display.flip()
            self.clock.tick(30)

    def _draw(self, pac_state: Tuple[int, int]):
        env = self.env
        scr = self.screen
        scr.fill((0, 0, 0))

        # Tiles
        for x in range(env.width):
            for y in range(env.height):
                rect = pygame.Rect(x * TILE, y * TILE, TILE, TILE)
                if (x, y) in env.walls:
                    pygame.draw.rect(scr, (40, 40, 40), rect)
                else:
                    pygame.draw.rect(scr, lerp_color(self.agent.V[x][y]), rect)
                pygame.draw.rect(scr, (30, 30, 30), rect, 1)

        # Goal outline
        gx, gy = env.goal
        goal_rect = pygame.Rect(gx * TILE, gy * TILE, TILE, TILE)
        pygame.draw.rect(scr, (255, 215, 0), goal_rect, 3)
        center = (gx * TILE + TILE // 2, gy * TILE + TILE // 2)
        pygame.draw.circle(scr, (255, 255, 0), center, TILE // 6) 

        # Pac-Man
        px, py = pac_state
        center = (px * TILE + TILE // 2, py * TILE + TILE // 2)
        # pygame.draw.circle(scr, (0, 255, 0), center, TILE // 2 - 4) 
                # determine direction (defaults to right if unknown)
        if hasattr(self, 'last_direction'):
            dx, dy = self.last_direction
        else:
            dx, dy = (1, 0)
        draw_pacman(scr, center, TILE // 2 - 4, (dx, dy))
