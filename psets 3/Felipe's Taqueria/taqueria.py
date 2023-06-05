def main():
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    order_total = 0.00

    try:
        while True:
            item = input("Enter an item: ").strip().title()
            if not item:
                continue

            if item in menu:
                order_total += menu[item]
                print("Order total: ${:.2f}".format(order_total))
            else:
                print("Invalid item.")

    except EOFError:
        print("\nThank you for your order!")


main()
