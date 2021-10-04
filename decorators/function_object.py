
def first(msg):
    print(msg)


first("Hello")

second = first

second("world")

# we must be comfortable with the fact that everything
# in PYthong (Yes! Even classes), are objects. Name that
# we define are simply identifiers bound to these object.
# Functions are no exceptions, they are objects too.

# Functions can be passed as arguments to another function.


def inc(x):
    return x + 1


def dec(x):
    return x - 1


def operator(func, x):
    result = func(x)
    return result


# func <- inc
print(operator(inc, 3))
print(operator(dec, 3))

# function in function


def print_msg(message):
    greating = "Hello"

    def printer():
        print(greating, message)
    return printer


func = print_msg("Python is awsome")
# ? TODO why func has greating variable
func()


def printer():
    print("Hello World!")


def display_info(func):

    def inner():
        print("Excute", func.__name__, "function")
        func()
        print("Finshed execute")
    return inner


decorator_func = display_info(printer)

decorator_func()


def display_info(func):

    def inner():
        print("Excute", func.__name__, "function")
        func()
        print("Finshed execute")
    return inner


@display_info
def printer():
    print("Hello World!")


printer()


def smart_divide(func):
    def inner(a, b):
        print('I am going to divide', a, "and", b)
        if b == 0:
            print("Whoops! can't divide")
            return
        return func(a, b)
    return inner


@smart_divide
def divide(a, b):
    print(a/b)


def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner


@star
@percent
def printer(msg):
    print(msg)


printer("ni hao")
