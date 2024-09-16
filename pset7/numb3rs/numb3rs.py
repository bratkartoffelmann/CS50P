import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # Check if input is string
    if not isinstance(ip, str):
        return False

    # Check if IPv4 address format is valid
    if valid_ip := re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip):

        # Split into sub IP addresses
        ip_sub1, ip_sub2, ip_sub3, ip_sub4 = valid_ip.groups()

        # Check if they wre within range 0 <= x <= 255
        for ip_sub in [ip_sub1, ip_sub2, ip_sub3, ip_sub4]:
            if int(ip_sub) < 0 or int(ip_sub) > 255:
                return False

        return True
    else: 
        return False


if __name__ == "__main__":
    main()