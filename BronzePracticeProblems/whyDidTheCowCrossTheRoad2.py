import sys

sys.stdin = open('circlecross.in','r')
sys.stdout = open('circlecross.out','w')

cows = input()

pairs = []

for i in range(len(cows)):
    if i == cows.index(cows[i]):
        continue
    else:
        times = []
        for x in range(cows.index(cows[i]) + 1, i):
            if cows[x] in times:
                times.remove(cows[x])
            else:
                times.append(cows[x])
        for y in times:
            temp = sorted([cows[i], cows[cows.index(y)]])
            if temp not in pairs:
                pairs.append(temp)

print(len(pairs))
