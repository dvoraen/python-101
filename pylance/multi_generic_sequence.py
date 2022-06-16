# mgs = Multi-Generic Sequence

from typing import Any, Protocol, TypeVar, Sequence

Number = int | float | complex

T = TypeVar("T", int, float, complex)


class SupportsMul(Protocol[T]):
    def __mul__(self, __x: T) -> T:
        ...


def proto(obj: SupportsMul[Any]):
    print(obj * 2)


def func(l: Sequence[Number | None]) -> None:
    print(l)


def func_double(l: Sequence[Number | None]):
    print([n * 2 for n in l if n is not None])


if __name__ == "__main__":
    from typing_extensions import reveal_type

    test_list: list[Number | None]
    test_list = [2, None, 3, None]
    reveal_type(test_list)

    proto(3)
    proto(4.6)
    func(test_list)
    func_double(test_list)
