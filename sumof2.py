nums = [2, 7, 11, 15]
target = 13
Flag = False

for i, num1 in enumerate(nums):
    for j, num2 in enumerate(nums):
        if(i != j):
            if(num1+num2 == target):
                results = [i, j]
                print(results)
                flag = True
                break
    if(flag):
        break        
