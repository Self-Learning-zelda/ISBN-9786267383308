# ch14_18.py
fn = 'test.txt'         # 設定欲開啟的檔案
with open(fn, 'r') as fObj:    
    data = fObj.read()      # 讀取檔案到變數data
print(data)                 # 輸出變數data
