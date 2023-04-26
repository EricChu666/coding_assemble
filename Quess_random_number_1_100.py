import random

r = random.randint(1, 100)
count = 0

while True:
	count += 1
	num = input('please quess a number(1-100):')
	num = int(num)
	if num == r:
		print('You hit it!')
		print('The number is:', r)
		break
	elif num > r:
		print('Your number is bigger than the answer.')
	elif num < r:
		print('Your number is smaller than the answer.')
	print('This is the,', count, 'times you quess')