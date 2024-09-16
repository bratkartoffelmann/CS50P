import sys
import os

class IllegalArgumentError(ValueError):
    pass

def check_arguments():
    # Check for 2 arguments
    if len(sys.argv) < 2:
        raise IllegalArgumentError("Too few command-line arguments")
    elif len(sys.argv) > 2:
        raise IllegalArgumentError("Too many command-line arguments")

    # Check if file is python file
    if ".py" not in sys.argv[1]:
        raise IllegalArgumentError("Not a python file")

    # Check if file is present
    if not os.path.exists(sys.argv[1]):
        raise FileNotFoundError("File does not exist")

def count_lines(file):
    valid_lines = list()

    # File exist
    with open(file, 'r') as file:
        lines = file.readlines()

        # check for conditions that makes it a line
        for line in lines:
            modified_line = line.strip() # remove whitespace

            if modified_line.startswith("#"): # invalid: comments
                continue

            if len(modified_line) == 0: # invalid: blank
                continue

            valid_lines.append(line)

        return len(valid_lines)

def main():

    try:
        check_arguments()
    except Exception as e:
        sys.exit(e)
    else:
        lines_count = count_lines(sys.argv[1])
        print(lines_count)


if __name__ == "__main__":
    main()