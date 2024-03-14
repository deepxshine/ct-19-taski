from typing import Any, Union, List
from queue import Queue

def f(a: Union[int , float]) -> Any:
    return a ** 2


def mximum_of_arr(arr:List[int]) -> int:
    maximum = arr[0]
    for item in arr[1:]:
        if item > maximum:
            maximum = item

    return maximum


def sum_of_arr(arr: List[int]) -> int:
    summa = 0
    for item in arr:
        summa += item

    return summa


class Foo:
    def __init__(self, boo: int) -> None:
        self.boo = boo

    def get(self) -> int:
        return self.boo

    def push(self, a:int) -> None:
        self.boo = a



def work_with_class(cls: Foo) -> None:
    a = cls.get()
    a*=10
    cls.push(a)


foo = Foo(12)
abs = Queue()
work_with_class(foo)
work_with_class(abs)