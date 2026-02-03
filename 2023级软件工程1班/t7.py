# 类
class Goods:
    def __init__(self,w,v):
        self.w = w
        self.v = v
    def __lt__(self,other):
        return 1.0 * self.v / self.w < 1.0 * other.v / other.w  
# 4个对象
g1 = Goods(2,3)
g2 = Goods(4,3)
g3 = Goods(2,3)
g4 = Goods(6,4)
# 对象列表
g = [g1,g2,g3,g4]
def greedly(g,W):# W背包的总容量,一开始的时候等于剩余容量,g代表对象列表 -- 贪心算法求背包问题的解
    global x,bestv
    n = len(g)
    x = [0] * n # 标志位
    g.sort() # 要能进行sort,对象中必须要实现__lt__方法
    bestv = 0
    i = 0 # 虚拟的,假想的第一个物品
    rw = W
    while i < n and g[i].w < rw:
        x[i] = 1 # ①刚刚虚拟的指向的第一个物品被选择(一定是最优选择)
        rw -= g[i].w # ②更新背包的剩余容量
        bestv += g[i].v # ③更新背包的价值
        i += 1
    if i <n and rw > 0:
        x[i] = rw / g[i].w # ④更新虚拟的第一个物品的选择数量
        bestv += rw * g[i].v / g[i].w # ⑤更新背包的价值
    return bestv
result = greedly(g,10)
print(result)