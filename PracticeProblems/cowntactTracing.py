import sys

sys.stdin = open('tracing.in','r')
sys.stdout = open('tracing.out','w')

N, T = map(int, input().split(" "))

a = input()
infected = []

for i in range(len(a)):
    infected.append(int(a[i]))

data = []

for _ in range(T):
    data.append(list(map(int, input().split(" "))))

data.sort()

init = []

ans = 0
kmin = -float("inf")
kmax = float("inf")

for i in range(T):
    tempmin = -float("inf")
    tempmax = float("inf")
    if infected[data[i][1] - 1] == 1 and infected[data[i][2] - 1] == 1 and data[i][1] not in init and data[i][2] not in init:
        init.append(data[i][1])
        lower += 1
        upper += 1
    elif infected[data[1][1] - 1] == 1 and infected[data[i][2] - 1] == 0:
        ans = upper
    elif infected[data[i][1] - 1] != 1 and infected[data[i][2] - 1] == 1 and data[i][2] not in init:
        init.append(data[i][2])
        lower += 1
        upper += 1

print(len(init), lower, ans)