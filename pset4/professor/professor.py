import random


def main():
    level = get_level()
    
    score = 0
    for i in range(10):
        x, y = generate_integer(level)
        tries = 0

        while tries < 3:
            try:
                z = int(input(f"{x} + {y} = "))
            except ValueError:
                print("EEE")
                tries += 1
            else:
                if z != (x + y):
                    print("EEE")
                    tries += 1
                    continue
                else:
                    score += 1
                
                break

        if tries == 3:
            print(f"{x} + {y} = {x + y}")
        
    print(f"Score: {score}")
        


def get_level():
    level = None
    while level not in ["1", "2", "3"]:
        level = input("Level: ")
    
    return int(level)


def generate_integer(level):
    match level:
        case 1:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
        case 2:
            x = random.randint(10, 99)
            y = random.randint(10, 99)
        case 3:
            x = random.randint(100, 999)
            y = random.randint(100, 999)

    return x, y


if __name__ == "__main__":
    main()