
nums = [1, 2, 3, 4, 5]

for num in nums:
    print(num)
    print(type(num))

print('*' * 10)
# break

nums = [1, 2, 3, 4, 5]

for num in nums:
    if num == 3:
        print('Found')
        break
    print(num)

print('*' * 10)

# Continue

for num in nums:
    if num == 3:
        print('Found')
        continue
    print(num)

print('*' * 10)

for num in nums:
    for letter in 'abc':
        print(num, letter)

print('*' * 10)

# range

for i in range(10):
    print(i)

print('*' * 10)

for i in range(1, 11):
    print(i)

for i in range(1, 11, 2):
    print(i)

print('*' * 10)

# while

x = 0

while x < 10:
    print(x)
    x += 1

print('*' * 10)


x = 0

while x < 10:
    if x == 5:
        break
    print(x)
    x += 1

x = 0

while True:
    if x == 5:
        break
    print(x)
    x += 1

# ctr + c break infinite loop.
