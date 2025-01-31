from typing import List, Union
"""
Program to find the maximum value in a hybrid list on numbers
"""

def find_max(nums: List[Union[int, float]]) -> Union[int, float, None]:
    if nums:
        maximum = nums[0]
        for i in nums[1:]:
            if i > maximum:
                maximum = i
        return maximum
    return None
