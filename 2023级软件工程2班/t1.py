"""
我有一个圆的半径radius,当这个半径为正数时,
求出1至radius的每一个半径构成的面积以及它们的和。
"""

# radius = int(input())
# if radius > 0:
#     sum = 0
#     for i in range(1, radius + 1):
#         area = i * i * 3.14
#         print(area)
#         sum += area
#     print(sum)
# 给我一个半径，我得求1-r的每一个面积，以及它们的和
# def f(radius,totalsum):
#     if radius > 0:
#         persum = 3.14 * radius * radius
#         print(persum)
#         totalsum *= persum
#         f(radius - 1,totalsum)
#     print(totalsum)
# f(3,1)



# def f(radius):
#     totalsum = []
#     eachsum = 1
#     if radius > 0:
#         persum = 3.14 * radius * radius
#         print(persum)
#         f(radius - 1)
#         eachsum *= persum
#     totalsum.append(eachsum)
#     print(totalsum)
# f(3)


# 递归
def f(radius):
    pi = 3.14
    # 返回当前的半径的面积和当前的半径构成的面积和
    if radius == 1: # 出口
        area = pi * 1 * 1
        return [area],area
    sub_areas,sub_total = f(radius - 1)
    # x,y = map(int,int(input().split()))
    current_area = pi * radius * radius
    new_areas = sub_areas + [current_area]
    new_total = sub_total + current_area
    return new_areas,new_total
# x,y = f(3)
# print(x)
# print(y)

# 迭代法
def k(radius):
    area_list = []
    total = 0
    pi = 3.14
    for r in range(1,radius + 1):
        perarea = pi * r ** 2 
        area_list.append(perarea)
        total += perarea
    return area_list,total

r = int(input())
if r > 0:
    x,y = k(r)
else:
    print('sorry,error')
print(x)
print(y)

# v = pow(r,10) # x power y 