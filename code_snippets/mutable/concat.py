employees = ['Corey', 'John', 'Rick', 'Steve', 'Carl', 'Adam']

output = '<ul>\n'

# id() is the address of the object in memory
# string is not mutalbe
for employee in employees:
    output += '\t<li>{}</li>\n'.format(employee)
    print('Adress of output is: {}'.format(id(output)))

output += '</ul>'

print(output)

# list is mutalbe

print(id(employees))

employees.append('zhang')

print(id(employees))

print('\n')

# 小结：Python的输出结果，最好能够用pyhton的其他程序来论证
# 比如这里，string和list的性质用id()方法来论证，这是深层次
# 的原因。该原因称为本质。

# 由深层原因导致的外在不同用法，成为表象。

# 符号表示 id() => method, attributes, assign

list_name = ['zhang', 'li', 'wang']
string_name = 'zhang'

list_name2 = list_name
string_name2 = string_name

list_name2.append('zhao')
string_name2 = 'li'

print(list_name, list_name2)
print(string_name, string_name2)
