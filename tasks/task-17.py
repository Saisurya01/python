with open("notes.txt", "w") as file:
    file.write(input("write your notes here: ") + "\n")

userinput= input("Do you want to see your notes? (yes/no): ")
if userinput.lower() == "yes":
    with open("notes.txt", "r") as file:
        content = file.read()
        print(content)