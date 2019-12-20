data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 # 等于 count = count +1
		if count % 10000  == 0: # count 除以 1000的余数是多少
			print (len(data))

print('档案读取完了，总共有', len(data), '笔资料')

sum_len = 0
for d in data: #每笔资料命名为d，每个d是一个字串
	sum_len += len(d) #每笔留言的长度和现在的留言长度加在一起，然后存入目前的总数

print('留言的平均长度为', sum_len/len(data), '个字') #总长度除以数据条数

#计算出，有多少笔留言字数小于100（筛选）
#写for loop 筛选数据
new = []
for d in data:
	if len(d) < 100:
		new.append(d) #把d的这个留言装入new清单里
print('一共有',len(new),'笔留言长度小于100')
print(new[0])
print(new[19820])

#提取关键词留言
good = []
for d in data: # d称呼每笔留言的变数名称
	if 'good' in d:
		good.append(d)
print('一共有',len(good),'笔留言提到good')
print(good[758])
