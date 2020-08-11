keep_going ='y'
while keep_going =='y' or keep_going =='Y':
    wholesale_cost = int(input("Enter the item's wholesale cost:"))
    reprice = wholesale_cost*2.5
    print('Retail Price: $',reprice)
    keep_going = input('Do you have another item?(Enter y for yes):' )
