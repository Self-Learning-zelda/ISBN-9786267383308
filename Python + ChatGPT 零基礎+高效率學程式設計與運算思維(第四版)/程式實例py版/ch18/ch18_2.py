# ch18_2.py
from wordcloud import WordCloud

with open("data18_2.txt") as fp:    # 含中文的文字檔
    txt = fp.read()                 # 讀取檔案
    
wd = WordCloud().generate(txt)      # 由txt文字產生WordCloud物件
imageCloud = wd.to_image()          # 由WordCloud物件建立詞雲影像檔      
imageCloud.show()                   # 顯示詞雲影像檔








