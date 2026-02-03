# adict = {
#     "a": 1,
#     "b": 2.3,
#     6: 3,
#     3.14: 6,
#     2: 5,
#     "f": 6,
#     "g": 7,
#     "h": 8,
# }
# dict_keys(['a', 'b', 6, 3.14, (1, 2), 'f', 'g', 'h'])
# keys = adict.keys()
# AttributeError: 'dict_keys' object has no attribute 'sort'
# keys.sort()
# TypeError: '<' not supported between instances of 'int' and 'str'
# dict_items([('a', 1), ('b', 2.3), (6, 3), (3.14, 'bac'), ((1, 2), 5), ('f', 6), ('g', 7), ('h', 8)]) <class 'dict_items'>
# l[0][1]
# print(adict.items(),type(adict.items()))
# lambda匿名函数
# TypeError: '<' not supported between instances of 'str' and 'int'
# [('a', 1), ('b', 2.3), (6, 3), ((1, 2), 5), (3.14, 6), ('f', 6), ('g', 7), ('h', 8)]
# newKeys = sorted(adict.items(),key=lambda x:x[1],reverse=True)
# print(newKeys)
# values = adict.values()
# items = adict.items()
# [8, 7, 6, 6, 5, 3, 2.3, 1]
# newValues = sorted(adict.values(),reverse=True)
# print(newValues)
# 对所有的可迭代对象进行排序，返回一个新的列表对象
# sorted()

# for i in adict:  # adict = adict.keys()
#     print(i)
# for i in adict.values():
#     print(i)

# for i,j in adict.items():
#     print(i,j)

# x = 1
# y = 101
# sum = 0
# for i in range(x, y):
#     if i % 2 == 0:
#         sum += i
# print(sum)

# 水仙花数
# 153 = 1**3 + 5**3 + 3**3
# x = 100
# y = 1000
# for i in range(x,y):
#     # 任何正整数对10取余，都得到它的个位数
#     g = i % 10
#     s = (i // 10) % 10
#     b = (i // 100) % 10
#     if g**3 + s**3 + b**3 == i:
#         print(i)

"""
j: 20
t: 10
30  20*2+10*4


100 300

1.穷举谁  先枚举鸡(0 < j <= 100), 再枚举兔子(0 < t <= 100)
2.穷举循环
3.约束条件
4.求解
"""
# tou = int(input("请输入头数:"))
# jiao = int(input("请输入脚数:"))
# for i in range(0,tou + 1):# 先枚举鸡i
#     for j in range(0,tou + 1):# 再枚举兔子j
#         if i + j == tou and i * 2 + j * 4 == jiao:
#             print(f"鸡:{i},兔子:{j}")

"""
最大连续子序列和
(-2,11,-4,13,-5,-2)
1.穷举谁
2.穷举循环
3.约束条件
    3.1子序列
    3.2连续
    3.3和中的最大值
4.求解
原序列:{-2,11,-4,13,-5,-2}
[-2]
[-2, 11]
[-2, 11, -4]
[-2, 11, -4, 13]
[-2, 11, -4, 13, -5]
[-2, 11, -4, 13, -5, -2]
-------------
[11]
[11, -4]
[11, -4, 13]
[11, -4, 13, -5]
[11, -4, 13, -5, -2]
-------------
[-4]
[-4, 13]
[-4, 13, -5]
[-4, 13, -5, -2]
-------------
[13]
[13, -5]
[13, -5, -2]
-------------
[-5]
[-5, -2]
-------------
[-2]

找到最大连续子序列及它的和
[
    [-2], 
    [-2, 11], 
    [-2, 11, -4],
    [-2, 11, -4, 13], 
    [-2, 11, -4, 13, -5], 
    [-2, 11, -4, 13, -5, -2], 
    [11], 
    [11, -4], 
    [11, -4, 13], 
    [11, -4, 13, -5], 
    [11, -4, 13, -5, -2], 
    [-4], 
    [-4, 13], 
    [-4, 13, -5], 
    [-4, 13, -5, -2], 
    [13], 
    [13, -5], 
    [13, -5, -2], 
    [-5], 
    [-5, -2], 
    [-2]
]
adict = {子序列:和}
adict = {"[-2]":-2,"[-2,11]":9}


{'[-2, 11]': 9, '[-2, 11, -4]': 5, '[-2, 11, -4, 13]': 18, '[-2, 11, -4, 13, -5]': 13, '[-2, 11, -4, 13, -5, -2]': 11, '[11, -4]': 7, '[11, -4, 13]': 20, '[11, -4, 13, -5]': 15, '[11, -4, 13, -5, -2]': 13, '[-4, 13]': 9, '[-4, 13, -5]': 4, '[-4, 13, -5, -2]': 2, '[13, -5]': 8, '[13, -5, -2]': 6, '[-5, -2]': -7, '[-2]': -2}
[('[11, -4, 13]', 20), ('[-2, 11, -4, 13]', 18), ('[11, -4, 13, -5]', 15), ('[-2, 11, -4, 13, -5]', 13), ('[11, -4, 13, -5, -2]', 13), ('[-2, 11, -4, 13, -5, -2]', 11), ('[-2, 11]', 9), ('[-4, 13]', 9), ('[13, -5]', 8), ('[11, -4]', 7), ('[13, -5, -2]', 6), ('[-2, 11, -4]', 5), ('[-4, 13, -5]', 4), ('[-4, 13, -5, -2]', 2), ('[-2]', -2), ('[-5, -2]', -7)]
"""
alist = [-2, 11, -4, 13, -5, -2]
n = len(alist)
result = []
adict = {}
for i in range(0, n):
    # print(alist[i])
    for j in range(i + 1, n + 1):
        adict[str(alist[i:j+1])] = sum(alist[i:j+1])
        # print(alist[i:j+1])
        # print(alist[i:j+1])  # i到j
        # result.append(alist[i:j+1])
    # print("-------------")
anewdict = sorted(adict.items(),key=lambda x:x[1],reverse=True)
print(anewdict[0][1])
# TypeError: 'int' object is not callable
# x = [-2, 11]
# r = sum(x)
# print(r)
'''

'''