# -*- coding: utf-8 -*-
import functools


class SpecialMetaClass(type):  # type类似于java的类，自定义类，便于反射类的属性等
    # cls代表动态修改的类
    # name代表动态修改的类名
    # bases代表被动态修改的类的所有父类
    # attr代表被动态修改的类的所有属性、方法组成的字典
    def __new__(cls, name, bases, attrs):
        print('name:%s' % name)
        print('bases:%s' % bases)
        print('attr:%s' % attrs)

        def ext_fun_include_self(self) -> str:
            return 'i am %s' % self

        def ext_fun_not_include_self() -> str:
            return 'i am %s' % cls

        # if 'ext_fun' not in attrs:
        attrs['ext_fun_lambda'] = lambda self, x: x
        attrs['ext_fun_include_self'] = ext_fun_include_self
        attrs['ext_fun_not_include_self'] = functools.partial(ext_fun_not_include_self)

        print('new attrs:%s' % attrs)
        return super().__new__(cls, name, bases, attrs)


# 继承object类
# 定义使用的元类
class SpecialClass(object, metaclass=SpecialMetaClass):
    ATTR_A = 'ATTR_A_VALUE'

    class Field:
        A = "A"


def main():
    special_class = SpecialClass()
    print(special_class)
    print(special_class.ext_fun_include_self())
    print(special_class.ext_fun_not_include_self())
    print(special_class.ext_fun_lambda('metaclass_lambda'))
    pass


if __name__ == '__main__':
    main()
