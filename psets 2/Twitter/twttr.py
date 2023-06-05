def vowel_replace(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for vowel in vowels:
        word = word.replace(vowel, "")
    return word

def main():
    while True:
        word_input = input("Input: ")
        if word_input == "q":
            break
        print("Output: ", vowel_replace(word_input))


main()
