
# search

student = {'name': 'zhang', 'age': 25, 'courses': ['Math', 'compSci']}

print(student)

print(student['name'])

print(student['courses'])

print(student.get('name'))

print(student.get('phone'), 'Not Found')

print('*' * 10)

# add

student = {'name': 'zhang', 'age': 25, 'courses': ['Math', 'compSci']}

student['phone'] = '555-5555'

student['name'] = 'li'

print(student)

student = {'name': 'zhang', 'age': 25, 'courses': ['Math', 'compSci']}

student.update({'name': 'li', 'age': 30, 'phone': '666-6666'})

print(student)

# delete

student = {'name': 'zhang', 'age': 25, 'courses': ['Math', 'compSci']}

del student['age']

print(student)

student = {'name': 'zhang', 'age': 25, 'courses': ['Math', 'compSci']}

poped = student.pop('age')

print(student)
print(poped)

# key, value

student = {'name': 'zhang', 'age': 25, 'courses': ['Math', 'compSci']}

print(student.keys())
print(student.values())
print(student.items())

print('*' * 10)

# loop

student = {'name': 'zhang', 'age': 25, 'courses': ['Math', 'compSci']}

for key in student:
    print(key)

for value in student.values():
    print(value)

for key, value in student.items():
    print(key, value)
print('*' * 10)

# Mutalbe

student = {'name': 'zhang', 'age': 25, 'courses': ['Math', 'compSci']}

student_2 = student

student_2.update({'name': 'li'})

print(student)
