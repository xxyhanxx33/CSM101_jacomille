jacomille_name = input("Enter your name: ").title()
jacomille_mnth = input("Enter Month: ").strip().capitalize()

if jacomille_mnth in ["January", "February", "March"]:
    jacomille_nat = "Rainy: Not a good month to travel due to flooding in many areas"
elif jacomille_mnth in ["April", "May"]:
    jacomille_nat = "Summer: A good time to travel"
elif jacomille_mnth in ["June", "July", "August"]:
    jacomille_nat = "Mixed Weather: Typhoon may come and the country may experience typhoon or good weather"
elif jacomille_mnth in ["September", "October", "November", "December"]:
    jacomille_nat = "Christmas Vibe: Still a mixed weather"
else:
    jacomille_nat = None

print(f"Hey {jacomille_name}")

if jacomille_nat:
    print(jacomille_nat)
else:
    print("Invalid month entered.")