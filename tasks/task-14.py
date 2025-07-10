print("guess the secret number")
print("you have 3 chances to guess the number [hint: it is between 1 and 10]")
secret_number = 7
i=0
for i in range(3):
    guess = int(input("Enter your guess: "))
    if guess == secret_number:
        print("Congratulations! You guessed the number.")
        break
    elif i == 2:
        print("Sorry, you've used all your chances. The secret number was", secret_number)
    else:
        print("Wrong guess. Try again.")
    