correct_password="saisurya@123"
password=input("Enter the password: ")
attempts = 1
if password == correct_password:
    print("Access granted ✅")

while password != correct_password:
    print("Incorrect password. Please try again.")
    print("You have", 3 - attempts, "attempts left.")
    password = input("Enter the password: ")
    attempts += 1
    if password == correct_password: 
        print("Access granted ✅")
    elif attempts >= 3:
       print("Too many attempts. Access denied.")
       break

