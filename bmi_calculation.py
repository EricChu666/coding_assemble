height = input('請輸入身高(m):')
height = float(height)
weight = input('請輸入體重(kg):')
weight = float(weight)
bmi = weight / (height * height)
if bmi < 18.5:
	print('你的bmi是:', bmi,)
	print('屬於體重過輕,多吃一點喔')
elif bmi >= 18.5 and bmi < 24:
	print('你的bmi是:', bmi,)
	print('你的bmi正常, 恭喜!')
elif bmi >= 24 and bmi < 27:
	print('你的bmi是:', bmi,)
	print('你是過重')
elif bmi >= 27 and bmi < 30:
	print('你的bmi是:', bmi,)
	print('你是輕度肥胖')
elif bmi >= 30 and bmi < 35:
	print('你的bmi是:', bmi,)
	print('你是中度肥胖')
else: 
	print('你的bmi是:', bmi,)
	print('你是重度肥胖')