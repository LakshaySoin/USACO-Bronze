import sys

sys.stdin = open('pails.in','r')
sys.stdout = open('pails.out','w')

X, Y, M = map(int, input().split(" "))

largest = 0
current = 0
cnt = 0

while Y <= M:
    if current + Y > M:
        break
    current += Y
    cnt += 1

largest = current

for i in range(cnt + 1):
    temp = current
    temp -= (Y * i)
    while temp <= M:
        if temp + X > M:
            break
        temp += X
    largest = max(largest, temp)

print(largest)