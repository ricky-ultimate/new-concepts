from typing import List, Any, Optional
"""
Function goal: to remove an element from a list and return the list without the element.
"""

def remove_element(lst: List[Any], item: Any) -> Optional[List[Any]]:
    if not lst: return None
    for i in range(len(lst)):
        if item == lst[i]:
            return lst[0:i] + lst[i+1:]
    return lst
