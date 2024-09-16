def main():
    while True:
        user_input = input("Fraction: ")

        try:
            x, y = get_x_y(user_input)
        except ValueError as e:
            print(e)
            continue

        try: 
            percentage = get_fuel_percentage(x, y)
        except ValueError as e1:
            print(e1)
            continue
        except ZeroDivisionError as e2:
            print(e2)
            continue

        print(get_fuel_reading(percentage))
        break
        


def get_x_y(user_input):
    "Check for valid fraction"
    
    try:
        fractionIndex = user_input.index("/")
    except Exception:
        raise ValueError("Input must be a valid fraction")

    x = user_input[:fractionIndex]
    y = user_input[fractionIndex+1:]

    if not (x.isnumeric() and y.isnumeric()):
        raise ValueError("Fraction must not contain other symbols")
    
    return int(x), int(y)

def get_fuel_percentage(x, y):

    if y == 0:
        raise ZeroDivisionError("y must be larger than 0")

    if x > y:
        raise ValueError("x must be smaller than y")
    
    return x/y * 100

def get_fuel_reading(percent):

    if percent <= 1:
        return "E"
    elif percent >= 99:
        return "F"
    else:
        return f"{round(percent)}%"

main()