def find_max(nums: list[int]) -> int:
    max_val = nums[0]
    for n in nums[1:]:
        if n > max_val:
            max_val = n
    return max_val


print(find_max([8, 4, 9, 2, 5, 7, 3]))
