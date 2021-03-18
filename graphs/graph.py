"""
An implementation of a Graph.

Contributors: Simon Chen.
"""
from __future__ import annotations
from typing import Any


class _Node:
    """ A node in a graph.
    """
    neighbours: set[_Node]
    value: Any


class Graph:
    """ A graph.
    """
    _nodes: set[_Node]
    _size: int

    def __init__(self):
        self._nodes = set()
        self._size = 0
