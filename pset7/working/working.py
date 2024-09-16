import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"^(\d+):?(\d+)?\s(\w+)\sto\s(\d+):?(\d+)?\s(\w+)", s):
        h1, min1, time1, h2, min2, time2 = matches.groups()

        # Check for invalid hours
        if int(h1) > 12 or int(h2) > 12:
            raise ValueError("Invalid hours input")
        
        # Check for invalid minutes
        if min1 is not None and int(min1) >= 60:
            raise ValueError("Invalid minutes input")
        if min2 is not None and int(min2) >= 60:
            raise ValueError("Invalid minutes input")
        
        # Check for invalid AM/PM
        if time1 not in ["AM", "PM"] or time2 not in ["AM", "PM"]:
            raise ValueError("Invalid AM/PM input")
        
        # Formatting
        if h1 == '12' and time1 == 'AM':
            h1 = 0
        elif time1 == 'PM' and h1 != '12':
            h1 = int(h1) + 12
        else:
            h1 = int(h1)

        if h2 == '12' and time2 == 'AM':
            h2 = 0
        elif time2 == 'PM' and h2 != '12':
            h2 = int(h2) + 12
        else:
            h2 = int(h2)

        min1 = 0 if min1 is None else int(min1)
        min2 = 0 if min2 is None else int(min2)

        return f"{h1:02d}:{min1:02d} to {h2:02d}:{min2:02d}"

    else:
        raise ValueError("Invalid time input")





if __name__ == "__main__":
    main()