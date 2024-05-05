# ch11_45.py
def recur(i):    
    if (i < 1):            # 檢查是否達到結束條件
        return 0           # 如果 i 小於 1，則終止遞迴
    else:
        recur(i-1)         # 遞迴調用自身，每次將 i 減 1
    print(i, end='\t')     # 打印當前的 i 值，然後加一個水平製表符

recur(5)                   # 調用遞迴函數，從 5 開始
