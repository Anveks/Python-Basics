print("This is Pizza Delivery practice.")
size = input("What size of pizza do you want? S, M, or L? ")
pepperoni = input("Add pepperoni? True or false? ").lower() == "true"
extra_cheese = input("Add extra cheese? True or false? ").lower() == "true"

price = 0

if size == "S":
    price += 15
    if pepperoni:
        price += 2

    if extra_cheese:
        price += 1

elif size == "M":
    price += 20
    if pepperoni:
        price += 3

    if extra_cheese:
        price += 1

else:
    price += 25
    if pepperoni:
        price += 3

    if extra_cheese:
        price += 1

print(f"The price is {price}")