import sys

sys.stdin = open('photo.in','r')
sys.stdout = open('photo.out','w')

N = int(input())
nums = list(input().split())

for i in range(1,N):
    global lst
    lst = []
    lst.append(i)
    n = 0
    if len(lst) == 1:
        new = int(nums[n]) - i
        lst.append(new)
        n += 1
    while n < N - 1:
        new = int(nums[n]) - lst[n]
        lst.append(new)
        n += 1
        if len(lst) != len(set(lst)):
            break
    if len(lst) == N:
        break

lst = map(str,lst)
print(" ".join(lst))