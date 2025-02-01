from typing import List, Any
"""
Program to remove duplicates from a list
"""

def remove_duplicates(lst: List[Any]) -> List[Any]:
    present = set()
    return [x for x in lst if not (x in present or present.add(x))]
