def brute_force_subset_sum_simple(nums, target):
    # 暴力破解子集和问题
    valid_subsets = []
    subsets = [[]]
    for num in nums:
        # 为每个现有子集添加当前数字
        for i in range(len(subsets)):
            new_subset = subsets[i] + [num]
            subsets.append(new_subset)
            # 检查新子集的和是否等于目标
            if sum(new_subset) == target:
                valid_subsets.append(new_subset)
    return valid_subsets

# 从[1,3,5,7]中找和为4的子集
if __name__ == "__main__":
    nums = [1, 3, 5, 7]
    target = 4
    result = brute_force_subset_sum_simple(nums, target)
    print(f"数组{nums}中和为{target}的子集有：")
    for subset in result:
        print(subset)  # 输出：[1, 3]