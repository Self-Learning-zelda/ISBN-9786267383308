# ch6_23.py
cars = ['Honda','bmw','Toyota','Ford','bmw']     
print(f"目前串列內容 = {cars}")
# 直接列印cars[::-1]顛倒排序,不更改串列內容
print(f"列印使用[::-1]顛倒排序\n{cars[::-1]}")
# 更改串列內容
print("使用reverse( )顛倒排序串列元素")
cars.reverse()            # 顛倒排序串列
print(f"新的串列內容 = {cars}")

    
