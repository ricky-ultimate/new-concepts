from typing import List, Union
"""
Program to sum a list of integers and floats
"""
def sum_list(list: List[Union[int,float]]) -> float:
    sum: float = 0
    for number in list:
        sum += number
    return sum
