import sys

sys.stdin = open('herding.in','r')
sys.stdout = open('herding.out','w')

cows = list(map(int, input().split(" ")))
cows.sort()

if cows[0] + 2 == cows[2]:
    minimum = 0
elif cows[0] + 2 == cows[1] or cows[1] + 2 == cows[2]:
    minimum = 1
else:
    minimum = 2

maximum = max(cows[2] - cows[1], cows[1] - cows[0]) - 1

print(minimum)
print(maximum)