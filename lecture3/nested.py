inchar = input("Input one character:")
if inchar >= 'A' and inchar <= 'Z':
    print("You in put Upper case Letter ", inchar)
elif inchar >= 'a'and inchar <='z':
    print("You in put Lower case Letter ", inchar)
elif inchar >= '0' and inchar <= '9':
      print("You in put Number case Letter ", inchar)  
else :
    print("It's not a letter or number.",inchar)     
    