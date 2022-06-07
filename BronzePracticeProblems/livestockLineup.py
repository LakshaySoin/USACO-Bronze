import sys

# sys.stdin = open('lineup.in','r')
# sys.stdout = open('lineup.out','w')

cows = ['Beatrice', 'Belinda', 'Bella', 'Bessie', 'Betsy', 'Blue', 'Buttercup', 'Sue']

N = int(input())

constraints = []

for _ in range(N):
    constraints.append(input().split())

for i in range(N):
    if abs(cows.index(constraints[i][0]) - cows.index(constraints[i][5])):
        temp = sorted([cows[cows.index(constraints[i][0])], cows[cows.index(constraints[i][5])]])
        if cows.index(temp[0]) > cows.index(temp[1]):
            cows[cows.index(temp[1]) - 1], cows[cows.index(temp[0])] = cows[cows.index(temp[0])], cows[cows.index(temp[1]) - 1]
            cows[cows.index(temp[1]) - 1:].sort()
        else:
            cows[cows.index(temp[1])], cows[cows.index(temp[0]) + 1] = cows[cows.index(temp[0]) + 1], cows[cows.index(temp[1])]
            cows[cows.index(temp[0]) + 1:].sort()
    print(cows)

for i in cows:
    print(i)