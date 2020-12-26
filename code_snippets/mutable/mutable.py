a = [1, 2, 3, 4]

print(f'Address of a is: {id(a)}')

a[0] = 6

print(f'Address of a is: {id(a)}')

s = 'zhang'

print(f'Address of s is: {id(s)}')

s += ', hello'
# s[0] = 'H' # wrong
print(f'Address of s after concating is: {id(s)}')

d = {'name': 'zhang', 'age': 34}

print(f'Address of d is: {id(d)}')

d['emali'] = 'zhang@xyz.com'

print(f'Address of d after changing is: {id(d)}')
