import sys

sys.stdin = open('crossroad.in','r')
sys.stdout = open('crossroad.out','w')

N = int(input())

data = []

for _ in range(N):
    id, pos = map(int, input().split(" "))
    data.append([id, pos])

crossings = 0

for i in range(N):
    for x in range(i, N):
        if data[x][0] == data[i][0] and i != x:
            if data[i][1] != data[x][1]:
                crossings += 1
                break
            else:
                break
        x += 1

print(crossings)