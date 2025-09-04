# It's an automatic pizza order program.
# Based on users' order, they will see a final bill amount for their order.

print("Welcome to Python Pizza Deliveries!")
pizza_price = 0

#pizza size choice
size = input("What size pizza do you want? S, M or L: ")
if size == "S":
    pizza_price += 15
elif size == "M":
    pizza_price += 20
else:
    pizza_price += 25

#pepperoni choice
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni == "Y":
    if size == "S":
        pizza_price += 2
    else:
        pizza_price += 3

#cheese choice
extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == "Y":
    pizza_price += 1

print(f"Your final bill is: ${pizza_price}.")



