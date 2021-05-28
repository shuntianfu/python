
import random
# Write a fucntion called nested_sum that takes a list of lists as elments from
# all of the nested lists.

t = [[1, 2], [3], [4, 5, 6]]

def nested_sum(t):
    result = 0
    for li in t:
        result = sum(li) + result
    return result

print(nested_sum(t))

# Write a function called cumsum that take a list of numbers and returns the
# cumulative sum; that is, a new list where the ith element is sum of the
# first i + 1 elments from the original list.


t = [1, 2, 3]

def cumsum(t):
    result = []
    i = 1
    for num in t:
        result.append(sum(t[:i]))
        i += 1
    return result

print(cumsum(t))

# Write a function called middle that takes a list and returns a new list
# contains all but first and last elememnts.


t = [1, 2, 3, 4, 8, 2]

def middle(t):
    new_list = t[1:-1]
    return new_list

print(middle(t))

t = [1, 3, 2]

def is_sorted(t):
    if t == sorted(t):
        return True
    return False

print(is_sorted(t))


def is_anagram(word, another):
    if len(word) != len(another):
        return False
    for letter in list(word):
        if letter in another:
            return True
    return False

print(is_anagram('zhang', 'angzh'))

def has_duplicates(t):
    for i in t:
        if t.count(i) != 1:
            return True
    return False

def has_duplicates_2(t):
    start = 1 
    for i in t:
        if i in t[start:len(t)]:
            return True
        start += 1
    print(start)
    return False


students = []

for i in range(23):
    # year = random.randint(2013, 2014)
    month = random.randint(1, 12)
    day = random.randint(1, 31)
    students.append([month, day])

print(sorted(students))
print(has_duplicates(students))

