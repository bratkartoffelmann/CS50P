user_input = input("Input: ")

for vowel in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
    user_input = user_input.replace(vowel, "")

print(f"Output: {user_input}")