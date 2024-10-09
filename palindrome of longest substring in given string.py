s='cbbd"'
l=[]
for sv in range(len(s)):
    for ev in range(sv+1,len(s)+1):
        if s[sv:ev]==s[sv:ev][::-1]:
            if len(s[sv:ev])>1:
                print(s[sv:ev])

