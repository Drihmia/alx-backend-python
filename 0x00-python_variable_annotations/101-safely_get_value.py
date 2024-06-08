#!/usr/bin/env python3
"""task 11"""
from typing import TypeVar, Mapping, Any, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None]) -> Union[Any, T]:
    """safely_get_value"""
    if key in dct:
        return dct[key]
    else:
        return default
