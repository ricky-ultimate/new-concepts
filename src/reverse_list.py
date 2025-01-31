from typing import List
"""
program to reverse the elements of a list
"""

def reverse_list(lst: List[Any]) -> Union[List[Any], None]:
    return lst[::-1] if lst else None
