# ch11_39_1.py
str_len = lambda x:len(x)
strs = ['abc', 'ab', 'abcde']
strs.sort(key = str_len)
print(strs)

