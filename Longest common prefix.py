l=["flower","flow","flight"]
output = ''
for i in range(len(l)):
    if l[0][i]==l[1][i] and l[2][i]==l[0][i]:
        output += l[i][i]
print(output)
