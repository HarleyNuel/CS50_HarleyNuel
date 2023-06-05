def convert(time):
    hours, minutes = map(int, time.split(':'))
    return hours + minutes / 60


def main():
    time = input("Enter the time (in 24-hour format HH:MM): ")

    converted_time = convert(time)

    if 7 <= converted_time <= 8:
        print("It's breakfast time!")
    elif 12 <= converted_time <= 13:
        print("It's lunch time!")
    elif 18 <= converted_time <= 19:
        print("It's dinner time!")


main()