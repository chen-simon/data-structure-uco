"""
An implementation of a Queue.

Contributors: Simon Chen, and Salman Husainie.
"""
from __future__ import annotations
from typing import Any
from singly_linked_list import SinglyLinkedList


class Queue:
    """ A queue.
    """
    _values: SinglyLinkedList  # The start of _values is the front of the queue
    _size: int  # To remove reliance on len(_values)

    def __init__(self):
        self._values = SinglyLinkedList()
        self._size = 0

    def is_empty(self) -> bool:
        """ Return whether stack is empty
        """
        return self._size == 0

    def enqueue(self, item: Any) -> None:
        """ Enqueue item.
        """
        self._values.insert(0, item)
        self._size += 1

    def dequeue(self) -> Any:
        """ Dequeue next item in queue. Raise ValueError if queue is empty.
        """
        if not self.is_empty():
            self._size -= 1
            return self._values.pop()
        else:
            raise ValueError
