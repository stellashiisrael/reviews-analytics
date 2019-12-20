data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 # 等于 count = count +1
		if count % 1000 == 0: # count 除以 1000的余数是多少
			print (len(data))

print(len(data))

print(data[0])
print(data[230]) 
print('--------------------')#分隔符
print(data[93])
