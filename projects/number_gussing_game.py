import random
num_to_guess=random.randint(1,100)
while True:
    try:
        guess=int(input("Guess the number (1 - 100): "))
        if guess < num_to_guess:
            print("Too lower...")
        if guess > num_to_guess:
            print("Too Higher...")
        if guess == num_to_guess:
            print("Great.. You Guessed The Number..")
            break
    except ValueError:
        print("enter a valid number!")

