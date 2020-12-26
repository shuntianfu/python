class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = f'{self.first}.{self.last}@email.com'
        self.pay = pay

    def fullname(self):
        return f'{self.first} {self.last}'


emp_1 = Employee('zhang', 'wen', 5000)
emp_2 = Employee('wang', 'liang', 6000)

print(type(Employee))
print(Employee)
print(emp_1)
emp_1.first = 'zhao'
print(emp_1.first)
print(Employee.fullname(emp_1))
print(type(Employee.fullname))
