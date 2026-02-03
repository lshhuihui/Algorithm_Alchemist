'''
输入样例:
2
3
输出样例:
5

输入样例:
3
6
输出:
9


输入样例:
19 20 21 18 19 20
19,20,21,18,19,20
输出年龄总和:
100
'''

s = input("请输入一行数据,空格隔开:") 
# s是字符串str , str有个函数叫split(x),x规则   拆分,拆分规则
s1 = s.split(",") # 以空格拆分 ,拆出来后是一个列表list  ['19', '20', '21', '18', '19', '20']
print(s)
print(s1)

s1  = ['19', '20', '21', '18', '19', '20'] # [19, 20,21]
s3 = [int(i) for i in s1]
print(s3)


s2 = []
for i in range(len(s1)):    
    s2.append(int(s1[i]))
print(s2)
print(sum(s2))


# x = input("请输入一个整数:")
# y = input("请输入一个整数:")
# x1 = eval(x) # str >> int   str >> float
# y1 = eval(y) # str >> int

# z  = x1 + y1 
# print(z)


