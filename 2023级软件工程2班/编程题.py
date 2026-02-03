'''
-2 11 -4 13 -5 -2
-6 2 4 -7 5 3 2 -1 6 -9 10 -2
10 2 -3 5 6 7 9 10 -20 30 0 6
-3 -4 -2 0 -10 -9 -32
-10 9 10 -3 -28 -33 20 28
'''
alist = list(map(int, input().split()))
n = len(alist)
adict = {}
for i in range(0,n):
    for j in range(i+1,n+1):
        s = sum(alist[i:j])
        if s > 0:
            adict[str(alist[i:j])] = s
        else:
            adict[str(alist[i:j])] = 0
adictList = sorted(adict.items(), key=lambda x:x[1], reverse=True)
print(adictList[0][0])
print(adictList[0][1])


