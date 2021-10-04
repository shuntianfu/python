import time

# Very very long long time
start = time.time()

with open('/home/zhang/learn_python/github_repo/python/word-play/words.txt') as f:
    words = []
    for line in f:
        word = line.strip()
        word = [word]
        words = words + word

end = time.time()

duration = end - start

print(duration)
