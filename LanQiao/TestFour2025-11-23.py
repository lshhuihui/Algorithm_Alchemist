"""
3
1 2 3 4 7 9 1
0

3
1 2 3 4 7 9 1
5

50%   49  一
40%   45  二
30%   35  三

"""

# n = int(input())
# a = list(map(int, input().split(" ")))
# n = len(a)
# ans = 0
# for i in range(n):# 左闭右开
#     for j in range(i + 1, n):
#         if a[i] > a[j]:
#             a[i], a[j] = a[j], a[i]
#             ans += 1
# print(ans)


# ins = input("hello")
# print(ins)


# import os
# import sys

"""
3
1 2 3
去尝试每一种可能的等间隔d
6
3 5 4 7 6 7
"""
# n = int(input())
# h = list(map(int, input().split()))
# n = len(h)
# # 边界 n <= 1 , result = 1
# if n <= 1:
#     print(1)
# else:
#     # n > 1
#     max_len = 1
#     # 枚举所有可能的间隔d(相邻保留树的下标差)
#     for d in range(1, n):
#         # 枚举所有起始位置start(初始尝试保留的第一颗树的下标) <---因为我不知道从哪颗树开始保留，所以从0开始枚举
#         for start in range(0,n - d):# 从0这颗树开始保留，到n-d这颗树结束，因为保留的树的下标差是d，所以保留的树的下标是start,start+d
#             cnt = 1
#             i = start # 当前正在遍历的树的下标
#             j = start + d # next 下一颗要保留的树的下标 起点+间隔
#             # 只要下一个下标j只要在范围内就不能结束这个循环
#             while j < n:
#                 # 满足递增
#                 if h[j] > h[i]: # 有可能是需要保留的一种情况
#                     cnt += 1
#                     # 更新遍历的下标就好了
#                     i = j # 尝试继续查找下一个
#                     j = j + d # j += d 
#                 else: # 非递增
#                     break
#             # 全部遍历完成
#             max_len = max(max_len, cnt)
#     print(max_len)



import os
import sys

# 请在此输入您的代码
A = [] # [[1, 3], [2, 3], [3, 3]]
n = 3
for xa in range(1,n+1):
    for ya in range(1,n+1):
        sub_A = [xa,ya]
    A.append(sub_A)
print(A)

B = [] #[[1, 4], [2, 4], [3, 4], [4, 4]]
n = 4
for xb in range(1,n+1):
    for yb in range(1,n+1):
        sub_B = [xb,yb]
    B.append(sub_B)
print(B)

# [[1, 3], [2, 3], [3, 3]] * [[1, 4], [2, 4], [3, 4], [4, 4]]
for i in range(len(A)):
    for j in range(len(B)):
        print(A[i],B[j])
        # Xa*Xb + Ya*Yb
        L = A[i][0] * B[j][0] + A[i][1] * B[j][1]
        print(L)
    print('-------------')