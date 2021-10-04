
target = "zymotic"

with open('/home/zhang/learn_python/github_repo/python/word-play/words.txt') as f:
    words = f.read()
    words = words.split()



target = ["one", "two", "three", "four", "five", "six", "seven"]

with open('testwords.txt') as f:
    words = f.read()
    words = words.split()


def search(target):
    index = len(words) // 2 + len(words) % 2 - 1
    pattern = len(words) // 2 + len(words) % 2
    while True:
        if target == words[index]:
            return index
        pattern = pattern // 2 + pattern % 2
            
        if target < words[index]:
            index = index - pattern
        elif target > words[index]:
            index = index + pattern
        if target == words[index]:
            return index
        if  pattern == 1:
            if target == words[index + 1]:
                return index + 1
            else: 
                pattern = 0
        if pattern == 0:
            return 'Not Found!'

for i in target:
    print(search(i))
print(search(target))
