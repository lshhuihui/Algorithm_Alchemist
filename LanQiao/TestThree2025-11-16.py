'''
5
1 2 3 4 5

3 5
1 2 8


2
3
4

IPO = input Precess Output



1 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 1 0 0 0
0 0 1 1 0 0
0 0 1 1 1 1


'''
# Scancer inf = new Scancer(System.in);
# inf.nextFloat();
# x = int(input()) # str
# y = eval(input()) # 还原
# z = float(input())
# print(x,y,z,type(x),type(y),type(z) )


# 一行就要带n个数，每个之间用空格或者逗号隔开 3:8:10
# x = input()
# '''
# # split(t)  
# # ①t表示拆分规则 
# # ②拆完之后给你一个新的列表['3', '5'] 
# # ③内部元素的类型要关注
# '''
# y = x.split(":") 
# # print(y)

# k = []
# for i in y:
#     k.append(int(i))

# print(k) # [3, 7, 9]


# result = list(map(float,input().split(" ")))
# print(result)#[3.144, 9.11, 1.2]


x,y = list(map(int,input().split(" ")))
# print(x)#[3.144, 9.11, 1.2]
k = list(map(int,input().split(" ")))
print(k)