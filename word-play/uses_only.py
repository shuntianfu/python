
letters = 'apple'

word = 'appleapple'

def uses_only(word, letters):
    for letter in word:
        if letter not in letters:
            return False
    else:  
        return True

print(uses_only(word, letters))
