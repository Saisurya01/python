import random
n=int(input("How Many dice Do You Want To Roll : "))
while True:
    choice=input("Do You Want To Roll The Dice? (Y/N): ")
    if choice=="y" or choice=="Y":
        for i in range(n):
            die1=random.randint(1,6)
            die2=random.randint(1,6)
            print(f"{i+1} - Dice :({die1},{die2})")
    elif choice=="n" or choice=="N":
        print("Thank You For Playing")
        break
    else:
        print("Invalid Input")
