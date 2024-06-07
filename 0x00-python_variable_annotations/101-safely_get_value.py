#!/usr/bin/env python3
"""task 11"""
from typing import TypeVar, Mapping, Any, Union


T = TypeVar('T')
NoneType = TypeVar('NoneType', bound=None)
# Key = int | float | str | bool | Tuple[int, int]


def safely_get_value(dct: Mapping[Any, Any],
                     key: Any,
                     default: Union[T, NoneType]) -> Union[Any, T]:
    """safely_get_value"""
    if key in dct:
        return dct[key]
    else:
        return default
