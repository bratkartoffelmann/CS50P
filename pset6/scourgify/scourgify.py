import sys
import os
import csv

class IllegalArgumentError(ValueError):
    pass

def check_arguments():
    # Check for 3 arguments
    # - input
    # - output
    if len(sys.argv) < 3:
        raise IllegalArgumentError("Too few command-line arguments")
    elif len(sys.argv) > 3:
        raise IllegalArgumentError("Too many command-line arguments")

    # Check if file is csv file
    if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        raise IllegalArgumentError("Not a CSV file")

    # Check if file is present
    if not os.path.exists(sys.argv[1]):
        raise FileNotFoundError("File does not exist")
    

def convert_files(before_file, after_file):
    info = list()
    with open(before_file, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            info.append({
                "name": {
                    "first": row["name"][row["name"].index(",")+2:],
                    "last": row["name"][:row["name"].index(",")],
                },
                "house": row["house"],
            })
        
    with open(after_file, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()

        for person in info:
            writer.writerow({
                "first": person["name"]["first"],
                "last": person["name"]["last"],
                "house": person["house"]
            })

def main():

    try:
        check_arguments()
    except Exception as e:
        sys.exit(e)
    else:
        convert_files(before_file=sys.argv[1], after_file=sys.argv[2])


if __name__ == "__main__":
    main()