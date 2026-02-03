"""活动安排:
no:1
beginTime 2023-01-01 00:00:00
endTime 2023-01-01 00:00:00
Action
"""


class Action:
    def __init__(self, number, beginTime, endTime):
        self.no = number
        self.bt = beginTime
        self.et = endTime
    # 按结束时间排序,我自己与别的活动按结束时间可以比较出来True或者False
    # 在对象中, __lt__方法表示小于,__gt__()方法表示大于,__eq__()方法表示等于 equals
    def __lt__(self, other):
        return self.et < other.et
    
    # 贪心算法实现活动安排,单个对象,对象列表
    def ArrangeActivities(self,al):
        ArrangeActivitiesList = []
        cnt = 0
        minBt = 0
        # 活动遍历出来
        for i in al:
            if i.bt >= minBt:
                ArrangeActivitiesList.append(i)
                cnt += 1
                minBt = i.et
        return ArrangeActivitiesList,cnt

a = Action(1, 1, 4)
b = Action(2, 3, 5)
c = Action(3, 2, 11)
d = Action(4, 5, 8)
actionsList = [a,b,c,d] # [Action(1,1,4),Action(2,3,5),Action(3,2,11),Action(4,5,8)]

actionsList.sort() # 贪心
acList,count = a.ArrangeActivities(actionsList)
print(acList,count)
for i in acList:
    print(i.no,i.bt,i.et)


# 对象排序方法一
# actionsList.sort() # 想要使用对象列表的sort方法,想要使用sort对一个列表中的对象进行排序,必须实现__lt__()方法
# print(actionsList)
# for i in actionsList:
#     print(i.no,i.bt,i.et)

# 对象排序方法二
# sorted(接受一个可迭代的对象)
# actionsListSort = sorted(actionsList,key=lambda x:x.et)
# for i in range(len(actionsListSort)):
#     print(actionsListSort[i].et)


# # 贪心算法实现活动安排,单个对象,对象列表
# def test(al):
#     ArrangeActivitiesList = []
#     cnt = 0
#     minBt = 0
#     # 活动遍历出来
#     for i in al:
#         if i.bt >= minBt:
#             ArrangeActivitiesList.append(i)
#             cnt += 1
#             minBt = i.et
#     return ArrangeActivitiesList,cnt

# testResult = test(actionsList)
# print(testResult)