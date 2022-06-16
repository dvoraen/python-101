from typing import Any
from collections import namedtuple
from dataclasses import dataclass


class MetaTest(type):
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls, *args, **kwargs)

        setattr(instance, "test", True)
        return instance

    def __setattr__(self, __name: str, __value: Any) -> None:
        return super().__setattr__(__name, __value)


class TestClass(metaclass=MetaTest):
    def __init__(self):
        setattr(self, "hello", "world")
        self.test2 = False


@dataclass
class DataClass:
    a: int = 5
    b: bool = True


TestTuple = namedtuple("TestT", ["good", "bye"])

tt = TestTuple(good="hi", bye="there")
# tt.good and tt.bye both appear in auto complete

test = TestClass()
print(test.test)  # setattr in MetaTest.__new__ not seen
print(test.hello)  # setattr in TestClass.__init__ not seen
print(test.test2)

dc = DataClass()
print(dc)
# dc.a and dc.b both appear


from typing import TypeVar, Sized

ST = TypeVar('ST', bound=Sized)

def longer(x: ST, y: ST) -> ST:
    if len(x) > len(y):
        return x
    else:
        return y

l1 = longer([1], [1, 2])  # ok, return type List[int]
l2 = longer({1}, {1, 2})  # ok, return type Set[int]
l3 = longer([1], {1, 2})  # ok, return type Collection[int]