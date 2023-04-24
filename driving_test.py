driving = input('Did you ever drive?')
if driving != 'yes' and driving != 'no':
	print('You are supposed to enter "yes" or "no."')
	raise SystemExit

age = input('How old are you?')
age = int(age)
if driving == 'yes':
	if age >= 18:
		print('Yes sure, you must be a good driver!')
	else:
		print('Well, something is wrong, isnt it?')
elif driving == 'no':
	if age >= 18:
		print('You can try another way to commute, like driving a car!')
	else:
		print('Good, you will be able to drive in a few years.')