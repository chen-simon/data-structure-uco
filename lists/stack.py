from __future__ import annotations
from typing import Any


class Stack:
    """ A stack.
    """
    _values: list  # The back of _values is the top of the stack
    _size: int  # To remove reliance on len(_values)

    def __init__(self):
        self._values = []
        self._size = 0

    def is_empty(self) -> bool:
        """ Return whether stack is empty
        """
        return self._size == 0

    def push(self, item: Any) -> None:
        """ Push item to stack.
        """
        self._values.append(item)
        self._size += 1

    def pop(self) -> Any:
        """ Pop item off stack. Raise ValueError if stack is empty.
        """
        if not self.is_empty():
            self._size -= 1
            return self._values.pop()
        else:
            raise ValueError
