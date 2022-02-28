nums = [0, 2, 3, 4, 6, 8, 9]
nums = [0, 1, 2, 4, 5, 7]
start = 0
end = 0

r = []
while start < len(nums) and end < len(nums):
    if end+1 < len(nums) and nums[end]+1 == nums[end+1]:
        end = end+1
    else:
        if start == end:
            r.append(str(nums[start]))
            start = start + 1
            end = end + 1
        else:
            r.append(str(nums[start])+'->'+str(nums[end]))
            start = end + 1
            end = end + 1

        
print(r)
