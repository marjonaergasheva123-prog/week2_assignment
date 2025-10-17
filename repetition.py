print('----The Movie Ticket Pricer----')
print()
age_str= input('Enter your age')
age= int(age_str)
if age <= 12:
     print(" You fall into the 'Children' category")
     print(' Your ticket price is : 8$')
elif  13<=age<=64:
     print("You fall into 'Adult' category")
     print('Your ticket price is : 15$')

else:
      age= 'Seniors'
      print( "You fall into 'Seniors' category")
      print('your ticket price is : 10$' )
