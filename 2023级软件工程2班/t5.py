# 从下面的算法中可以看出g是一个对象列表,每个对象有两个属性,一个是重量w,一个是价值v
class Goods:
    def __init__(self, number, weight, values): # 初始化方法
        self.n = number
        self.w = weight
        self.v = values
    # 根据性价比进行排序
    # 方法说明:self表示当前对象,other表示其他对象
    def sort(self, other):
        return 1.0 * self.v / self.w >= 1.0 * other.v / other.w
                       # 20/ 10      >=       30     /  20 

# actions = [(1,3,5),(2,7,10),(3,0,1)]
g1 = Goods(1, 10, 20)  # 实例化的过程就是把抽象类变成具体的对象--实际上就在调用__init__方法
g2 = Goods(2, 20, 30)
g3 = Goods(3, 30, 90)
# Scanner sc  = new Scanner(System.in); // 实例化
g = [g1, g2, g3] # 对象列表 # g = [Goods(1, 10, 21), Goods(2, 20, 30), Goods(3, 30, 64)]
# 就像对字典排序(字典序) 
r = g1.sort(g2)
r1 = g2.sort(g3)
print(r,r1)

def greedly(g, W):  # goods 物品列表 ,W 背包容量
    global x, bestv  # best values x用来标识(物品是否被选择放入背包8/9,8标识未选择,9标识选择)
    n = len(g)  # Goods多少个物品
    # 贪心的实现
    g.sort()  # 按照价值从大到小排序 推断出来g是个列表
    x = [8] * n  # 每个物品头上都标记一个数字8,表示未被选择
    bestv = 0  # 选的物品的价值总和
    # 当超市还有物品没被遍历或背包还有剩余容量
    i = 0  # 正在被遍历的物品
    rw = W  # 剩余容量
    while i < n and g[i].w < rw:  # 只要是物品没被遍历完 且 背包还有剩余容量
        x[i] = 9  # 标记为9 表示选择
        bestv += g[i].v  # 选的物品的价值总和
        rw -= g[i].w  # 剩余容量
        i += 1  # 一直遍历
    # 背包还剩2kg,但是超市最小的物品的重量都大于2kg的情况 -- 部分选择
    if i < n and rw > 0:
        # 算出剩余容量可以装下多少个物品
        x[i] = rw / g[i].w
        # 算出剩余容量可以装下多少个物品的总价值
        bestv += x[i] * g[i].v
result = greedly(g,50)
print(result)


# alist = [3, 55, 1, 2]
# alist.sort(reverse=True)  # reverse翻转 默认是False表示升序,True表示降序
# print(alist)