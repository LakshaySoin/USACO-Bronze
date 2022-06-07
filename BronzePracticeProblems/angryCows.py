import sys

# sys.stdin = open('angry.in','r')
# sys.stdout = open('angry.out','w')

N = int(input())

data = []

for _ in range(N):
    data.append(int(input()))

data.sort()

# 3 4 5 6 8 13

dist = []

for i in range(N - 1):
    dist.append(data[i + 1] - data[i])

for i in range(len(dist)):
    for x in range(len(dist)):
        if 