a = {}
a[0] = ''
print(a)
memory_address = id(a)
print(memory_address)
a[1] = 'zhang'
memory_address = id(a)
print(memory_address)
