# ch19_2.py
import csv

fn = 'csvReport.csv'
with open(fn,encoding='utf-8') as csvFile:  # 開啟csv檔案
    csvReader = csv.reader(csvFile)     # 建立Reader物件
    listReport = list(csvReader)        # 將資料轉成串列    

print(listReport[0][1], listReport[0][2])
print(listReport[1][2], listReport[1][5])
print(listReport[2][3], listReport[2][6])



