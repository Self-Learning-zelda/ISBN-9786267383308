# ch19_5.py
import csv

fn = 'out19_5.csv'
with open(fn,'w',newline='') as csvFile:  # 開啟csv檔案
    csvWriter = csv.writer(csvFile)       # 建立Writer物件   
    csvWriter.writerow(['姓名', '年齡', '城市'])
    csvWriter.writerow(['Hung', '35', 'Taipei'])
    csvWriter.writerow(['James', '40', 'Chicago'])


