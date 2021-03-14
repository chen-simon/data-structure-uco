from __future__ import annotations
from typing import Any, Optional


class _Node:
    """ A node in a singly linked list.
    """
    item: Any
    next: Optional[_Node]

    def __init__(self, item: Any, next: Optional[_Node] = None) -> None:
        self.item = item
        self.next = next


class SinglyLinkedList:
    """ A singly linked list.
    """
    _first: Optional[_Node]
    _size: int  # To prevent worst case Theta(n) size calls

    def __init__(self, lst: Optional[list[Any]] = None) -> None:
        if lst is None or lst == []:  # If lst is empty
            self._size = 0
            self._first = None
        else:
            self._size = 1
            self._first = _Node(lst[0])

            curr = self._first
            for i in range(1, len(lst)):
                new_node = _Node(lst[i])
                curr.next = new_node
                self._size += 1
                curr = new_node
        return

    def __str__(self) -> str:
        """ Return as if it were a regular Python built-in list.
        """
        string_so_far = '['
        curr = self._first

        while curr is not None:
            string_so_far += str(curr.item)
            if curr.next is not None:
                string_so_far += ', '
            curr = curr.next

        string_so_far += ']'
        return string_so_far
