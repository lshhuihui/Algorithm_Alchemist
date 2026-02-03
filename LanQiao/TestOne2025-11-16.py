# 注释（怎么思考的过程）+测试（确保我的想法和实际情况一致）
# 先有一个序列，故意让它乱序
arr = [5,7,8,1,2,9,10,11]
# 排序
arr.sort(reverse=False)
# 打印--测试
print(arr)
# 序列是奇数个还是偶数个 sizeof() 
n = len(arr)  # length
if n % 2 == 0:
    # print("偶数个")
    # 偶数个取中间值
    # [1, 2, 5, 7, 8, 9, 10,11]  8//2 = 4    n//2= 8  n//2 - 1 = 7
    one = n // 2 - 1
    two = n // 2
    mid = (arr[one] + arr[two]) / 2
    print(mid)

else:
    # print("奇数个")
    mid = int(n / 2) # 取中间值得用//
    print(arr[mid])



# 求所有的子序列  注释+测试

'''
[3,9,1,5]
i j
3 [9,1,5]


1 [5] 含i,那么就是[1,5] , 不含i是[5]
'''

alist = [3,9,1,5]
print("原始列表:", alist)
print("所有子序列:")

# 通用的递归方法
def get_all_subsequences(arr):
    """递归获取所有子序列"""
    if len(arr) == 0:
        return [[]]  # 基本情况：空列表只有空子序列
    if len(arr) == 1:
        return [[arr[0]], []]  # 基本情况：只有一个元素的列表只有空子序列和自身
    # 递归获取除了第一个元素外的所有子序列
    rest_subsequences = get_all_subsequences(arr[1:]) #从头到尾
    
    # 对于rest_subsequences中的每个子序列，有两种选择：
    # 1. 不包含第一个元素（保持原样）
    # 2. 包含第一个元素（在子序列前添加第一个元素）
    result = []
    for subseq in rest_subsequences:
        # 不包含第一个元素
        result.append(subseq)
        # 包含第一个元素
        result.append([arr[0]] + subseq)
    
    return result

# 获取所有子序列
subsequences = get_all_subsequences(alist)

# 按长度排序
subsequences.sort(key=len)

# 打印结果
for i, subseq in enumerate(subsequences):
    print(f"子序列 {i+1}: {subseq}")

print(f"\n总共有 {len(subsequences)} 个子序列")

# 测试4个元素的情况
print("\n--- 测试4个元素的情况 ---")
alist4 = [1, 2, 3, 4]
subsequences4 = get_all_subsequences(alist4)
print(f"列表 {alist4} 有 {len(subsequences4)} 个子序列")

# 测试5个元素的情况
print("\n--- 测试5个元素的情况 ---")
alist5 = [1, 2, 3, 4, 5]
subsequences5 = get_all_subsequences(alist5)
print(f"列表 {alist5} 有 {len(subsequences5)} 个子序列")