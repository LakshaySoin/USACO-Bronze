import sys

sys.stdin = open('gymnastics.in','r')
sys.stdout = open('gymnastics.out','w')

K, N = map(int, input().split(" "))
data = []

for i in range(K):
    data.append(list(map(int, input().split(" "))))

pos = []
temp = []

for i in data:
    for x in range(1, N + 1):
        temp.append(i.index(x))
    pos.append(temp)
    temp = []

temp = 0
cnt = 0
num = 0

while temp < N:
    for x in range(N):
        for i in pos:
            if i[temp] < i[x]:
                cnt += 1
        if cnt == K:
            num += 1
        cnt = 0
    temp += 1

print(num)
