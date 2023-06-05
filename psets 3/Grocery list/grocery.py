grocery_list = {}
try:
    while True:
        item = input()
        item = item.strip().lower()  # Remove leading/trailing spaces and convert to lowercase


        if item == "":
            continue

        if item in grocery_list:
            grocery_list[item] += 1
        else:
            grocery_list[item] = 1

except EOFError:
    sorted_list = sorted(grocery_list.items())

    for item, count in sorted_list:
        print(f"{count} {item.upper()}")
