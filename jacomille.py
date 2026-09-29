jacomille_menu = [
    ("Cheese", "Small", 100),
    ("Cheese", "Medium", 150),
    ("Cheese", "Large", 200),

    ("Pork", "Small", 120),
    ("Pork", "Medium", 170),
    ("Pork", "Large", 220),

    ("Ham", "Small", 140),
    ("Ham", "Medium", 190),
    ("Ham", "Large", 240),
]

jacomille_flavor = input("Select Flavor (Cheese/Pork/Ham): ").lower()
size = input("Enter Size (Small, Medium, Large): ").lower()

jacomille_found = False

print("\n--- JACOMILLE ORDER SUMMARY ---")

for jacomille_pizza in jacomille_menu:
    if jacomille_pizza[0].lower() == jacomille_flavor and jacomille_pizza[1].lower() == size:
        print("You Have Selected:", jacomille_pizza[0])
        print("Size:", jacomille_pizza[1])
        print("Pizza Price: Php", jacomille_pizza[2])
        jacomille_found = True
        break

if not jacomille_found:
    print("Invalid Flavor or Size")