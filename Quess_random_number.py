import random

start = input('Please enter the started number:')
end = input('Please enter the ended number:')
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0

while True:
	count += 1
	num = input('please quess a number:')
	num = int(num)
	if num == r:
		print('You hit it!')
		print('The number is:', r)
		print('Total you quessed', count, 'times')
		break
	elif num > r:
		print('Your number is bigger than the answer.')
	elif num < r:
		print('Your number is smaller than the answer.')
	print('This is the,', count, 'times you quess')