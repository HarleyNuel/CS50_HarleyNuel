def balance(total_amount, cost):
    return total_amount - cost


def validate(coin):
    accepted_coins = [25, 10, 5]
    return coin in accepted_coins


def main():
    total_amount = 0
    cost = 50
    remaining_amount = 0

    print("Amount Due: 50")
    while total_amount < cost:
        coin = input("Insert a coin: ")
        if coin.isdigit():
            coin = int(coin)
            if validate(coin):
                total_amount += coin
                remaining_amount = cost - total_amount
            else:
                print("Amount owed: ", remaining_amount)
        else:
            print("Amount owed: ", remaining_amount)

    if total_amount > cost:
        change = balance(total_amount, cost)
        print("Change owed: ", change)
    else:
        print("No change owed")


main()
