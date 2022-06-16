from typing import Generic, Callable, TypeVar, Any
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

    def __get__(
        self: Self, obj: object | None, objtype: type[object] | None = None
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
        return self.func(obj) if obj else self


class EmptyTest(object):
    name = "Empty"


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
    if test_lzp is not lzp:
        print(test_lzp.name)  # I'm unsure how to resolve this type error.

    test_prop = test.prop
    print(test_lazy)
    print(test_lzp)
    print(test_prop)
