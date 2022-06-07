import sys

sys.stdin = open('guess.in','r')
sys.stdout = open('guess.out','w')

N = int(input())
data = []
animals = []
nums = []
chars = []

for _ in range(N):
    temp = input().split(" ")
    data.append(temp)
    animal, K = temp[0], temp[1]
    animals.append(animal)
    nums.append(int(K))

commons = []

for i in range(N):
    for x in range(N):
        if i != x:
            common = 0
            for y in range(int(data[i][1])):
                for j in range(int(data[x][1])):
                    if data[i][y + 2] == data[x][j + 2]:
                        common += 1
            commons.append(common)

print(max(commons) + 1)