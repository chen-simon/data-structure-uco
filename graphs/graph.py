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
        """ Return the number of vertices in the Graph
        """
        return self._size

    def __contains__(self, item: Any) -> bool:
        """ Return whether item is in the graph.
        """
        for vertex in self._vertices:
            if vertex == item:
                return True
        return False

    def __getitem__(self, item: Any) -> _Vertex:
        """ Return whether item is in the graph. Raise value error if item not in Graph.
        """
        for vertex in self._vertices:
            if vertex == item:
                return vertex
        raise ValueError

    def add(self, item: Any) -> None:
        self._vertices.add(item)
        self._size += 1

    def add_edge(self, item1: Any, item2: Any) -> None:
        """ Add an edge between two items in the graph. Raise ValueError if either one not in graph.
        item1 and item2 must be unique items.
        """
        vertex1, vertex2 = None, None
        for vertex in self._vertices:
            if vertex.value == item1:
                vertex1 = vertex
            elif vertex.value == item2:
                vertex2 = vertex
            if vertex1 and vertex2:  # Break from loop when both items are found
                break

        if vertex1 and vertex2:
            vertex1.neighbours.add(vertex2)
            vertex2.neighbours.add(vertex1)
        else:
            raise ValueError
