class Employee:
    raise_amount = 1.04

    def __init__(self, name):
        self.name = name


emp_1 = Employee('zhang')
emp_2 = Employee('wang')

# ##################### proof 1

# 证明instance寻找变量的路径是，首先看自己有没有这个变量，有的话就采用。要是没有
# 就看自己的类里面有没有，有的话就采用。self --> class(inner --> outter)，
# 按照这个理论，在上面
# 这个类里面，没有给instance，raise_amount的变量，但是Instance 应该在类里面找到这个值.

print(emp_1.raise_amount)

# ##################### proof 2

# python scope 相互不影响，只能自己修改自己的属性。

emp_1.raise_amount = 2

print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.raise_amount)

# 方法2 查询__dict__属性。

print(emp_1.__dict__)
print(emp_2.__dict__)
print(Employee.__dict__)

# python的灵魂是可以借用，但是不能修改借用的，只能修改自己。
