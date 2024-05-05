# ch9_7.py
fruits = {'西瓜':15, '香蕉':20, '水蜜桃':25}
print("水果字典:", fruits)
fruit = input("請輸入要刪除的水果 : ")
f = fruits.pop(fruit, "刪除的水果不存在")
print(f"刪除的水果 : {fruit}:{f}")
print(f"新水果字典: {fruits}")

   
