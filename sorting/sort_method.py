
li = [9, 1, 8, 2, 7, 3, 6, 4, 5]

s_li = sorted(li)

print('Sorted Variable:\t', s_li)
print('Original Variable:\t', li)

li.sort()

print('Original Variable\t', li)

re_li = sorted(li, reverse=True)

print(re_li)
