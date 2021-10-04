
target = "zymotic"

with open('/home/zhang/learn_python/github_repo/python/word-play/words.txt') as f:
    words = f.read()
    words = words.split()



target = ["one", "two", "three", "four", "five", "six", "seven"]

with open('testwords.txt') as f:
    words = f.read()
    words = words.split()


def search(target):
    index = len(words) // 2 + len(words) % 2 
    while True:
        if target == words[index]:
            return index
        index = index // 2 + index % 2
            
        elif target < words[index]:
            index = index - index // 2
        elif target > words[index]:
            index = index + index // 2
        if index index 
        

for i in target:
    print(search(i))
print(search(target))
