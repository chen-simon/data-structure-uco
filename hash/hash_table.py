"""
An implementation of a HashTable.

Contributors: Simon Chen, and Salman Husainie.
"""
from __future__ import annotations
from typing import Any
from lists.singly_linked_list import SinglyLinkedList


class HashTable:
    """ A Hash Table that is implemented using linked-list chaining.
        Assume all keys are Strings.
    """
    _buckets: list[SinglyLinkedList]  # This implementation will used linked-list chaining.
    _size: int  # Size of Hash Table.

    def __init__(self, buckets: int) -> None:
        if buckets < 1:
            raise ValueError('Cannot have less than 1 buckets')

        self._buckets = [SinglyLinkedList() for bucket in range(0, buckets)]
        self._size = 0

    def __str__(self) -> str:
        """ Return string representation of a list of linked lists.
        """
        string_so_far = '['
        for bucket in self._buckets:
            string_so_far += bucket.__str__() + ', '
        return string_so_far[:-2] + ']'

    def __len__(self) -> int:
        """ Return the size of the hash table.
        """
        return self._size

    def __contains__(self, key: Any) -> bool:
        """ Return whether item is in the hash table.
        """
        hash_code = self._get_hash_code(key)
        for item in self._buckets[hash_code]:
            if item[0] == key:
                return True
        return False

    def _get_hash_code(self, key: str) -> int:
        """ Returns a hash code of the string.
        """
        hash_code = 0
        for char in key:
            hash_code = (ord(char) + hash_code) % len(self._buckets)
        return hash_code

    def add(self, key: str, item: Any) -> None:
        """ Adds the key-item pair to the hash table.
        """
        hash_code = self._get_hash_code(key)
        key_value_pair = (key, item)
        self._buckets[hash_code].append(key_value_pair)
        self._size += 1
