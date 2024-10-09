S = '0123'
try:
    sub = ''
    for i in S:
        if i=='-' or i == '0':
            continue
        if i.isdigit():
            sub += i
        else:
            break
    print(sub)
finally:
    print('Executed successfully..!')
