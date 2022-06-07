import sys

sys.stdin = open('buckets.in','r')
sys.stdout = open('buckets.out','w')

for i in range(10):
    row = input()
    for x in range(10):
        if row[x] == "B":
            b_0 = x
            b_1 = i
        if row[x] == "R":
            r_0 = x
            r_1 = i
        if row[x] == "L":
            l_0 = x
            l_1 = i

dist = abs(l_0 - b_0) + abs(l_1 - b_1) - 1

if (r_0 == l_0 == b_0) and ((l_1 < r_1 < b_1) or (b_1 < r_1 < l_1)):
    dist += 2
elif (r_1 == l_1 == b_1) and ((l_0 < r_0 < b_0) or (b_0 < r_0 < l_0)):
    dist += 2

print(dist)