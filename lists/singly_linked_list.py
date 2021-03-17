"""
An implementation of a SinglyLinkedList.

Contributors: Simon Chen, and Salman Husainie
"""
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

        if curr is None:
            self._first = _Node(item)

        else:
            while curr.next is not None:  # Iterates until last element
                curr = curr.next
            curr.next = _Node(item)  # Sets the .next value of that element to a new node with item.

        self._size += 1

    def insert(self, item: Any, i: int) -> None:
        """ Insert item to the given index of the linked list.
            If occupied, shift the rest to the right.
            Raise IndexError if index is negative or greater than length of list.
        """
        new_node = _Node(item)

        if i == 0:  # Insertion at start
            new_node.next, self._first = self._first, new_node
            self._size += 1
        else:
            prev, curr, curr_index = self._first, self._first.next, 1

            while curr is not None and curr_index < i:  # Iterates until ith element
                prev, curr = curr, curr.next
                curr_index += 1

            if len(self) + 1 > i:  # insert if possible
                new_node.next, prev.next = curr, new_node
                self._size += 1
            else:
                raise IndexError

    def remove(self, item: Any) -> None:
        """ Remove the item from the linked list. Raise ValueError if not in linked list.
        """
        prev, curr = None, self._first

        while not (curr is None or curr.item == item):
            prev, curr = curr, curr.next

        assert curr is None or curr.item == item

        if curr is None:
            # This means that item is not in the linked list.
            raise ValueError

        elif prev is None:
            # The case where we remove the first node.
            self._first = curr.next

        else:
            # The case where we remove a node later in the linked list.
            prev.next = curr.next

    def remove_at_index(self, i: int) -> None:
        """ Remove the item at index i from the linked list. Raise IndexError if not in linked list.
        """
        prev, curr, curr_index = None, self._first, 0

        while not (curr is None or curr_index == i):
            prev, curr, curr_index = curr, curr.next, curr_index + 1

        assert curr is None or curr_index == i

        if curr is None:
            # The case where i is out of bounds.
            raise IndexError

        elif prev is None:
            # The case where the node at index i is self._first
            self._first = curr.next

        else:
            # The case where the node at index i is later in the linked list.
            prev.next = curr.next

    def index(self, i: int) -> Any:
        """ Return the value at index i. Raise IndexError if not in linked list.
        """
        curr, curr_index = self._first, 0

        while not (curr is None or curr_index == i):
            curr, curr_index = curr.next, curr_index + 1

        assert curr is None or curr_index == i

        if curr is None:
            # The case where i is out of bounds.
            raise IndexError

        else:
            # The case where there is a node at index i.
            return curr.item

    def pop(self) -> Any:
        """ Pops the item off the back of the linked list.
        """
        prev, curr = None, self._first

        while curr.next is not None:
            prev, curr = curr, curr.next

        if prev is None:
            # curr is the first and only item in the linked list.
            item, self._first = curr.item, None

        else:
            # curr is the last node in the linked list
            item = curr.item
            prev.next = curr.next   # Essentially making prev.next = None

        return item
