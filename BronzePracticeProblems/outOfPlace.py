import sys

sys.stdin = open('outofplace.in','r')
sys.stdout = open('outofplace.out','w')

N = int(input())

heights = []

for _ in range(N):
    heights.append(int(input()))

sorted_heights = sorted(heights)

swaps = 0

for i in range(N):
    if heights[i] != sorted_heights[i]:
        swaps += 1

print(swaps - 1)