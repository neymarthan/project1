import random

print("WHat is my magic number(1 to 100) ?")
mynumber = random.randint(1,100)
ntries = 1
yourguess = -1
while ntries < 7 and  yourguess!=mynumber :
    msg = str(ntries)+ ">>"
    if(ntries == 6) :
        print('This is your last chance!!')
    yourguess = int(input(msg))   
    if (yourguess>mynumber)               :
      print("-->too high")
    if (yourguess<mynumber)               :
      print("--> too low")
      ntries  +=1

if mynumber ==  yourguess :                  
      print("Yes! it's",mynumber)
else:
          print("Sorry! my number is ",mynumber)