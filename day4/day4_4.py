from math import sqrt

num = int(input('positive int:'))
end = int(sqrt(num))
is_prime = True
for x in range(2, end+1):
	if num % x == 0:
		is_prime = False
		break
if is_prime and num != 1:
	print('%d is prime' % num)
else:
	print('%d is not prime' %num)