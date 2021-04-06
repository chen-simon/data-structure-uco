"""
An implementation of a Graph.

Contributors: Simon Chen.
"""
from __future__ import annotations
from typing import Any


class _Vertex:
    """ A vertex in a graph.
    """
    neighbours: set[_Vertex]
    value: Any


class Graph:
    """ A graph. All objects in the graph are unique.
    """
    _vertices: set[_Vertex]
    _size: int

    def __init__(self):
        self._vertices = set()
        self._size = 0
        
    def __len__(self) -> int:
        return self._size

    def __contains__(self, item: Any) -> bool:
        """ Return wheter item is in the graph
        """
        for vertex in self._vertices:
            if vertex == item:
                return True
        return False

    def add(self, item: Any) -> None:
        self._vertices.add(item)
