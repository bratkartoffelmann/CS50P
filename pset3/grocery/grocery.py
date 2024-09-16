groceries = dict()

while True:
    try:
        user_input = input().upper()
    except EOFError:
        break

    # check if present in dictionary
    if user_input not in groceries:
        groceries[user_input] = 0
    
    # Increment
    groceries[user_input] += 1

# print
for item, qty in sorted(groceries.items()):
    print(f"{qty} {item}")