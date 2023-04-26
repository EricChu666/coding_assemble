data = []
count = 0
sum_len = 0

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
print('Files analysis is complete, the total length is:', len(data))

for d in data:
	sum_len = sum_len + len(d)
print('The average length of the data is:', sum_len/len(data))