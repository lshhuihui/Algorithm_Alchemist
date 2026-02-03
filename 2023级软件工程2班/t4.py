# public class Person extends Animal implements Cats,Kings(Interface){ # 单继承,多实现
# public 公开
# private 私有
# protected 保护,同包
# 继承/封装/多态
# 子承父业(公开的)

# python:
# package === model 
# default 默认
# private 私有
#     # 构造方法/函数 -- 天生自带的属性或方法的
#     public void Person(){


#     }
#     public void Person(String name){
#         this.name = name;
#     }


# }

class Actions():
    # 不定长参数
    def __init__(self,argments):
        self.id = argments[0]
        self.beginTime = argments[1]
        self.endTime = argments[2]

    def s(self,alist):
        n = len(alist)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if alist[j] > alist[j + 1]:
                    alist[j],alist[j + 1] = alist[j + 1],alist[j]
        return alist
k = [2,6,4]
p = Actions(k)
print(p.id)
# 如果要判断活动开始时间大于结束时间
if p.beginTime > p.endTime:
    print("开始时间大于结束时间")
m = [2,5,1,2,3,232,11,123,123]
blist = p.s(m)
print(blist)