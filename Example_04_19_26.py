#holder
Supplies = ['pencil', 'paper', 'folder', 'journal', 'eraser', 'pen']

fruit = ['mangos' ,'guava', 'lemon', 'cucumber', 'berries', 'coconut']

prices = 2.00

#bag = zip(Supplies, fruit)
#print(bag)
#print(' ')
#print(list(bag))

cakepops = 1.25
cakes_with_sprinkles = 2.25

string = 'Welcome to the bakery! We have fresh fruit pastries and new items every Monday. All fruit drinks are ' + str(prices) + ' dollars each!'
print("-----")
string_2 = ' We also have school/office supplies sponsored by Hello Kitty\'s Art and Craft shop! All items are buy one get one free! Addtionally, We have cake pops for sale for ' + str(cakepops) + ', and cakes with sprinkles for ' + str(cakes_with_sprinkles) + '!' 
print(string + string_2)
print("-----")


cakes = "raspberry lemon ice box", "coconut lime", "carmel cake", 'strawberry shortcake'
cherry_cakes = lambda cakes: list(cakes)
print(cherry_cakes(cakes))
kind_fruits = lambda fruit: list(fruit)
order_two = input("What flavor of cake would you like to order? ").upper() in cakes
if order_two in cakes:
        print(input("Would you like to add fruit to your cake for an additional 50 cents? "))
    if input("Would you like to add fruit to your cake for an additional 50 cents? ").upper() == "yes":
        print(input("What kind of fruits would you like to add to your cake? ")).upper() in fruit:
        print(list(kind_fruits(fruit)))
        print("Great! We will add fruit to your " + order_two + " cake for an additional 50 cents.")
    else:
        print("No problem! We will prepare your " + order_two + " cake without fruit.")
        
print("Thank you for ordering at Lele\'s Sweets & Treats!")