# ch14_4.py
fn = 'data14_2.txt'         # 設定欲開啟的檔案
with open(fn, 'r', encoding='cp950') as fObj:    
    for line in fObj:       # 相當於逐列讀取
        print(line)         # 輸出line
