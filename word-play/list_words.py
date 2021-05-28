
import time

start = time.time()

with open('./words.txt') as f:
    words = []
    for line in f:
        word = line.strip()
        words.append(word)

end = time.time()

duration = end - start

print(duration)

start = time.time()

# with open('words.txt') as f:
#     words = []
#     for line in f:
#         word = [line.strip()]
#         words = words + word

end = time.time()

duration = end - start

print(duration)

# with open('words.txt') as f:
#     words = [line.strip() for line in f]
#
# print(words)

