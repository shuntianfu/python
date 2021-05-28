
word = 'abcasfsddfds'

def is_abecdarian(word):
    first = 0
    for letter in word[:-1]:
        if letter > word[first + 1]:
            return False
        first += 1
    return True

print(is_abecdarian(word))
            
def is_abecdarian_2(word):
    i = 0
    while i <= len(word) - 2:
        current = word[i]
        forwoard = word[i + 1]
        if current <= forwoard:
            i += 1
            continue
        return False
    return True

print(is_abecdarian_2(word))
    
