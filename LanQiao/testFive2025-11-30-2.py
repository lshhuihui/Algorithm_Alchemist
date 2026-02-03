"""
3 4 5

QQQ
QQQ
QQQ
QQQ
QQQQQQQQ
QQQQQQQQ
QQQQQQQQ
"""

# w, h, v = map(int, input().split())
# for _ in range(h):
#     print("Q" * w)
# for _ in range(w):
#     print("Q" * (v + w))


# s = 'abc'
# print(s[::-1])

# s1 = list(s)
# s1.reverse() # 翻转列表的，不能翻转字符串
# print(''.join(s1))

# words.txt

words = []
with open('/workspace/LanQiao/words.txt', 'r') as f: # r(read) 只读, w(write)写,a(append)追加,e(execute)执行
    for line in f:
        word = line.strip() # 去除换行符
        if word: # word != None
            words.append(word)
print(words) # ['b', 'bc', 'cbd', 'dbca']

r = False
beautiful_words = []
for i in words:
    if len(i) == 1:
        beautiful_words.append(i)
        r = True
    i_1 = i[0:len(i)-1:1]
    print(i_1)
    if i_1 in words and i_1 in beautiful_words: # 截取n-1后的字符串在words中出现过 and 还得是优美字符串
        r = True
if r:print('yes')
else:('no')


# s1 = 'b'
# k = "dbca"
# k_1 = k[0:len(k)-1:1]
# if s1 in words:
#     print('yes')

# def beautiful_word(s):# 正反是不是一样
#     if len(s) == 1:
#         return True
#     elif s == s[::-1]:
#         return True
#     else:
#         return False
# print(beautiful_word('abcba'))
allx = [15,10,7,5,2] # 排序
# 当x满足题目给的条件时就选x
for i in range(2025,0,-x):# 当血量低于1
    pass