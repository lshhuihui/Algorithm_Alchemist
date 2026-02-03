# # 1-10^17
# result = []
# youxiao = set([1,2,1,4])
# for i in range(1, pow(10,17) + 1):
#     # print(i)
#     # 2-49
#     for j in range(2, 50):
#         # print(j)
#         if i % j == 3 or i % j == 6 or i % j == 7 or i % j == 8:
#             break
#         else:
#             result.append(i)

# print(len(result))

"""
[
    [0], [0], [0],
    [0], [0], [0],
    [0], [0], [0]
]

[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
"""

row = 3
col = 4
# [0]*col一行有col个[0]
# for i in range(row) 循环row行
A = [[0] * col for i in range(row)]
print(A)
