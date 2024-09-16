received = 0

while received < 50:
    print(f"Amount Due: {50-received}")

    user_input = int(input("Insert coin: "))
    if user_input in [25, 10, 5]:
        received += user_input


print(f"Change Owed: {received-50}")