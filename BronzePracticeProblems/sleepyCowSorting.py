import sys

sys.stdin = open('sleepy.in','r')
sys.stdout = open('sleepy.out','w')

N = int(input())
data = list(map(int, input().split(" ")))

i = N - 1

temp = 0

while i >= 0:
    temp += 1
    if data[i] < data[i - 1]:
        ans = N - temp
        break
    i -= 1

print(ans)