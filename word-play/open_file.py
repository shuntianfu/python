
no_e_count = 0
total = 0

f = open('words.txt')


def has_no_e(word):
    letter = 'e'
    if letter not in word:
        return True
    else:
        return False

# print(has_no_e('apple'))


for line in f:
    word = line.strip()
    if has_no_e(word) == True:
        # print(word)
        no_e_count += 1
    total += 1


# print(round(no_e_count / total, 2))

avo_letters = 'aoeiu'


def avoid(word):
    for letter in avo_letters:
        if letter in word:
            return False
    return True


f.close()

f = open('words.txt')

for line in f:
    word = line.strip()
    if avoid(word) == True:
        print(word)


f.close()
