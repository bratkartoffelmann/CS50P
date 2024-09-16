import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r'<iframe[^>]*src="https?://(?:www\.)?youtube\.com/embed/(\w+)"', s, re.IGNORECASE):
        unique_link = matches.groups()[-1]

        return f"https://youtu.be/{unique_link}"
    else:
        return None



if __name__ == "__main__":
    main()