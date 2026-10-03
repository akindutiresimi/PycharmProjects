while (True):
    print("========   Welcome to GBeda Station!  =========== ")
    print("Available petroleum")
    print("     1. Buy Petroleum")
    print("     2. Show Transaction History")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            print("1. Buy Petroleum")
            while(True):

                buy_petroleum = """
                press 1 to buy petrol @ 650 / liter
                press 2 to buy Diesel @ 720 / liter
                press 3 to buy Kerosene @ 550 / liter
                press 4 to buy Gas @ 480 / liter
                                """
                print(buy_petroleum)
                buy_petroleum_list = int(input("Buy petroleum: "))

                match buy_petroleum_list:
                    case 1:
                        print("1. Buy petrol")
                    case 2:
                        print("2. Buy Diesel")
                    case 3:
                        print("3. Buy Kerosene")
                    case 4:
                        print("4. Buy Gas")




        case 2:
            print("2. Show Transaction History")
        case 3:
            prin



