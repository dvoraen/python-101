from operator import contains
from typing import Any, ClassVar, Collection, NamedTuple, TypeVar


class Dynamics(object):
    test: bool
    hello: str


class MetaTest(type):
    def __new__(cls, *args: Any, **kwargs: Any):
        instance = super().__new__(cls, *args, **kwargs)

        setattr(instance, "test", True)
        return instance

    def __setattr__(self, __name: str, __value: Any) -> None:
        return super().__setattr__(__name, __value)


class TestClass(metaclass=MetaTest):
    def __init__(self):
        setattr(self, "hello", "world")
        self.test2 = False


# I can't currently find a way to properly annotate a ClassVar and
# an instance variable that share the same name.  So far the only
# apparent solution involves type: ignore.
class DataClass:
    a: ClassVar[int] = 10

    def __init__(self):
        self.a: int = 5


# namedtuple (not NamedTuple, note the caps) does not support typing well
TestTuple = NamedTuple("TestTuple", good=str, bye=str)

tt = TestTuple(good="hi", bye="there")
# tt.good and tt.bye both appear in auto complete

test = TestClass()
print(getattr(test, "test"))  # setattr in MetaTest.__new__ not seen
print(getattr(test, "hello"))  # setattr in TestClass.__init__ not seen
print(test.test2)

dc = DataClass()
print("dc.a is", dc.a)
print("DataClass.a is", DataClass.a)

# This originally had a TypeVar "ST" bound=Sized, but ST implies
# the same type in this context, yet list() and dict()
# can both be passed in without worry.  Better use is
# the Sized protocol being the annotation.

# Collection[T] is our solution!  It implements Sized and derives from
# Iterable[T] and Container[T].
T = TypeVar("T")
U = TypeVar("U")


def longer(x: Collection[T], y: Collection[U]) -> Collection[T] | Collection[U]:
    if len(x) > len(y):
        return x
    else:
        return y


l1 = longer([1], ["hi", "there", 2])
l2 = longer({1}, {1, 2})
l3 = longer([1], {1, 2})

# This is for examining types at runtime regarding the contents of a Collection[T].
# Note how Pylance says OK! to word.upper() due to the presence of isinstance(word, str)
# there at the end.  Yay.
print([word.upper() for word in l1 if isinstance(word, str)])
