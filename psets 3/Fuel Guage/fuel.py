def calculate_fuel_percentage(fuel_fraction):
    try:
        numerator, denominator = map(int, fuel_fraction.split('/'))
        if denominator == 0 or numerator > denominator:
            return False

        fuel_percentage = (numerator / denominator) * 100
        if fuel_percentage <= 1:
            return 'E'
        elif fuel_percentage >= 99:
            return 'F'
        else:
            return round(fuel_percentage)

    except (ValueError, ZeroDivisionError):
        return False


while True:
    user_input = input("Enter the fuel fraction (X/Y): ")
    fuel_percentage = calculate_fuel_percentage(user_input)
    if fuel_percentage is not False:
        break
    print("Invalid input. Please try again.")

print(fuel_percentage)
