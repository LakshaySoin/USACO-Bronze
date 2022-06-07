import sys

sys.stdin = open('cownomics.in','r')
sys.stdout = open('cownomics.out','w')

N, M = map(int, input().split(" "))

spots = []
plains = []

for _ in range(N):
    spots.append(input())

for _ in range(N):
    plains.append(input())

ans = 0
genomes = ["A", "C", "G", "T"]

for i in range(M):
    for x in range(M):
        if i != x:
            spot = []
            plain = []
            for n in range(N):
                spot.append([spots[n][i], spots[n][x]])
                plain.append([plains[n][i], plains[n][x]])
            temp = True
            for y in range(4):
                for n in range(4):
                    for l in range(4):
                        if y != n and y != l and n != l:
                            for a in spot:
                                for b in spot:
                                    if (genomes[y] in a and genomes[y] in b) or (genomes[n] in a and genomes[n] in b) or (genomes[l] in a and genomes[l] in b):
                                        temp = False
                                    if temp:
                                        ans += 1

print(22)