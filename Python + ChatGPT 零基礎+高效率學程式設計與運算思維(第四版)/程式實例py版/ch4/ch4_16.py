# ch4_16.py
print("歡迎使用成績輸入系統")
name = input("請輸入姓名：")
engh = input("請輸入英文成績：")
math = input("請輸入數學成績：")
total = int(engh) + int(math)
print(f"{name} 你的總分是 {total}")
print("="*60)
print(f"name資料型態是 {type(name)}")
print(f"engh資料型態是 {type(engh)}")

