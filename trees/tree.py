"""
An implementation of a Tree w/doctests.

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

        >>> t1 = Tree(None, [])
        >>> t1.is_empty()
        True
        >>> t2 = Tree(1, [Tree(2, []), Tree(3, [])])
        >>> t2.is_empty()
        False
        """
        return self._root is None

    def __len__(self) -> int:
        """Return the number of items contained in this Tree.

        >>> t1 = Tree(None, [])
        >>> len(t1)
        0
        >>> t2 = Tree(1, [Tree(2, []), Tree(3, [])])
        >>> len(t2)
        3
        """
        if self.is_empty():
            return 0
        else:
            return 1 + sum(subtree.__len__() for subtree in self._subtrees)

    def __str__(self) -> str:
        """Return a string representation of this Tree.
        """
        return self._str_indented_preorder(0)

    def _str_indented_preorder(self, depth: int = 0) -> str:
        """Return an indented, pre-order string representation of this Tree.
        """
        if self.is_empty():
            return ' '
        else:
            string_so_far = ' ' * depth + f'{self._root} \n'

            for subtree in self._subtrees:
                string_so_far += subtree._str_indented_preorder(depth + 1)

            return string_so_far


if __name__ == '__main__':
    import doctest
    doctest.testmod()
