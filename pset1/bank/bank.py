user_input = input("Greeting: ").lower().strip()

if user_input.startswith("hello"):
    value = 0
elif user_input.startswith("h"):
    value = 20
else:
    value = 100

print(f"${value}")