with open("notes.txt", "w") as file:
    file.write("Recent edits in Python files:\n\n")

with open("notes.txt", "a") as file:
    file.write("1. Added a function to add two numbers in my_modul.py.\n")
    file.write("2. Demonstrated the use of the custom module in main.py.\n")
    file.write("3. Created a greet function and an is_even function in my_moduals.py.\n")
    file.write("4. Called these functions in task-16.py.\n")

    
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)
