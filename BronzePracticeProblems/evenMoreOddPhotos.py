N = int(input())
cows = list(map(int, input().split(" ")))

odd = 0
even = 0

for i in cows:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

while even != odd or even - 1 == odd:
    if even < odd:
        if even - odd == 2:
            odd += 1
            break
        else:
            odd -= 2
            even += 1
    elif even > odd:
        even = odd + 1
        break

print(even + odd)