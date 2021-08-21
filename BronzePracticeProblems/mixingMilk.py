import sys

file_in = open('mixmilk.in','r')
data = file_in.read().split('\n')
data = [list(map(int, data[l].split(" "))) for l in range(3)]
sys.stdout = open('mixmilk.out','w')

def pour(i, j):
    amount = min(data[i][1], data[j][0] - data[j][1])
    data[i][1] -= amount
    data[j][1] += amount

for i in range(100):
    pour(i%3, (i + 1)%3)

for x in range(3):
    print(data[x][1])