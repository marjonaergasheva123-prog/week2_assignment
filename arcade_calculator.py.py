#put user input inside of your while loop
# move total += price outside of if statements
print('===Arcade Game Center===')
total=0
while True:
     game_type=input ("Enter game type: (classic, modern, or premium) or 'done': ")
     if  game_type=="done":
         break    
     if game_type=="classic":
        price=0.50
        print(f"Price:{price}")
        total += price
        print(f"Total: {total}")
     elif game_type=="modern":
          price=1.50
          print(f"Price: {price}")
          total +=price
          print(f"Total:{total}")

     elif game_type=="premium":
          price=2.50
          print(f"Price:{price}")
          total+=price
          print(f"Total:{total}")
     else:
        print("invalid game type")
total+=price

     
print(f"Price:{price:.2f}$")
print(f"Current total: {total:.2f}$")
special_offer=0.0
if total>=10.00:
    special_offer=1.50
final_total=total- special_offer
print("===Game Summary===")
print(f"Subtotal: {total}$")
print(f"Token Bonus Credit:{special_offer}$")
print(f"Final Total: {final_total}$")
print("Thank you for playing!")