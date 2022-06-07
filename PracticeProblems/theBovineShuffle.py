import sys

file_in = open('shuffle.in','r')
data = file_in.read().split('\n')
N = int(data[0])
nums = list(map(int, data[1].split(" ")))
pos = list(map(int, data[2].split(" ")))
temp = list(map(int, data[2].split(" ")))

for _ in range(3):
    for i in range(N):
        pos[i] = temp[nums[i] - 1]
    temp = [x for x in pos]

sys.stdout = open('shuffle.out','w')

for x in pos:
    print(x)