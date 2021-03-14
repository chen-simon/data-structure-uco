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

    def __len__(self) -> int:
        """ Returns size of linked list.
        """
        return self._size

    def __str__(self) -> str:
        """ Return as if it were a regular Python built-in list.
        """
        string_so_far = '['
        curr = self._first

        while curr is not None:
            string_so_far += curr.item.__str__()
            if curr.next is not None:
                string_so_far += ', '
            curr = curr.next

        string_so_far += ']'
        return string_so_far

    def __contains__(self, item: Any) -> bool:
        """ Return whether item is in the linked list.
        """
        curr = self._first

        while curr is not None:
            if curr.item == item:  # Early return pattern.
                return True
            curr = curr.next
        return False

    def append(self, item: Any) -> None:
        """ Append item to back of the linked list.
        """
        curr = self._first

        while curr.next is not None:  # Iterates until last element
            curr = curr.next
        curr.next = _Node(item)  # Sets the .next value of that element to a new node with item.
        self._size += 1

    def remove(self, item: Any) -> None:
        """ Remove the item from the linked list. Raise ValueError if not in linked list.
        """
        # TODO: Implement this method.

    def remove_at_index(self, i: int) -> None:
        """ Remove the item at index i from the linked list. Raise ValueError if not in linked list.
        """
        # TODO: Implement this method.

    def index(self, i: int) -> Any:
        """ Return the value at index i. Raise ValueError if not in linked list.
        """
        # TODO: Implement this method.

