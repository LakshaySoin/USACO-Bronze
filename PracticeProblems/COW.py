import sys

sys.stdin = open('cow.in','r')
sys.stdout = open('cow.out','w')

N = int(input())

letters = input()

ans = 0
c = 0
co = 0
cow = 0

for i in range(N):
    if letters[i] == "C":
        c += 1
    if letters[i] == "O":
        co += c
    if letters[i] == "W":
        cow += co

print(cow)