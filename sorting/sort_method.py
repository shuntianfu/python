
# li = [9, 1, 8, 2, 7, 3, 6, 4, 5]
# 
# s_li = sorted(li)
# 
# print('Sorted Variable:\t', s_li)
# print('Original Variable:\t', li)
# 
# li.sort()
# 
# print('Original Variable\t', li)
# 
# re_li = sorted(li, reverse=True)
# 
# print(re_li)

# tup = (1, 9, 2, 3, 7, 5, 3, 4)
# 
# s_tup = sorted(tup)
# 
# print(s_tup)
# 
# di = {'name': 'zhang', 'job': 'programming', 'age': None, 'os': 'Mac'}
# 
# s_di = sorted(di)
# 
# print('Dict\t', s_di)

# li = [-5, -7, 1, 2, -3, 0]
# 
# s_li = sorted(li)
# 
# abs_li = sorted(li, key=abs)
# 
# 
# print(s_li)
# 
# print(abs_li)

class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f'{self.name}, {self.age}, ${self.salary}'

e1 = Employee('zhang', 35, 7000)
e2 = Employee('li', 25, 8000)
e3 = Employee('wang', 33, 10000)

employees = [e1, e2, e3]

def e_name(emp):
    return emp.name

# s_emp = sorted(employees, key=e_name)
# 
# 
# print(s_emp)

# s_emp = sorted(employees, key=lambda e: e.salary)

# print(s_emp)

from operator import attrgetter

s_employees = sorted(employees, key=attrgetter('name'))

print(s_employees)

