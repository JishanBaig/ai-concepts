from abc import abstractmethod, ABC
from collections import deque

from search_space import Node


class SearchStrategy(ABC):
    @abstractmethod
    def search(self, space):
        pass


class Frontier(ABC):
    @abstractmethod
    def add(self, node):
        pass

    @abstractmethod
    def contains_state(self, state):
        pass

    @abstractmethod
    def empty(self):
        pass

    @abstractmethod
    def remove(self):
        pass


class DFS(SearchStrategy):
    """
    """

    def search(self, space):
        # Initialize the frontier with the start state
        start = Node(state=space.get_start(), parent=None, action=None)
        frontier = StackFrontier()
        frontier.add(start)

        # Initialize an empty explored set
        explored = set()

        while frontier:
            # Pop the last node from the frontier (stack)
            node = frontier.remove()

            # Check if this node is the goal
            if space.is_goal(node.state):
                # If it is, reconstruct the path and return it
                actions = []
                cells = []
                while node.parent is not None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                actions.reverse()
                cells.reverse()
                # solution found
                return actions, cells

            # Mark the node as explored
            explored.add(node.state)

            # Add neighbors to the frontier if they are not already in the frontier or explored
            for action, state in space.get_neighbors(node.state):
                if not frontier.contains_state(state) and state not in explored:
                    child = Node(state=state, parent=node, action=action)
                    frontier.add(child)

        # If no solution was found, return None
        return None


class StackFrontier(Frontier):
    """
    """

    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            return self.frontier.pop()


class BFS(SearchStrategy):
    """
    """

    def search(self, space):
        # Initialize the frontier with the start state
        start = Node(state=space.get_start(), parent=None, action=None)
        frontier = QueueFrontier()
        frontier.add(start)

        # Initialize an empty explored set
        explored = set()

        while frontier:
            # Pop the last node from the frontier (queue)
            node = frontier.remove()

            # Check if this node is the goal
            if space.is_goal(node.state):
                # If it is, reconstruct the path and return it
                actions = []
                cells = []
                while node.parent is not None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                actions.reverse()
                cells.reverse()
                # solution found
                return actions, cells

            # Mark the node as explored
            explored.add(node.state)

            # Add neighbors to the frontier if they are not already in the frontier or explored
            for action, state in space.get_neighbors(node.state):
                if not frontier.contains_state(state) and state not in explored:
                    child = Node(state=state, parent=node, action=action)
                    frontier.add(child)

        # If no solution was found, return None
        return None


class QueueFrontier(Frontier):
    """
    """
    def __init__(self):
        self.frontier = deque()

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            return self.frontier.popleft()
