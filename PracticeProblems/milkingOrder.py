import sys
from operator import itemgetter

sys.stdin = open('milkorder.in','r')
sys.stdout = open('milkorder.out','w')

N, M, K = map(int, input().split(" "))

hierarchy = list(map(int, input().split(" ")))

pos = []
fixed = []
cows = []

for _ in range(K):
    cow, position = map(int, input().split(" "))
    pos.append([cow, position])
    cows.append(cow)
    fixed.append(position)

lst = [0 for _ in range(N)]

for i in range(K):
    lst[fixed[i] - 1] = cows[i]

if 1 in cows:
    ans = fixed[cows.index(1)]
elif 1 not in hierarchy:
    i = N - 1
    pointer = M - 1
    while pointer >= 0:
        if hierarchy[pointer] in lst:
            i = lst.index(hierarchy[pointer]) - 1
            pointer -= 1
        else:
            if lst[i] == 0:
                lst[i] = hierarchy[pointer]
                pointer -= 1
                i -= 1
            else:
                i -= 1
    for x in range(N):
        if lst[x] == 0:
            ans = x + 1
            break
else:
    i = 0 
    pointer = 0
    while pointer <= M - 1:
        if hierarchy[pointer] in lst:
            i = lst.index(hierarchy[pointer]) + 1
            pointer += 1
        else:
            if lst[i] == 0:
                lst[i] = hierarchy[pointer]
                i += 1
                pointer += 1
            else:
                i += 1
    for x in range(N):
        if lst[x] == 1:
            ans = x + 1
            break

print(ans)