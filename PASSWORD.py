import re

def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    errors = [length_error, digit_error, uppercase_error, lowercase_error, symbol_error]

    if all(not error for error in errors):
        strength = "Strong"
    elif sum(errors) == 1 or sum(errors) == 2:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength

# Example
password = input("Enter your password: ")
strength = check_password_strength(password)
print(f"Password Strength: {strength}")
