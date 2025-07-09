def password_checker(correct_password, max_attempts=3):
    attempts = 0
    while attempts < max_attempts:
        password = input("Enter your password: ")
        if password == correct_password:
            return "Password is correct!"
        attempts += 1
        print(f"Incorrect password. You have {max_attempts - attempts} attempts left.")
    return "Password is incorrect. Please try again later."
# Example usage
correct_password = "saisurya@123"
result = password_checker(correct_password)
print(result)
# This function checks the password and allows a maximum of 3 attempts before denying access.