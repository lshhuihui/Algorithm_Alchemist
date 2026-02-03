'''
((xx|xxx)x|(x|xx))xx
'''
s = input() # ---》xxxxxx
split_roles = ["|", "(", ")", "x"]
split_list = []
each_x_count = []
max_num = 0
for i in split_roles:
    each_list = s.split(i)
    for i in each_list:
        per_x_count = i.count('x')
        if per_x_count > max_num:
            max_num = per_x_count
print(max_num)





# s1 = s.split("|") # ['((xx', 'xxx)x', '(x', 'xx))xx']
# s2 = s.split('(')
# s3 = s.split(')')
# s4 = s.split('x')

# result = []
# for i in range(len(s1)):
#     eachx = s1[i].count('x')
#     result.append(eachx)
#     # print(eachx)
# for i in range(len(s2)):
#     eachx = s2[i].count('x')
#     result.append(eachx)
# for i in range(len(s3)):
#     eachx = s3[i].count('x')
#     result.append(eachx)
# for i in range(len(s4)):
#     eachx = s4[i].count('x')
#     result.append(eachx)

# result.sort(reverse=True)
# print(result[0])