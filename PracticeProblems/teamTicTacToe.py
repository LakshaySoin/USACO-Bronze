import sys

sys.stdin = open('tttt.in','r')
sys.stdout = open('tttt.out','w')

single = 0
double = 0

data = [input() for _ in range(3)]
letters = []

for i in data:
    for x in i:
        if x not in letters:
            letters.append(x)

for i in letters:
    for x in range(3):
        hcnt = 0
        vcnt = 0
        for y in range(3):
            if data[x][y] == i:
                hcnt += 1
            if data[y][x] == i:
                vcnt += 1
        if hcnt == 3:
            single += 1
        if vcnt == 3:
            single += 1
    if data[0][0] == i and data[1][1] == i and data[2][2] == i:
        single += 1
    if data[0][2] == i and data[1][1] == i and data[2][0] == i:
        single += 1

for i in letters:
    for j in letters[letters.index(i):]:
        for x in range(3):
            hcnt = 0
            vcnt = 0
            for y in range(3):
                if data[x][y] == i or data[x][y] == j:
                    hcnt += 1
                if data[y][x] == i or data[y][x] == j:
                    vcnt += 1
            if hcnt == 3:
                double += 1
            if vcnt == 3:
                double += 1
        if (data[0][0] == i or data[0][0] == j) and (data[1][1] == i or data[1][1] == j) and (data[2][2] == i or data[2][2] == j):
            double += 1
        if (data[0][2] == i or data[0][2] == j) and (data[1][1] == i or data[1][1] == j) and (data[2][0] == i or data[2][0] == j):
            double += 1
    
print(single)
print(double)