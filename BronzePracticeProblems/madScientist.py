import sys

sys.stdin = open("breedflip.in","r")
sys.stdout = open("breedflip.out","w")

N = int(input())
A = list(input())
B = list(input())

ans = 0

increase = True

for x, y in zip(A, B):
    if x != y:
        increase = False
    elif increase == False:
        ans += 1
        increase = True

print(ans)