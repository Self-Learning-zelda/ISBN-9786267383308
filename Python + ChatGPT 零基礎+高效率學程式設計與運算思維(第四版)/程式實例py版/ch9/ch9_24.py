# ch9_24.py
# 創建一個包含鍵列表的變數
keys = ['apple', 'banana', 'orange']
# 使用 fromkeys() 創建一個新的字典my_dict1
my_dict1 = dict.fromkeys(keys)
print(my_dict1)
# 使用 fromkeys() 創建一個新的字典my_dict2
my_dict2 = dict.fromkeys(keys, 0)
print(my_dict2)
