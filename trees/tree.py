"""
An implementation of a Tree.

Contributors: Salman Husainie.
"""
from __future__ import annotations
from typing import Any, List, Optional


class Tree:
    """A tree data structure.
    """
    _root: Optional[Any]
    _subtrees: List[Tree]

    def __init__(self, root: Optional[Any], subtrees: List[Tree]) -> None:
        """Initialize a new Tree with the appropriate root and subtrees.
        """
        self._root = root
        self._subtrees = subtrees

    def is_empty(self) -> bool:
        """Return whether this Tree is empty.
        """
        return self._root is None

    def __len__(self) -> int:
        """Return the number of items contained in this Tree.
        """
        # TODO: Write this method

    def __str__(self) -> str:
        """Return a string representation of this Tree."""
        return self._str_indented_preorder(0)

    def _str_indented_preorder(self, depth: int = 0) -> str:
        """Return an indented, pre-order string representation of this Tree.
        """
        # TODO: Write this method

