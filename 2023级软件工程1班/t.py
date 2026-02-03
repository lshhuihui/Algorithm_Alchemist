class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort() # 胃口
        s.sort() # 饼干尺寸
        i, j = 0, 0
        ans = 0 # 被满足的孩子的数量
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:# 把j这块饼干发给i这个孩子
                i = i + 1
                ans = ans + 1
            j = j + 1  # 遍历其他饼干试图去满足孩子i的胃口
        return ans
'''
g: 1 2 3 4 5 6 7 8 9 10
i: 0 1 2 3 4 5 6 7 8 9

s: 2 3 4 5 6 7 8 9 10 11
j: 0 1 2 3 4 5 6 7 8 9
'''



def fcc(g,s):
    g.sort()
    s.sort()
    for i in range(len(g)):
        for j in range(len(s)):
            if g[i] <= s[j]:
                s.pop(j)
                break
    return len(g) - len(s)




def s():
    sum = 0 
    for i in range(1,101):
        sum += i
    return sum

    for j in range(1,101):
        sum *= j
    return sum



'''
A 14:00 14:15
B 1:00  5:00
C 17:00 19:00

'''