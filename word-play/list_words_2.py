import time

# Very very long long time

with open('words.txt') as f:
    words = []
    for line in f:
        word = line.strip()
        word = [word]
        words = words + word

print(words)
