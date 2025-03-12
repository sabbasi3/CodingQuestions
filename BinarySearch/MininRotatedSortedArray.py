
nums = [4,5,6,7,0,1,2]

l,r = 0, len(nums) - 1

while l < r: 
    mid = (l+r) // 2

    if nums[mid] > nums[r]:
        l = mid +1
    else:
        r = mid

print(nums[l])

# nums = [4,5,6,7,0,1,2]

# l, r = 0, len(nums) - 1
# min_val = float('inf')

# while l <= r: 
#     mid = (l + r) // 2

#     if nums[mid] < min_val:
#         min_val = nums[mid]

#     if nums[mid] > nums[r]:
#         l = mid + 1
#     else:
#         r = mid - 1

# print(min_val)  # Output: 0