def phn_number():
    digit = int(input('Enter the digits:'))
    first_digit = (digit%100)
    secon_digit = (digit%10)
    char_2 = ['a','b','c']
    char_3 = ['d','e','f']
    char_4 = ['g','h','i']
    char_5 = ['j','k','l']
    char_6 = ['m','n','o']
    char_7 = ['p','q','r','s']
    char_8 = ['t','u','v']
    char_9 = ['w','x','y','z']
    if first_digit ==2:
        a = char_2
        
    elif first_digit ==3:
        a = char_3
        
    elif first_digit ==4:
        a = char_4
        
    elif first_digit ==5:
        a = char_5
       
    elif first_digit ==6:
        a = char_6
        
    elif first_digit ==7:
        a = char_7
        
    elif first_digit ==8:
        a = char_8
        
    elif first_digit ==9:
        a = char_9
        
    if secon_digit ==2:
        b =char_2
        
    elif secon_digit ==3:
        b = char_3
        
    elif secon_digit ==4:
        b = char_4
        
    elif secon_digit ==5:
        b = char_5
        
    elif secon_digit ==6:
        b = char_6
        
    elif secon_digit ==7:
        b = char_7
        
    elif secon_digit ==8:
        b = char_8
        
    elif secon_digit ==9:
        b = char_9
        
    output =[]
    for i in range(len(a)):
        for j in range(len(b)):
            output.append(a[i]+b[j])
    print(output)
phn_number()
    
    
