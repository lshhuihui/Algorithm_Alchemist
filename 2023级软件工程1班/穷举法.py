"""
水仙花数(三位数)
153 = 1^3 + 5^3 + 3^3
"""


def getS(i, j):  # ①确定穷举遍历 从i穷举到j
    for k in range(i, j):  # ②构造穷举循环
        # ③约束条件:个十百位的3次方的和等于本身
        # 153怎么得到1/5/3
        # 任何正整数对10取余都得到它的个位数
        g = k % 10
        s = k // 10 % 10
        b = k // 100 % 10
        # ④求解
        if g**3 + s**3 + b**3 == k:
            print(k)


# getS(100,1000)


# print(153%10)
# print(662%10)
# print(231%10)
# print(7%10)
# print(-2%10)
# print(0%10)
# print(10%10)
# print(int(15.3%10))

"""
a个头,b个腿

x表示鸡,y表示兔子


a = x + y
b = 2*x + 4*y

假设0~x先是鸡,然后0~y才是兔子
"""

# ①穷举变量x,y
# ②构造穷举循环
# for i in range(0,a+1):# 外层循环,先枚举鸡
#     # 再枚举兔子
#     for j in range(0,a+1):
#         if i + j == a and 2*i + 4*j == b:
#             print(f"鸡:{i},兔子:{j}")
# ③约束条件:a个头,b个腿
# a = x + y
# b = 2*x + 4*y
# ④求解


def getSum(a, b):  # a 个头, b 个腿
    for x in range(0, a + 1):  # 外层循环,枚举鸡
        for y in range(0, a + 1):
            if x + y == a and 2 * x + 4 * y == b:
                print(f"鸡:{x},兔子:{y}")


# 50j 50t
# getSum(50000,150000)

"""
最大连续子序列和

约束条件:
1.子序列
2.连续的
3.和最大的


nums = [-2,11,-4,13,-5,-2]
        i  j
        
k = -2
k = -2 11 
k = -2 11 -4
k = -2 11 -4 13
k = -2 11 -4 13 -5
k = -2 11 -4 13 -5 -2

subList = [
(-2),
(-2,11),
(-2, 11 ,-4)
'
'
'
(11),
(11,-4)
'
'
(-4),
(-4,13)
.
.
]
①穷举谁 nums
②构造穷举循环
③约束条件

朴素的算法思想:
逻辑思维:
1.思考的方向
2.思考的步骤
3.思考的策略

算法:
把握数据的变化:测试



"""


def getMaxSum(nums):# nums = [-2,11,-4,13,-5,-2]
    n = len(nums)
    result = []
    # maxI = 0
    for i in range(0, n):
        # print(nums[i])
        for j in range(i + 1, n + 1):
            # print(nums[i:j])
            result.append(nums[i:j])
            # if maxI < sum(nums[i:j]):
            #     maxI = sum(nums[i:j]) 
        print("-----------------")
    print(result)
    '''
    adict = {"序列本身":序列和}
    adcit = {"[-2]":-2,"[-2, 11]":9,"[-2, 11, -4]":3,"[-2, 11, -4, 13]":16,"[-2, 11, -4, 13, -5]":10,"[-2, 11, -4, 13, -5, -2]":-2}
    '''
    adict = {}
    for i in result:
        adict[str(i)] = sum(i) # key:i的字符串形式,value:i的和 {key:value}构成字典
    print(adict)
    print(max(adict.values()))
    anewdict = sorted(adict.items(),key=lambda x:x[1],reverse=True) # 排完序后返回一个新的列表
    print(anewdict)
    print(anewdict[0]) # ('[11, -4, 13]', 20) ('[-2, 11, -4, 13]', 18)
    print(anewdict[0][1]) # 20 
    sums = []
    for i in range(0, len(result)):
        sums.append(sum(result[i]))
    print(sums)
    print(max(sums))

nums = [-2, 11, -4, 13, -5, -2]
getMaxSum(nums)



