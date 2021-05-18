
# Comparisons:
# ==, <, >, <=, >=, !=, Object Identity: is

if True:
    print('Conditional was True')

if False:
    print('Conditional was True')

print('*' * 10)

language = 'Python'

if language == 'Python':
    print('Conditional was True')

print('*' * 10)

language = 'Java'

if language == 'Python':
    print('Conditional was True')
else:
    print('No match')

print('*' * 10)

language = 'Java'

if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
else:
    print('No match')

print('*' * 10)

# and or not

user = 'zhang'
logged_in = True

if user == 'zhang' and logged_in:
    print('zhang page')
else:
    print('Bad Creds')

user = 'zhang'
logged_in = False

if user == 'zhang' and logged_in:
    print('zhang page')
else:
    print('Bad Creds')

user = 'zhang'
logged_in = False

if user == 'zhang' or logged_in:
    print('zhang page')
else:
    print('Bad Creds')

user = 'zhang'
logged_in = False

if not logged_in:
    print('zhang page')
else:
    print('Bad Creds')
print('*' * 10)

# identity

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)
print(id(a))
print(id(b))

a = [1, 2, 3]
b = a

print(a == b)
print(a is b)
print(id(a))
print(id(b))


# False Values:
# False, None, 0, '', (), [], {}.

if '':
    print('Evaluated to True')
else:
    print('Evaluated to False')

if 'string':
    print('Evaluated to True')

condition = [False, 0, '', (), [], {}, None]

for value in condition:
    if value:
        print('Evaluated to True')
    else:
        print('Evaluated to False')
