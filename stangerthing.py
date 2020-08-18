firstname = input('Enter your firstname:')
lastname = input('Enter your lastname:')
studentID = input('Enter your ID')
 
allmight = firstname[:3] + lastname[:6] +studentID[-4:]
print('Your system login name is :',allmight)