data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 # count = count +1
		if count % 1000 == 0:  # 每1000筆
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


new = [] 
for d in data:  # 在1百萬筆資料中
	if len(d) < 100: # 挑出小於 100字元
		new.append(d) 
print('一共有', len(new), '筆留言長度小於 100字元') 
print('-------------')
print('第一筆資料內容, 本文小於100字元') 
print(new[0])  
print('-------------')
print('第二筆資料內容, 本文小於100字元') 
print(new[1])   