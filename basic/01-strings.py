
print('hello world')

message = 'Hello World'

print(message)

print(len(message))
print('*' * 10)

message = '"Hello" World'

print(message)

book = "zhang's book"

print(book)

print('*' * 10)
# Wrong
# book = 'zhang's book'

# print(book)

message = """zhang
li
wang"""

print(message)

print(len(message))

print('*' * 10)

# slicing

slice_string = "Hello World"

print(slice_string[0:5])
print(slice_string[6:])
print(slice_string[:-1])
print(slice_string[1:3])
print(slice_string[:])

print('*' * 10)

# method

message = 'Hello World'

print(message.upper())
print(message)

message = 'Hello World'

print(message.count('hello'))
print(message.count('Hello'))
print(message.count('l'))
print(message.find('l'))
print(message.find('World'))

print('*' * 10)

message = 'Hello World'

message.replace('World', 'Universe')

print(message)
print( message.replace('World', 'Universe'))

message = message.replace('World', 'Universe')

print(message)

print('*' * 10)

greeting = 'Hello'
name = 'Michael'

message = greeting + name

print(message)

message = greeting + ', ' + name + '. Welcome!'

print(message)

message = '{}, {}. Welcome!'.format(greeting, name)

# f string

message = f'{greeting}, {name}. Welcome!'

print(message)

message = f'{greeting}, {name.upper()}. Welcome!'

print(message)

print('*' * 10)

# dir, help function

# print(dir(name))

# print(help(str))

# print(help(str.upper))


