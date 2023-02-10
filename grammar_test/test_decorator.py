from functools import wraps


def function_0_decorator_0(func):
    print('function_0_decorator_0, decorator func name:{}'.format(func))

    def decorator():
        print('before execute')
        func()
        print('after execute')

    return decorator


@function_0_decorator_0
def function_0_decorator_0_test():
    print('function_0_decorator_0_test')


print('function [function_0_decorator_0_test] handle:{}'.format(function_0_decorator_0_test))

print('********************')


def function_0_decorator_1(url: str):
    print('function_0_decorator_1, url:{}'.format(url))

    def decorator(func):
        print('1111111111')

        def a():
            print(func)
            print('function_0_decorator_1, decorator func name:{}'.format(func))

        return a

    return decorator


@function_0_decorator_1('aaa')
def function_0_decorator_1_test():
    print('function_0_decorator_1_test')


print('function [function_0_decorator_1_test] handle:{}'.format(function_0_decorator_1_test))

print('********************')


def function_1_decorator_0(func):
    print('function_1_decorator_0, decorator func name:{}'.format(func))

    @wraps(func)
    def decorator(*args, **kwargs):
        print(args)
        print(kwargs)

    return decorator


@function_1_decorator_0
def function_1_decorator_0_test(name: str):
    print('function_1_decorator_0_test, parameter[name]:{}'.format(name))


print('function [function_1_decorator_0_test] handle:{}'.format(function_1_decorator_0_test))
function_1_decorator_0_test('name')
print('********************')


def function_1_decorator_1(url: str):
    print('function_1_decorator_1, url:{}'.format(url))

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('-----{}'.format(args))
            print('-----{}'.format(kwargs))
            func(*args, **kwargs)

        print('function_1_decorator_1, decorator func name:{}'.format(func))
        return wrapper

    return decorator


# def
@function_1_decorator_1('bbb')
def function_1_decorator_1_test(name: str):
    print('function_1_decorator_1_test.name:{}'.format(name))


print('function [function_1_decorator_1_test] handle:{}'.format(function_1_decorator_1_test))
function_1_decorator_1_test('xxxxxx')
print('********************')


def decorator_1(func):
    print('decorator_1: func{}'.format(func))

    def wrapper():
        print('decorator_1: before execute func')
        func()
        print('decorator_1: after execute func')

    return wrapper


def decorator_2(func):
    print('decorator_2: func{}'.format(func))

    def wrapper():
        print('decorator_2: before execute func')
        func()
        print('decorator_2: after execute func')

    return wrapper


def decorator_3(func):
    print('decorator_3: func{}'.format(func))

    def wrapper():
        print('decorator_3: before execute func')
        func()
        print('decorator_3: after execute func')

    return wrapper


def decorator_4(func):
    print('decorator_4: func{}'.format(func))

    def wrapper():
        print('decorator_4: before execute func')
        func()
        print('decorator_4: after execute func')

    return wrapper


@decorator_1
@decorator_2
@decorator_3
@decorator_4
def multi_decorator_test():
    print('bbbbbbbbb')


multi_decorator_test()
print('function [multi_decorator_test] handle:{}'.format(multi_decorator_test))
print('********************')

if __name__ == '__main__':
    # main()
    pass
