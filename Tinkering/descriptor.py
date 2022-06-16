from typing import Any, TypeVar

_T = TypeVar("_T")


class Descriptor(object):
    def __set_name__(self, owner: object, name: str):
        self.pub_name = name
        self.priv_name = "_" + self.pub_name

    def __get__(self, obj: object, objtype: type[object] | None = None):
        value = getattr(obj, self.priv_name)
        return value

    def __set__(self, obj: object, value: Any):
        setattr(obj, self.priv_name, value)


class TestClass:

    hello = Descriptor()

    def __init__(self, value: str):
        self.hello = value


if __name__ == "__main__":
    test = TestClass("Hi!")
    print(test.hello)
