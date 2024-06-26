# ch15_5.py
def wordsNum(fn):
    """適用英文文件, 輸入文章的檔案名稱,可以計算此文章的字數"""
    try:
        with open(fn) as file_Obj:  # 用預設mode=r開啟檔案
            data = file_Obj.read()  # 讀取檔案到變數data
    except FileNotFoundError:
        print(f"找不到 {fn} 檔案")
    else:
        wordList = data.split()     # 將文章轉成串列
        print(f"{fn} 文章的字數是 {len(wordList)}")   # 文章字數

file = 'data15_5.txt'               # 設定欲開啟的檔案
wordsNum(file)



