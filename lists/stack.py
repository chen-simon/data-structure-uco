from __future__ import annotations
from typing import Any
from singly_linked_list import SinglyLinkedList


class Stack:
    """ A stack.
    """
    _values: SinglyLinkedList  # The front of _values is the top of the stack
    _size: int  # To remove reliance on len(_values)

    def __init__(self):
        self._values = SinglyLinkedList()
        self._size = 0

    def is_empty(self) -> bool:
        """ Return whether stack is empty
        """
        return self._size == 0

    def push(self, item: Any) -> None:
        """ Push item to stack.
        """
        self._values.insert(item, 0)
        self._size += 1

    def pop(self) -> Any:
        """ Pop item off stack. Raise ValueError if stack is empty.
        """
        if not self.is_empty():
            self._size -= 1
            return self._values.remove_at_index(0)
        else:
            raise ValueError
