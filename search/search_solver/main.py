# This is a sample Python script.
from search_space import MazeSearchSpace
from strategies import DFS, BFS
from visualizer import Visualizer


def solveByDfs(datafile):
    space = MazeSearchSpace(datafile)
    strategy = DFS()
    solution = strategy.search(space)
    Visualizer.visualize(space, solution)


def solveByBfs(datafile):
    space = MazeSearchSpace(datafile)
    strategy = BFS()
    solution = strategy.search(space)
    Visualizer.visualize(space, solution)


def solve(datafile):
    solveByDfs(datafile)
    solveByBfs(datafile)


def main():
    solve("Data/maze.txt");
    solve("Data/maze1.txt");
    solve("Data/maze2.txt");
    solve("Data/maze3.txt");


if __name__ == "__main__":
    main()
