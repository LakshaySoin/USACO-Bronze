import sys

sys.stdin = open('teleport.in','r')
sys.stdout = open('teleport.out','w')

a,b,x,y = map(int, input().split(' '))

if b < a:
    if abs(b - min(x,y)) + abs(a - max(x,y)) > (a - b):
        print(a - b)
    else:
        print(abs(b - min(x,y)) + abs(a - max(x,y)))
else:
    if abs(b - max(x,y)) + abs(a - min(x,y)) > (b - a):
        print(b - a)
    else:
        print(abs(b - max(x,y)) + abs(a - min(x,y)))