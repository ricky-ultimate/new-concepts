from typing import List, Union

def find_max(nums: List[Union[int, float]]) -> Union[int, float, None]:
    if nums:
        maximum = nums[0]
        for i in nums[1:]:
            if i > maximum:
                maximum = i
        return maximum
    return None
