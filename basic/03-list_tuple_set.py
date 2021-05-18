
# index [0, 1, 2, 3...]

courses = ['History', 'Math', 'Math', 'Phythsics', 'CompSci']

print(courses)

print(len(courses))

print(courses.count('Math'))

print(courses[3])

print(courses[-1])

print(courses[:-1])
print(courses[:])

print(courses[0:2])

print('*' * 10)

# add item


courses = ['History', 'Math', 'Math', 'Phythsics', 'CompSci']

courses.append('last')

print(courses)

courses = ['History', 'Math', 'Math', 'Phythsics', 'CompSci']

courses.insert(0, 'first')

print(courses)

courses = ['History', 'Math', 'Math', 'Phythsics', 'CompSci']

courses_2 = ['list1', 'list2']

courses.insert(0, courses_2)

print(courses)

courses = ['History', 'Math', 'Math', 'Phythsics', 'CompSci']

courses.extend(courses_2)

print(courses)

print('*' * 10)

courses = ['History', 'Math', 'Math', 'Phythsics', 'CompSci']

courses.remove('Math')

print(courses)

courses = ['History', 'Math', 'Math', 'Phythsics', 'CompSci']

courses.pop()

print(courses)


courses = ['History', 'Math', 'Math', 'Phythsics', 'CompSci']

poped = courses.pop()

print(poped)

# reverse

courses = ['History', 'Math', 'Math', 'Phythsics', 'CompSci']

courses.reverse()

print(courses)

courses.sort()

print(courses)


courses = ['History', 'Math', 'Math', 'Phythsics', 'CompSci']

nums = [3, 5, 2, 4, 1]

courses.sort(reverse=True)
nums.sort(reverse=True)

print(courses, nums)

print('*' * 10)

# function

courses = ['History', 'Math', 'Math', 'Phythsics', 'CompSci']

nums = [3, 5, 2, 4, 1]

sorted_courses = sorted(courses)

print(courses)
print(sorted_courses)

print(max(nums), min(nums), sum(nums))

print('*' * 10)

# index


courses = ['History', 'Math', 'Math', 'Phythsics', 'CompSci']

print(courses.index('CompSci'))

print('Art' in courses, 'Math' in courses)

print('*' * 10)

# loop


courses = ['History', 'Math', 'Math', 'Phythsics', 'CompSci']

for course in courses:
    print(course)

for index, course in enumerate(courses):
    print(index, course)


for index, course in enumerate(courses, start=1):
    print(index, course)

print('*' * 10)

# join method

courses = ['History', 'Math', 'Math', 'Phythsics', 'CompSci']

courses_str = ', '.join(courses)

print(courses_str)

new_list = courses_str.split(', ')

print(new_list)

# Mutable

list_1 = ['History', 'Math', 'Physics', 'CompSci']

list_2 = list_1

print(list_1)

print(list_2)

list_1.append('Art')

print(list_1)

print(list_2)

list_2.append('Education')

print(list_1)

print(list_2)

# Imutalbe

tuple_1 = ('History', 'Math', 'Physics', 'ComSci')

tuple_2 = tuple_1

print(tuple_2)

# wrong
# tuple_1.append('Art')

print('*' * 10)

# Sets

cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}

print(cs_courses)

print('Math' in cs_courses)

art_courses = {'History', 'Math', 'Art', 'Design'}

print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses - art_courses)
print(cs_courses.union(art_courses))
# wrong
# print(cs_courses + art_courses)

# empty

empty_list = []
empty_list = list()

empty_tuple = ()
empty_tuple = tuple()

empty_set = set()
# wrong
# empty_set = {}
dictionary = {}
