def main():
    word = input("Input: ")
    twttr = shorten(word)
    print(f"Output: {word}")


def shorten(word):
    if not isinstance(word, str):
        raise TypeError("Input must be a string")
    for vowel in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
        word = word.replace(vowel, "")
    return word


if __name__ == "__main__":
    main()



