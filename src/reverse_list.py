from typing import List, Any, Optional
"""
program to reverse the elements of a list
"""

def reverse_list(lst: List[Any]) -> Optional[List[Any]]:
    return lst[::-1] if lst else None
