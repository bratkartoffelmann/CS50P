user_input = input("Expression: ").lower().strip()

first_whitespace = user_input.index(" ")
last_whitespace = user_input.rfind(" ")

x = int(user_input[:first_whitespace]) # Integer (to first whitespace)
y = user_input[first_whitespace+1:last_whitespace] # +, -, *, /
z = int(user_input[last_whitespace+1:]) # Integer (to last whitespace)

match y:
    case "+":
        value = x + z
    case "-":
        value = x - z
    case "*":
        value = x * z
    case "/":
        value = x / z

print(float(value))