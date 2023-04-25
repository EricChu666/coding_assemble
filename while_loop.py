password = 'a123456'
times = 3

while times >= 0:
	enter = input('please enter the password:')
	if enter == password:
		print('Success! Welcome!')
		break
	else:
		times = times - 1
		if times == 0:
			print('You have tried over three times!')
			raise SystemExit
		else:
			print('The password is wrong, please try again.')
			print('You have', times, 'times')
