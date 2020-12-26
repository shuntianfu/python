# 理论：如果修改之后，RAM地址不变 => mutable
# 如果修改之后，RAM地址改变 => imutable

# proof:

a = [1, 2, 3, 4]

before = id(a)

a[0] = 6

after = id(a)

if before == after:
    print('list is mutable')
else:
    print('list is imutable')


s = 'zhang'

before = id(a)

s += ', hello'

after = id(s)

if before == after:
    print('string is mutable')
else:
    print('string is imutable')


d = {'name': 'zhang', 'age': 34}

before = id(d)

d['email'] = 'zhang@xyz.com'

after = id(d)

if before == after:
    print('dictionary is mutable')
else:
    print('dictionary is imutable')
