import sys

# sys.stdin = open('revegetate.in','r')
# sys.stdout = open('revegetate.out','w')

N, M = map(int, input().split())

data = []

for _ in range(M):
    a, b = map(int, input().split())
    data.append([a, b])

ans = [0 for _ in range(N)]

for i in range(N):
    temp = []
    cnt = 0
    for x in range(M):
        if i + 1 == data[x][0]:
            if ans[data[x][1] - 1] != 0 and ans[data[x][1] - 1] not in temp:
                temp.append(ans[data[x][1] - 1])
        elif i + 1 == data[x][1]:
            if ans[data[x][0] - 1] != 0 and ans[data[x][0] - 1] not in temp:
                temp.append(ans[data[x][0] - 1])
    if cnt == 3:
        cnt = 0
    ans[i] = len(set(temp)) + 1

for i in ans:
    print(i, end="")