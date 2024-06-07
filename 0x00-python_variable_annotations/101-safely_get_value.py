#!/usr/bin/env python3
"""task 11"""
from typing import TypeVar, Mapping, Any, Dict


T = TypeVar('T')
# Key = int | float | str | bool | Tuple[int, int]


def safely_get_value(dct: Dict[Any, Any],
                     key: Any,
                     default: T | None = None) -> T | Any:
    """safely_get_value"""
    if key in dct:
        return dct[key]
    else:
        return default
