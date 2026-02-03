'''
i=1
starttime=1
endtime=5
'''
A = [(30,5,6),(11,1,4),(33,0,6)]# 默认是升序的
AS = sorted(A,key=lambda x:x[2])
n = len(AS)
flag = [0] * n # [0,0,0] # 标志位 0表示未选择该活动
k = 0 # 假设了一个不存在的活动
for i in range(n):
    if AS[i][1] > k:#i这个活动是排在k之后的活动，可选
        flag[i] = 1 # 表示当前的i活动被选择了
        k = AS[i][2]
print(flag.count(1))
# 哪些活动被安排了，请输出它们的编号
for i in range(n):
    if flag[i] == 1:# 
        print(AS[i][0])