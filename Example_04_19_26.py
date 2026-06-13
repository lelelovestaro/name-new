fruit = "mangos" ,"guava", "lemon", "cucumber", "berries", "coconut" 

string = 'Welcome to the bakery! We have fresh fruit pastries and new items every Monday.'

cakes = "raspberry lemon ice box", "coconut lime", "carmel cake", 'strawberry shortcake'

print(str(cakes))
order_two = input("What flavor of cake would you like to order? ").lower()
if order_two in cakes:
        if input("Would you like to add fruit to your cake for an additional 50 cents? ").lower() in ["yes", "sure", "Y", "yeah", "yep"]:
            print(fruit)
            new_fruit = input("What kind of fruit would you like to add to your cake? ").lower()
            print("Great! We will add " + new_fruit + " to your " + order_two + " cake for an additional 50 cents.")
        else:
            print("No problem! We will prepare your " + order_two + " cake without fruit.")
else:
    print("Sorry, We do not have that flavor in stock. Please choose from the following options: " + str(cakes))

print("Thank you for ordering at Lele\'s Sweets & Treats! Enjoy :)")
