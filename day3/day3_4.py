from random import randint

face = randint(1,6)
if face == 1:
	result = 'sing'
elif face == 2:
	result = 'dance'
else:
	result = 'laugh'
print(result)