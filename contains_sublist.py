from typing import List, Any
"""
program to check if a list contains a sublist
"""

def contains_sublist(lst: List[Any], sublist: List[Any]) -> bool:
    for i in range(len(lst) - len(sublist) + 1):
        if lst[i:i+len(sublist)] == sublist:
            return True
    return False
