country =input('請問你是哪一個國家')
age=input('輸入年齡')
age= int(age)
if country == 'taiwan':
    if age >=18:
        print('you can get the drinving exam')
    else:
        print('you are not allowed to have the exam')
elif country=='america':
    if age >=16:
        print('you can get the drinving exam')
    else:
        print('you are not allowed to have the exam')
