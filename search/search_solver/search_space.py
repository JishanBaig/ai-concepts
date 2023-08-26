from abc import ABC, abstractmethod


class SearchSpace(ABC):
    @abstractmethod
    def get_start(self):
        pass

    @abstractmethod
    def get_goal(self):
        pass

    @abstractmethod
    def is_goal(self, state):
        pass

    @abstractmethod
    def get_neighbors(self, state):
        pass


class Node:
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


class MazeSearchSpace(SearchSpace):
    """
    Implements SearchSpace and methods
    def get_start(self):
    def get_goal(self):
    def is_goal(self, state):
    def get_neighbors(self, state):
    """
    def __init__(self, filename):
        """
        fetch data and store in MazeSearchSpace class variables
        Args:
            filename: file to be read in order to feed data and store in MazeSearchSpace class
        """
        # Read file and set height and width of maze
        with open(filename) as f:
            contents = f.read()

        # Validate start and goal
        if contents.count("A") != 1:
            raise Exception("maze must have exactly one start point")
        if contents.count("B") != 1:
            raise Exception("maze must have exactly one goal")

        # Determine height and width of maze
        contents = contents.splitlines()
        self.height = len(contents)
        self.width = max(len(line) for line in contents)

        # Keep track of walls, to get the valid set of neighbours.
        self.walls = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                try:
                    if contents[i][j] == "A":
                        self.start = (i, j)
                        row.append(False)
                    elif contents[i][j] == "B":
                        self.goal = (i, j)
                        row.append(False)
                    elif contents[i][j] == " ":
                        row.append(False)
                    else:
                        row.append(True)
                except IndexError:
                    row.append(False)
            self.walls.append(row)

    def get_start(self):
        return self.start

    def get_goal(self):
        return self.goal

    def is_goal(self, state):
        return state == self.goal

    def get_neighbors(self, state):
        """

        Args:
            state:

        Returns:

        """
        row, col = state
        candidates = [
            ("up", (row - 1, col)),
            ("down", (row + 1, col)),
            ("left", (row, col - 1)),
            ("right", (row, col + 1))
        ]

        result = []
        for action, (r, c) in candidates:
            if 0 <= r < self.height and 0 <= c < self.width and not self.walls[r][c]:
                result.append((action, (r, c)))
        return result
