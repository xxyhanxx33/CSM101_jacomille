jacomilleflavor = input("Enter what flavor (Cheese/Pepperoni): ").lower()
jacomilleprice = 0

match jacomilleflavor:
    case "cheese":
        print("Selected flavor: Cheese")

        size = input("Enter size (small/medium/large): ").lower()

        if size == "small":
            jacomilleprice = 275
        elif size == "medium":
            jacomilleprice = 375
        elif size == "large":
            jacomilleprice = 475
        else:
            jacomilleprice = 0
            print("Invalid size.")

    case "pepperoni":
        print("Selected flavor: Pepperoni")

        size = input("Enter size (small/medium/large): ").lower()

        if size == "small":
            jacomilleprice = 300
        elif size == "medium":
            jacomilleprice = 400
        elif size == "large":
            jacomilleprice = 500

        else:
            jacomilleprice = 0
            print("Invalid size.")

    case _:
        jacomilleprice = 0
        print("Invalid pizza flavor.")

if jacomilleprice > 0:
    print("Pizza price:", jacomilleprice)