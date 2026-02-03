'''
g:5 6 8 9 10 12

s:4 6 9 10 12 14

输入样例：
    5 6 8 9 10 12
    4 6 9 10 12 14
输出样例：
    5
'''
g = list(map(int, input().split()))# 孩子的胃口
# 定义一个指针i,分别用来指向孩子的胃口
i = 0
s= list(map(int, input().split())) # 饼干的尺寸
j = 0 # 指向饼干
cnt = 0
while i < len(g) and j < len(s):
    if g[i] <= s[j]: # 孩子被满足
        i += 1 # 指向下一个孩子
        cnt += 1
    j += 1 # 指向下一个饼干
print(cnt)

'''
beginTime  endTime
0   1   [0,1]
2   4   (2,4)
3   5   (3,5)
actions = [(0,7),(2,4),(3,5)]
'''
actions = [(0,7),(2,3),(3,5)]
# x[1]结束时间
actions_sort = sorted(actions, key=lambda x:x[1])
print(actions_sort)
n = len(actions_sort)
# 所以你得定义上一个活动的结束时间
k = 0
count = 0
for i in range(n):
    # print(actions_sort[i][1]) # (0,7)
    if actions_sort[i][0] >= k: 
        count += 1
        k = actions_sort[i][1] # 更新结束时间
print(count)

'''
分治算法:排列 - 最大连续子序列
活动安排:组合
1.最多有多少个活动被安排?它们是哪些呢?
2.如何提升资源的利用率?
3.到底哪些活动被安排是最恰当的?

到底哪些活动被安排了,是否是最优秀方案?
where id = ?
(id,b,e)
actions = [(11,3,5),(8,1,2),(9,3,7)]  # 矩阵/邻接矩阵
another_way = {"11":(3,5),"8":(1,2),"9":(3,7)} # 邻接表
第一行输入一个n,表示有n个活动(1 <= n << 30000)
下面n就是这些活动的参数,分别是编号、开始时间、结束时间

输入样例:
3
11 3 5
8 1 2
9 3 7
输出样例:
    2

another_way = {"11":(3,5),"8":(1,2),"9":(3,7)}
'''
n = int(input())
another_way = {} # 使用花括号时,内部没有数据,他就是字典,我想要一个空的集合 set()
# print(another_way,type(another_way))
for i in range(n):
    eachLine = list(map(int, input().split()))
    another_way[eachLine[0]] = (eachLine[1],eachLine[2])
# print(another_way)
sort_another_way = sorted(another_way.items(), key=lambda x:x[1][1])
# 是否需要下标参与运算
# for i in another_way:# 直接就取值
k = 0 # 虚拟的最开始被选择的活动的结束时间
flag = [8] * n
for i in range(n): # 先遍历下标,再用下标去取值
    '''
    (8, (1, 2))
    (11, (3, 5))
    (9, (3, 7))
    '''
    # print(sort_another_way[i][1][0])
    if sort_another_way[i][1][0] >= k:
        flag[i] = 9
        k = sort_another_way[i][1][1]
print(flag,flag.count(9)) 



# n = int(input())
# actions = []
# for i in range(n):
#     eachLine = tuple(map(int, input().split()))
#     # print(eachLine)
#     actions.append(eachLine)
# print(actions)
# # IPO  I=input P=process O=output 
# sorted_actions = sorted(actions, key=lambda x:x[2])
# print(sorted_actions)
# fronSelectedActionEndTime = 0 # 虚拟的最开始被选择的活动的结束时间
# table = [0] * n # 相当于每个活动头上都标记一个0
# for i in range(n):
#     # 要检查当前正在遍历的活动sorted_actions[i]它的开始时间是否大于等于上一个被选择的活动的结束时间
#     if sorted_actions[i][1] >= fronSelectedActionEndTime:
#         # i活动被选择了
#         table[i] = 1 #头上的标记修改为1
#         fronSelectedActionEndTime = sorted_actions[i][2]
# # 当循环结束,说明所有活动都被遍历完成了
# print(table)
# for i in range(n):
#     if table[i] == 1:
#         print("被选择的活动的编号是:",sorted_actions[i][0],end=" ")