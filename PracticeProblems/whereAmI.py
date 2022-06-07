import sys

sys.stdin = open('whereami.in','r')
sys.stdout = open('whereami.out','w')

N = int(input())
string = input()

vals = []

for i in range(N):
    for x in range(i, N + 1):
        if string.count(string[i:x]) > 1:
            vals.append(len(string[i:x]))

print(max(vals) + 1)