def find_min(nums: list[int]) -> int:   
    min_val = nums[0]
    for n in nums[1:]:
        if n < min_val:
            min_val = n
    return min_val

print(find_min([8, 4, 9, 2, 5, 7, 3])) 
