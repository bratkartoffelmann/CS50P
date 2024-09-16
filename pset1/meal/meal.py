def main():
    user_input = input("What time is it? ").lower().strip()
    user_time = convert(user_input)

    if user_time >= 7 and user_time <= 8:
        print("breakfast time")
    elif user_time >= 12 and user_time <= 13:
        print("lunch time")
    elif user_time >= 18 and user_time <= 19:
        print("dinner time")



def convert(time):
    """
    Return time, but return float
    """

    colonIndex = time.index(':')
    hour = int(time[:colonIndex])
    minute = int(time[colonIndex+1:])

    return hour + minute/60


if __name__ == "__main__":
    main()