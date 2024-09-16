def main():
    while True:
        fraction = input("Fraction: ")

        try:
            percentage = convert(fraction)
        except Exception as e:
            print(e)
            continue

        print(gauge(percentage))
        break
        

def convert(fraction):
    "Check for valid fraction"
    
    # Check if input is a function
    try:
        fractionIndex = fraction.index("/")
    except Exception:
        raise ValueError("Input must be a valid fraction")

    # Check if fraction contains other symbol
    x = fraction[:fractionIndex]
    y = fraction[fractionIndex+1:]

    if not (x.isnumeric() and y.isnumeric()):
        raise ValueError("Fraction must not contain other symbols")
    

    # Return fraction
    x = int(x)
    y = int(y)

    if y == 0:
        raise ZeroDivisionError("y must be larger than 0")

    if x > y:
        raise ValueError("x must be smaller than y")
    
    return x/y * 100


def gauge(percentage):

    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{round(percentage)}%"

if __name__ == "__main__":
    main()