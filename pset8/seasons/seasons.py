from datetime import date
import re
import inflect
import sys

def main():
    user_date = input("Date of Birth: ")

    try: 
        birthday = get_date(user_date)
    except ValueError as e:
        sys.exit(e)
    else:
        today = get_today_date()

        minutes = get_timedelta_minutes_string(birthday, today)
        print(minutes)



def get_date(user_date):
    if matches := re.search(r"^(\d{4})-(\d{2})-(\d{2})$", user_date):
        year, month, day = matches.groups()
        return date(int(year), int(month), int(day))
    else:
        raise ValueError("Invalid date")


def get_today_date():
    today = date.today()

    return date(today.year, today.month, today.day)

def get_timedelta_minutes_string(birthday, today):
    timedelta = today - birthday
    minutes = timedelta.days * (24 * 60)

    p = inflect.engine()
    return f"{p.number_to_words(minutes, andword='').capitalize()} minutes"




if __name__ == "__main__":
    main()