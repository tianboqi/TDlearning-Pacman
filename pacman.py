import argparse
from src import GridWorld, TDAgent, PacmanGUI, simulate

def main():
    parser = argparse.ArgumentParser(description="Simple Pac-Man with TD(0) learning.")
    parser.add_argument("--simulate", "-s", type=int, default=0,
                        help="pre-train with N episodes before the GUI starts")
    parser.add_argument("--policy", "-p", type=str, default="random",
                        choices=["random", "epsilon-greedy"],
                        help="policy to use for simulation (random or epsilon-greedy, default: random)")
    args = parser.parse_args()

    env = GridWorld()
    agent = TDAgent(env)

    # optional pre-training
    if args.simulate > 0:
        print(f"Running {args.simulate} simulation episodes with {args.policy} policy...", flush=True)
        simulate(env, agent, args.simulate, args.policy)
        print("...done. Launching GUI.", flush=True)

    # launch interactive GUI
    PacmanGUI(env, agent).run()

if __name__ == "__main__":
    main()