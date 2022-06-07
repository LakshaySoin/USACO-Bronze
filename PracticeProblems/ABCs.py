data = list(map(int, input().split(" ")))
A = min(data)
data.pop(data.index(A))
B = min(data)
C = max(data) - A - B
print(A, B, C, sep=" ")