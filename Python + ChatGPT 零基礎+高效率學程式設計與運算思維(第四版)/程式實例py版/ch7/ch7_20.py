# ch7_20.py
scores = [33, 22, 41, 25, 39, 43, 27, 38, 40]
games = 0
for score in scores:
    if score < 30:                  # 小於30則不往下執行
        continue
    games += 1                      # 場次加1              
print(f"有{games}場得分超過30分")


