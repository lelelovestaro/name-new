fruit = ['mangos' ,'guava', 'lemon', 'cucumber', 'berries', 'coconut']

string = 'Welcome to the bakery! We have fresh fruit pastries and new items every Monday.'

cakes = "raspberry lemon ice box", "coconut lime", "carmel cake", 'strawberry shortcake'

cherry_cakes = lambda cakes: list(cakes)

kind_fruits = lambda fruit: list(fruit)
order_two = input("What flavor of cake would you like to order? ").upper()
if order_two in cakes:
        print(input("Would you like to add fruit to your cake for an additional 50 cents? "))
        if input("Would you like to add fruit to your cake for an additional 50 cents? ").upper() == "yes":
            print(input("What kind of fruits would you like to add to your cake?")).upper() in fruit
            print(list(kind_fruits(fruit)))
            print("Great! We will add fruit to your " + order_two + " cake for an additional 50 cents.")
        else:
            print("No problem! We will prepare your " + order_two + " cake without fruit.")
else:
    print("Sorry, We do not have that flavor in stock. Please choose from the following options: " + str(cakes))

print("Thank you for ordering at Lele\'s Sweets & Treats!")