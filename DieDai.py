#演示迭代的用法：

#======
for i, value in enumerate(['A', 'B', 'C']):
    print i, vlaue
#内置函数：enumerate，将list编程‘索引-元素’对
0 A
1 B
2 C

#======
for x, y in [(1,1),(2,4),(3,9)]:
    print x, y
#同时迭代两个数
1 1
2 4
3 9

#======
for value in {'a':'aaa', 'b':'bbb', 'c':'ccc'}.itervalues()
    print value
#将字典按value迭代
aaa
ccc
bbb

#======
for i,value in {'a':'aaa', 'b':'bbb', 'c':'ccc'}.iteritems():
    print i,'-->',value
#同时迭代key，value
a --> aaa
c --> ccc
b --> bbb

#======
a = [1, 2, 3]
b = ['a', 'b', 'c']
for i, j in zip(a,b):
    print i,'-->',j
#并行迭代，zip将两个序列“压缩”在一起，并返回一个元组的列表
1 --> a
2 --> b
3 --> c

