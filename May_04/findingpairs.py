def find_pairs(nums,target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j]==target:
                print(nums[i],nums[j])
print(find_pairs([2,4,3,5,7,8],6))

