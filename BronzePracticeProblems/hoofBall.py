import sys

sys.stdin = open('hoofball.in','r')
sys.stdout = open('hoofball.out','w')

N = int(input())
data = list(map(int, input().split()))

data.sort()
data.reverse()

