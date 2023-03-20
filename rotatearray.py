nums = [1,2,3,4,5,6,7]
k = 2

for i in range(k):
    for j, num in enumerate(nums):
        temp = nums[j+1]
        nums[j+1] = nums[j]
        
        