# ch14_17.py
fn = 'test.txt'         # 設定欲開啟的檔案
with open(fn, 'r', encoding='cp950') as fObj:    
    data = fObj.read()      # 讀取檔案到變數data
print(data)                 # 輸出變數data
