import random

answer = random.randint(1,100)
counter = 0

while True:
	counter += 1
	number = int(input("输入： "))
	if number < answer:
		print('bigger')
	elif number > answer:
		print('smaller')
	else:
		print('bingo!')
		break
print('you guessed %d times' % counter)
if counter > 7:
	print('your IQ is low')