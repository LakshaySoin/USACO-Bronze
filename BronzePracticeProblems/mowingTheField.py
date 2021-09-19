import sys

sys.stdin = open('mowing.in','r')
sys.stdout = open("mowing.out",'w')

N = int(input())
direction = []
steps = []
for i in range(N):
    data = input().split(" ")
    direction.append(data[0])
    steps.append(int(data[1]))

map = [[0, 0] for _ in range(sum(steps))]
location = [0, 0]
index = 0

for t in range(N):
    if direction[t] == "N":
        for _ in range(steps[t]):
            location[1] += 1
            map[index][0] = location[0]
            map[index][1] = location[1]
            index += 1
    if direction[t] == "S":
        for _ in range(steps[t]):
            location[1] -= 1
            map[index][0] = location[0]
            map[index][1] = location[1]
            index += 1
    if direction[t] == "E":
        for _ in range(steps[t]):
            location[0] += 1
            map[index][0] = location[0]
            map[index][1] = location[1]
            index += 1
    if direction[t] == "W":
        for _ in range(steps[t]):
            location[0] -= 1
            map[index][0] = location[0]
            map[index][1] = location[1]
            index += 1

sets = []

for x in map:
    if map.count(x) > 1:
        temp1 = map.index(x)
        map.pop(map.index(x))
        temp2 = map.index(x) + 1
        map.insert(temp1, x)
        sets.append(temp2 - temp1)

if len(sets) > 1:
    print(min(sets))
else:
    print(-1)