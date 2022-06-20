from typing import Generic, TypeVar, overload

from typing_extensions import Self

_T = TypeVar("_T")


class Descriptor(Generic[_T]):
    myname: str = "Descriptor!"

    def __set_name__(self: Self, owner: type[object], name: str):
        self.name = name
        print(f"__set_name__ ({self.name}): {owner}")

    # VERY IMPORTANT.  None is a subtype of object(), so if the obj: object
    # function is listed first, the type checker will declare it the correct
    # overload.
    @overload
    def __get__(self: Self, obj: None, owner: type[object]) -> Self:
        ...

    @overload
    def __get__(self: Self, obj: object, owner: type[object]) -> _T:
        ...

    # Cannot use setattr/getattr here, as a rule.  It will recurse infinitely
    # because it's basically calling __get__/__set__ from within getattr/setattr
    def __get__(self: Self, obj: object | None, owner: type[object]) -> Self | _T:
        print(f"__get__ ({self.name}):", dict(obj=obj, owner=owner))
        if obj is None:
            return self
        value = obj.__dict__.get(self.name)
        return value

    def __set__(self, obj: object, value: _T):
        obj.__dict__[self.name] = value


class TestClass:
    # For hello to type check correctly, it has to be typed
    # as what you assign to it.
    hello = Descriptor[str]()
    desc = Descriptor[str]()

    def __init__(self, value: str):
        self.hello = value


if __name__ == "__main__":
    print("Start.")

    test = TestClass("Hi!")

    print("After test.__init__()")

    h1 = test.hello
    h2 = TestClass.desc
    test = TestClass.desc.myname

    print(h1)
    print(h2)
