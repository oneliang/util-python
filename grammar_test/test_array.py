# -*- coding: utf-8 -*-
from typing import (
    Any
)


class Array(list):
    def __init__(self, array: list):
        super().__init__()
        self.array = array

    def __getitem__(self, item) -> Any:
        if isinstance(item, int):
            return self.array[item]
        if isinstance(item, tuple):
            value = self.array
            for tuple_index in range(0, len(item)):
                value = value[item[tuple_index]]
            return value
        return None

    def __str__(self) -> str:
        return self.array.__str__()


my_array = Array([[1, 2], [3, 4], [5, 6]])
print(my_array[1, 1])
