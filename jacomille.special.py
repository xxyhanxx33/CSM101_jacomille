while True:
    print("\n--- A-LENDING INCORPORATED ---")

    jacomille_share_capital = float(input("Enter share capital: "))

    if jacomille_share_capital > 100000:
        jacomille_loanable_amount = jacomille_share_capital * 2.00
    else:
        jacomille_loanable_amount = jacomille_share_capital * 1.50

    jacomille_term = int(input("Enter payment term (3, 6, or 12 months): "))

    if jacomille_term == 3:
        jacomille_interest_rate = 0.05
    elif jacomille_term == 6:
        jacomille_interest_rate = 0.07
    elif jacomille_term == 12:
        jacomille_interest_rate = 0.10
    else:
        print("Invalid term! Please enter 3, 6, or 12.")
        continue

    jacomille_service_fee = 200.00
    jacomille_advance_interest = jacomille_loanable_amount * jacomille_interest_rate
    jacomille_take_home_loan = jacomille_loanable_amount - (jacomille_service_fee + jacomille_advance_interest)
    jacomille_monthly_due = jacomille_loanable_amount / jacomille_term

    print("\n--- COMPUTATION SUMMARY ---")
    print(f"Share Capital       : PHP {jacomille_share_capital:,.2f}")
    print(f"a. Loanable Amount  : PHP {jacomille_loanable_amount:,.2f}")
    print(f"b. Term & Interest  : {jacomille_term} months @ {int(jacomille_interest_rate * 100)}%")
    print(f"c. Service Fee      : PHP {jacomille_service_fee:,.2f}")
    print(f"d. Advance Interest : PHP {jacomille_advance_interest:,.2f}")
    print(f"e. Take Home Loan   : PHP {jacomille_take_home_loan:,.2f}")
    print(f"f. Monthly Due      : PHP {jacomille_monthly_due:,.2f}")

    jacomille_choice = input("\nCalculate another loan? (yes/no): ").lower()
    if jacomille_choice != 'yes' and jacomille_choice != 'y':
        print("Goodbye!")
        break