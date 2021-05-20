
##############
#LEGB
#Local, enclosing, Global, Built-in
#############

x = 'global x'

def test():
    x = 'local x'
    # print(y)
    print(x)

# find varible, local -> enclosing -> global -> built-in
test()
print(x)

y = 'global y'

def test_1():
    global y
    y = 'local y'
    # print(y)
    print(y)

test_1()
print(y)


def test_3():
    global w
    w = 'local w'
    print(w)

test_3()
print(w)

def test_2(z):
    print(z)

test_2('local z')
# print(z)

