from typing import List, Any
"""
Program to count the number of occurences of an item in a list
"""

def count_occurrences(lst: List[Any], item: Any) -> int:
    count = 0
    for i in lst:
        if i == item:
            count += 1
    return count
