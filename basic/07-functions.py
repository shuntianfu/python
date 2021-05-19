
def func():
    return "Hello Word"

print(func)
print(func())

print('*' * 10)

def hello_func(greeting):
    return "{} Function".format(greeting)

print(hello_func('hello'))

def hello_func(greeting, name='You'):
    return "{}. {}".format(greeting, name)

print(hello_func("hello"))
print(hello_func("hello", "zhang"))

print("*" * 10)

def student_info(*arg, **kwargs):
    print(arg)
    print(kwargs)

student_info('Math', 'History', name='zhang', age=40)

print("*" * 10)

def student_info(*arg, **kwargs):
    print(arg)
    print(kwargs)
courses = ['Math', 'History']

info = {'name': 'zhang', 'age': 22}

student_info(courses, info)

student_info(*courses, **info)

print('*' * 10)

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    if not 1 <= month <= 12:
        return "Invalid Month"
    if month ==2 and is_leap(year):
        return 29
    return  month_days[month]

print(is_leap(2020))

print(days_in_month(2021, 2))
