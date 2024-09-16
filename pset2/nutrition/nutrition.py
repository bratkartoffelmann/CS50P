fruits_calories = {
    "apple": 130,
    "avocado": 50,
    'banana': 110,
    'cantalope': 50,
    'grapefruit': 60,
    'honeydew melon': 50,
    'kiwifruit': 90,
    'lemon': 15,
    'lime': 20,
    'nectarine': 60,
    'orange': 80,
    'peach': 60,
    'pear': 100,
    'pineapple': 50,
    'plums': 70,
    'strawberries': 50,
    'sweet cherries': 100,
    'tangerine': 50,
    'watermelon': 80,
}

user_input = input("Item: ").lower()
if user_input in fruits_calories:
    print(f"Calories: {fruits_calories[user_input]}")