x = int(input('x = '))
y = int(input('y = '))
if x > y:
	x, y = y, x
for factor in range(x, 0 ,-1):
	if x % factor == 0 and y % factor == 0:
		print('%d and %d biggest factor%d' %(x, y, factor))
		print('%d and %d smallest factor%d' %(x, y, x*y // factor))
		break