"""
An implementation of a Min Binary Heap.

Contributors: Simon Chen.
"""
from __future__ import annotations
from typing import Optional
from random import randint


class MinBinaryHeap:
    """ A min heap binary tree. All values in tree satisfy min heap property.
    """
    value: int
    left: Optional[MinBinaryHeap]
    right: Optional[MinBinaryHeap]

    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None

    def __str__(self) -> str:
        """ Return as if it were a regular Python built-in list.
        """
        string_so_far = '['
        if self.left is not None:  # Recurse left
            string_so_far += self.left.__str__()[1:-1] + ', '
        string_so_far += str(self.value)
        if self.right is not None:  # Recurse right
            string_so_far += ', ' + self.right.__str__()[1:-1]
        string_so_far += ']'
        return string_so_far

    def __contains__(self, item: int) -> bool:
        """ Return whether item is in the BST
        """
        if item == self.value:  # Base case
            return True
        elif item > self.value:  # Search below
            return item in self.left or item in self.right
        else:
            return False  # By Min Heap property

    def add(self, value: int) -> None:
        """ Add the value to the heap. Must satisfy heap property.
        """
        new_tree = MinBinaryHeap(value)

        if randint(0, 1) == 0:  # Random between left and right for tree balance.
            if self.left is not None:
                self.left.add(value)
            else:
                self.left = MinBinaryHeap(value)
                self._shift_up()  # TODO: finish this later

        else:  # Go right.
            if self.right is not None:
                self.right.add(value)
            else:
                self.right = MinBinaryHeap(value)

    def _shift_up(self, parents: list[MinBinaryHeap], leaf: MinBinaryHeap) -> None:

