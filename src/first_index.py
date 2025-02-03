from typing import List, Any, Optional
"""
Function Goal: Return the index of the first occurrence of an element in a list. Returns None if not found.
"""

def first_index(lst: List[Any], item: Any) -> Optional[int]:
    for i, val in enumerate(lst):
        if val == item: return i
    return None
