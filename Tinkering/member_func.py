from typing import Any, Callable


class TestObject:
    def func_a(self):
        print("A")

    def func_b(self):
        print("B")

    def func_c(self):
        print("C")


def caller(func: Callable[..., Any]):
    print("Calling function")
    func()


obj = TestObject()

caller(obj.func_a)
