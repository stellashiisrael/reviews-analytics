data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f: #for loop：把清单中的东西一个一个拿出来
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

#提取关键词留言 快写法（list comprehension)
# output = [(number - 1) for number in reference if number % 2== 0]
                #符合条件后    变数        清单          筛选条件   
                #将这个装进output里     
good = [d for d in data if 'good' in d]
#good = [d + '123' for d in data if 'good' in d]
#如果留言中有good，输出时，每隔留言后面加上123

print('一共有',len(good),'笔留言提到good')
print(good[758])
