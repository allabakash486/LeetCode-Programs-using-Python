def Sum_of_two_list():
    l1  = [9,9,9,9,9,9,9]
    l2  = [9,9,9,9];
    First_sol,second_sol  = 0,0;
    for ind in range(len(l1)):
        First_sol  = (First_sol*10)+l1[ind];
    for ind in range(len(l2)):
        second_sol = (second_sol*10)+l2[ind];
    sum1 = First_sol+ second_sol;
    l=[]
    while sum1 !=0:
        l.append(sum1%10)
        sum1 //= 10
    print(l)
Sum_of_two_list()
        
        
