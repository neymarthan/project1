hours= int(input('Enter the number of hours worked:'))
hourly=int(input('Enter the hourly pay rate:'))
hoursever=(hours-40)*1.5
fullltime = hourly = 40 

if hours >40:
    print('the gross pay is $',hoursever*hourly+fullltime)
else:
    print('the gross pay is $',hours*hourly)