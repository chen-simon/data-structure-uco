from __future__ import annotations
from typing import Any, Optional


class BST:
    """ An integer binary search tree. Values in tree are always sorted.
    """
    value: int
    left: Optional[BST]
    right: Optional[BST]

    def __init__(self, value: Any) -> None:
        self.value = value
        self.left = None
        self.right = None

    def __str__(self) -> str:
        """ Return as if it were a regular Python built-in list.
        """
        string_so_far = '['
        if self.left is not None:  # Recurse left
            string_so_far += self.left.__str__().strip('[').strip(']') + ', '
        string_so_far += str(self.value)
        if self.right is not None:  # Recurse right
            string_so_far += ', ' + self.right.__str__().strip('[').strip(']')
        string_so_far += ']'
        return string_so_far

    def __contains__(self, item) -> bool:
        """ Return whether item is in the BST
        """
        if item == self.value:  # Base case
            return True
        elif item < self.value:  # Search left
            if self.left is not None:
                return item in self.left
        else:  # Search right
            if self.right is not None:
                return item in self.right

    def add(self, value: int) -> None:
        """ Add the value to this BST.
        """
        if value < self.value:  # Add left
            if self.left is not None:
                self.left.add(value)
            else:
                self.left = BST(value)
        else:  # Add right
            if self.right is not None:
                self.right.add(value)
            else:
                self.right = BST(value)

