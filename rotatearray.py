nums = [1,2,3,4,5,6,7]
k = 2
for i in range(k):
    temp = nums[0]
    nums[0] = nums[-1]
    for j, num in enumerate(nums[1:]):
        moving = nums[j+1]
        nums[j+1] = temp
        temp = moving
            
print(nums)
        