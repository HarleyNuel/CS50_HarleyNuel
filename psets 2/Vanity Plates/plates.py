def main():
    while True:
        plate = input("Plate: ")
        if is_valid(plate):
            print("Valid")
        else:
            print("Invalid")


def is_valid(s):
    length = len(s)

    if length < 2 or length >= 6:
        return False

    if not s[0:2].isalpha():
        return False

    for i in range(length):
        if s[i].isnumeric():
            if s[i] == '0':
                return False

            for j in range(i + 1, length):
                if s[j].isalpha():
                    return False
                break

        if not s.isalnum():
            return False

    return True


main()