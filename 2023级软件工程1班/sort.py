def k(nums):
    n = len(nums)
    for i in range(n - 1):
        for j in range(n - i - 1):
            print(i, "-->", j)
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
        print('---------------------')
    return nums


nums = [3, 2, 1, 4, 9, 5]
print(k(nums))
