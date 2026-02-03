text = 'Python is a great language,Python is easy to learn,Python is powerful,but you should to pracitice every day'
new_test = text.lower().replace(','," ")
print(new_test)
tlist = new_test.split(" ")
print(tlist)
cntmap = {}
for word in tlist:
    # if word in cntmap:
    #     cntmap[word] += 1
    # else:
    #     cntmap[word] = 1
    cntmap[word] = cntmap.get(word,0) + 1
    
print(cntmap)