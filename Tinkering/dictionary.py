from typing import Any

dict1: dict[str, int] = {"hi": 1, "hello": 2, "how goes?": 3}
# For strict typing, indicating what's in the dict is necessary when using get()
# even if the dict is empty.
dict2: dict[Any, Any] = {}


def func(data: dict[Any, Any] | None = None):
    fdict = data or {}

    # This is what I want: the paired data.
    for value in fdict:
        print(fdict[value])


print(dict2.get("Hi", "Hello"))
