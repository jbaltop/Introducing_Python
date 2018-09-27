# p136


def answer():
    print(42)


answer()


def run_something(func):
    func()


run_something(answer)

print(type(run_something))


def add_args(arg1, arg2):
    print(arg1 + arg2)


print(type(add_args))


def run_something_with_args(func, arg1, arg2):
    func(arg1, arg2)


run_something_with_args(add_args, 5, 9)


def sum_args(*args):
    return sum(args)


def run_with_positional_args(func, *args):
    return func(*args)


print(run_with_positional_args(sum_args, 1, 2, 3, 4))
