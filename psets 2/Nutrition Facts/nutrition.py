fruit_data = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plums": 70,
    "strawberries": 50,
    "sweet cherries": 100,
    "tangerine": 50,
    "watermelon": 80
}


def main():
    while True:
        # Take input from the user
        fruit = input("Item: ")
        fruit_lower = fruit.strip().lower()

        # Check if fruit exists in the dictionary
        if fruit_lower in fruit_data:
            # Access the value using the input as a key
            calories = fruit_data[fruit_lower]
            print("Calories: ", calories)
        else:
            print("Input a valid fruit")


main()
