# '''
# 100101 19
# 111010 21
# =
# 011111 40 41

# 000101110高位补零
# 100011010


# 019
# 110


# 异或的结果是默认转化为10进制

# 101001

# 1*2^0 + 0*2^1 + 1*2^2 + 0*2^3 + 0*2^4 + 1*2^5 = 41


# # int()把其他的进制转化为10进制
# # bin()把10进制转化为2进制   0b
# # oct()把10进制转化为8进制   0o
# # hex()把10进制转化为16进制  0x
# '''
# x = '0b101111'
# y = int(x, 2)
# print(y)

# k = '0o51'
# print(int(k, 8))

# print(oct(41))

'''
[
    [a],
    [b],
    [c],
    [d],
    [a,b],
    [a,c],
    [a,d],
    [b,c],
    [b,d],
    [c,d],
    [a,b,c],
    [a,b,d],
    [a,c,d],
    [b,c,d],
    [a,b,c,d],
    [a,c,b,d],
]
'''
def get_permutations(input_str):
    # 避免使用递归,使用迭代
    if len(input_str) == 0:
        return []
    result = [input_str[0]] # 'a'
    # abcd
    for i in range(1, len(input_str)): # 'b'
        current_char = input_str[i] # 'b'
        new_result = [] # 新生成的排列
        # 新来的字母插入到原来的排列中# 遍历原来的每个序列
        for perm in result: # 'a'
            for j in range(len(perm) + 1): # 0 1 2 3
                new_result.append(perm[:j] + current_char + perm[j:]) # 插空
        result = new_result
    return result
# print(get_permutations('xf'))# ['cba', 'bca', 'bac', 'cab', 'acb', 'abc']

def filter_permutations(input_str,min_length = 4): # abcd
    # 所有大于3的排列找出来
    all_perm = get_permutations(input_str)
    # 使用列表的推导式筛选长度大于等于min_length的排列
    long_perms = [per for per in all_perm if len(per) >= min_length]
    # per = []
    # for per in long_perms:
    #     if len(per) >= min_length:
    #         per.append([per])
    # print(long_perms)#['dcba', 'cdba', 'cbda', 'cbad', 'dbca', 'bdca', 'bcda', 'bcad', 'dbac', 'bdac', 'badc', 'bacd', 'dcab', 'cdab', 'cadb', 'cabd', 'dacb', 'adcb', 'acdb', 'acbd', 'dabc', 'adbc', 'abdc', 'abcd']
    # 排重
    union_long_perms = list(set(long_perms)) # 有一种情况不适用---有顺序要求的时候
    return union_long_perms

'''
['dcba', 'cdba', 'cbda', 
'cbad', 'dbca', 'bdca', 
'bcda', 'bcad', 'dbac', 
'bdac', 'badc', 'bacd', 
'dcab', 'cdab', 'cadb', 
'cabd', 'dacb', 'adcb', 
'acdb', 'acbd', 'dabc', 
'adbc', 'abdc', 'abcd']

['cabd', 'acdb', 'cdba', 'abcd', 'adcb', 'cadb', 'acbd', 'bcad', 'cbad', 'adbc', 'cdab', 'bcda', 'dacb', 'badc', 'dabc', 'abdc', 'bdac', 'cbda', 'bdca', 'dcba', 'dcab', 'dbca', 'dbac', 'bacd']
'''

test_string = 'abcd'
result = filter_permutations(test_string)
print(result)
print(f"字符串'{test_string}'中长度大于3的排列有{len(result)}个.")
# 打印所有的结果
for i,perm in enumerate(result): # enumerate枚举,菜单
    print(f"第{i+1}个排列是: {perm}")

far = get_permutations("lqb") # ['bql', 'qbl', 'qlb', 'blq', 'lbq', 'lqb']
print(far)
# 从24个中是否有这6个中的任意一个
