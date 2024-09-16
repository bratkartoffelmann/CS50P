import string

user_input = input("camelCase: ")

upper = list(string.ascii_uppercase)
lower = list(string.ascii_lowercase)

# Replace all upper with _lower
for i in range(len(upper)):
    user_input = user_input.replace(upper[i], f"_{lower[i]}")


print(f"snake_case: {user_input}")


