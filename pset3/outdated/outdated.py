months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    while True:
        date = input("Date: ").strip()
        
        try:
            if "-" in date:
                d, m, y = check_normal_date(date)
            elif "/" in date:
                d, m, y = check_numeric_date(date)
            else:
                d, m, y = check_word_date(date)
        except ValueError:
            continue
        else:
            output(d, m, y)
            break
    

def check_normal_date(date):
    year, month, day = date.split("-")

    if int(month) > 12 or int(day) > 31:
        raise ValueError("Date format is wrong.")

    return day, month, (year) 


def check_numeric_date(date):
    month, day, year = date.split("/")

    if int(month) > 12 or int(day) > 31:
        raise ValueError("Date format is wrong.")

    return day, month, year 


def check_word_date(date):
    month, day, year = date.split(" ")
    day = day[:-1]

    if int(day) > 31:
        raise ValueError("Date format is wrong.")

    if month not in months:
        raise ValueError("Date format is wrong.")
    else:
        month = months.index(month)+1 # return the index of month, aka numeric

    return day, month, year 


def output(day, month, year):
    print(f"{int(year)}-{int(month):02d}-{int(day):02d}")

main()