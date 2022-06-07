import sys

file_in = open('word.in','r')
data = file_in.read().split("\n")
N,K = map(int, data[0].split(" "))
words = data[1].split(" ")
sys.stdout = open('word.out','w')
counter = 0
t = []

for i in words:
    if counter + len(i) > K:
        print(" ".join(t))
        t = [i]
        counter = len(i)
    else:
        counter += len(i)
        t.append(i)
print(" ".join(t))
