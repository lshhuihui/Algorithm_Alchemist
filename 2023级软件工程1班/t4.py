"""
活动:编号 开始时间 结束时间 以什么策略来选择活动(贪心选择性质)
1 1 4
2 3 5
3 0 6
"""

# actions = [(1,3,5),(2,7,10),(3,0,1)]
# new_actions = sorted(actions,key=lambda x:x[2])
# print(new_actions)
# count = 0
# k = 0 # 上一个被选择的活动的结束时间
# for i in range(len(new_actions)):
#     if new_actions[i][1] >= k: # new_actions[i][1]当前正在被遍历的活动的开始时间
#         count += 1
#         k = new_actions[i][2]
# print(count)


# my_dict = {"name" : "Bob" , "age" : "30" , "city" : "London"}
# nums = {values : key for key , values in my_dict.items()}
# print(nums)

# A = {1,2,3,4,5}
# new_set = set()
# for x in A :
#     if x > 3 :
#         new_set.add(x)
# print(new_set)

# for i in range(1,11) :
# print(i)

# num = 7
# if num <= 1 :
#     print("不是素数")
# elif num % 2 == 0 :
#     print("是素数")
# elif :
#     for num in range(3,n+1) :
#         print("是素数")
# else :
#     is_prime = True
#     for num in range(int(num) for num in (num * 0.5) + 1 , 2)


# num = int(input())

# for i in range(2,num): # 2 - 12  8 % (2-7)
#     if num % i == 0 :
#         print("不是素数")
#         break
# else : # 7 % (2 - 6)  7%2  and 7 % 3 and 7 % 4 and 7 % 5 and 7 % 6
#     print("是素数")


# # 想要找找1024是不是在1-1000的范围内
# for i in range(1,1001):
#     if i == 1024 :
#         print("在")
#         break
# else:# 已经把1-1000都遍历完了，没有找到1024
#     print("不在")


# for i in range(1, 10):
#     if i == 1:
#         print(0)
#     elif i == 2:
#         print(1)
#     else:
#         result = (i - 1) + (i - 2)
#         print(result)



# year == 2024
# if year % 4 == 0 & year % 100 != 0 or year % 400 == 0:
#     print("是闰年")
# else
#     print("不是闰年")


# hello == olleh  abc == cba
# s = 'abc'
# result = ''
# for i in range(2,-1,-1):
#     result += s[i]
# print(result)
# if s == result:
#     print("是回文")
# else:
#     print("不是回文")
# k = "1234567654321" # 对称数字

# 要求你精确到小数点后6位
# import math as m # 3.141592653589793
# r = float(input())
# s = m.pi * r * r
# print(f"{s:.3f}") # format .6f float
# s = round(s,2) # just look around  # 55.417694 round(x,y)是把x保留y位小数(四舍五入)
# print(s) # 84.94866535306801  100991293.231241414  保留原值的小数点后3位

# 集合: 去重/随机 
s = "bcaabc"
new_set = set(s)

print(new_set)
new_list = list(new_set)
print(new_list)
new_list_sort = new_list.sort()
print(new_list)
new_list_sort = sorted(new_list)