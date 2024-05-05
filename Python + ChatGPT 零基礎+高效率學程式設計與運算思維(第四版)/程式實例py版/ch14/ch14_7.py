# ch14_7.py
fn = 'data14_7.txt'         # 設定欲開啟的檔案
with open(fn, 'r', encoding='cp950') as fObj:    
    mylist = fObj.readlines()
print(mylist)       
