def main():
    nums = [1,2,3,3]
    nums2 = list(set(nums))
    if len(nums) != len(nums2):
        return True
            
main()