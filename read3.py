data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 # count = count +1
		if count % 1000 == 0:
			print('第', len(data), '筆數')  
print('總共留言筆數: ', len(data))  
print('---------------')
# print('第一筆留言內容:')
# print(data[0])
# print('---------------')
# print('第二筆留言內容:')
# print(data[1]) 


sum_len = 0 # 計算留言平均長度
for d in data:
	sum_len = sum_len + len(d) 

print('留言的平均長度是', sum_len/len(data)) 