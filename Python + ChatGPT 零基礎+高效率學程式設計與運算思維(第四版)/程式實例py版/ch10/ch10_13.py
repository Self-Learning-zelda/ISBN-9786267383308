# ch10_13.py
# 賦值
numset = {1, 2, 3}
# 拷貝shallow copy
shallow_numset = numset.copy( )
shallow_numset.add(100)
print("拷貝 - 觀察numset        ", numset)
print("拷貝 - 觀察shallow_numset", shallow_numset)

