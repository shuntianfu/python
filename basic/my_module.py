
print('Importing my_module......')

test = 'some strings'

def find_index(to_search, target):
    for key, value in enumerate(to_search):
        if value == target:
            return key
    return -1

