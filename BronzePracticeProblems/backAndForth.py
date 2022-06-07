import sys

sys.stdin = open('backforth.in','r')
# sys.stdout = open('backforth.out','w')

first = list(map(int, input().split(" ")))
second = list(map(int, input().split(" ")))

ans = len(set(first))



print(ans)