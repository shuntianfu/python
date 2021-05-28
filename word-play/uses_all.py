
letters = 'abc'

word = 'appleappcleb'

def uses_all(word, letters):
    for letter in letters:
        if letter not in word:
            return False
    return True

print(uses_all(word, letters))

