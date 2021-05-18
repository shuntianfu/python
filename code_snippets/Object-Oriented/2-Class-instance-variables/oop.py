class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = f'{self.first}.{self.last}@email.com'
        self.pay = pay

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee('zhang', 'wen', 5000)
emp_2 = Employee('wang', 'liang', 6000)

# raise_amount instance variable

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)
