# ch11_43.py
def fibonacci(n):
    # 定義起始值
    a, b = 0, 1
    # 迴圈計算直到第n項
    for i in range(n):
        a, b = b, a + b
    # 返回第n項的值
    return a

# 輸入要計算的項數
n = int(input("請輸入要計算的項數："))

# 輸出結果
for i in range(n+1):
    print(f"第 {i} 項的值為：{fibonacci(i)}")


