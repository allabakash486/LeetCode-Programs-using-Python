number = 123
sol = 0
if number>0:
    while number !=0:
        sol = (sol*10)+(number%10)
        number //= 10
    else:
        print(sol)
else:
    number = ~number+1
    while number !=0:
        sol = (sol*10)+(number%10)
        number //= 10
    print(~sol+1)
    
