strings = 'it is string'

# 문자열 표현 방법-1
print(strings)
print('{0}'.format('it\'s string2'))

# 문자열 표현 방법-2
strings = "double and single quotation marks have the same result"
print(strings)

# 문자열 표현 방법-3
strings = 'Buusan city'
print(strings[0], strings[2])
print(strings[-1], strings[-2], strings[-3])
print(strings[0:5] + strings [-4:-1])