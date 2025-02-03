from typing import List, Union
"""
Program contains two functions for determining if a list contains an item.
Constraints: This program assusmes the list only contains Integers and floating point numbers
"""

def contains_item(lst: List[Union[int, float]], item: Union[int, float]) -> bool:
    if not lst: return False
    elif lst[0] == item: return True
    else: return contains_item(lst[1:], item)


def contains_item_sorted(lst: List[Union[int, float]], item: Union[int, float]) -> bool:
    if not lst: return False
    elif lst[0] == item: return True
    elif lst[0] > item: return False
    else: return contains_item_sorted(lst[1:], item)
