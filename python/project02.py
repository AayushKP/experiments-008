#Random Passowrd Generator

# Collect User preferences
# - length
# - should contain uppercase
# - should contain special chars
# - should contain digits

# get all available chars
# randomly pick characters up to the length
# ensure we have at least one of each character type
# ensure length is valid


import random
import string

def generate_password():
    length = int(input("Enter the length of pswd: ").strip())
    include_uppercase = input("Include uppercase letters?: Y/N ")
    include_special = input("Include special chars?: Y/N ")
    include_digits = input("Include digits?: Y/N ")

    if length<4: 
        print("Password length must be at least 4 characters")
        return
    
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if include_uppercase=="Y" else ""
    special = string.punctuation if include_special=="Y" else ""
    digits = string.digits if include_digits=="Y" else ""
    all_characters = lower+upper+special+digits
    
    required_characters = ""
    if include_uppercase=="Y":
        required_characters += random.choice(upper)
    if include_special=="Y":
        required_characters += random.choice(special)
    if include_special=="Y":
        required_characters += random.choice(digits)

    left = length-len(required_characters)
    for _ in range(left):
        required_characters += random.choice(all_characters)

    print(f"{required_characters}")
generate_password()