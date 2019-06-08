str1 = 'hello, world!'
print('lens=:', len(str1))
print('Capital:', str1.title())
print('String Capital: ', str1.upper)

print('if start with hello:', str1.startswith('hello)'))
print('if end with !:',str1.endswith('!'))

str2 = '- \u9a86\u660a'
str3 = str1.title() + ' ' + str2.lower()
print('str3=:', str3)