x = """a b
c d
e
"""  # str  string
print(x)
y = 10  # int
k = 100.123  # float
print(y * 2)
"""
①print(x)   # 打印x 
②input()    # 输入,凡是input()函数输入的数据,类型都是str
③type(x)    # 打印x的类型
④类型转换, eval()还原  , int(x), float(x), str(x), bool(x)
⑤str有个函数叫split(x),x规则
    19 20 21 18 19 20 变成 ['19', '20', '21', '18', '19', '20']
"""
# m = "10"
# print(2 * m)
# h = input("请输入一个整数:")
# print(type(h))
# print(h * 2)  # 这里的100不是整数,是字符串str


print("a",1,123.444,"hello world")
print("a" + str(1),123.444,"hello world")

# 计算结果是100。
print("计算结果是",100)
print("计算结果是" + str(100))

