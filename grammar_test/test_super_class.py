# -*- coding: utf-8 -*-

class SuperClass:
    def __init__(self):
        super().__init__()

    def test(self, case: int):
        if case == 1:
            print('normal')
        else:
            raise ValueError("aaa")  # TypeError("aaa")


class SubClass(SuperClass):

    def __init__(self):
        super().__init__()

    def test(self, case: int):
        super().test(case)


if __name__ == '__main__':
    # AttributeError: 'super' object has no attribute 'test'， when error occur in super.test()
    SubClass().test(0)
