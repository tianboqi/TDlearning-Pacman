# Pac-Man demo for TD Learning

A minimalist grid-world Pac-Man implementation using TD learning in Python with `pygame`.  
This game was written as a demo to show **neuroscientists** how reward prediction error (RPE) is used to update value.

**Features**:
- Keyboard-controlled Pac-Man
- State value function visualization (color-coded)
- TD(0) learning updates on every step
- Optional random-policy and epsilon-greedy simulation for auto-learning

<p align="center">
  <img src="https://github.com/tianboqi/TDlearning-Pacman/blob/main/img/demo.png" width="500">
</p>

## Usage

To launch a game, use
```
python pacman.py
```

To show simulated value function, use
```
python pacman.py --simulate <number of simulation> --policy <policy>
```
where the `<policy>` can be `random` or `epsilon-greedy`.

Configurations (grid configurations, learning configurations) can be changed in `src/config.py`.

**Requirements**: `pygame`
