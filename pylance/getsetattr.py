from dataclasses import dataclass
from typing import Any, TypeVar

_T = TypeVar("_T")


@dataclass
class TypeMeta(object):
    attribute: Any
    attr_type: _T


class TestClass(object):

    test1: str
    test2: str

    def __init__(self):
        self.test1 = "Hello"
        setattr(self, "test2", "there!")


if __name__ == "__main__":
    test = TestClass()

    print(test.test1, test.test2)
    print(test.__dict__)
    for k, v in test.__dict__.items():
        print(k, v)
