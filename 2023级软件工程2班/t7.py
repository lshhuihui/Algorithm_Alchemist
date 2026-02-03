class money:
    def __init__(self, moneyType,value, num):
        self.mt = moneyType
        self.v = value
        self.no = num
    def __lt__(self, other):
        return self.v > other.v
    # 贪心算法求零钱问题
    def greedy(self,g,A):
        cnt = 0 #最开始找出去0个硬币
        result = []
        # A // g[0].v  --->A // g[1].v 直到A==0
        for i in range(len(g)):# 从面前的箱子中去遍历钱(从大到小)
            eachCount = A // g[i].v
            result.append((g[i].no,g[i].v,eachCount))
            cnt += eachCount
            A %= g[i].v
        return cnt,result
c = int(input()) # 2
k = int(input()) # 4
A = int(input()) # 23
g = []
for i in range(k):
    print(i)
    values = c ** i
    g.append(money(i+1,values,'a'+str(i+1)))
# m1 = money(1,1,'a')
# m2 = money(2,2,'b')
# m3 = money(3,4,'c')
# m4 = money(4,8,'d')
# g = [m1,m2,m3,m4] # k+1个硬币一定要从大到小
g.sort()
x,y = money(1,2,3).greedy(g,A)
print(x,y)

[16, 12, 8, 5]
[8,  4,  2, 1]
# 到底哪一种硬币找出去多少个？8元找出去2个，4元找了1个。。