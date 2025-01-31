from typing import List

def reverse_list(lst: List[Any]) -> Union[List[Any], None]:
    return lst[::-1] if lst else None
