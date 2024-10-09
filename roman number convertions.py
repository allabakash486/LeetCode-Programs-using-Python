number = 3749
output = ''
while number != 0:
    if (number//1000):
        output += 'M'*(number//1000)
        number %= 1000
    elif (number //500):
        output += 'D'*(number//500)
        number %= 500
    elif (number //100):
        output += 'C'*(number//100)
        number %= 100
    elif (number //50):
        output += 'L'*(number//50)
        number %= 50
    elif (number //10):
        output += 'X'*(number//10)
        number %= 10
    elif (number //5):
        output += 'V'*(number//5)
        number %= 5
    elif (number //1):
        output += 'I'*(number//1)
        number %= 1
else:
    print(output)

    
    
