MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def convert_to_iso_date(date_str):
    parts = date_str.split("/")
    if len(parts) == 3:
        month, day, year = parts
    else:
        parts = date_str.split(" ")
        if len(parts) == 3:
            month, day, year = parts[0], parts[1][:-1], parts[2]
        else:
            return None

    try:
        month_index = MONTHS.index(month.capitalize()) + 1
        month_str = f"{month_index:02}"
        day_str = f"{int(day):02}"
        year_str = f"{int(year):04}"
        return f"{year_str}-{month_str}-{day_str}"
    except ValueError:
        return None


while True:
    date_input = input("Enter a date (in month-day-year format): ")
    iso_date = convert_to_iso_date(date_input)
    if iso_date is not None:
        print(iso_date)
        break
    else:
        print("Invalid date format. Try again.")
