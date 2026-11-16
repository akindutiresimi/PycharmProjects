from datetime import date

from admin import Admin
from pharmacist import Pharmacist
from customer import Customer
from drug import Drug
from pharmacy import Pharmacy


admin = Admin("Ada Obi", "08011111111", 1)
pharmacist = Pharmacist("Tunde Bello", "08022222222", 10)
pharmacy = Pharmacy(pharmacist, admin)
customer = Customer("Chioma Eze", "08033333333")

while True:
    print("1. Add drug")
    print("2. List drugs")
    print("3. Add drug to cart")
    print("4. Show cart")
    print("0. Quit")
    choice = input("Choose: ")

    match choice:
        case "1":
            name = input("Name: ")
            price = int(input("Price: "))
            quantity = int(input("Quantity: "))
            pharmacy.drugs.append(Drug(name, date(2026, 12, 31), price, quantity))
            print("Drug added.")

        case "2":
            for drug in pharmacy.drugs:
                print(drug.name, drug.price, drug.quantity)

        case "3":
            name = input("Drug name: ")
            qty = int(input("How many: "))
            customer.cart[name] = customer.cart.get(name, 0) + qty
            print("Added to cart.")

        case "4":
            print(customer.cart)

        case "0":
            break

        case _:
            print("Invalid choice.")