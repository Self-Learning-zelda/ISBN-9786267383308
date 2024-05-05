# ch14_1.py
fstream1 = open("out14_1w.txt", mode="w") # 取代先前資料
print("Testing for output", file=fstream1)
fstream1.close( )
fstream2 = open("out14_1a.txt", mode="a") # 附加資料後面
print("Testing for output", file=fstream2)
fstream2.close( )
