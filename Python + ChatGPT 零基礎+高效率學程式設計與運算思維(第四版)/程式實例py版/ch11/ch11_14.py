# ch11_14.py
def product_msg(customers):
    str1 = '親愛的: '
    str2 = '本公司將在2023年12月20日夏威夷舉行產品發表會'
    str3 = '總經理:深智公司敬上'
    for customer in customers:
        msg = str1 + customer + '\n' + str2 + '\n' + str3
        print(msg, '\n')

members = ['Damon', 'Peter', 'Mary']
product_msg(members)


