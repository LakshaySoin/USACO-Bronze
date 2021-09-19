alpha = input()
word = input()
index = 0
cnt = 0
while len(word) != index:
    for i in alpha:
        if index == len(word):
            break
        elif word[index] == i:
            index += 1
    cnt += 1

print(cnt)