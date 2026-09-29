flavor = input("Enter what flavor Cheese/Pepperoni").lower()

if flavor == "cheese":
    print ("selected flavor Cheese")

    size =  input("enter sizes small/medium/large").lower()

    if size == "small":
        price = 275
    elif size == "medium":
        price = 375
    elif size == "large":
        price = 475
    else:
        price = 0
        print ("invalid size.")

else:
    price = 0
    print("invalid pizza flavor")

if price > 0:
    print ("pizza prices", price)



if flavor == "Pepperoni":
    print("selected flavor Cheese")

    size = input("enter sizes small/medium/large").lower()

    if size == "small":
        price = 300
    elif size == "medium":
        price = 400
    elif size == "large":
        price = 500
    else:
        price = 0
        print("invalid size.")

else:
    price = 0
    print("invalid pizza flavor")

if price > 0:
    print("pizza prices", price)





