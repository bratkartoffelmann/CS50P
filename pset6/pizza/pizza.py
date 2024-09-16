import sys
import os
import csv
from tabulate import tabulate

class IllegalArgumentError(ValueError):
    pass

def check_arguments():
    # Check for 2 arguments
    if len(sys.argv) < 2:
        raise IllegalArgumentError("Too few command-line arguments")
    elif len(sys.argv) > 2:
        raise IllegalArgumentError("Too many command-line arguments")

    # Check if file is csv file
    if ".csv" not in sys.argv[1]:
        raise IllegalArgumentError("Not a CSV file")

    # Check if file is present
    if not os.path.exists(sys.argv[1]):
        raise FileNotFoundError("File does not exist")
    

def menu_reader(filepath):
    table = list()
    with open(filepath, 'r') as file:
        # Get name of pizza
        pizza_name = filepath[:filepath.index(".csv")].title()
        table.append([f"{pizza_name} Pizza", "Small", "Large"]) # Append table header

        # Get info of menu in the form of Dict()
        reader = csv.DictReader(file)
        for row in reader:
            # Append menu
            table.append([
                row[f"{pizza_name} Pizza"], # Toppings
                row["Small"],               # Price of small pizza
                row["Large"]                # Price of large pizza
            ])
    return table

def print_menu(menu):
    print(tabulate(menu, headers="firstrow", tablefmt="grid"))


def main():

    try:
        check_arguments()
    except Exception as e:
        sys.exit(e)
    else:
        menu = menu_reader(sys.argv[1])
        print_menu(menu)


if __name__ == "__main__":
    main()