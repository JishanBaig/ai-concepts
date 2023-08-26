# This is a sample Python script.
from search_space import MazeSearchSpace
from strategies import DFS, BFS
from visualizer import Visualizer


def main():
    space = MazeSearchSpace("maze.txt")
    strategy = DFS()
    solution = strategy.search(space)
    Visualizer.visualize(space, solution)

    strategy = BFS()
    solution = strategy.search(space)
    Visualizer.visualize(space, solution)


if __name__ == "__main__":
    main()
