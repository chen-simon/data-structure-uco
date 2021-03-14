from __future__ import annotations
from typing import Any, Tuple, Optional
from singly_linked_list import SinglyLinkedList


class PriorityQueue:
    """ A priority queue. Priority is an integer. Queue is always sorted.
    """
    _values: SinglyLinkedList[Tuple[Any, int]]  # The start of _values is the front of the queue
    _size: int  # To remove reliance on len(_values)

    def __init__(self):
        self._values = []
        self._size = 0

    def is_empty(self) -> bool:
        """ Return whether stack is empty
        """
        return self._size == 0

    def enqueue(self, item: Any, priority: Optional[int] = 0) -> None:
        """ Push item to stack.
        """
        list_item = (item, priority)
        self._values.insert(0, list_item)
        self._size += 1

    def dequeue(self) -> Any:
        """ Pop item off stack. Raise ValueError if queue is empty.
        """
        if not self.is_empty():
            self._size -= 1
            return self._values.pop()
        else:
            raise ValueError
