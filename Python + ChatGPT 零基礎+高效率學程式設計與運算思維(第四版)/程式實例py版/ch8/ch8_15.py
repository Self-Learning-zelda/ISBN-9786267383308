# ch8_15.py
# 計算平均值
vals = (5,6,8,9)
mean = sum(vals) / len(vals)
print(f"平均值 : {mean:5.3f}")

# 計算變異數
var = 0
for v in vals:
    var += ((v - mean)**2)
var = var / (len(vals)-1)
print(f"變異數 : {var:5.3f}")

# 計算標準差
dev = 0
for v in vals:
    dev += ((v - mean)**2)
dev = (dev / (len(vals)-1))**0.5
print(f"標準差 : {dev:5.3f}")





