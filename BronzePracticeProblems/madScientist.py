import sys

sys.stdin = open("breedflip.in","r")
sys.stdout = open("breedflip.out","w")

N = int(input())
A = list(input())
B = list(input())

index = 0
current = 0
cnt = 0
increase = False

for i in range(N):
    if A[i] == B[i]:
        for x in range(index, current):
            if B[x] == "H":
                B[x] = "G"
            else:
                B[x] = "H"
            increase = True
        if increase == True:
            cnt += 1
        increase = False
        current += 1
        index = current
    elif A[i] != B[i]:
        current += 1

print(cnt)