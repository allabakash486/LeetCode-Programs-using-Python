l1 = [1,3]
l2 = [2,4,5,6,7,8]
l  = sorted(l1 + l2)
if len(l)%2!=0:
    print(float(l[len(l)//2]))
else:
    print((l[len(l)//2]+l[len(l)//2-1])/2)
          
