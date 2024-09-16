user_input = input("File name: ").lower().strip()

dotIndex = user_input.rfind(".")
ext = f"{user_input[dotIndex+1:]}"

if ext in ["gif", "jpg", "png", "jpeg"]:
    if ext == "jpg":
        ext = "jpeg"
    print(f"image/{ext}")
elif ext in ["txt"]:
    print(f"text/{user_input[:dotIndex]}")
elif ext in ["pdf", "zip"]:
    print(f"application/{ext}")
else:
    print(f"application/octet-stream")