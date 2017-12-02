x = ['a', 'b', 'c', 'd']
y = ['b', 'c']
x_new = []
for i in x:
    if i not in y:
        x_new.append(i)
x = x_new
print (x)

'''
#x已经不是原来的x了，但x的分片还是x的分片
for i in x[:]:
    if i in y:
        idx = x.index(i)
        x.pop(idx)
'''
