jacomillegrade = int(input("enter grade: "))

match jacomillegrade:
        case n if 90 <= n <= 100:
            print("excellent")
        case n if 80 <= n <= 89:
            print("very good")
        case n if 75 <= n <= 79:
            print ("passed")
        case n if 0 <= n <= 74:
            print ("failed")
        case _:
            print ("invalid grade")
