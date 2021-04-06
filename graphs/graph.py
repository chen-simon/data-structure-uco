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
    """ A graph.
    """
    _vertices: set[_Vertex]
    _size: int

    def __init__(self):
        self._vertices = set()
        self._size = 0
        
    def __len__(self) -> int:
        return self._size
