str1=('English = 78 science = 83 math = 68 history = 65')
sum1=0
i=0
malee = str1.split()
for king in malee:
    if king.isnumeric():
        sum1 = sum1 + int(king)
        i = i + 1
    

print (sum1)
print(sum1/i)
