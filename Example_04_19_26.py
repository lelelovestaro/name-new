
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

string_2 = ' We also have school/office supplies sponsored by Hello Kitty\'s Art and Craft shop! All items are buy one get one free! Addtionally, We have cake pops for sale for ' + str(cakepops) + ', and cakes with sprinkles for ' + str(cakes_with_sprinkles) + '!' 
print(string + string_2)



cakes = "raspberry lemon ice box", "coconut lime", "carmel cake", 'strawberry shortcake'
cherry_cakes = lambda cakes: list(cakes)
print(cherry_cakes(cakes))
kind_fruits = lambda fruit: list(fruit)
order_two = input("What flavor of cake would you like to order? ").upper()
if input("What flavor of cake would you like to order? ").upper() in order_two:
    if input(cakes):
        print(input("Would you like to add fruit to your cake for an additional 50 cents? "))
    if input("Would you like to add fruit to your cake for an additional 50 cents? ").upper() == "yes":
        print(input("What kind of  " + list(kind_fruits) + " would you like to add to your cake? "))
        print("Great! We will add fruit to your " + order_two + " cake for an additional 50 cents.")
    else:
        print("No problem! We will prepare your " + order_two + " cake without fruit.")
        
for orders in order_two:
    print(orders + order_two)
# how to make a lambda function for a beginner using the cakes line and wanting to add cherries to it in the loop using lambda function
cake_with_cherries = lambda cakes: [cake + " with cherries" for cake in cakes]
#print("how does the lambda work in cake_with_cherries is that it takes each cake in the cakes list and adds the string "+"with cherries"+" to it, creating a new list of cakes that now have cherries as part of their description."+"The lambda function is a concise way to define this operation without needing to write a full function definition.")
#print(list(cake_with_cherries(cakes)))

order = input("What would you like to order? ").lower()
print("Thank you for your order of " + order + "! We will have it ready for you shortly.")


inventory = [len(cakes) + len(fruit)]
if list(inventory) <= 0:
    print("We are sorry, but we are currently out of stock for that item.")
else:
    print("Thank you for your purchase!") 