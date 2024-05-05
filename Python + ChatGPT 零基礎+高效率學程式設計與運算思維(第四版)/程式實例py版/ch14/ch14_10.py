# ch14_10.py
fn = 'out14_10.txt'
string = 'I love Python.'

with open(fn, 'w', encoding='cp950') as fObj:
    print(fObj.write(string))        
