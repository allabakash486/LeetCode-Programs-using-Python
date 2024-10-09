s='pwwkew'
sub = ''
for charecter in s:
    sub += ' '+ charecter
list1 = sorted(list(set(sub.split())))
output = ''
for i in range(len(list1)):
    output += list1[i]

print(output,len(output))
