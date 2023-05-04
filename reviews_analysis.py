data = []
count = 0
sum_len = 0
new = []
wc = {}	#word_count

for d in data:
	if len(d) < 100:
		new.append(d)
	sum_len = sum_len + len(d)

print('The average length of the data is:', sum_len/len(data))
print('There are', len(new), 'datas which length is under 100.')

good = []
for d in data:
	if 'good' in d:
		good.append(d)

faster typing: good   =   [d   for   d	 in   date   if good in d]
#			   output	 運算	   變數		 清單	篩選條件

print('There are', len(good), 'datas include the word "good."')

bad = ['bad' in d for d in data]
print(bad)
bad = []
for d in data:
	bad.append('bad' in d)

#文字計數

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
	print('Files analysis is complete, the total length is:', len(data))

	for d in data:
		words = d.strip().split()
		for word in words:
			if word in wc:
				wc[word] += 1
			else:
				wc[word] = 1


while True:
	word = input('請輸入你想要查找的字: ')
	if word == 'q':
		break
	if word in wc:
		print(word, '的出現次數為:', wc[word], '次')
	else:
		print('這個字沒有出現過喔!')
print('感謝你使用查找功能。')



