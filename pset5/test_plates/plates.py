def main():
    plate = input("Plate: ")
    print(is_valid(plate))
    
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s=""):
    s = s.upper()

    # vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters
    if len(s) < 2 or len(s) > 6: 
        return False

    # All vanity plates must start with at least two letters.
    if not s[:2].isalpha():
        return False
    
    # No periods, spaces, or punctuation marks are allowed
    if not s.isalnum():
        return False
    
    # Numbers cannot be used in the middle of a plate; they must come at the end.
    num = False
    firstNum = True
    for i in s[2:]:
        if i.isnumeric(): # If numbers appears, ...
            num = True

            # The first number used cannot be a ‘0’.
            if firstNum:
                if i == "0":
                    return False
                firstNum = False
                
        if num and i.isalpha(): # ... no letters should appear
            return False
        
    return True


if __name__ == "__main__":
    main()