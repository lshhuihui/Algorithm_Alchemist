# 求所有的子序列  注释+测试
alist = [3, 9, 1, 5]
n = len(alist)
result = []
for i in range(n):
    # print(i,alist[i])
    for j in range(i + 1, n + 1):
        # print(j,alist[j])
        result.append(alist[i:j])
        # print(alist[i:j]) #从I到J 已经把所有连续子序列求出来了

    # print('----------------')


jresult = []
for i in range(len(result)):
    # print(result[i])
    item = result[i] # item每个子序列
    print(item)
    nitem  = len(item) # nitem每个子序列的长度
    print(nitem)
    if nitem % 2 != 0:
        jresult.append(item)

    # itemsum = item[0] + mid 子序列的起始位置 * 子序列的中位数
    # sum += itemsum


print(jresult)

"""

alist = [3,9,1,5]
[
    [3], 
    [3, 9], 
    [3, 9, 1], 
    [9], 
    [9, 1], 
    [1]
]
[
[3], 
[3, 9], 
[3, 9, 1],
[3, 9, 1, 5], 

[9], 
[9, 1], 
[9, 1, 5], 

[1], 
[1, 5], 
[5]

]

"""


def get_all_subsequences(arr):
    """递归获取所有子序列"""
    if len(arr) == 0:
        return [[]]  # 基本情况：空列表只有空子序列
    # 递归获取除了第一个元素外的所有子序列
    rest_subsequences = get_all_subsequences(arr[1:])  # 从1到尾

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


blist = [3, 9, 1, 5]
r = get_all_subsequences(blist)
# print(r)
