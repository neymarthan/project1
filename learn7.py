number=5

def main():
    global number
    number=int(input('Enter a number:'))
    show_number()

def show_number():
    print('The number you enterd is',number)    

main()    