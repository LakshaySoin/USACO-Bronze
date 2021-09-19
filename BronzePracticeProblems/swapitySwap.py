import sys

sys.stdin = open('swap.in','r')
sys.stdout = open('swap.out','w')

N, K = map(int, input().split())
A1, A2 = map(int, input().split())
B1, B2 = map(int, input().split())

order = [i + 1 for i in range(N)]

for _ in range(K):
    temp = order[A1 - 1:A2]
    temp.reverse()
    order[A1 - 1:A2] = temp
    temp = order[B1 - 1:B2]
    temp.reverse()
    order[B1 - 1:B2] = temp

for i in order:
    print(i)