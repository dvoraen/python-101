from typing import Any, Callable, Generic, Optional, TypeVar, overload

from typing_extensions import Self

T = TypeVar("T")
U = TypeVar("U", bound=object)

missing = object()


# The solution to the property issue is that lazy_property has to be generic.
# That means inheriting from Generic[T] and ensuring that __get__ returns the
# right type(s).
class lazy_property(Generic[T]):
    """Hello, this is me testing out typing hints on lazy_property"""

    def __init__(self, func: Callable[..., T]) -> None:
        self.__name__ = func.__name__
        self.func = func

    # See notes in descriptor.py about why None has to be first.
    @overload
    def __get__(self: Self, obj: None, objtype: Optional[type[object]] = ...) -> Self:
        ...

    @overload
    def __get__(self: Self, obj: object, objtype: Optional[type[object]] = ...) -> T:
        ...

    def __get__(
        self: Self, obj: object | None, objtype: Optional[type[object]] = None
    ) -> Self | T:
        if obj is None:
            return self
        value = obj.__dict__.get(self.__name__, missing)
        if value is missing:
            value = self.func(obj)
            obj.__dict__[self.__name__] = value
        return value


class lzp(Generic[T]):
    def __init__(self, func: Callable[..., T]) -> None:
        self.func = func

    def __get__(self: Self, obj: Any, objtype: type[object] | None = None) -> Self | T:
        val = self.func(obj) if obj else self
        return val


class EmptyTest(object):
    name = "I'm EmptyTest!"


class Test:
    @lazy_property
    def lazy(self) -> EmptyTest:
        return EmptyTest()

    @lzp
    def lzp(self) -> EmptyTest:
        return EmptyTest()

    @property
    def prop(self) -> EmptyTest:
        return EmptyTest()


if __name__ == "__main__":
    test = Test()
    test_lazy = test.lazy
    test_lzp = test.lzp

    # Since the overload for __get__ is there, it type checks to being
    # EmptyTest, so you can use .name directly without error here.
    # Compare the Pylance results for test_lazy and test_lzp.
    # The former is EmptyTest, the latter is the union returned by __get__.
    print("test_lazy", test_lazy.name)

    # Use of isinstance here apparently narrows the type of test_lzp to
    # EmptyTest, which is what makes the Unknown type for .name go away.
    if isinstance(test_lzp, EmptyTest):
        print("test_lzp", test_lzp.name)

    test_prop = test.prop

    print(test_lazy)
    print(test_lzp)
    print(test_prop)
