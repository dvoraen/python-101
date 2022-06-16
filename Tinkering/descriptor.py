from typing import Any, TypeVar

_T = TypeVar("_T")


class Descriptor(object):
    def __set_name__(self, owner: object, name: str):
        self.name = name

    # Cannot use setattr/getattr here, as a rule.  It will recurse infinitely
    # because it's basically calling __get__/__set__ from within getattr/setattr
    def __get__(self, obj: object, objtype: type[object] | None = None):
        value = obj.__dict__.get(self.name)
        return value

    def __set__(self, obj: object, value: Any):
        obj.__dict__[self.name] = value


class TestClass:

    hello = Descriptor()

    def __init__(self, value: str):
        self.hello = value


if __name__ == "__main__":
    test = TestClass("Hi!")
    print(test.hello)
