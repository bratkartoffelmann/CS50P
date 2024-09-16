import validators

def main():
    email = input("What's your email address? ")
    valid_email = validators.email(email)

    if valid_email:
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
