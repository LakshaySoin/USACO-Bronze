import sys

N = int(input())
nums = list(map(int, input().split(" ")))
delete = []
temp = []
cnt = 0
even = True
findEven = False
findOdd = False

while len(nums) != 0:
    for i in range(N):
        if even == True:
            if nums[i] % 2 == 0:
                cnt += 1
                delete.append(i)
                even = False
                findEven = True
        elif even == False:
            if nums[i] % 2 == 1:
                cnt += 1
                delete.append(i)
                even = True
                findOdd = True
    N -= len(delete)
    for y in delete:
        del nums[y]
    print(cnt)
    if findEven != True and even == True:
        for i in range(N):
            if nums[i] % 2 == 1:
                temp.append(nums[i])
        if len(temp) > 2:
            cnt += 1
            del nums[nums.index(temp[0])]
            del nums[nums.index(temp[1])]
            if len(nums) == 0:
                    sys.exit()
            temp = []
    if findOdd != True and even == False:
        for i in range(N):
            if nums[i] % 2 == 0:
                temp.append(nums[i])
        if len(temp) > 2:
            cnt += 1
            del nums[nums.index(temp[0])]
            del nums[nums.index(temp[1])]
            if len(nums) == 0:
                    sys.exit()
            temp = []
        
        