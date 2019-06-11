password = input('口令')
username = input('输入用户名')
import getpass
password = getpass.getpass('口令：')

if usename == 'admin' and password == '123456':
	print('chenggong')
else:
	print('fail')