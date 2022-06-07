import sys

sys.stdin = open('swap.in','r')
sys.stdout = open('swap.out','w')

N, K = map(int, input().split())
A1, A2 = map(int, input().split())
B1, B2 = map(int, input().split())

order = [i + 1 for i in range(N)]
temp_order = order.copy()
index = -1
orders = []

while True:
    if len(orders) != 0:
        n = orders[index]
        temp_order = n.copy()
    temp = temp_order[A1 - 1:A2]
    temp.reverse()
    temp_order[A1 - 1:A2] = temp
    temp = temp_order[B1 - 1:B2]
    temp.reverse()
    temp_order[B1 - 1:B2] = temp
    orders.append(temp_order)
    if temp_order == order:
        break
    index += 1

ans = orders[(K - 1) % len(orders)]

for i in ans:
    print(i)