emp_1 = {'name': 'zhang', 'raise_amount': 2}
emp_2 = {'name': 'wang'}
Employee = {'__module__': '__main__', 'raise_amount': 1.04,
            '__init__': '<function Employee.__init__ at 0x7f17904d6ee0>',
            '__dict__': "<attribute '__dict__' of 'Employee' objects>",
            '__weakref__': "<attribute '__weakref__' of 'Employee' objects>",
            '__doc__': None}

# loop 的是 keys.

for k in emp_1:
    print(k)

for k in emp_1.keys():
    print(k)

print(emp_1.keys())
print(emp_1.values())
print(emp_1.items())

search = 'raise_amount'

if search in emp_1:
    print(search + ' --> ' + str(emp_1[search]))

if search in emp_2:
    print(search + ' --> ' + str(emp_2[search]))
else:
    print('not found')

if search in Employee:
    print(search + ' --> ' + str(Employee[search]))
else:
    print('not found')
