data = []
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		print(len(data)) #这行的意思是，显示读行的进度 
	    #每行读数据
#因为print很花时间，所以如果要求打印出读到哪一行了，运行到结果的的速度会比较慢
print(len(data))

print(data[0])
print(data[230]) 
print('--------------------')#分隔符
print(data[93])
