data = []
count = 0
sum_len = 0
new = []

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
print('Files analysis is complete, the total length is:', len(data))

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

#faster typing: good = [d for d in date if good in d]

print('There are', len(good), 'datas include the word "good."')