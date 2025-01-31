from typing import Union, Any, Sequence
"""
program to safely return the first element of a list, if it exists
"""

def first_element(list: Sequence[Any]) -> Union[Any, None]:
    if list:
        return list[0]
    else:
        return None


if __name__ == "__main__":
    print(first_element([90,89,90]))
